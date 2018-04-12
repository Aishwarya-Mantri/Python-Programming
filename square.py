# find the nearest square number of a given positive integer n.
'''example :nearest_sq(2), 1)
            nearest_sq(10), 9)
            nearest_sq(111), 121) '''

import math

def nearest_sq(n):
  n1=math.floor(n**0.5)  
  smin=n1**2
  smax=(n1+1)**2
  return smin if n-smin < smax-n else smax
  #return round(n ** 0.5) ** 2

print(nearest_sq(111))
  
