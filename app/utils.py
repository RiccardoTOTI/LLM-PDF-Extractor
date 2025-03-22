import logging
import sys

def get_logger(name="app_logger"):
    """
    Configura un logger che scrive direttamente nel terminale.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # Creazione di un handler per lo stream output (console)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    
    # Formattazione del log
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    
    # Aggiunge l'handler al logger
    if not logger.handlers:
        logger.addHandler(handler)
    
    return logger
