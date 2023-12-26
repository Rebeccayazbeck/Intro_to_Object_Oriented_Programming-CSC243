




class Employee:
    def __init__(self, id, username, timestamp, gender, salary):
        self.id = id
        self.username = username
        self.timestamp = timestamp
        self.gender = gender
        self.salary = salary

file = open('Employee.txt').read()
line =  file.split('\n')
database = []
for i in range (len(line)):
    emp = Employee(*line[i].split(', '))
    database.append(emp)
