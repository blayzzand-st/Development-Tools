def calculator(a, op, b):
    if op == '/' and b == '0':
        raise ValueError('Can not divide by zero!')
    return eval(f'{a} {op} {b}')


if __name__ == '__main__':
    a, op, b = input().split(' ')
    print(calculator(a, op, b))
