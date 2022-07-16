import string


# def lengthOfLongestSubstring(s: string) -> int:
#     found = []
#     substringCount = 0
#     windowStart = 0

#     # if (len(s) <= 2):
#     #     return substringCount

#     for i, v in enumerate(s):
#         while (v in found): 
#             found.remove(s[windowStart])
#             windowStart += 1
          
#         found.append(v);
#         substringCount = max(substringCount, len(found))
#     return substringCount
  

def lengthOfLongestSubstring(s) -> int:
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i
        print(usedChar)

        return maxLength

'''
The code below is just me trying to do KMP
'''
# def lengthOfLongestSubstring(s):
#     pattern = {'a':0, 'b': 0, 'a':1, 'b':2, 'd': 0}

#     for i in s:


# print(lengthOfLongestSubstring('pwwkew'))

# te = {
#     'henry': 'hdnf',
#     'funv': def func(s)
# }
