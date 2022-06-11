import random
import smtplib
import traceback
from threading import Thread
from time import sleep

import email_validator
from flask_mail import Message

from app import app, mail
from app.logger_setup import logger


def send(recipient, subject, body, attachment=None):
    """
    Handles sending email asynchronously

    @param recipient: list or str
        Email(s) of recipients
    @param subject: str
        Email subject
    @param body: str
        Support html or plain text
    @param attachment: str or list
        Path to attachment(s)

    """

    #for dev environment, override all email deliveries to developer.
    if app.config['APP_ENV'] != 'production':
        recipient = app.config['DEVELOPMENT_TESTING_EMAIL']
    sender = (app.config['MAIL_DEFAULT_SENDER_DISPLAY_NAME'], app.config['MAIL_DEFAULT_SENDER'])
    r = recipient if type(recipient) == list else [recipient]
    validate_recipients(recipient_list=r)
    message = Message(subject, sender=sender, recipients=r)
    message.html = body

    if attachment:
        if type(attachment) == str:
            with app.open_resource(attachment) as fp:
                message.attach(attachment.split('/')[-1], "application/pdf", fp.read())
        else:
            for a in attachment:
                with app.open_resource(a) as fp:
                    message.attach(a.split('/')[-1], "application/pdf", fp.read())

    # Create a new thread
    thr = Thread(target=send_async, args=[app, message])
    thr.start()


def send_async(app, message):
    """
    Sends the mail asynchronously
    @param app: app
    @param message: Flask Mail Message Object

    """

    with app.app_context():
        count=0
        while count < 11:
            count += 1
            try:
                mail.send(message)
                logger.info('Email logging', details='Subject: %s; Recipients: %s' % (
                    message.subject, message.recipients))
                break
            except smtplib.SMTPDataError as e:
                logger.info('Attempting to resend email: %s of 10' % count,
                             details=' Error: %s; Subject: %s; Recipients: %s' % (
                                 e, message.subject, message.recipients),
                             url="toolbox.email.send")
                sleep(random.randrange(0,10))
                try:
                    mail.send(message)
                except:
                    if count == 10:
                        logger.error('Unable to send email. Max resend attempts achieved.',
                                     details=' Error: %s; Subject: %s; Recipients: %s' % (
                                        e, message.subject, message.recipients),
                                     url="toolbox.email.send")
                    continue
                break
            except Exception as e:
                traceback.print_exc()
                logger.error('Unable to send email.',
                             details=' Error: %s; Subject: %s; Recipients: %s' % (
                                 e, message.subject, message.recipients),
                             url="toolbox.email.send")
                break


def validate_recipients(recipient_list):
    """
    This validates a list of email addresses as real addresses
    @param recipient_list: list of str
    """
    for email_address in recipient_list:
        email_validator.validate_email(email_address)