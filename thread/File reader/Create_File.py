import threading
import time


class Create_File:
    def __init__(self):
        self.file_out_name = 'out.txt'
        self.file = open(self.file_out_name, 'a++')

    def Write(self, text):
        text = str(text)
        self.file.write(text)

    def get_name_and_type(self):
        return self.file_out

    def Closed(self):
        self.file.close()
