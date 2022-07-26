def canConstruct(ransomNote: str, magazine: str) -> bool:
        mag = {}
        
        # first for loop adds key (letter) and value (number of occurence) to the mag dict and increments for every occurence
        # I KNOW I COULD HAVE USED COUNTER, BUT I DIDN'T😅!!!
        for i in magazine:
            if i in mag:
                mag[i] += 1
            else:
                mag[i] = 1

        # second for loop reduces the value by 1 if letter is founc
        for j in ransomNote:
            if j in mag:
                mag[j] -= 1
                if(mag[j] == 0): # deletes key when value is zero
                    del mag[j]
            else:
                return False    
        return True

print(canConstruct(ransomNote='aa', magazine='ab'))
        