import random

def winner(player,computer):
    if player=="ROCK":
        if computer=="PAPER":
            print("Computer won")
            return 0
        elif computer=="SCISSORS":
            print("Player won")
            return 1
    elif player=="PAPER":
        if computer=="ROCK":
            print("Player won")
            return 1
        elif computer=="SCISSORS":
            print("Computer won")
            return 0
    elif player=="SCISSORS":
        if computer=="ROCK":
            print("Computer won")
            return 0
        elif computer=="Paper":
            print("Player won")
            return 1

def random_value():
    number=random.randint(1,3)
    result=number
    if result==1:
        result=str("ROCK")
        return result
    elif result==2:
        result=str("PAPER")
        return result
    elif result==3:
        result=str("SCISSORS")
        return result

score_player=0
score_computer=0

while(score_player<3 and score_computer<3):
    player_choice=input("Choose: ")
    player=player_choice.upper()
    computer=random_value()
    if(player!="ROCK" and player!="SCISSORS" and player!="PAPER"):
        print("Please enter rock,paper or scissors")
        continue
    else:
        if player==computer:
            print("DRAW!")
            continue
        elif(player!=computer):
            win=winner(player,computer)
            if win==1:
                score_player+=1
                continue
                
            elif win==0:
                score_computer+=1
                continue

if (score_player>score_computer):
    print("<=====RESULT=====>\nPlayer:{}\nComputer:{}".format(score_player,score_computer))
    print("PLAYER WON THE GAME!")
elif(score_player<score_computer):
    print("<=====RESULT=====>\nPlayer:{}\nComputer:{}".format(score_player,score_computer))
    print("COMPUTER WON THE GAME!")