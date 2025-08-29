#==========================================================================================
# https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion/description/
#
# this problem is pretty straight forward if you know how to convert from decimal to \
# hexadecimal by hand. Set up a function you can call that takes in the base as parameter \
# that way you can just call the same function twice or however many times you would like \
# instead of having to rewrite the conversion logical multiple times. For this problem \
# you need to apply an exponent to the given number so I added that as a paramter for my \
# convert decimal function as well. the logic for converted is to divide the number by the \
# base you are converting to and the remainder of that division each time is a digit in \
# the conversion. the quotient is what you will divide by the base next so you continue to \
# divide and take the remainder and build your string, hexadecimal number with it until \
# the quotient you have left is less than the base and then you add that on to your string.
# after the conversion logical for this problem concatenate the strings received from \
# hexadecimal and hextrigesmal and return on string as the solution to the problem.
#==========================================================================================

class Solution:
    def concatHex36(self, n: int) -> str:
        
        # need function to find decimal -> conversion based on base input -> conversion: str
        def convertDecimal(n: int, base: int, exp: int) -> str:
            num_after_exp = n ** exp
            build = ""

            digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", \
                       "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", \
                        "S", "T", "U", "V", "W", "X", "Y", "Z"]

            while num_after_exp >= base:
                div = num_after_exp // base
                modulo = num_after_exp % base
                num_after_exp = div
                build += digits[modulo]

            build += digits[num_after_exp]
            
            return build[::-1]


        # need to store conversions and concat
        hexadecimal = convertDecimal(n, 16, 2)
        hexatrigesmal = convertDecimal(n, 36, 3)

        return hexadecimal + "" + hexatrigesmal
    

test = Solution()

n = 13

print(test.concatHex36(n))