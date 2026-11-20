class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<0:
            return False
        sum=0
        i=1
        for i in range (1,int(num**0.5)+1):
            if num%i==0:
                sum+=i
                if (i*i)!=num:
                    sum+=num//i

        return sum-num==num

        