import json
import difflib

data = json.load(open('data.json'))


def simlarto(word):
    mostrelativeword = difflib.get_close_matches(word.lower(), data.keys(), n=1)
    if len(mostrelativeword) > 0:
        return mostrelativeword[0]
    else:
        return False


def translate(word):
    if word.lower() in data.keys():
        return data[word.lower()]
    else:
        suggest = simlarto(word)
        if suggest:
            return suggest
        else:
            return "this word does't exsits"


while True:
    word = input('enter word or enter end to end the journy: ')
    if word.lower() == 'end':
        break
    else:
        if word in data.keys():
            answer = data[word]
            for defi in answer:
                print(f'{defi} \n')
        elif word.capitalize() in data.keys():
            answer = data[word.capitalize()]
            for defi in answer:
                print(f'{defi} \n')
        else:
            answer = translate(word)
            if answer == "this word does't exsits":
                print('this word dose not exsits')
            else:
                temp = input(f'did you mean {answer} enter y if you mean it and n if no: ')
                if temp.lower() == 'y':
                    answer = translate(answer)
                    for defi in answer:
                        print(f'{defi} \n')
                else:
                    print("will improve our program to learn from you soon")
