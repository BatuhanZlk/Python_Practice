import sys
import time
def fibonacci():

    fibonacci_list=[]
    first_number=0
    second_number=1
    x=0
    fibonacci_list.append(first_number)
    fibonacci_list.append(second_number)

    while(x<20):    #First 20 number
        third_number=second_number+first_number
        first_number=second_number
        second_number=third_number
        fibonacci_list.append(third_number)
        fibonacci_list.append(second_number)
        fibonacci_list.append(first_number)
        x+=1
    return fibonacci_list
try:
    fibonacci_fonk=fibonacci()
    text0=("Enter a number: ")
    for i in text0:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.02)
    number=int(input())

    if number in fibonacci_fonk:
        text1=("The number is in fibonacci sequence.")
        for i in text1:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.02)
    else:
        text2=("The number is not in fibonacci sequence.")
        for i in text2:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.02)
except (ValueError):
    text3=("Please enter a number.")
    for i in text3:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.02)