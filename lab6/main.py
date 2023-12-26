from function import *
from classs import *


print( 'Hello user!')

database = readFromFile('lab6.txt')


displayMenu()
choice = int(input('Enter your choice: '))
while choice != 3:
    if choice == 1:
        for i in range (len(database)):
            r1 = database[i].getRoot1()
            r2 = database[i].getRoot2()
            print(r1, r2)

    elif choice == 2:
        a = int(input('Enter a: '))
        b = int(input('Enter b: '))
        c = int(input('Enter c: '))
        new_equation = Equation(a,b,c)
        r1 = new_equation.getRoot1()
        r2 = new_equation.getRoot2()
        print (r1,r2)


    else:
        print('Enter a valid choice!')

    displayMenu()
    choice = int(input('Enter your choice: '))


