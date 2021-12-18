import logging
from pathlib import Path
# section
logger = logging.getLogger(__name__)
# logging.disable es para desactivar todos los logs sin tener que eliminarlos
# logging.disable(logging.ERROR)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

path = Path(r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-11", "logs.log")
file_handler = logging.FileHandler(filename=path, mode="a")
file_handler.setFormatter(formatter)


stream_handlear = logging.StreamHandler()
stream_handlear.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handlear)

logger.debug('Start of program')


def factorial(n):
    logger.critical('Start of factorial(%s%%)' % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logger.debug('i is ' + str(i) + ', total is ' + str(total))
    logger.debug('End of factorial(%s%%)' % (n))
    return total


print(factorial(5))
logger.debug('End of program')
