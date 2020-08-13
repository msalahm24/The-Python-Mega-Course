def area(a,b=5):
    return a*b

#postional arguments
print(area(4,2))
#keywords arguments
print(area(b=5,a=4))
#postional arguments must be before keywords arguments
print(area(4,b=6))
# if you want to pass any number of arguments
# *args is a tuple
def sumthis(*args):
    return sum(args)


print(sumthis(1,2,3,3,3,3,3,5,5,5,4,70))
#if you want to pass keywords arguments
# **kwargs is a dictionary
def printname(**kwargs):
    print(type(kwargs))
    for key,value in kwargs.items():
        print(f'the name of {key} is {value} ')

printname(student1='mahmoud',student2='ahmed')
