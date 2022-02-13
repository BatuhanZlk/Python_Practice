def leap_year_control(year):
    if(year%100==0):
        if (year%400==0):
            if(year%4000==0):
                return 0
            else:
                return 1
        else:
            return 0
    elif(year%4==0):
        return 1
    else:
        return 0


try:
    year=int(input("Enter year: "))
    result=leap_year_control(year)
    if result==1:
        print("Leap Year!")
    elif result==0:
        print("Not Leap Year!")
    else:
        pass
except ValueError:
    print("Enter a year!")