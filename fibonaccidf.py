print("fibnacci sequence using do while")
a=int(input("fibnacci length series:"))
first=0
second=1
print(first)
print(second)
i=0
while(i<a-2):
    temp=first+second
    print(temp)
    first=second
    second=temp
    i=i+1
    
      
    
