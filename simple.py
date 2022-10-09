def simple_intrest(p,n,r):
    simpleintrest = int(p*n*r)/100
    return simpleintrest
a=int(input("Enter the value of principal amount"))
b=int(input("Enter the value of year"))
c=int(input("Enter the value of rate of intrest"))
print(simple_intrest(a,b,c))
