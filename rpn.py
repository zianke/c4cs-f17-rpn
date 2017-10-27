def calculate(arg):
    stack = list()
    for x in arg:
        if x.isdigit():
            stack.append(float(x))
        elif x == '+':
            num1 = stack[-1]
            num2 = stack[-2]
            stack = stack[:-2]
            stack.append(num2 + num1)
        elif x == '-':
            num1 = stack[-1]
            num2 = stack[-2]
            stack = stack[:-2]
            stack.append(num2 - num1)
        elif x == '*':
            num1 = stack[-1]
            num2 = stack[-2]
            stack = stack[:-2]
            stack.append(num2 * num1)
        elif x == '/':
            num1 = stack[-1]
            num2 = stack[-2]
            stack = stack[:-2]
            stack.append(num2 / num1)
        else:
            pass
    if len(stack) == 1:
        print(stack[0])
        return stack[0]
    else:
        print("Error: Malformed expression")
        return "Error: Malformed expression"


def main():
    while True:
        calculate(input("rpn calc> "))


if __name__ == '__main__':
    main()
