def sumprod (tuple):
    sum = 0
    prod = 1
    for i in tuple:
        sum += i
        prod *= i
    return sum , prod

tuple = (1 , 2, 3, 4)
print (sumprod(tuple))

def reverse(tuple):
    return tuple[ : :-1]
    
print (reverse(tuple))

my_tuple = (1, 2, 3, 4, 5)

# Create an empty tuple to store the reversed elements
reversed_tuple = ()

# Iterate over the tuple in reverse order
for i in range(len(my_tuple)-1, -1, -1):
  # Append the element to the reversed tuple
  reversed_tuple += (my_tuple[i],)

print(reversed_tuple)  # Output: (5, 4, 3, 2, 1)


def reverse_tuple(t):
  if len(t) == 0:
    return ()
  else:
    return (t[-1],) + reverse_tuple(t[:-1])

# Test the function
my_tuple = (1, 2, 3, 4, 5)
print(reverse_tuple(my_tuple))  # Output: (5, 4, 3, 2, 1)

def eventuple(tuple):
    eventup = ()
    for i in tuple:
        if i%2 ==0:
            eventup += (i,)
    return eventup

print(eventuple(tuple))

def sumofeven(tuple):
    ntuple = eventuple(tuple)
    sum = 0 
    for i in ntuple:
        sum+=i
    return sum

print(sumofeven(tuple))

tuple1 = ('cat', 'dog', 'bird', 'fish')

print(reverse_tuple(tuple1))


def reverselist(l):

    if len(l)==0:
        return []
    else: 
       return  [l[-1]] + reverselist(l[:-1])
        
l=["rebecca", "i",1,3]

print (reverselist(l))


def sqtuple(tuple):
    newtup = ()
    for i in tuple:
        newtup += (i**2,)
    return newtup

print(sqtuple(my_tuple))
def reverse(n):
   str = ""
   for i in range (len(n)-1,-1,-1):
     str += n[i]
   return (str)




def revtupel(tuple):
    newtup=()
    for i in range (len(tuple)):
       newtup += (reverse(tuple[i]),)

    return reverse_tuple(newtup)

print(revtupel(tuple1))