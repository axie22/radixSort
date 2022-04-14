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

def generateRandomList():
    nums = []
    for i in range(600):
        #nums.append(random.randint(0, 600))
        nums.append(i)
        #nums.append(random.randint(0, 10000))
    random.shuffle(nums)
    return nums

def drawRectangles(nums):
    i = 0
    while i < len(nums):
        fill(0, 200, 50)
        rect(i * 2, 600 - nums[i], 3, nums[i])
        i += 1
        #delay(100)
        

nums = generateRandomList()
maxDigit = max(nums)
digit = 1
count = 0

def setup():
    global nums
    size(1200, 600)
    background(0)

def draw():
    global nums, maxDigit, digit, count
    background(0)
    #fill in the rectangles green
    
    # buckets is a list of lists that will hold the numbers in each bucket
    drawRectangles(nums)
    if maxDigit >= digit:
        buckets = [[] for i in range(10)]
        for num in nums:
            buckets[(num // digit) % 10].append(num)
        nums = []
        for i in range(len(buckets)):
            nums.extend(buckets[i]) 
        digit *= 10
        count += 1
        print(count)
        
    saveFrame()
    delay(500)
    
