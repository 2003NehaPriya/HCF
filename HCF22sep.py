a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
if(a<b):
    x=a
else:
    x=b
i=1
while(i<=x):
    if(a%i==0 and b%i==0):
        hcf=i
    i+=1
print("HCF:",hcf)
