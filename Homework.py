
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s"
)
FormatterForFile = logging.Formatter("%(levelname)s | %(message)s")


Logger = logging.getLogger('Test')

FileHand = logging.FileHandler('Homework.log')
FileHand.setFormatter(FormatterForFile)


Logger.addHandler(FileHand)




def divide(a, b):
    try:
         res = a // b
    except: 
         
         Logger.error("Division by zero is impossible")
         res = None
    Logger.debug("divide args   -> %s  %s", a, b)
    Logger.info("divide result ->: %s", res)




divide(10, 2)
divide(10, 0)