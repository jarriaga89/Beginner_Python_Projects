#calculator project

from art import logo
print(logo)

print("Welcome to Josh's calculator. You can do basic math operations with this Python app using text commands for operations.")

#add/sum
def add(n1, n2):
    return n1 + n2

# subtract
def subtract(n1, n2):
    return n1 - n2

#multiplication
def multiply(n1, n2):
    return n1 * n2

#division
def division(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division
}

def calculator():
    num1 = float(input("What is the first number? "))
    for showoperationsymbols in operations:
        options = (str(showoperationsymbols))
        print(options)
    operation_symbol = input("Choose an operation sumbol from the line above: ")
    num2 = float(input("What is the next number? "))
    should_continue = True
    calculationtodo = operations[operation_symbol]
    first_answer = calculationtodo(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {first_answer}")
    
    while should_continue == True:
        if input(f"Type 'Y' to continue calculating with {first_answer}, or 'N' to start a fresh calculation: ").lower() == "y":
            operation_symbol = input("Choose another operation to apply to this result: ")
            calculationtodo = operations[operation_symbol]
            num3 = float(input("What is the next number to use with the previous result? "))
            second_answer = calculationtodo(first_answer, num3)
            print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")    
            first_answer = second_answer
        else:
            should_continue = False
            from replit import clear
            clear()
            calculator()

calculator()