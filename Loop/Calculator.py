while(True):
    print('Which operation you want to perform: ')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Power')
    option = int(input('Enter option: '))
    # print(option)
    if (option >= 1 and option <= 5):
        # print('Valid Option')
        if (option == 1):
            num1, num2 = input('Enter two number: ').split()
            num1 = int(num1)
            num2 = int(num2)
            print(num1 + num2)
        elif (option == 2):
            num1, num2 = input('Enter two number: ').split()
            num1 = int(num1)
            num2 = int(num2)
            print(num1 - num2)
        elif (option == 3):
            num1, num2 = input('Enter two number: ').split()
            num1 = int(num1)
            num2 = int(num2)
            print(num1 * num2)
        elif (option == 4):
            num1, num2 = input('Enter two number: ').split()
            num1 = int(num1)
            num2 = int(num2)
            print(num1 / num2)
        else:
            num1, num2 = input('Enter two number: ').split()
            num1 = int(num1)
            num2 = int(num2)
            print(num1 ** num2)
    else:
        print('Invalid Option')
