import sys #to manupulate exception in  Python runtime environment

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() #to get the exception information
    file_name = exc_tb.tb_frame.f_code.co_filename #to get the file name where exception occurred
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message) #calling the constructor of the parent class Exception
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message