file = open('D:/Викторина/voprosy-dlya-viktoriny.txt') #encoding='utf-8'
import random
str_list = []
line = file.readline()         # считываем первую строку
while line != '':              # пока не конец файла
    #print(line.strip())        # обрабатываем считанную строку
    line = file.readline()     # читаем новую строку
    str_list.append(line)
file.close()

user_input = int(input('Сколько вопросов нужно? '))
for i in range(0,user_input):
    rand_int = random.randint(0,8280)
    print(rand_int, str_list[rand_int])