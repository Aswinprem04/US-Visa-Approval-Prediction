# from us_visa.pipline.training_pipeline import TrainPipeline

# obj = TrainPipeline()
# obj.run_pipeline()

from us_visa.logger import logging
from us_visa.exception import USvisaException

#logging.info("welcome to my custom log")
try:
    a = 2/0
except Exception as e:
    raise USvisaException(e,sys)