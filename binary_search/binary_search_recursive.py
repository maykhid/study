def binarySearch(arr: list, num: int, low: int, high: int):
    mid = (high + low) // 2

    if low > high:  # This ends the recursion
        print ("NOT FOUND")
        return

    if arr[mid] == num:
        print ("FOUND AT", mid)
    elif arr[mid] < num:
        binarySearch(arr, num, mid + 1, high)
    else:
        binarySearch(arr, num, low, mid - 1)

arr = [3, 6, 8, 9, 10, 14, 16, 19, 21, 23, 24, 27, 30, 32, 35]
target = 32
print(binarySearch(arr, target, 0, len(arr) - 1))