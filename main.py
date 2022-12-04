def calculator(a, op, b):
    if op == '/' and b == '0':
        raise ValueError('Can not divide by zero!')
    return eval(f'{a} {op} {b}')


if __name__ == '__main__':
    while True:
        command = input()
        if command != "exit":
            a, op, b = command.split(' ')
            print(calculator(a, op, b))
        else:
            break
