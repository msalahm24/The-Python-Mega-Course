#built in moduls
import os
import time
import pandas as pd

i=0
while i <=2 :
    if os.path.exists('../files/test.csv'):
        data=pd.read_csv('../files/test.csv')
        print(type(data))
    else:
        print('file not exists')
    # sleep here will freeze the execution for 2 sec
    time.sleep(2)
    i+=1


