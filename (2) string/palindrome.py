import re

def isPalindrome(s: str):
    temp = re.sub(r'[^a-zA-Z0-9]', '', s)
    s = temp.lower()

    j = len(s) - 1
    i = 0

    while(i <= j):
        if (s[j] != s[i]):
            return False
        i = i + 1
        j = j - 1

    return True
        


print(isPalindrome('A man, a plan, a canal: Panama'))