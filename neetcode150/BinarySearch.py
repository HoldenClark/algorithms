#==========================================================================================
# https://neetcode.io/problems/binary-search?list=neetcode150
#
# use binary search to find a target number in a _sorted_ list in O(logN) time complexity
# 
# we set the middle index to be (left + right) // 2
# if the number at that middle index is smaller than the target we know that we must \
# search the right partition as the target can not be in the left partition so to \
# eliminate the left partition we set left to middle + 1 and recalculate the middle \
# index. We do the same for the right but set it to the middle - 1 if the number at \
# the middle index is greater than the target. If at any point the number at the mid \
# index is the same as the target we return the middle index as the problem is looking \
# for us to return an int that represents the index at which the target is in the list \
# if at any point the left index through our iteration becomes greater than the right \
# index then we have found that the target does _not_ exist in the given array and \
# return -1 as specified in the problem statement.
#==========================================================================================


class Solution:
    def binary_search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
            
        return -1
    
test_nums = [2,3,66,130,234,499]
test_target = 66

test = Solution()

ans = test.binary_search(test_nums, test_target)

print(ans)