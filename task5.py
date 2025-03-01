
file = 'start_file.txt'

#Завдання (кількість слів, що починаються з літери(і великої і маленької), яку задав користувач. )

letter = input('Введіть літеру: ')
count_letters = 0
with open(file, 'r') as read_file:
    text_file = read_file.read()
    text_file = text_file.split()
    lower_text_file = [item.lower() for item in text_file]
    for i in lower_text_file:
        if i.startswith(letter.lower()):
            count_letters += 1
    print(f'В тексті {count_letters} починається з літери {letter}')



#print(count_letters)