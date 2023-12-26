import random


def loadNumbersFromFile():
  
 with open(' LAB1.txt ', 'r') as file:
    numbers = new_func(file)
    numbers = list(map(int, numbers))
    return numbers

def new_func(file):
    numbers = file.read().split('\n')
    return numbers


def reverseList(L):

  temp_l = []
  for i in range(len(L) - 1, -1, -1):
    temp_l.append(L[i])
  return temp_l


def without(L1, L2):
 
  temp_l = []
  for e in L1:
    if e not in L2:
      temp_l.append(e)
  return temp_l


def removeDuplicates(L):
  
  temp_l = []
  for e in L:
    if e not in temp_l:
      temp_l.append(e)
  return temp_l


def checkIfIdentical(L1, L2):
  
  if len(L1) != len(L2):
    return False
  for i in range(len(L1)):
    if L1[i] != L2[i]:
      return False
  return True


def divideIntoChunks(L, x):
  

  num_of_elements = len(L) // x
  i = 0
  list_of_chunks = []

  while i < x:
    start = i * x
    end = len(L) if i == x - 1 else i * x + num_of_elements

    list_of_chunks.append([])
    for j in range(start, end):
      list_of_chunks[i].append(L[j])
    i += 1
  return list_of_chunks


def isSubSet(L1, L2):
 
  for e in L2:
    if e not in L1:
      return False
  return True


def shuffleArray(L1):
  
  temp_l = []
  temp_l1 = []
  for e in L1:
    temp_l1.append(e)

  while len(temp_l1) != 0:
    i = random.randint(0, len(temp_l1) - 1)
    item = temp_l1.pop(i)

    temp_l.append(item)
  return temp_l


def dashArray(L):
 
  result = ''
  for i, num in enumerate(L):
    result += str(num)
    if (i != len(L) - 1):
      result += '-'
  return result


def computeSumOfSquares(L):
  
  squared_L = []
  for num in L:
    squared_L.append(num**2)
  squared_sum = 0
  for num in squared_L:
    squared_sum += num
  return squared_sum


def displayMenu():
  print('1. Reverse \n' + '2. Without \n' + '3. Unique \n' + '4. Compare \n' +
        '5. Divide \n' + '6. Subset \n' + '7. Shuffle \n' + '8. Dashes \n' +
        '9. Square Sum \n' + '10. Exit')


def mapOptionToFunction(option, numbers):
  running = True
  if option == 1:
    print('Reversed list:', reverseList(numbers))

  elif option == 2:
    user_list = list(
      map(int,
          input('Enter numbers seperated by spaces: ').split(' ')))
    print('Result:', without(numbers, user_list))

  elif option == 3:
    print('Result', removeDuplicates(numbers))

  elif option == 4:
    user_list = list(
      map(int,
          input('Enter numbers seperated by spaces: ').split(' ')))
    print('isEqual:', checkIfIdentical(numbers, user_list))

  elif option == 5:
    user_int = int(input('Enter integer x: '))
    print('Result:', divideIntoChunks(numbers, user_int))

  elif option == 6:
    user_list = list(
      map(int,
          input('Enter numbers seperated by spaces: ').split(' ')))
    print('isSubSet:', isSubSet(numbers, user_list))

  elif option == 7:
    print('Shuffled array:', shuffleArray(numbers))

  elif option == 8:
    print('Dasshed array:', dashArray(numbers))

  elif option == 9:
    print('Sum of squares', computeSumOfSquares(numbers))

  elif option == 10:
    running = False
    print('bye!')
  else:
    print('Please enter an option from 1 to 10')
  return running


running = True
numbers = loadNumbersFromFile()
name = input('Enter your name: ')
print('Hello', name, '!')
while running:

  displayMenu()
  option = int(input('Enter option: '))
  running = mapOptionToFunction(option, numbers)
