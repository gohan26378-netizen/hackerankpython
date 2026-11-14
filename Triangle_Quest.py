#Write a Python program to print a numerical triangle pattern in which each row displays the row number repeated according to its position.#
for i in range(1, int(input()) + 1):
    print(i * (10**i - 1) // 9)