'''Problem Statement: The key for each list in the dictionary should be the number.
The list associated with each key should possess the factors for the number.
If a number possesses no factors (only 1 and the number itself),
the list for the key should state 'None'. '''

def factorsRange(n, m):
    a={}
    for k in range(n,m+1):
        key=k
        a.setdefault(key, [])
        for v in range(2,k):
            if k%v==0:
                a[k].append(v)
        if a[k]==[]:
            a[k]=['None']
    return a
print(factorsRange(2,6))

#Output: {2: ['None'], 3: ['None'], 4: [2], 5: ['None'], 6: [2, 3]}
