'''Develop a Basic Calculator using Python : 

Implement Arthmetic Operations such as :-
.Addition(a + b) .Substraction(a - b) .Multiplication(a*b) 
.Division(a/b)   .Modulus(a%b)       .power(a**b)'''

while True:
    first = input("Enter first number: ")
    operator = input("Enter operator (+, -, *, /, %, **): ")
    second = input("Enter second number: ")

    # Convert inputs to integers (assuming user enters valid numbers)
    first = int(first)
    second = int(second)

    # Perform the calculation based on the operator
    if operator == '+':
        print(first + second)
    elif operator == '-':
        print(first - second)
    elif operator == '*':
        print(first * second)
    elif operator == '/':
        if second != 0:
            print(first / second)
        else:
            print("Error: Cannot divide by zero")
    elif operator == '%':
        print(first % second)
    elif operator == '**':
        print(first ** second)
    else:
        print("Invalid Operator")

    # Ask if the user wants to continue or exit
    continue_choice = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if continue_choice != 'yes':
        print("Exiting calculator. Goodbye!")
        break
