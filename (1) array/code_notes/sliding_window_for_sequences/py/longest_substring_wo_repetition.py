import string


def lengthOfLongestSubstring(s: string) -> int:
    found = []
    substringCount = 0
    windowStart = 0

    # if (len(s) <= 2):
    #     return substringCount

    for i, v in enumerate(s):
        while (v in found): 
            found.remove(s[windowStart])
            windowStart += 1
          
        found.append(v);
        substringCount = max(substringCount, len(found))
    return substringCount
  


print(lengthOfLongestSubstring('pwwkew'))
