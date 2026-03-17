while True:
    print("--- Simple Calculator ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("q. Quit")

    choice = input("Enter choice (1/2/3/4/5 or q): ")

    if choice == 'q':
        print("Exiting the program. Goodbye!")
        break

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == '1':
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")

    elif choice == '2':
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    
    elif choice == '3':
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    
    elif choice == '4':
        #Prevent division by zero error
        if num2 != 0:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Error: You cannot divide by zero.")
            
    elif choice == '5':
        result = num1 % num2
        print(f"Result: {num1} % {num2} = {result}")
        
    else:
        print("Invalid input! Please run the program again.")
    