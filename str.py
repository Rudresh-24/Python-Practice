str = input()
n = len(str)
for i in range(1,n,2):
    print(str[i],end=" ")
for j in range(0,n,2):
    print(str[j],end=" ")
