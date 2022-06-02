def merge(nums1: list, nums2: list, m: int, n: int) -> None:
    i = 0
    j = 0
    merged = []

    if(len(nums1) > m):
        nums1 = nums1[0 : m]
        
    if(len(nums2) > n):
        nums2 = nums2[0 : n]

    while (i < m and j < n):
        if(nums1[i] < nums2[j]):
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
        
    merged += nums1[i::] + nums2[j::]
    nums1.clear
    nums1 = merged


print(merge([1, 2, 3, 0, 0, 0], [2, 5, 6], 3, 3))