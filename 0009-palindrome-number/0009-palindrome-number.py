class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        rev=0
        i=x
        while i>0:
            digit=i%10
            rev=rev*10+digit
            i=i//10
        return x==rev

        