import time
import logging

# Configure the logger globally
logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level to DEBUG
    format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s',  # Custom log message format
    handlers=[
        logging.StreamHandler(),  # Log messages to the console
        # You can add more handlers here (e.g., logging.FileHandler) for logging to files
    ]
)

class SingleTon(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SingleTon, cls).__new__(cls)
            cls._instance.setup_logger()  # Initialize the logger
        return cls._instance

    def __init__(self, sleep_time=None) -> None:
        if hasattr(self, 'sleep_time'):
            self.logger.debug("Used Previous Arguments")
            self.logger.debug(f"{self.sleep_time=}")
        else:
            self.sleep_time = sleep_time
            self.logger.debug(f"{self.sleep_time=}")
            if self.sleep_time is not None:
                time.sleep(self.sleep_time)
            else:
                time.sleep(5)
            self.logger.debug("Called init function")

    def setup_logger(self):
        self.logger = logging.getLogger(__name__)

    def print_hello_world(self):
        self.logger.debug("Hello World")

if __name__ == "__main__":
    a = SingleTon(sleep_time=5)
    a.print_hello_world()
    b = SingleTon(sleep_time=1)

    print(a is b)
