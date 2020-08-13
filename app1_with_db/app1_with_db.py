import mysql.connector as mysql
import difflib

try:
    con=mysql.connect(
        user='root',
        password='12369478521',
        host='localhost',
        database='Dictionary'
    )
    cursor=con.cursor()

except Exception as ex:
    print(ex.__str__(), ', this error for try connection')
try:
    query=cursor.execute('select word,definition from words')
    data=cursor.fetchall()
except Exception as ex:
    print(ex.__str__(),', this error for fetching data from the database ')



data_dic={}

def translate(userinput):
    definition=[]
    allkeys=[]
    most_raltive_word=''
    for tup in data:
        if tup[0]==userinput:
             definition.append(tup[1])
        elif tup[0]== userinput.capitalize():
            definition.append(tup[1])
        else:
            allkeys.append(tup[0])
    if len(definition)>0:
        return definition
    else:
        if len(difflib.get_close_matches(userinput,allkeys))>0:
            most_raltive_word=difflib.get_close_matches(userinput,allkeys)[0]
            if len(most_raltive_word)>0:
                return most_raltive_word
            else:
                return False

while True:
    userinput=input(' enter word or end to end the program: ')
    if userinput=='end':
        break
    else:
        answer=translate(userinput)
        if answer:
            if type(answer)==list:

                for defi in answer:
                    print(defi)
            else:
                userinput=input(f'did you mean {answer} if you mean it press y if not press any key')
                if userinput=='y' or userinput == answer:
                    answer=translate(answer)
                    for defi in answer:
                        print(defi)
                else:
                    print('this program will improve soon')
        else:
            print('this word does not exsits')
print("don't forget to drop this database after you end from it")





