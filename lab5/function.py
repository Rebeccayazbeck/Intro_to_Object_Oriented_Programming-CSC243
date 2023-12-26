from Employee import Employee
from Employee import *
import datetime




def displayAdmin():
    print("1) Display Statistics")
    print("2) Add an Employee")
    print("3) Display all Employees")
    print("4) Change Employee's Salary")
    print("5) Remove Employee")
    print("6) Raise Employee's Salary")
    print("7) Exit")


def displayUser():
    print("1) Check my Salary")
    print("2) Exit")


def findAdmin(username, password):
    if username == "admin" and password == "admin123":
        return True
    return False

def findUser(username, password, count):
    if findAdmin(username, password) == True:
        return False
    elif password == "":
        return True
    elif count == 5:
        return True


def displayStatics(database):
    countmale = 0
    countfemale = 0
    for i in range (len(database)):
        if database[i].gender == 'male':
            countmale += 1
        else:
            countfemale += 1
    return countmale , countfemale


def addEmployee(username, gender, salary, database):
 date = datetime.datetime.now()
 previd = database[len(database)-1].id.split('emp')
 id = float(previd[len(previd)-1]) +1
 emp = Employee(id, username, date, gender, salary)
 database.append(emp)
 return database

def displayAll(database):
    username = []
    timestamp = []
    for i in range (len(database)):
     username.append(database[i].username)
     timestamp.append(database[i].timestamp)
    return(username, timestamp)


def changeSalary(id, database, salary):
    for i in range (len(database)):
        if database[i].id == id:
            database[i].salary = salary
    return database 


def removeEmployee(id, database):
    new_database=[]
    for i in range (len(database)):
        if database[i].id == id:
            continue
        new_database.append(database[i])
        return (new_database)


def raiseSalary (id, database, pourcentage):
    for i in range (len(database)):
        if database[i].id == id:
            database[i].salary = float(database[i].salary) * pourcentage
    return database 


def showSalary(username, database) :
    for i in range (len(database)):
        if database[i].username == username:
            return(database[i].salary)
        else:
            return('enter a valid username' )


