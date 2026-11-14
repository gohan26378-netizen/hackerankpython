#Write a Python program to print all integers from 1 to a given number \(n\) consecutively without spaces or using any string methods.#
n = int(input())
for i in range(1,n+1):
 print(i,end="")