# Explain your approach in **three sentences only** at top of your code m len(list) n avg len(string)
# 1) approach 1 we sort the string create maps using sorted string and then hash anagrams o(m*nlog(n))
# 2) approach 2 we count freq of each char store in a list and then hash string with same freq or countarray o(m*n*26)
# 3) create our own hashfunc map string to same hash and return the list same time as 2)

from typing import List
from collections import defaultdict

# Approach 1
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = defaultdict(list)
#         for s in strs:
#             sortedString = ''.join(sorted(s))
#             res[sortedString] .append(s)
#         return list(res.values())


# Approach 2
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = defaultdict(list) #Mapping characterCount to s list of anagrams 
#         for s in strs:
#             count = [0]*26
#             for c in s:
#                 count[ord(c) - ord('a')]+=1
#             res[tuple(count)].append(s) #def dict handles is key is not in hashmap case
#         return list(res.values()) # return list of values of map

#Approach 3
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            primeProduct = self.primeProduct(s)
            res[primeProduct].append(s)
        return list(res.values())

    def primeProduct(self,s):
        prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103]
        result = 1.0
        for c in s:
            result*=prime[ord(c)-ord('a')]
        return result


sol = Solution()
anagrams = sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
for l in anagrams:
    for s in l:
        print(s, end=" ")
    print("\n")
