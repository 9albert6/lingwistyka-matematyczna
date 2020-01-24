#!/usr/bin/python3
PRIORYTET = {'(': 0, ')': 1, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

def onp(input: str) -> str:
    stack = []
    output = ''

    for i in range(len(input)):
        if input[i].isdigit():
            if i - 1 >= 0 and input[i-1].isdigit():
                output = output[:-1] +  input[i] + ' '
            elif i -1 >= 0 and input[i-1] == '-':
                output += input[i] + ' '
            else:
                output += input[i] + ' '
        if input[i] in '+*/-^':
            if input[i] is '-':
                if i - 1 >= 0 and input[i-1].isdigit() != True:
                    output += '-'
                    continue
                elif i == 0:
                    output += '-'
                    continue
                

            while stack and PRIORYTET[input[i]] <= PRIORYTET[stack[-1]]:
                output += stack.pop() + ' '
            stack.append(input[i])
        if input[i] is '(':
            if i - 1 >= 0 and input[i-1].isdigit():
                stack.append('*')
            stack.append(input[i])
        if input[i] is ')':
            while stack[-1] != '(':
                output +=  stack.pop() + ' '
            stack.pop()


    while len(stack):
        if(stack[-1] == "("):
            stack.pop()
        else:
            output += ' ' + stack.pop()

    return output

def main():
    fileName: str = 'dane.txt'
    with open(fileName) as f:
        inputed_strings: List[str] = f.read().replace(" ", "").splitlines()

    for single_string in inputed_strings:
        postfix: str = onp(single_string)
        print("Infix:", single_string)
        print("Postfix:", postfix.replace("  ", ' '))

if __name__ == "__main__":
    main()