def calculator(a, op, b):
    if op == '/' and b == '0':
        raise ValueError('Can not divide by zero!')
    return eval(f'{a} {op} {b}')


if __name__ == '__main__':
    try:
        while True:
            command = input()
            if command != "EXIT":
                a, op, b = command.split(' ')
                print(calculator(a, op, b))
            else:
                break
    except EOFError:
        print("Exception handled")
