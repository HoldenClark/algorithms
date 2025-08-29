#==========================================================================================
# https://neetcode.io/problems/buy-and-sell-crypto?list=neetcode150
#
# for this problem we need to find the max profit we can make by selling low and buying \
# high for one value each from prices. we can use a sliding window to find the max price \
# we start both left and right pointers at the beginning of the list and always increment \
# right by one, and check for the diff between right and left, if the diff is greater that \
# our max profit we store this as the new max profit. we move the left pointer to where \
# the right pointer is if the right pointer's value is smaller than the current value \
# of the left pointer. this is because we want to buy as low as possible and if the left \
# pointer is our buy pointer.
#==========================================================================================

class Solution:
    def buy_and_sell_stock(self, prices: list[int]) -> int:
        maxPrice = 0
        left, right = 0, 0

        while right < len(prices) - 1:
            price = prices[right] - prices[left]
            maxPrice = max(maxPrice, price)

            right += 1
            if prices[right] < prices[left]:
                left = right

        return maxPrice
    

prices = [33,23,37,38,41,40,49,45,38,33]

test = Solution()

print(test.buy_and_sell_stock(prices))