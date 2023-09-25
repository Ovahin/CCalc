# This is a final version of the Calculator :)

# This is a path to our history file:
historyfile = '..\\History\\history.txt'


# This function is responsible for reading and writing a history of evaluations:
def historyview(*, action, evaluation='null'):
    # Call the reading code if the user want it:
    if action == 'read' and evaluation == 'null':
        # A standard operation of file reading:
        file = open(historyfile, 'r')
        history = []
        while True:
            string = file.readline()
            if len(string) == 0:
                break
            history.append(string)
        file.close()
        # Return the latest operations:
        return history[-5:]
    # If the action is writing open the file and write the operation we evaluated just now:
    elif action == 'write' and evaluation != 'null':
        file = open(historyfile, 'a')
        file.write(evaluation + '\n')
        file.close()


# This is a program main loop:
while True:
    # Get the user's operation:
    operation = input('>> Enter the operation: ')
    # Edit the string:
    operation = operation.replace(' ', '')
    operation = operation.lower()
    # Evaluate the string or read the history:
    if operation == 'history':
        print('>> The latest evaluations:')
        latest = historyview(action='read')
        for line in latest:
            print(line.replace('\n', '').replace(' ', ''))
    else:
        # Try to evaluate the string:
        try:
            print(f'>> Result: {eval(operation)}')
            historyview(action='write', evaluation=f'{operation}={eval(operation)}')
        # If there are letters and special symbols in the string:
        except SyntaxError:
            print(f'>> Error in the evaluation {operation}. Try again')
        except NameError:
            print(f'>> Error in the evaluation {operation}. Try again')
        except ZeroDivisionError:
            print(f'>> Error in the evaluation {operation}. Try again')
