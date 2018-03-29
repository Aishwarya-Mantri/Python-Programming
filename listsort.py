def sorter(textbooks):
    return sorted(textbooks,key=str.lower)
    
print(sorter(['Algebra', 'history', 'Geometry', 'english']))
