#!/usr/bin/python3

# calculate using Lebniz formula

# Initialize denominator
k = 1
 
# Initialize sum
s = 0
 
# calc to 100M models
for i in range(100000000):
  # even index elements are positive
  if i % 2 == 0:
    s += 4/k
  else:
    # odd index elements are negative
    s -= 4/k
 
  # denominator is odd
  k += 2
     
print(s)
