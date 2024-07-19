import logging
import os

from from_root import from_root
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # create logging string

log_dir = 'logs'

logs_path = os.path.join(from_root(), log_dir, LOG_FILE) # logging folder

os.makedirs(log_dir, exist_ok=True) 


logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s", # info about the logging
    level=logging.DEBUG,
)