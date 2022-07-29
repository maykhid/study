import string


def binarySearch(arr: list, num: int):
    low = 0
    high = len(arr)
    mid = (high + low) // 2

    while(low <= high):
        if arr[mid] == num:
            print ("FOUND")
            break
        elif arr[mid] < num:
            low = mid + 1
            mid = (high + low) // 2
            print("resetting low pos")
        elif arr[mid] > num:
            high = mid - 1
            mid = (high + low) // 2
            print("resetting high pos")
    else:
        print("NOT FOUND")

print(binarySearch([3, 6, 8, 9, 10, 14, 16, 19, 21, 23, 24, 27, 30, 32, 35], 21))