# Dynamic variant sliding window increases and decreases pointers size as it traverses through the sequence depending on the set conditions
# The code snippet below is an example of Dynamic variant.

# Find the size of the smallest subarray which when summed gives you your targetSum

def smallestSubarray (targetSum: int, arr: list[int]) -> int:
    minWindowSize = float('inf') #init minWindowSize with the highest possible value
    currentWindowSum = 0
    windowStart = 0

    for windowEnd, v in enumerate(arr):
        currentWindowSum += v
        
        while(currentWindowSum >= targetSum): # basically while currentWindowSum >= tragetSum do
            minWindowSize = min(minWindowSize, windowEnd - windowStart + 1) # assign minWindowSize
            currentWindowSum -= arr[windowStart] # reduce the leftside by one. shrink as long as criteria is met
            windowStart += 1 # change location (index) of starting point by incrementing by one
            
    return minWindowSize

print(smallestSubarray(8, [4, 2, 2, 7, 8, 1, 2, 8, 10]))
