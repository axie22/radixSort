import random

def radixSort(nums):
    maxDigit = max(nums)
    digit = 1
    while maxDigit >= digit:
        # buckets is a list of lists that will hold the numbers in each bucket
        buckets = [[] for i in range(10)]
        #print(nums)
        for num in nums:
            #print(buckets)
            #input()
            buckets[(num // digit) % 10].append(num)
        nums = []
        #print(buckets)
        #print(nums)
        for bucket in buckets:
            #print(nums)
            nums.extend(bucket) 
        digit *= 10
    return nums

def generateRandomList(length):
    # generates a random list of length length
    nums = []
    for i in range(length):
        nums.append(random.randint(20, 10000))
    return nums

nums = generateRandomList(1000)

def setup():
    size(600, 600)
    background(0)

def draw():
    global nums
    fill(0, 200, 50)
    rect(5, 50, 5, 50)
    for i in range(len(nums)):
        rect(i, 50, 5, 50)
        #rect(i, nums[i], 1, nums[i])
    
