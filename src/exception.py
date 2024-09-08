import sys
from src.logger import logging
#sys : contain the details of any error if happend 
# NOTE : make sure to look into sys "custom exception handling in python" documentation

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()# return of sys i'm just intersted in the 
                                    # 3th one so i'm skiping the first two _,_,
    file_name=exc_tb.tb_frame.f_code.co_filename # in the exception handeling documnetion 
    error_message="Erorr occured in python script name [{0}] line number [{1}] error message [{2}]".format(
       file_name,exc_tb.tb_lineno,str(error)
    )
       
    return error_message 
   
# NOTE: WHENVER error raised i will call this function !!


class CustomException(Exception):# inherit from the Exception 
    # the constructer 
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)# beacuse we are inheriting form the Exception 
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    # to ensurewhen it  printed it print the error message 

# for test:
# if __name__=="__main__":
    
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Divide by Zero")
#         raise CustomException(e,sys)     
        