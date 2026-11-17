#Python – Loops
#Given a non-negative integer n, print the square of each non-negative integer that is less than n, starting from 0.
#Print each square on a separate line.
n = int(input("enter a number"))
for i in range(0,21):
 if i<n:
  print(i**2)
