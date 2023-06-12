import win32file
import win32pipe


class PipeServer():
    def __init__(self, pipeName):
        self.pipe = win32pipe.CreateNamedPipe(
            r'\\.\pipe\\'+pipeName,
            win32pipe.PIPE_ACCESS_OUTBOUND,
            win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_READMODE_MESSAGE | win32pipe.PIPE_WAIT,
            1, 65536, 65536,
            0,
            None)
    def t(self):
        print(self)
    # Carefull, this blocks until a connection is established
    def connect(self):
        win32pipe.ConnectNamedPipe(self.pipe, None)

    # Message without tailing '\n'
    def write(self, message):
        win32file.WriteFile(self.pipe, message.encode()+b'\n')

    def close(self):
        win32file.CloseHandle(self.pipe)
