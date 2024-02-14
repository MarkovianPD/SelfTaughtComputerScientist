from bisect import bisect_left


# Linear search algorithm
def linear_search(a_list, n):
    for i in a_list:
        if i == n:
            return True
    return False


a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(linear_search(a_list, 91))


# Binary search algorithm
def binary_search(a_list, n):
    first = 0
    last = len(a_list) - 1
    while last >= first:
        mid = (first + last) // 2
        if a_list[mid] == n:
            return True
        else:
            if n < a_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False


a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(a_list, 2))


# Challenge: Given a list of words in alphabetical order, write a function that performs a binary search for a word and returns whether it is in the list.
# I'll build a binary search and then use python's built in binary search to solve this challenge.

# Full binary tree
def custom_binary_search(a_list, n):
    first = 0
    last = len(a_list) - 1
    while last >= first:
        mid = (first + last) // 2
        if a_list[mid] == n:
            return True
        else:
            if n < a_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False


a_list = ['apple', 'banana', 'cherry', 'orange', 'passion fruit', 'pineapple', 'tangerine']
print(custom_binary_search(a_list, 'banana'))


# Using python bisect
def python_binary_search(a_list, n):
    index = bisect_left(a_list, n)
    if index <= len(a_list) and a_list[index] == n:
        return True
    return False


a_list = ['apple', 'banana', 'cherry', 'orange', 'passion fruit', 'pineapple', 'tangerine']
print(python_binary_search(a_list, 'ash'))
