import mypackage
import logging
from mypackage.dataset import Dataset

if __name__ == "__main__":
    d = Dataset()
    print("The root log level is: ", logging.root.level)
    print("Making a debug call")
    d.debug_msg()
    print("The root log level is: ", logging.root.level)
    print("Making a warning call")
    d.warn_msg()
    print("Changing the root log level to debug")
    logging.root.setLevel(logging.DEBUG)
    d.debug_msg()