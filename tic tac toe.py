from tkinter import *

def sum(a,b,c):
    a+b+c
    
def printboard(xstate,zstate):
    zero='X' if xstate[0] else('O' if zstate[0]else 0)
    one='X' if xstate[1] else('O' if zstate[1] else 1)
    two='X' if xstate[2] else('O' if zstate[2] else 2)
    three='X' if xstate[3] else('O' if zstate[3] else 3)
    four='X' if xstate[4] else('O' if zstate[4] else 4)
    five='X' if xstate[5] else('O' if zstate[5] else 5)
    six='X' if xstate[6] else('O' if zstate[6] else 6)
    seven='X' if xstate[7] else('O' if zstate[7] else 7)
    eight='X' if xstate[8] else('O' if zstate[8] else 8)
    
    if turn==1:
        b['text']='X'
    else:
        b['text']='O'
        
def checkwin(xstate,zstate):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
         if sum(xstate[win[0]], xstate[win[1]],xstate[win[2]])==3:
            print("X Won the Match")
            return 1
         if (sum(zstate[win[0]], zstate[win[1]],zstate[win[2]])==3):
            print("O Won the Match")
            return 0
    return -1

    if __name__=="__main__":
        xstate=[0,0,0,0,0,0,0,0,0]
        zstate=[0,0,0,0,0,0,0,0,0]
        turn=1


    while(True):
        printboard(xstate,zstate)
        if turn==1:
            print("X's Chance")
            xstate[value]=1
        else:
            print("O's Chance")
            zstate[value]=1

        cwin=checkwin(xstate,zstate)
        if cwin!= -1:
            print("Match Over")
        break
        turn=1-turn

root=Tk()
root.config(bg='blue')
root.geometry('500x550')

Label(text="Welcome to Tic Tac Toe",bg='blue',fg='white',font="times 20 bold").pack()

for row in range(3):
    f=Frame(bg='white')
    for cols in range(3):
        b=Button(f,command=checkwin,height=1,width=3,font='times 30',bg='blue',fg='white')
        b.pack(side='left',padx=9,pady=8)
    f.pack(padx=4)

printboard()


        
