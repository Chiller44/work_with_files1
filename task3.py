file = 'start_file.txt'

#Завдання3 (записав в новий файл слова, рядки в зворотньму порядку)

with open(file, 'r') as read_file, open('finish_task3.txt', 'w') as write_file:
    text_file = read_file.read()
    text_file = text_file.split('\n')[::-1]
    for line in text_file:
        write_file.write(line + '\n')