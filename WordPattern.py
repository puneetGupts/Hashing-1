# Explain your approach in **three sentences only** at top of your code m len(list) n avg len(string)
# similar to isomorphic strings # use 2 hashMaps to keep track of similar keys

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pMap , sMap = {} ,{}
        splitArray = s.split(" ")
        plen, slen = len(pattern), len(splitArray)
        if plen!=slen:
            return False
        for i in range(plen):
            pChar = pattern[i]
            sString = splitArray[i]
            if pChar in pMap:
                if pMap.get(pChar) != sString:
                    return False
            else:
                pMap[pChar] = sString

            if sString in sMap:
                if sMap.get(sString) != pChar:
                    return False
            else:
                sMap[sString] = pChar
        return True
            
            
        
