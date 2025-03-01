
file = 'start_file.txt'

#Завдання10(підрахував кількість рядків в тексті)

with open(file, 'r') as read_file:
    text_file = read_file.read()
    text_file = text_file.split('\n')
print(f'В тексті {len(text_file)} рядків')
