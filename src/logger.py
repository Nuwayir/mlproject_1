# to track any logging information even the exceptions see where is the errors 

import logging
import os 
from datetime import datetime

# create the log file with time format:s -> i can take the format from the documention 
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# give a path for the LOG_FIEL: 
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)# getcwd : current working dic -> src 
                                    # star witl log ... whatever name of the LOG_FILE
os.makedirs(logs_path,exist_ok=True)#even though there is a file keep adding new files as well !                                  

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO # Adjust this to the desired logging level
)

# NOTE: to test : 
# if __name__=="__main__":
#     logging.info("Logging has started")
#     # now it will make folder insied it a file with the message as the format above 