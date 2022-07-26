
'''
            | 
[a, a, a, b, b, b, c, c] 

set count and increment while moving sliding window until you get to another different character different from initial
insert the char and its count only if its greater than 1
'''
# first solution

# def compress(chars: list[str]) -> int:
#     arr = []
#     count = 0
#     windowStart = 0
#     windowEnd = 0

#     while windowEnd < len(chars):
#         while(windowEnd < len(chars) and chars[windowStart] == chars[windowEnd]):
#             count = count + 1
#             windowEnd = windowEnd + 1
#         else:
#             if count > 1:
#                 arr.extend([chars[windowStart], str(count)])
#             else:
#                 arr.extend(chars[windowStart])
#             count = 0
#             windowStart = windowEnd
#     return arr

# second solution that works on leetcode

class Solution:
    def compress(self, chars: list[str]) -> int:
        s = ""
        count = 0
        windowStart = 0
        windowEnd = 0

        while windowEnd < len(chars):
            while(windowEnd < len(chars) and chars[windowStart] == chars[windowEnd]):
                count = count + 1
                windowEnd = windowEnd + 1
            else:
                if count > 1:
                    s = s + chars[windowStart] + str(count)
                else:
                    s = s + chars[windowStart]
                count = 0
                windowStart = windowEnd

        chars.clear()
        
        for i in s:
            chars.append(i)
        
        return len(chars)
        



