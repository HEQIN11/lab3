
# Author: heqin wang hbw5248@psu.edu
# Collaborator:Anthony Aguilar axa6168@psu.edu
# Collaborator:Bryce Awono bna5160@psu.edu
# Section: 12
# Breakout: 12
def sum_n(n):
  if (n==0):
    return 0 
  else:
    return n + sum_n(n-1)

def print_n(s,n):
  if (n==0):
    return
  else:
    print(s)
    print_n(s,n-1)

def run():
  a=input("Enter an int: ")
  b=int(a)
  print(f"sum is {sum_n(b)}.")
  c=input("Enter a string: ")
  d=str(c)
  print_n(d,b)

if  __name__=="__while__":
  run()
