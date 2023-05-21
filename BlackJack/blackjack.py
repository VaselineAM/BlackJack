import random
import os
from blackjackart import logo
hsf = {1:"h",2:"s",3:"h"}
hitorstandorforfeit=""
def sumofelements(array):
    sum=0
    for x in range(len(array)):
        sum = sum + array[x]
    return sum

def appendinglist(array,numberof11):
    randomnumber = random.randint(1,11)
    if randomnumber==11:
        if (sumofelements(array)+11)<=21 and numberof11==0:
            array.append(11)
            numberof11 = numberof11+1
        else:
            array.append(1)
    else:
        array.append(randomnumber)
    return array,numberof11

def print2(list_user,list_computer,numberof11_user,numberof11_computer):
    print(f"Your hand: {list_user} and your score is {sumofelements(list_user)}")
    print(f"Computer's hand: {list_computer} and computer's score is {sumofelements(list_computer)}\n")     

def wonorlost(won,list_user,list_computer,numberof11_user,numberof11_computer):
    print2(list_user,list_computer,numberof11_user,numberof11_computer)
    if won==True:
        print("You have won the game.\n")
    if won==False:
        print("You have lost the game.\n") 
    start()

def compare(list_user,list_computer,numberof11_user,numberof11_computer):
    if (sumofelements(list_computer))>21:
        wonorlost(True,list_user,list_computer,numberof11_user,numberof11_computer) 

    elif (sumofelements(list_computer))==21:
        wonorlost(False,list_user,list_computer,numberof11_user,numberof11_computer)

    elif sumofelements(list_user)>sumofelements(list_computer):
        wonorlost(True,list_user,list_computer,numberof11_user,numberof11_computer)
                
    elif sumofelements(list_user)<sumofelements(list_computer):
        wonorlost(False,list_user,list_computer,numberof11_user,numberof11_computer)

    elif sumofelements(list_user)==sumofelements(list_computer):
        print2(list_user,list_computer,numberof11_user,numberof11_computer)
        print("You have drawn the game.")
        start()

def initialplay():
    list_user=[]
    list_computer=[]
    numberof11_user=0
    numberof11_computer=0

    for x in range(2):
        list_user,numberof11_user=appendinglist(list_user,numberof11_user)
        list_computer,numberof11_computer=appendinglist(list_computer,numberof11_computer)

    print(f"Your initial hand: {list_user} and your score is {sumofelements(list_user)}")
    print(f"Computer's initial hand: {list_computer} and computer's score is {sumofelements(list_computer)}\n")

    if sumofelements(list_user)==21:
        wonorlost(True,list_user,list_computer,numberof11_user,numberof11_computer)
    elif sumofelements(list_computer)==21:
        wonorlost(False,list_user,list_computer,numberof11_user,numberof11_computer)

    play(list_user,list_computer,numberof11_user,numberof11_computer)  

def play(list_user,list_computer,numberof11_user,numberof11_computer):     

    hitorstandorforfeit = input("Press H to hit, S to stand, F to forfeit:  ").lower()

    if hitorstandorforfeit == "h":

        if sumofelements(list_user)>21:
            wonorlost(False,list_user,list_computer,numberof11_user,numberof11_computer)

        elif sumofelements(list_user)==21:
            wonorlost(True,list_user,list_computer,numberof11_user,numberof11_computer)

        else:
            list_user, numberof11_user = appendinglist(list_user,numberof11_user)
            print2(list_user,list_computer,numberof11_user,numberof11_computer)
            if sumofelements(list_user)>21:
                wonorlost(False,list_user,list_computer,numberof11_user,numberof11_computer)

            elif sumofelements(list_user)==21:
                wonorlost(True,list_user,list_computer,numberof11_user,numberof11_computer)
            play(list_user,list_computer,numberof11_user,numberof11_computer)

    elif hitorstandorforfeit == "s":

        randomhsf = random.randint(1,2)
        list_computer, numberof11_computer = appendinglist(list_computer,numberof11_computer)

        if hsf[randomhsf] == "h":
            while hsf[randomhsf] == "h":
                randomhsf = random.randint(1,2)
                print2(list_user,list_computer,numberof11_user,numberof11_computer)                
                compare(list_user,list_computer,numberof11_user,numberof11_computer)                
                list_computer, numberof11_computer = appendinglist(list_computer,numberof11_computer)
                if sumofelements(list_computer)<12:randomhsf=1

        elif hsf[randomhsf] == "s":
            compare(list_user,list_computer,numberof11_user,numberof11_computer)
            print2(list_user,list_computer,numberof11_user,numberof11_computer)
            play(list_user,list_computer,numberof11_user,numberof11_computer)
            print2(list_user,list_computer,numberof11_user,numberof11_computer)
    else:
        start()
            
def start():
    if input("\nDo you want to play a game of blackjack? Y or N:  ").lower()=='y':
        os.system('clear')
        print(logo)
        initialplay()
    else:
        exit()
start()    
