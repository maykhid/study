def isAnagram(s, t):
        dic1, dic2 = [0]*26, [0]*26 # create a list of 0's of length 26 denoting the length of alphabet
        
        '''
         traverse string, for each letter 'item', minus the ord('item') from the ord('a'). This trick is actually really beautiful🥰.
         we know ord('a') is 97 (ascii), so lets say the item is b the ascii of b is 98, when subtracted we have 1, so we increment the value of the element 
         at index 1 by one. 

         so basically we use this as a record keeper for char we've seen before. so at the end of the day we check if both records dic1 and dic2 are equal. 
         if equal it means its a valid anagram.
        '''
        for item in s:
            dic1[ord(item)-ord('a')] += 1 
        for item in t:
            dic2[ord(item)-ord('a')] += 1
        return dic1 == dic2


print(isAnagram('anagram', 'margana'))