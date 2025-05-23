def main():
    print('Select your desired function:')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Remainder')
    selection = input('Enter selection here: ').strip()
    selection_int = check_validity_selection(selection, 1, 5)

    x = input('Enter the first number: ')
    x = check_validity_integer(x)
    y = input('Enter the second number: ')
    y=check_validity_integer(y)


    match selection_int:
        case 1:
            print(f'{x+y:,}')
        case 2:
            print(f'{x-y:,}')
        case 3:
            print(f'{x*y:,}')
        case 4:
            print(f'{round(x/y, 2):,}')
        case 5:
            print(f'{x%y:,}')


def check_validity_selection(numString, floor, ceiling):
    isValid = 0
    while isValid == 0:
        try:
            converted = int(numString)
            if (converted <= ceiling) and (converted >= floor):
                isValid = 1
                #print('here')
            else:
                numString = input(f'Invalid input. Please enter a number between {floor} and {ceiling}: ')
        except:
            numString = input('Invalid input. Please enter a valid number: ').strip()

    return converted

def check_validity_integer(numString):
    isValid = 0
    while isValid == 0:
        try:
            if '.' in numString:
                converted = float(numString)
            else:
                converted = int(numString)
            isValid = 1
                #print('here')
        except:
            numString = input('Invalid input. Please enter a valid number: ').strip()

    return converted

main()