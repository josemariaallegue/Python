import logging


print("Debugging - logging")
""" es para remplazar la tactica de debbugear con print() ya que permite escribir facilmente en un archivo, darle formato,
establecer que solamente se escriba informacion segun niveles, etc."""

# creo un objeto logger
# __name__ estable que cuando escriba se pone el nombre de donde se encuentra el codigo
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # se estable el nivel general a debug

# los nives son:
# DEBUG - Detailed information, typically of interest only when diagnosing problems.
# INFO - Confirmation that things are working as expected.
# WARNING - An indication that something unexpected happened, or indicative of some
# problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
# ERROR - Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL - A serious error, indicating that the program itself may be unable to continue running.

formatter = logging.Formatter(
    " %(asctime)s -  %(levelname")  # el formato de los mensajes

# el fileHandler es para escribir en archivos
# estable la ruta del archivo
file_handler = logging.FileHandler(
    r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-11\11-3.log")
# establece que solo se escriben los tipo error
file_handler.setLevel(logging.ERROR)
# establece el formato
file_handler.setFormatter(formatter)

# el streamHandler para escribir en consola
stream_handler = logging.StreamHandler()
# el formato
stream_handler.setFormatter(formatter)

# agrego los handlers al logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
