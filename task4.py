file = 'start_file.txt'

#Завдання4 (знайшов останній рядок, в якому є кома і після нього вставив рядок ************,
# якшо ком немаю, додаю хірочки останнім рядком)

a = []
with open(file, 'r') as read_file, open('finish_task4.txt', 'w') as write_file:
    start_text = read_file.read()
    start_text = start_text.split('\n')
    for i in start_text:
        if ',' in i:
            a.append(i)

    if len(a) > 0:
        last = str(a[-1])
        index_last_comma = start_text.index(last)
        start_text.insert((index_last_comma + 1), '************')
        write_file.write('\n'.join(start_text))
    else:
        start_text.insert((len(start_text) + 1), '************')
        write_file.write('\n'.join(start_text))
