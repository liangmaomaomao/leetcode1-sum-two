#brutal
#time complexity: O(n2)
#space complexity: O(1)

#define class
class Solution:
#define object methods, alternative: def twoSum(self, nums, target):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#define a list
         result = []
         for i in range(0, len(nums)):
             for j in range(i+1,len(nums)):
                 total = nums[i] + nums[j]
                 if total == target:
                     result.append(i);
                     result.append(j);
                     return result 

#hashmap
#time complexity: O(n)
#space complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#define a dict
         prevHash = {}
#enumerate loop      
         for i, n in enumerate(nums):
             diff = target - n
             if diff in prevHash:
                   return [prevHash[diff], i]
             prevHash[n] = i
         return
         
         
         
#detect by pairs with for-loop
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)   #to count the number of the elements in the list
        for i in range(n):   #to use for-loop to detect one by one
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []    #no result returns empty
        
        
#detect and store in dictionary at the same time(dic looking-for time complexity is 1)

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()   #construct a dictionary
        for i, num in enumerate(nums):  #this will get the (0,1,2...)index and the element in it simultaneously
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []
        
what we have learned: hash table definition/use it to reduce the time complexity, which use the formal information.

A hash table (hash map) is a data structure that can map keys to values.
A hash table uses a hash function to compute an index, also called a hash value, into an array of buckets or slots, from which the desired value can be found.



