#Python If-Else – Weird or Not Weird

#Given a positive integer n, determine whether the number is weird or not based on the following conditions:
#1. If n is odd, print Weird.
#2. If n is even and between 2 and 5 (inclusive), print Not Weird.
#3. If n is even and between 6 and 20 (inclusive), print Weird.
#4. If n is even and greater than 20, print Not Weird.
n = int(input("enter a number"))
if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")
