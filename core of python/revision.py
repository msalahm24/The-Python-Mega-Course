#you can use start with method is built in method in python
def is_qustion (user_input):
    keywordsq=('how','where','is','are','does','do','when','what','who','whom','whose','which')
    temp=False
    for keyword in keywordsq:
        if user_input == keyword:
            temp=True
    return temp
all_user_inputs=''
while True:
    user_input=input('enter some strings : ')
    if user_input == '\end':
        print(all_user_inputs)
        break
    else:
        words=user_input.split(' ')
        if is_qustion(words[0]):
            user_input=user_input.capitalize()
            user_input=' '+user_input + ' ?'
            all_user_inputs+=user_input
        else:
            user_input=user_input.capitalize()
            user_input=' '+user_input+ ' .'
            all_user_inputs+=user_input



