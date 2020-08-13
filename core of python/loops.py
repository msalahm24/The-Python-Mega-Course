import datetime
for letter in 'hello':
    print(letter.title())
ages={
          'mohamed':28,
          'ahmed':26,
          'mahmoud':22
      }
#this will return tuple of item
for age in ages.items():
    print(age)
#return value from dic
for age in ages.values():
    print(age)
#return keys of dic
for key in ages.keys():
    print(key)
#return age and keys
for key,age in ages.items():
    print(f'the age of {key} is {age}')


while True:
    username=input("user name is : ")
    if username=='pypy':
        break
    else:
        print('enter agian')
        continue
#infinit loop
while datetime.datetime.now() < datetime.datetime(2090,5,24,5,30,30):
    print('wait to 2090')
