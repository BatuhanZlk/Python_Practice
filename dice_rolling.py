import random
import sys
import time

def dice_roller():
    result=random.randint(1,6)
    return result

dıce_rolling_program=("<=========================DICE_ROLLING_PROGRAM=========================>\n")
welcome=("\"Welcome to dice rolling program...\"\n")
for letter in dıce_rolling_program:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.01)
for letter in welcome:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.02)
while(True):
    question=("\"Do you want dice roll?\" (y/n): ")
    for letter in question:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)
    answer1=input()
    if answer1.lower()=="y":
        dice=dice_roller()
        print(dice)
        continue
    if answer1.lower()=="n":
        break
    else:
        inform=("Enter y or n.\n")
        for letter in inform:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.02)
        

