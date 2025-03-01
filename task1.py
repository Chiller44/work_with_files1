file = 'start_file.txt'

#Завдання1 (записав в новий файл слова, в яких більше 7 букв.)
with open(file, 'r') as read_file, open('finish_task1.txt', 'w') as write_file:
    ban_symb = ['.', ',', '!', '?', ':', ';']
    text_file = read_file.read()
    for i in ban_symb:
        text_file = text_file.replace(i, '')
    words = text_file.split()
    for word in words:
        if len(word) > 6:
            write_file.write(word + '\n')

