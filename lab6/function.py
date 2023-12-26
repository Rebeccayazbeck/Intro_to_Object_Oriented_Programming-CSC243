from classs import Equation

def displayMenu():
    pass

def readFromFile(filename ):
    database = []
    file = open (filename , 'r')
    for line in file:
        a, b, c = line.split(', ')
        database.append(Equation(a,b,c))
    return database    
        

