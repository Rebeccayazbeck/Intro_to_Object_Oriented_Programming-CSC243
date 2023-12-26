def displayMenu ():
  print ('1. Sum (1...n)')
  print ('2. Product (1...n)')
  print ('3. Simple Check')
  print ('4. Simple Count')
  print ('5. Password Check ')
  print ('6. Guess Game')
  print ('7. Factorial Task')
  print ('8. Exit')

def sum ():
  n = eval(input (' enter a number:  '))
  s = 0
  for i in range ( 1 , n+1 ):
    s = s + i
  print('the summ of all the number between 1 and', n ,'is', s)

def prod ():
  n = eval (input ('Enter a number:  '))
  p = 1
  for i in range (1, n+1 ):
    p = p*i
  print ("the product of the numbers between 1 and", n, "is", p)  
def neg ():
  x = int (input('Enter a number:  '))
  if x<0 or x>56:
    print ('error')
  else :
      print ( x , 'is  between 0 and 56 ')
def pos ():
  num1 = eval(input('Enter number 1: '))
  num2 = eval(input('Enter number 2: '))
  num3 = eval(input('Enter number 3; '))
  num4 = eval(input('Enter number 4: '))
  num5 = eval(input('Enter number 5: '))
  p = 0
  n = 0 
  if num1 < 0:
    n = n + 1
  else: 
    p = p + 1
    
  if num2 < 0:
    n = n + 1
  else: 
    p = p + 1  
    
  if num3 < 0:
    n = n + 1
  else: 
    p = p + 1
    
  if num4 < 0:
    n = n + 1
  else: 
    p = p + 1
    
  if num5 < 0:
    n = n + 1
  else: 
    p = p + 1
  print ('there is ', p, 'positive numbers')
  print (' there is ' ,n ,' negative numbers')
def pas ():
  x = str( input ('Enter the password:   '))
  if x == '4A56H9':
    print ('correct password')
  else: 
    print(' incorrect ')
  while x != '4A56H9':
     x = str( input ('Enter the password:   '))
     if x == '4A56H9':
       print ('correct password')
     else: 
       print(' incorrect ')
def sec ():
  print(' GUESS THE NUMBER ')
  num = eval ( input ( ' ENTER A NUMBER: ') )
  x = 56
  count = 1
  if num < x :
   print (' too small')
  elif num > x:
   print ( ' TOO BIG ')
  else: 
   print ('CONGRATULATIONS! YOU WON!')  

  while num != x :
    count += 1
    num = float ( input ( ' ENTER A NUMBER: ') )
    if num < x :
      print (' too small')
    elif num > x:
      print ( ' TOO BIG ')
    else: 
      print ('CONGRATULATIONS! YOU WON!')  


def fac():
  p = 1
  a=eval(input('enter a number:  '))
  for i in range ( 1 , a + 1 ):
   p = p * i
  print( ' the factorial of',a, 'is equal to ' ,p)  
def main():
  option = None
  while option != 8:
   displayMenu()
   option = int(input('Enter option:'))
   if option == 1:
     sum ()
   if option == 2:
     prod()
   if option == 3:
     neg()
   if option == 4:
     pos()
   if option == 5:
     pas()
   if option == 6:  
     sec()
   if option == 7:
     fac()
  if option == 8:
    print ('bye <3')
main()
