#The gateSDK currently only handles errors.
import anki_vector
import os
def raiseError(error_code=50):
    print(error_code)
def raiseCriticalError(error_code=50):
    print(error_code)

def GetFilePath(file):
    return os.path.abspath(file)
