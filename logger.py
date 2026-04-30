import logging
import os
from datetime import datetime

def setup_logger():
    """Configura el logger para guardar en logs/log_dia_mes_año.log"""
    if not os.path.exists("logs"):
        os.makedirs("logs")
    
    # Formato solicitado: log_dia_mes_año.log
    log_filename = datetime.now().strftime("logs/log_%d_%m_%Y.log")
    
    logger = logging.getLogger("RataBot")
    logger.setLevel(logging.INFO)
    
    # Evitar duplicar handlers si se llama varias veces
    if logger.hasHandlers():
        # Verificamos si el archivo del handler actual es el mismo que el esperado
        current_fh = next((h for h in logger.handlers if isinstance(h, logging.FileHandler)), None)
        if current_fh and current_fh.baseFilename.endswith(log_filename.split('/')[-1]):
            return logger
        # Si el día cambió, limpiamos y reconfiguramos
        logger.handlers.clear()

    # Formato: [HH:mm] Mensaje
    formatter = logging.Formatter('[%(asctime)s] %(message)s', datefmt='%H:%M')

    # Handler para archivo
    fh = logging.FileHandler(log_filename)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    # Handler para consola
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    
    return logger
