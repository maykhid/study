def canConstruct(ransomNote: str, magazine: str) -> bool:
        mag = {}
        
        for i in magazine:
            if i in mag:
                mag[i] += 1
            else:
                mag[i] = 1

        for j in ransomNote:
            if j in mag:
                mag[j] -= 1
                if(mag[j] == 0):
                    del mag[j]
            else:
                return False    
        return True

print(canConstruct(ransomNote='aa', magazine='ab'))
        