import re

def isPalindrome(s: str):
    temp = s.replace(' ', '')
    temp = temp.replace(',', '')
    temp = temp.replace(':', '')
    s = temp

    j = len(s) - 1
    i = 0

    while(i <= j):
        if (s[j] != s[i]):
            return False
        i = i + 1
        j = j - 1

    return True
        


print(isPalindrome('A man, a plan, a canal: Panama'))