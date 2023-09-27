"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    count = 0
    for item in items:
        item_to_string = str(item)

        if item_to_string in frequencies:
            count += 1
            frequencies.update({str(item) : count})
        else:
            count = 1
            frequencies.update({str(item) : count}) 
    return frequencies

lst = ['a', 'a', 'b', 'b', 'b', 'c']
lst2 = [100, 'Hello', '100', '100', 100]
print(frequencies(lst))
print(frequencies(lst2))