#==========================================================================================
# https://neetcode.io/problems/duplicate-integer?list=neetcode150
#
# we can solve this problem in O(n) time complexity by using a set an using a little bit \
# more space (O(n) space complexity). The set allows us to do lookups in O(1) time as \
# opposed to using a list where a line like 'if n in list' would cause the time complexity \
# of the overall problem to be O(n^2)
#
#==========================================================================================

class Solution:
    def contains_duplicate(self, nums: list[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)

        return False
    
test = Solution()
test_nums = [1,2,3,77,77,801,90001]

ans = test.contains_duplicate(test_nums)

print(ans)