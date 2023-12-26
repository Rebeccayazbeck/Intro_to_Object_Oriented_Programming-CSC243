def insertion_sort(lst):
  # Iterate through the list, starting at the second element
  for i in range(1, len(lst)):
    # Save the current element to a variable
    current_element = lst[i]
    # Set a counter to the index of the current element
    j = i
    # While the counter is greater than 0 and the element at the counter - 1 is greater than the current element
    while j > 0 and lst[j - 1] > current_element:
      # Shift the element at the counter - 1 to the right
      lst[j] = lst[j - 1]
      # Decrement the counter
      j -= 1
    # When the while loop ends, the current element is in its correct position
    # Insert it into the list at the index of the counter
    lst[j] = current_element
 
  # Return the sorted list
  return lst




def insertion_sort_recursive(lst, n):
  # Base case: if the list has only one element, it is already sorted
  if n <= 1:
    return
  
  # Recursively sort the list with one fewer element
  insertion_sort_recursive(lst, n - 1)
  
  # Save the last element to a variable
  last = lst[n - 1]
  # Set a counter to the index of the last element
  j = n - 2
  # While the counter is greater than or equal to 0 and the element at the counter is greater than the last element
  while j >= 0 and lst[j] > last:
    # Shift the element at the counter to the right
    lst[j + 1] = lst[j]
    # Decrement the counter
    j -= 1
  # When the while loop ends, the last element is in its correct position
  # Insert it into the list at the index of the counter + 1
  lst[j + 1] = last

def insertion_sort(lst):
  return insertion_sort_recursive(lst, len(lst))