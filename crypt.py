import os
from cryptography.fernet import Fernet


class Crypt:
    def __init__(self):
        if os.path.exists("filekey.key"):
            self.key = open("filekey.key").read()
        else:
            self.key = Fernet.generate_key()
            self.__store(self.key)

    def __store(self, key):
        with open("filekey.key", "wb") as filekey:
            filekey.write(self.key)

    def encrypt(self, txt):
        fernet = Fernet(self.key)
        encrypted = fernet.encrypt(txt)
        return encrypted

    def decrypt(self, encrypted):
        fernet = Fernet(self.key)
        decrypted = fernet.decrypt(encrypted)
        return decrypted
