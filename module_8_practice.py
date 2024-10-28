def calc(line):
    operand_1, operation, operand_2 = line.split(' ')
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    if operation == '+':
        print(f'Результат: {operand_1 + operand_2}')
    if operation == '-':
        print(f'Результат: {operand_1 - operand_2}')
    if operation == '/':
        print(f'Результат: {operand_1 / operand_2}')
    if operation == '//':
        print(f'Результат: {operand_1 // operand_2}')
    if operation == '%':
        print(f'Результат: {operand_1 % operand_2}')
    if operation == '*':
        print(f'Результат: {operand_1 * operand_2}')


count = 0

with open('data.txt', 'r') as file:
    for line in file:
        count += 1
        try:
            calc(line)
        except ValueError as exc:
            print(f'Ошибка в линии {count}, возникло {exc} с параметрами {exc.args}')
