# This is a programming practice by coding a simple calculator

# Start an endless loop:
while True:
    # Get user's numbers and operation:
    number1 = float(input('Enter the first number: '))
    operator = input('Enter the operation (+, -, *, /): ')
    number2 = float(input('Enter the second number: '))
    # Check the operation and print the result:
    if operator == '+':
        print(f'Result: {number1 + number2}')
    elif operator == '-':
        print(f'Result: {number1 - number2}')
    elif operator == '*':
        print(f'Result: {number1 * number2}')
    elif operator == '/':
        print(f'Result: {number1 / number2}')
    else:
        print('Unknown operation, try again!')
