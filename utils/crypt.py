import os
from cryptography.fernet import Fernet


class Crypt:
    def __init__(self):
        if os.path.exists("files/filekey.key"):
            self.key = open("files/filekey.key").read()
        else:
            self.key = Fernet.generate_key()
            self.__store(self.key)

    def __store(self, key):
        with open("files/filekey.key", "wb") as filekey:
            filekey.write(self.key)

    def encrypt(self, txt):
        fernet = Fernet(self.key)
        encrypted = fernet.encrypt(txt)
        return encrypted

    def decrypt(self, encrypted):
        fernet = Fernet(self.key)
        decrypted = fernet.decrypt(encrypted)
        return decrypted
