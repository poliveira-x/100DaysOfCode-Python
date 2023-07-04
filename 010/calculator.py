#This is a simple calculator that asks us for typing a number,
#to choose the operation and then typing another number.
#after calculating it asks whether we want to keep using the result
#or to start with a new number.
#

def add(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

def mul(n1, n2):
    return n1*n2

def div(n1, n2):
    return n1/n2

num1 = 0
result = 0

for i in range(5):
    if num1 == 0:
        num1 = float(input("What's the first number: "))
    
    print(" +\n -\n *\n /")
    op = input("Pick an operation: ")[0]
    num2 = float(input("What's the next number: "))
    
    if op == '+':
        result = add(num1, num2)
    elif op == '-':
        result = sub(num1, num2)
    elif op == '*':
        result = mul(num1, num2)
    elif op == '/':
        result = div(num1, num2)

    print(f"\n {num1} + {num2} = {result}")   

    again = input(f"\nType 'y' to continue calculating with {result} or 'n' to start a new calculation: ")[0]
    if again ==  'y':
        num1 = result
    else:
        num1 = 0


