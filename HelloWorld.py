name = input("What's your name? \n").title().strip() #input from command line

nameList = name.split(' ')

while '' in nameList:
    nameList.remove('')


#print('Hello', name + '!')
if len(nameList) == 1:
    print(f'Hello {nameList[0]}!')

else:
    print(f'Hello {nameList[0]} {nameList[-1]}!') #F string to embed variables
#print('I AM STEVE!')
