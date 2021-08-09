def leapYears(years):
    leap = False
    if(years%400 == 0):
        leap = True
    elif years%4 == 0 and years%100 != 0:
                leap = True
    return leap
years = int(input())
print(leapYears(years))
""" years = int(input())
if (years%4 == 0):
    if(years%100 == 0):
        if(years%400 == 0):
            print("This years is leap year ")
        else:
            print("This years is not leap year")
    else:
        print("This years is not leap year")    
else:
    print("This  years is not leap year") """


""" def leapYears(years):
    leap = False
    if (years%4 == 0):
        if(years%100 == 0):
            if(years%400 == 0):
                leap = True
            else:
                leap= False
        else:
            leap= False   
    else:
        leap = False
    return leap
years = int(input())
leapYears(years) """

""" def is_leap(year):
    leap = False
    if (year%4 == 0):
        leap = True
        if(year%100 ==0):
            leap = False
        if(year%400 == 0):
            leap = True
    return leap
is_leap(year)
year = int(input()) """
