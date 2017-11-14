import enchant
d=enchant.Dict("en_UK") #create dictionary for UK English
from itertools import permutations
data=['a','b','c','d','e','f','g','h','i']  #input
print data
res1=list(permutations(data,4)) #calculates all possible 4 letters combination
ip=[]
result=[]
for i in res1:
    ip.append(''.join(i)) #convert list to string and stores it in ip
for k in ip:
    if d.check(k) == True:  #check whether the word is valid english word or not
        if k in result:
            pass         #pass if the word already exists in result list
        else:
            result.append(k)
print result   #print all 4 letters english word formed from given list
    



