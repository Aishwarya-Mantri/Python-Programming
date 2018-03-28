#The parameter of the function findNb (num) will be an integer m
#you have to return the integer n such as n^3 + (n-1)^3 + ... + 1^3 = m if such a n exists or -1 if there is no such n.

def find_nb(m):
    sum=0
    n=1
    while sum<m:
        sum=sum+(n**3)
        n+=1
    if sum==m:
        return n-1
    else:
        return -1
print(find_nb(441))
