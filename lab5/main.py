from Employee import *
from function import * 


print ('WELCOME USER')

username = input('USERNAME: ')
password = input('PASSWORD: ')
count =1 
while count < 5:


    if findAdmin(username, password) == True:
        findAdmin = True
        break
    if findUser(username, password, count) == True:
        findUser = True
        break
    else:
     count += 1
     username = input('USERNAME: ')
     password = input('PASSWORD: ')
    if findUser(username, password, count) == True:
        findUser = True
        break
  
if findAdmin == True:   
    displayAdmin()
    choice = int(input('CHOOSE AN OPTION:  ') )
    while choice != 7:
        if choice == 1:
            print(displayStatics(database))

        elif choice == 2:
            username = input('ENTER USERNAME: ')
            gender =  input('ENTER GENDER: ')
            salary = input('ENTER SALARY: ')
            database = addEmployee(username, gender, salary, database)
            print ('THE NEW EMPLOYEE IS: ', database[len(database)-1].username)

        elif choice == 3:
            print(displayAll(database))

        elif choice == 4:
            id = input("ENTER THE EMPLOYEE'S ID: ")
            salary = float(input('ENTER THE NEW SALARY: '))
            database = changeSalary(id, database, salary)

        elif choice == 5:
            id = input("ENTER THYE EMPLOYEE'S ID: ")
            database=removeEmployee(id, database)
        elif choice == 6:
            id = input("ENTER THE EMPLOYEE'S ID: ")
            pourcentage = float(input("ENTER THE RAISE POURCENTAGE: "))
            database = raiseSalary (id, database, pourcentage)
        else:
            print('ENTER A VALID NUMBER')
        
        displayAdmin()
        choice = int(input('CHOOSE AN OPTION:  ') )
        


if findUser == True:
    displayUser()
    choice = int (input('CHOOSE AN OPTION: '))
    while choice != 2:
        if choice == 1:
            username = input('ENTER YOUR USERNAME: ')
            print(showSalary(username , database))
        else:
            print ('ENTER A VALID NUMBER')
       
        displayUser()
        choice = int (input('CHOOSE AN OPTION: '))
        
