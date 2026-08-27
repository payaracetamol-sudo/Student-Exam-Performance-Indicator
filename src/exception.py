import sys

def error_message_detail(error,error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    # this exc_tb variable or exception traceback will give info about every exception
    # like in which file the exception has occurred, on which line, etc.

    file_name = exc_tb.tb_frame.f_code.co_filename   
    # finds the file name where we are getting the error
    
    error_message = "Error occured in python script name [{0}] line number[{1}] error message[{2}]".format(
        file_name,
        exc_tb.tb_lineno,
        str(error)
    )

    return error_message
    

# Inheriting our custom exception class from python's built in Exception class
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message , error_detail=error_detail)

    def __str__(self):
        return self.error_message



        

    