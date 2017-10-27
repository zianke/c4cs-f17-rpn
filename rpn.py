import numbers


def calculate(arg):
    stack = list()
    for x in arg:
        if x.isdigit():
            stack.append(float(x))
        elif x == '+':
            num1 = stack[-1]
            num2 = stack[-2]
            stack = stack[:-2]
            stack.append(num1 + num2)
        elif x == '-':
            num1 = stack[-1]
            num2 = stack[-2]
            stack = stack[:-2]
            stack.append(num1 - num2)
        elif x == '*':
            num1 = stack[-1]
            num2 = stack[-2]
            stack = stack[:-2]
            stack.append(num1 * num2)
        else:
            pass
    if len(stack) == 1:
        print(stack[0])
    else:
        print("Error: Malformed expression")


def main():
    while True:
        calculate(input("rpn calc> "))


if __name__ == '__main__':
    main()
