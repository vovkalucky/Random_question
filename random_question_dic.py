file = open('D:/Викторина/voprosy-dlya-viktoriny.txt') #encoding='utf-8'
import random
str_dict = {}
line = file.readline()         # считываем первую строку
while line != '': # пока не конец файла
    #line.strip()
    ans_question = line.split('*')        # обрабатываем считанную строку
    if len(ans_question) == 2:
        str_dict[ans_question[0]] = ans_question[1]
    line = file.readline()     # читаем новую строку

file.close()

user_input = int(input('Сколько вопросов нужно? '))
for i in range(0,user_input):
    question = random.choice(list(str_dict.keys()))
    print(question)
    user_input = input('Нужен ответ? (д/н): ')
    if user_input == "д":
        print(str_dict[question])
    else:
        continue
