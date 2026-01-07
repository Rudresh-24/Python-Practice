print("sum of individuals digits of a given number")
num=int(input("Enter a number: "))
sum=0
num1=num
while num>=1:
    r=num%10
    sum=sum+r
    num=int(num/10)
print("The sum of {} is : {}".format(num1,sum))
