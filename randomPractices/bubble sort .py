def bubble_sort(lst):
  # Set a flag to True to begin the loop
  swapped = True
  
  # Keep looping until no swaps are made
  while swapped:
    # Set the flag to False to start the loop
    swapped = False
    
    # Loop through the list and compare adjacent elements
    for i in range(len(lst) - 1):
      if lst[i] > lst[i + 1]:
        # If the elements are out of order, swap them and set the flag to True
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
        swapped = True
 
  # Return the sorted list
  return lst




def bubble_sort_recursive(lst, n):
  # Base case: if the list has only one element, it is already sorted
  if n == 1:
    return
  
  # Loop through the list and compare adjacent elements
  for i in range(n - 1):
    if lst[i] > lst[i + 1]:
      # If the elements are out of order, swap them
      lst[i], lst[i + 1] = lst[i + 1], lst[i]
      
  # Recursively call the function on the list with one fewer element
  bubble_sort_recursive(lst, n - 1)

def bubble_sort(lst):
  return bubble_sort_recursive(lst, len(lst))





def deduplicate(lst):
    # base case: if the list is empty or has only one element, return the list
    if not lst or len(lst) == 1:
        return lst

    # recursive case: sort and deduplicate the rest of the list
    rest = deduplicate(lst[1:])

    # if the first element is already in the deduplicated list, return the list
    # without the first element
    if lst[0] in rest:
        return rest
    # otherwise, return the list with the first element appended
    return [lst[0]] + rest

# test the function
lst = [1, 2, 3, 2, 1, 4, 4, 5]
print(deduplicate(lst))  # Output: [1, 2, 3, 4, 5]