file = 'start_file.txt'

#Завдання2 (записав в новий файл слова, порядок рядків збігається)

with open(file, 'r') as read_file, open('finish_task2.txt', 'w') as write_file:
    text_file = read_file.read()
    text_file = text_file.split('\n')
    for line in text_file:
        write_file.write(line + '\n')
