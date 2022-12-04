def calculator(a, op, b):
    if op == '/' and b == '0':
        raise ValueError('Can not divide by zero!')
    return eval(f'{a} {op} {b}')


if __name__ == '__main__':
    try:
        while True:
            command = input()
            if command == "exit":
                break
            elif command == "easter egg":
                print("HHHHH")
            else:
                a, op, b = command.split(' ')
                print(calculator(a, op, b))
    except EOFError:
        print("Exception handled")
