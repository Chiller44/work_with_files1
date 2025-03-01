
file = 'start_file.txt'
#Завдання6(змінити одну літеру на іншу і навпаки. В данному випадку региср має значення)
#ломав голову, а виявилося все легко завдяки неіснуючому символу. Піддивився)


symbol_1 = input('Введіть перший символ: ')
symbol_2 = input('Введіть другий символ: ')

temp_symbol = '#'

with open(file, 'r') as read_file, open('finish_task6.txt', 'w') as write_file:
    text_file = read_file.read()
    text_file = text_file.replace(symbol_1, temp_symbol)
    text_file = text_file.replace(symbol_2, symbol_1)
    text_file = text_file.replace(temp_symbol, symbol_2)

    write_file.write(text_file)


    print(text_file)


