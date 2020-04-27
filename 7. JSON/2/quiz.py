# Utwórz quiz z wykorzystaniem struktury zaproponowanej na początku lekcji.
# Może być to quiz z wiedzy o Pythonie ;)
# https://realpython.com/quizzes/

import json


def mechanics_quiz():
    for t in range(1,10):
        c = str(t)

        question = data["quiz"]["python"][c]['question'][0::]
        k = len(question)
        print(question)
        for i in range(4):
            print(data["quiz"]["python"][c]['options'][i])

        question_first = int(input('► Wybieram: '))
        c = data["quiz"]["python"][c]['answer']
        print(f'► Prawidłowa odpowiedź: {c}')
        print('-' * k)
        print('')

filename = 'categories.json'
with open(filename, 'r') as f:
    data = json.loads(f.read())


s = ' Python Quiz '

print('.' * 60)
print(s.center(60))
print('.' * 60)

mechanics_quiz()


