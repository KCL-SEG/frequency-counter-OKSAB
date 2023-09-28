"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    count = 0
    for item in items: # Iterating throught the items
        item_to_string = str(item) # Convert items to string

        if item_to_string in frequencies.keys(): # If the item appears more the once the count is increased by 1
            frequencies[item_to_string] += 1 
        else:
            frequencies[item_to_string] = 1 # If the item is only found once 1 will be the count
    return frequencies




