"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
 

Constraints:

1 <= s.length <= 105
s[i] is either'(' , ')', or lowercase English letter.
"""

"""
possible solution:
Use two pointers, one at the start and one at the end of the String, when I find a '(' or ')',
when I find a '(' I start moving the end pointer to know if theres a closing ')' and vice versa
"""

"""
solution found on leet code:
Use a stack, in python you can transform the string to a list, anytime we find a '(' we add/push the index to the stack and whenever we find a ')' we pop,
if the stack is empty it means there isn't any closing pair left for the found pair which is '(' 
"""

# def minRemoveToMakeValid(s: str) -> str:
#     start = 0
#     end = len(s) - 1

#     while start <= end:
#         if s[start] == '(':
#             while s[start] == '(' and s[end] != '(':
#                 if s[end] != ')':
#                     end = end - 1
#                     continue
#                     # end = end - 1
#                     # start = start + 1 
#                 else:
#                     print('found match )', str(start), str(end))
#                     end = end - 1
#                     break
#             else:
#                 s =  s[:start] + s[start+1:]
                    
#         elif s[start] == ')':
#             while s[start] == ')' and s[end] != ')':
#                 if s[end] != '(':
#                     end = end - 1
#                     continue
#                 elif s[end] == ')':
#                     print('found match ( at', str(start), str(end))
#                     end = end - 1
#                     break
#             else:
#                 s =  s[:start] + s[start+1:]
                    
#         start = start + 1

#         print(s)

def minRemoveToMakeValid(s: str) -> str:
    stack = []
    string_list = list(s)

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            if len(stack) != 0:
                stack.pop()
            else:
                string_list[i] = ""
    
    for i in stack:     # changes all left over char to "" - empty
        string_list[i]=""

    return "".join(string_list)

print(minRemoveToMakeValid('lee(t(c)o)de)'))