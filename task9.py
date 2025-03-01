file = 'start_file.txt'

#Завдання9(підрахував кількість символів в тексті. пробіли не враховую)

count_symb = 0
with open(file, 'r') as read_file:
    text_file = read_file.read()
    text_file = text_file.split()
    for word in text_file:
        count_symb += len(word)

print(f'В даному тексті {count_symb} без пробілів')

