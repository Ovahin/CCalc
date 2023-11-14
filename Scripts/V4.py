# This is a new CCalc version with JSON file as history's database:
import json

# Initialize history file's path and preinitialize the history list: 
historyfile = "..\\History\\history.json"
history = []
with open(historyfile, 'r') as hf:
    history = list(json.load(hf)['history'])[-5:]


# Read history from the file:
def viewhistory():
    print('-'*100)
    print('>>> There is the history of calculations:\n')
    for expression in history:
        print(expression)
    print('-'*100)


# Write history to th file:
def writehistory(expression):
    history.append(expression)
    data = {"history": history}
    # Rewrite ALL history (with new expressions):
    with open(historyfile, 'w') as hf:
        json.dump(data, hf)


# Evaluate a string:
def perform(expression):
    try:
        result = eval(expression)
        print(f'>>> Result: {result}')
        # Write the evaluated expression to the end of the history file:
        writehistory(f'{expression}={result}'.replace(' ', ''))
    # Message about errors:
    except SyntaxError:
        print('!!! There are forbidden symbols in the expression! Try again.')
    except ZeroDivisionError:
        print("!!! You can't devide by zero! Try again.")
    except NameError:
        print("!!! Error!")


# Main program's circle:
while True:
    expression = input('>>> Input an expression: ')
    # View the history:
    if expression == 'history':
        viewhistory()
    # Break the circle:
    elif expression == 'quit':
        break
    # Evaluate the string:
    else:
        perform(expression)
