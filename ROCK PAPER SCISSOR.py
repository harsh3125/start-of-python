#     for playing with pc
import random
#   global varables for playing unlimited times 
play=True
#   global variables for counting the points
pc=0
player=0
    
def result():
    global play
    global pc
    global player
    print("THIS IS THE GAME OF ROCK PAPER SCISSOR")
    #    THIS IS THE WHILE LOOP FOR PLAYING UNLIMITED TIME
    while play:
        print("CHOOSE anything if you want to play else if you want to exit press 2")
        e=int(input())
        if e==2:
            play=False
            print("YOUR PC SCORES ARE:",pc)
            print("YOUR POINTS ARE:",player)
        else:
            game=['ROCK', 'PAPER', 'SCISSOR']
            a=random.choice(game)
            print("CHOOSE ANY AMONG ROCK PAPER AND SCISSOR")
            b=input()
            if a==b:
                a=random.choice(game)
                print("GAME TIE!")
            elif a=='ROCK' and b=='SCISSOR':
                print("YOU LOSE!")
                pc+=1
            elif a=='ROCK' and b=='PAPER':
                print("YOU WIN!")
                player+=1
            elif a=='PAPER' and b=='SCISSOR':
                print("YOU WIN!")
                player+=1
            elif a=='PAPER' and b=='ROCK':
                print("YOU LOSE!")
                pc+=1
            elif a=='SCISSOR' and b=='PAPER':
                print("YOU LOSE!")
                pc+=1
            elif a=='SCISSOR' and b=='ROCK':
                print("YOU WIN!")
                player+=1
    
result()