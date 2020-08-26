ar =[' ',' ',' ',' ',' ',' ',' ',' ',' ']

def initialize():
    for i in range(9):
        ar[i] = str(i+1)
    display()

def chance_x(num):
    ar[num-1]='X'
    display()

def chance_o(num):
    ar[num-1]='O'
    display()

def check():
    if ar[0]==ar[1]==ar[2] or ar[3]==ar[4]==ar[5] or ar[6]==ar[7]==ar[8]:
        return True
    elif ar[0]==ar[3]==ar[6] or ar[1]==ar[4]==ar[7] or ar[2]==ar[5]==ar[8]:
        return True
    elif ar[0]==ar[4]==ar[8] or ar[2]==ar[4]==ar[6]:
        return True
    else:
        return False

def tie():
    for i in range(9):
        if not ar[i].isalpha():
            return False
    return True


def play():
    print("Begin game \n")
    turn = 'o'
    while not check() and not tie():
        if turn == 'o':
            num = int(input("Position: "))
            chance_x(num)
            turn = 'x'
        elif turn == 'x':
            num = int(input("Position: "))
            chance_o(num)
            turn = 'o'
    return turn

def winner(turn):
    print(turn.upper(),"has won the game!!")
    for i in range(9):
        ar[i] = turn.upper()
    display()

def display():
    print(ar[0],"  "+ar[1]+"  "+ar[2]+"   \n")
    print(ar[3],"  "+ar[4]+"  "+ar[5]+"   \n")
    print(ar[6],"  "+ar[7]+"  "+ar[8]+"   \n")

def main():
    initialize()
    x = play()
    if tie():
        print("It is a tie!")
    else:
        winner(x)
    while input("Play Again? (Y/N): ").upper()=='Y':
        initialize()
        x = play()
        if tie():
            print("It is a tie!")
        else:
            winner(x)


if __name__ == "__main__":
    main()
