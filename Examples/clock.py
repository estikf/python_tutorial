import os
import datetime
from time import sleep

def myFunc():
    os.system("CLS")
    x = datetime.datetime.now()
    print(x)
    sleep(1)

while True:
    myFunc()