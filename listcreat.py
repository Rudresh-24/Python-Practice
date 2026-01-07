a=int(input("enter the size of list"))
u=[]
for i in range(a):
    element=input("enter the {} element : ".format(i))
    u.append(element)
print("the elements in list are :\n",end=" ")
for element in u:
    print(element,end=" ")
                  
