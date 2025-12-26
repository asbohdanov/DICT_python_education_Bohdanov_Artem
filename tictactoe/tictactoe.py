cels=input("Enter cells:>")
def celsout():
    print("---------")
    print("|", cels[0], cels[1], cels[2], "|")
    print("|", cels[3], cels[4], cels[5], "|")
    print("|", cels[6], cels[7], cels[8], "|")
    print("---------")
x_win=0
o_win=0
def wincheck():
    if cels[0]==cels[4]==cels[8] or cels[1]==cels[4]==cels[7] or cels[3]==cels[4]==cels[5] or cels[2]==cels[4]==cels[6] or cels[0]==cels[3]==cels[6] or cels[2]==cels[5]==cels[8] or cels[0]==cels[1]==cels[2] or cels[6]==cels[7]==cels[8]:
        if cels[4]=="X" or cels[3]=="X" or cels[5]=="X" or cels[1]=="X" or cels[7]=="X":
            x_win=1
        elif cels[4]=="O" or cels[3]=="O" or cels[5]=="O" or cels[1]=="O" or cels[7]=="O":
            o_win=1
while x_win==0 and o_win==0:
    user_cell=input("Enter the coordinates:>")
    if user_cell[0].isdigit()==False or user_cell[2].isdigit()==False:
        print("You should enter numbers!")
    elif int(user_cell[0])>3 or int(user_cell[2])>3:
        print("Coordinates should be from 1 to 3!")
    elif :
        print("This cell is occupied! Chose another one!")
    celsout()
    wincheck()
if x_win==1:
    print("X wins")
elif o_win==1:
    print("O wins")