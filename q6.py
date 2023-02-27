# Write a function named solution which takes a list containing valid integers (2 to 10)
# and valid strings ('Jack', 'Queen', 'King' and 'Ace') with exact spellings as argument.
# This function should return the same list after sorting.
# Sorting precedence: 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'


def solution(x):
    list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
    # here we use lamda to specify the order of sorting
    return sorted(x, key=lambda x: list.index(x))


x = [4, 5, 7, 3, 2, 'Ace']
print(solution(x))

#
# The solution function takes a list lst as input and returns the sorted list
# using a custom sorting order specified by the order list.
# The order list contains the valid integers and strings in the desired sorting order.
#
# The sorted function is used to sort the input list lst based on the index of each
# element in the order list. The key parameter is used to specify
# the sorting key as a lambda function that returns the index of each element in the order list.
# The index method of the order list returns the index of the first occurrence of the element in the list.
#
# Here's an example of how to use the solution function: