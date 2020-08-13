#myfile=open('test.txt')
#content=myfile.read()
# # if want to use .read() again you will get empty string
# # because the cursor in the end of the file
#print(myfile.read())
#myfile.close()
#print(content)


## but the good way of openning file and process it
## using with statement
with open('test.txt') as myfile:
    content=myfile.read()
#print(content)

with open('testwrite.txt','w') as myfile:
    myfile.write('testwrite\ntestwrite\ntestwrite')

# if yow use option 'w' with open in already file exists
#this will overwrite the content
with open('testwrite.txt','w') as myfile:
    myfile.write('overwrite')
# but if you want to append not overwrite
with open('testwrite.txt','a') as myfile:
    myfile.write('\nappending')

with open('testwrite.txt','a+') as myfile:
    myfile.write('\n the the last point of the cursor')
    print(myfile.read())
    myfile.seek(0)
    print(myfile.read())

