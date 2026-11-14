#Write a Python function to check whether a given year is a leap year or not using the Gregorian calendar rules. Return True if it is a leap year; otherwise, return False.#
def is_leap(year):
    leap = False
    
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        leap=True
    else:
       leap=False
    
    return leap

year = int(input())