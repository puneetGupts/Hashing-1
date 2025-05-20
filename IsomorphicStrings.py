# Explain your approach in **three sentences only** at top of your code m len(list) n avg len(string)
# Approach 1 - push into hashmap key from s1 and value from s2 and keep track if key in s2 is already mapped using set return false if key in s1 is mapped to diff valu or value is already mapped to some key in s1
# approach 2 - similar to 1 instead of hashmap and set use 2 hashmap
# approach 3 - use a count array to store the mappings

from typing import List

# Approach 1
# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         hashMap = {}
#         hashSet = set()
#         i = 0
#         while i < len(s):
#             if not hashMap.get(s[i]):
#                 if t[i] not in hashSet:
#                     hashMap[s[i]]= t[i]
#                     hashSet.add(t[i])
#                     i+=1 
#                     continue
#                 else:
#                     return False
#             elif hashMap.get(s[i])!= t[i]:
#                 return False
#             else:
#                 i+=1
#                 continue
#         return True

# Approach 2
# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         sMap, tMap = {},{}
#         sl = len(s)
#         for i in range(sl):
#             sChar = s[i]
#             tChar = t[i]
#             if sChar in sMap:
#                 # value is diff from tChar
#                 if sMap.get(sChar)!=tChar:
#                     return False
#             else:
#                 sMap[sChar] = tChar
                
#             if tChar in tMap:
#                 # value is diff from sChar
#                 if tMap.get(tChar)!=sChar:
#                     return False
#             else:
#                 tMap[tChar] = sChar
#         return True
        
            
# Approach 3
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMap,tMap = [0]*256, [0]*256
        for i in range(len(s)):
            schar,tchar = s[i],t[i]
            if sMap[ord(schar) - ord(' ')] == 0:
                sMap[ord(schar) - ord(' ')] = tchar
            elif sMap[ord(schar) - ord(' ')] != tchar:
                return False
            
            if tMap[ord(tchar) - ord(' ')] == 0:
                tMap[ord(tchar) - ord(' ')] = schar
            elif tMap[ord(tchar) - ord(' ')] != schar:
                return False
        return True

sol = Solution()
s = 'abcd'
t = 'mnfm'
print(sol.isIsomorphic(s, t))