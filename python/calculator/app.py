# add,sub,mul,div,m
def add(a,b):
    answer = a + b
    print(f'The value of {str(a)} and {str(b)} is {str(answer)}')

def sub(a,b):
    answer = a - b
    print(f'The value of {str(a)} and {str(b)} is {str(answer)}')

def mul(a,b):
    answer = a * b
    print(f'The value of {str(a)} and {str(b)} is {answer}')

def div(a,b):
    answer = a / b
    print(f'The value of {str(a)} and {str(b)} is {str(answer)}')

def mod(a,b):
    answer = a % b
    print(f'The value of {str(a)} and {str(b)} is {str(answer)}')

while True:
    print('1. addition')
    print('2. subtraction')
    print('3. multiply')
    print('4. division')
    print('5. modulus')
    print('6. exit')

    choice = int(input('Enter your choice: '))
    if choice == 1:
        a = int(input('Enter the first value: '))
        b = int(input('Enter the second value: '))
        add(a,b)
    elif choice == 2:
        a = int(input('Enter the first value: '))
        b = int(input('Enter the second value: '))
        sub(a,b) 
    elif choice == 3:
        a = int(input('Enter the first value: '))
        b = int(input('Enter the second value: '))
        mul(a,b)
    elif choice == 4:
        a = int(input('Enter the first value: '))
        b = int(input('Enter the second value: '))
        div(a,b)
    elif choice == 5:
        a = int(input('Enter the first value: '))
        b = int(input('Enter the second value: '))
        mod(a,b)
    elif choice == 6:
        break
    else:
        print('enter valid number')
    print()
