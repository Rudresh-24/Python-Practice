temp=input("enter the temperature in celsius or fahreheit:")
d=int(temp[:-1])
i=temp[-1]
if i.upper()=="C":
    r=int(round(d*9)/(5+32))
    h="Fahreheit"
elif i.upper()=="F":
    r=int(round(d-32)*(5/9))
    h="Celsius"
print("the temperature in{h} is {r}degrees")
