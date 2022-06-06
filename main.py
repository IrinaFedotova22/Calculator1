print('Welcome to calculator! Enter "exit" to finish calculations!')
operation = 0
while operation != 'exit':
    operation = input("Enter your operation:")
    if operation == 'R':
        import random
        print(random.random())
    elif operation == '||':
        first_num = int(input("Enter the 1st number:"))
        print(abs(first_num))
    elif operation == '!':
        first_num = int(input("Enter the 1st number:"))
        import math
        print(math.factorial(int(first_num)))
    elif operation == 'arccos':
        first_num = int(input("Enter the 1st number:"))
        import math
        print("arccos:", math.acos(first_num))
    elif operation == '+':
        first_num = int(input("Enter the 1st number:"))
        second_num = int(input("Enter your 2nd number:"))
        print(first_num + second_num)
    elif operation == '-':
        first_num = int(input("Enter the 1st number:"))
        second_num = int(input("Enter your 2nd number:"))
        print(first_num - second_num)
    elif operation == '/':
        first_num = int(input("Enter the 1st number:"))
        second_num = int(input("Enter your 2nd number:"))
        print(first_num / second_num)
    elif operation == '*':
        first_num = int(input("Enter the 1st number:"))
        second_num = int(input("Enter your 2nd number:"))
        print(first_num * second_num)
    elif operation == '**':
        first_num = int(input("Enter the 1st number:"))
        second_num = int(input("Enter your 2nd number:"))
        print(first_num ** second_num)
    else:
        print("This is an invalid input")

else:
    print("The calculator is turned off")