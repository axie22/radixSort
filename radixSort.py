"""

Radix sort sorts the elements in a list by comparing the digits of the elements in the ones, tens, ... place of the number. The largest number in the list determines the number of digits in the list.
"""

__author__ = "Alex Xie"
__version__ = "2022-03-20"

import random
import time

def radixSort(nums):
    maxDigit = max(nums) #finds the largest number in the list
    digit = 1 # start with the ones digit
    while maxDigit >= digit: # while we have not reached the largest digit
        # buckets is a list of lists that will hold the numbers in each bucket
        buckets = [[] for i in range(10)] # 10 buckets for the digits 0-9
        #print(nums)
        for num in nums:
            buckets[(num // digit) % 10].append(num) # places the number in the correct bucket based on the place value of the digit being examined
        nums = [] # clear the list
        for bucket in buckets:
            nums.extend(bucket)  # add the numbers in the buckets back to the list
        digit *= 10   # move to the next number place
    return nums

def countingSort(nums):
    # counts the number of times each number appears in the list
    counts = [0] * 10
    for num in nums:
        counts[num % 10] += 1
    # counts the number of times each number appears in the list
    counts = [0] * 10
    for i in range(1, 10):
        counts[i] += counts[i - 1]
    # puts the numbers in the correct positions
    sortedNums = [0] * len(nums)
    for num in nums:
        sortedNums[counts[num % 10] - 1] = num
        counts[num % 10] -= 1
    return sortedNums

def generateRandomList(length):
    # generates a random list of length length
    nums = []
    for i in range(length):
        nums.append(random.randint(0, 100000))
    return nums

def generateBinaryList(length):
    # generates a random list of length length
    nums = []
    for i in range(length):
        nums.append(bin(random.randint(0, 4000000))[2:])
        #[2:] removes the '0b' from the beginning of the string
    return nums

def checkList(nums):
    # checks if the list is sorted
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True

def insertionSort(nums):
    for index in range(len(nums)):
        #print(nums)
        currentvalue = nums[index]
        position = index
        while position > 0 and nums[position - 1] > currentvalue:
            nums[position] = nums[position - 1]
            position = position - 1
        nums[position] = currentvalue

    return nums

def selection_sort(nums):
    first_item_index = 0
    for first_item_index in range(len(nums)):
        smallest_value_index = first_item_index
        for i in range(first_item_index + 1, len(nums)):
            if nums[i] < nums[smallest_value_index]:
                smallest_value_index = i
        #exchange first item index and smallest value index
        nums[first_item_index], nums[smallest_value_index] = nums[smallest_value_index], nums[first_item_index]
    
    return nums



def main():
    print("Radix Sort:")
    for i in range (100, 1100, 100):
        nums = generateRandomList(1000 * i)
        start = time.time()
        nums = radixSort(nums)
        end = time.time()
        print(1000 * i, end - start)
    print()
    
    print("Python built-in sort:")
    for i in range (100, 1100, 100):
        nums = generateRandomList(1000 * i)
        start = time.time()
        nums.sort()
        end = time.time()
        print(1000 * i, end - start)
    
    print("Counting Sort:")
    for i in range (100, 1100, 100):
        nums = generateRandomList(1000 * i)
        start = time.time()
        nums = countingSort(nums)
        end = time.time()
        print(1000 * i, end - start)

if __name__ == '__main__':
    main()

