def error_message_details(error, tb):
    filename = tb.tb_frame.f_code.co_filename
    lineno = tb.tb_lineno
    return f"Error in Python script '{filename}' at line {lineno}: {error}"

class Custom_Exception(Exception):
    def __init__(self, error, tb=None) -> None:
        super().__init__(error)
        self.error_message = error_message_details(error, tb)

    def __str__(self) -> str:
        return self.error_message
