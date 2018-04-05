#Problem Statement: 
'''Given a string of words, you need to find the highest scoring word.
Each letter of a word scores points according to it's position in the alphabet: a = 1, b = 2, c = 3 etc.
You need to return the highest scoring word as a string.
If two words score the same, return the word that appears earliest in the original string.
All letters will be lowercase and all inputs will be valid.'''

def high(data):
  ip=" abcdefghijklmnopqrstuvwxyz"
  res=[]
  ip1=data.split()   #convert string to list
  print(ip1)
  for word in ip1:
      var=sum(ip.index(letter) for letter in word)  #sum of index of each letter in string
      #print(var)
      res.append(var)          

  f=res.index(max(res))   #find index of max sum
  return ip1[f]             #return word with max sum
  
print(high("what time are we climbing up the volcano"))
