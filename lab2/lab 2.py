def display_menu():
  print('1. Reserve Order \n' + '2. Display Leap Years \n' +
        '3. Fibonacci Series \n' + '4. Display Pattern \n' +
        '5. Guess Game \n' + '6. Display Matrix \n' + '7. Exit \n ')


def reverse(n):
  rev = ''
  temp = 0
  if (n < 0):
    n = n * (-1)
    rev += '-'
  elif (n == 0):
    print(0)
  while n != 0:
    temp += n % 10
    temp = temp * 10
    n = n // 10
  temp = temp // 10
  rev += str(temp)
  print(rev)


def Leap_Years(n):
  if n < 2022:
    for i in range(n, 2022 + 1):
      if i % 4 == 0 and i % 100 != 0:
        print('the Leap Years are: ', i)
      elif i % 100 == 0 and i % 400 == 0:
        print('the Leap Years are: ', i)
  else:
    for i in range(2022, n + 1):
      if i % 4 == 0 and i % 100 != 0:
        print('the Leap Years are: ', i)
      elif i % 100 == 0 and i % 400 == 0:
        print('the Leap Years are: ', i)


def series(n):
  if n <= 0:
    print('invalid')
  else:
    x, y = 0, 1
    for i in range(n):
      print('the numbers are', x, end='')
      x, y = y, x + y


def patt(n):
  for i in range(1, n):
    print('*' * i)
  for i in range(n, 0, -1):
    print('*' * i)


def main():
  n = 1
  while n != 7:
    display_menu()
    n = eval(input('Enter your choice:  '))
    if n == 1:
      a = int(input('enter a number:  '))
      reverse(a)
    if n == 2:
      b = int(input('enter a year:  '))
      Leap_Years(b)
    if n == 3:
      c = eval(input('Enter a number: '))
      series(c)
    if n == 4:
      d = int(input('Enter a number:  '))
      patt(d)
    if n> 7 or n< 1:
        print ('enter a valid number')


main()
