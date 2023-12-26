# Create a dictionary that maps integers to their squares
squares = {x: x**2 for x in range(1, 11)}

print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

def reverse_dict(d):
    # Create a new dictionary with the keys and values reversed
    reversed_dict = {value: key for key, value in d.items()}

    return reversed_dict

# Test the function
original_dict = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = reverse_dict(original_dict)
print(reversed_dict)  # Output: {1: 'a', 2: 'b', 3: 'c'}



def merge_dicts(d1, d2):
    # Create a new empty dictionary
    merged_dict = {}

    # Iterate over the key-value pairs in the first dictionary
    for key, value in d1.items():
        # Add the key-value pair to the new dictionary
        merged_dict[key] = value

    # Iterate over the key-value pairs in the second dictionary
    for key, value in d2.items():
        # If the key is not in the new dictionary, add the key-value pair
        # If the key is already in the new dictionary, update the value
        merged_dict[key] = value

    return merged_dict

# Test the function
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5, 'f': 6}
merged_dict = merge_dicts(dict1, dict2)
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}



def merge_dicts(d1, d2):
    # Create a new dictionary that contains all the key-value pairs from both dictionaries
    merged_dict = {**d1, **d2}

    return merged_dict

# Test the function
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5, 'f': 6}
merged_dict = merge_dicts(dict1, dict2)
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

def dict_to_lists(d):
    # Create lists for the keys and values
    keys = []
    values = []

    # Iterate over the key-value pairs in the dictionary
    for key, value in d.items():
        # Add the key and value to the appropriate lists
        keys.append(key)
        values.append(value)

    # Return the lists as a tuple
    return (keys, values)

# Test the function
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys, values = dict_to_lists(my_dict)
print(keys)  # Output: ['a', 'b', 'c']
print(values)  # Output: [1, 2, 3]


def count_occurrences(lst):
    counts = {}
    for elem in lst:
        if elem in counts:
            counts[elem] += 1
        else:
            counts[elem] = 1
    return counts

# test the function
lst = [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(count_occurrences(lst))  # Output: {1: 3, 2: 3, 3: 3}


def dict_to_tuples(d):
    return d.items()

# test the function
d = {'a': 1, 'b': 2, 'c': 3}
print(dict_to_tuples(d))  # Output: [('a', 1), ('b', 2), ('c', 3)]

def max_key(d):
    max_key = None
    max_value = -float('inf')
    for key, value in d.items():
        if value > max_value:
            max_key = key
            max_value = value
    return max_key

# test the function
d = {'a': 1, 'b': 2, 'c': 3}
print(max_key(d))  # Output: 'c'

def max_key(d):
    return max(d, key=d.get)

# test the function
d = {'a': 1, 'b': 2, 'c': 3}
print(max_key(d))  # Output: 'c'