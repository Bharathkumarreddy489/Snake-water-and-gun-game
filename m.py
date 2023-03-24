#importing random module
import random

def check(comp,user):
    if user==comp:
        return 0
    elif (comp==0 and user==1):
        return -1
    elif (comp==1 and user==2):
        return -1
    elif (comp==2 and user==0):
        return -1
    elif (comp==1 and user==0):
        return 1
    elif (comp==2 and user==1):
        return 1
    elif (comp==0 and user==2):
        return 1
    else: 
        return 5
#main
print("HEY FOLKS WELCOME TO SNAKE, WATER AND GUN GAME")
print()
print("Hey buddy you just 5 chances")
print()
for i in range(0,5):
    if i<5:
        comp=random.randint(0,2)
        print("Enter 0 for snake , 1 for water and 2 for gun:")
        user=int(input())
        print("user selection is>",user)
        print("System selection is>",comp)
        score=check(comp,user)
        if score==0:
            print("Match TIE")
        elif score==-1:
            print("YOU LOST")
        elif score==1:
            print("YOU WON")
        else:
            print("PLEASE SELECT VALID INPUT")
        
        
        
