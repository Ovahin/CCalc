# There is a harder calculator with a history of operations :)

historyFile = '..\\History\\history.txt'


def readhistory():
    file = open(historyFile, 'r')  # Open the history file
    history = []
    while True:  # Read the file until the EOF
        line = file.readline()
        if len(line) == 0:
            break
        history.append(line)  # Add the operation to the history of operations
    latest = history[-5:]
    for line in latest:
        print(line.replace('\n', ''))  # Print the latest 5 operations


def perform():
    result = 0
    # Get user's numbers and operation:
    number1 = float(input('Enter the first number: '))
    operation = input('Enter the operation (+, -, *, /): ')
    number2 = float(input('Enter the second number: '))
    # Check the operation and print the result:
    if operation == '+':
        result = number1 + number2
    elif operation == '-':
        result = number1 - number2
    elif operation == '*':
        result = number1 * number2
    elif operation == '/':
        result = number1 / number2
    else:
        print('Unknown operation, try again!')
        perform()
    print(f'Result: {result}')
    history = open(historyFile, 'a')  # Open the history file
    history.write(f'{number1} {operation} {number2} = {result}\n')  # Write a history note to the file
    history.close()  # Close the file


while True:  # This is a general loop of the program
    operator = input('Enter a command (history/perform): ')  # Get a user's command
    # Call a method for the operation:
    if operator == 'history':
        readhistory()
    elif operator == 'perform':
        perform()
    else:
        print('Unknown command :(')
