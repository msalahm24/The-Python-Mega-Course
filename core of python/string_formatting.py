name=input('enter your first name : ')
surname=input('enter your surname : ')
#python 2 ---> 3.3
message='your name is %s and surname is %s ' % (name,surname)
#python 3.3 ----> later version
message2=f'yourname is {name} and surname is {surname}'
print('python 2 : ',message)
print('python 3.3 to leter version: ',message2)
#if you want to know if any object is instance from class(ay haga) use
print(isinstance('str',str))
