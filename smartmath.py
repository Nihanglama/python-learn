'''Write a python module with two functions:
GCD
LCM
'''
def GCD(num1,num2):
    a=num1
    b=num2
    small = a if (a < b) else b
    for i in range(1, small + 1):
        if (a % i) == 0 and (b % i) == 0:
            gcd = i
    return gcd


def LCM(num1,num2):
    gcd=GCD(num1,num1)

    return int(abs(num1*num2)/gcd)

'''Write a python module with multiple sorting algorithms as its functions'''

def bubble_sort(lis):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(lis) - 1):
            if lis[i] > lis[i + 1]:
                # Swap the elements
                lis[i], lis[i + 1] = lis[i + 1], lis[i]
                # Set the flag to True so we'll loop again
                swapped = True
            
def selection_sort(num):
    for i in range(len(num)):
        lowest_value_index = i
        for j in range(i + 1, len(num)):
            if num[j] < num[lowest_value_index]:
                lowest_value_index = j
        # Swap values of the lowest unsorted element with the first unsorted
        # element
        num[i], num[lowest_value_index] = num[lowest_value_index], num[i]

def insertion_sort(nums):
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        # the item to insert
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Insert the item
        nums[j + 1] = item_to_insert