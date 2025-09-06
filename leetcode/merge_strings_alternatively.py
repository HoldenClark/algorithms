class Solution:
    def merge_string_alternatively(self, str1: str, str2: str) -> str:
        # init return string
        res = ""

        # if input strings are of equal length then alternate adding to return string
        if len(str1) == len(str2):
            for i in range(len(str1)):
                res += str1[i]
                res += str2[i]

        # else if string1 is larger than string2 alternate adding to return string for length of the smaller string, then add remainder of string from larger string to the return string
        elif len(str1) > len(str2):
            for i in range(len(str2)):
                res += str1[i]
                res += str2[i]

            res += str1[len(str2):]

        # else if string2 is larger than string1 alternate adding to return string for length of the smaller string, then add remainder of string from larger string to the return string
        elif len(str2) > len(str1):
            for i in range(len(str1)):
                res += str1[i]
                res += str2[i]

            res += str2[len(str1):]
        
        return res
    


str1 = "abcdeffffffffffffffffff"
str2 = "fghzzzzzzz"

test = Solution()
print(test.merge_string_alternatively(str1, str2))