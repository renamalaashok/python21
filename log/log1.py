import logging
logging.basicConfig(level=logging.DEBUG, filename="log1.txt", format="%(asctime)s-->%(levelname)s;%(message)s")
logging.debug("debug message")
logging.info("info meaage")
logging.warn("Warn mesaage")
logging.error("Error message")
logging.exception("exception message")