def display(R1,R2,R3):
    for i in [R1,R2,R3]:
        for j in range(3):
            print(i[j],end="|")
        if i==R3:
            print("\n")
            break
        else:
            print("\n---------------")
ch=input("Do u wish to play single player(type S) or multi player(type M)???")
if ch in "Ss":
    import random 
    R1=["   ","   ","   ",1]
    R2=["   ","   ","   ",2]
    R3=["   ","   ","   ",3]
    display(R1,R2,R3)
    for i in range(4):
        while True:
            print("1st player")
            r=int(input("Enter rowno"))
            c=int(input("Enter column no"))
            if c>0 and c<4:
                if r==1:
                    if R1[c-1][1] in "XxOo" in "XxOo":
                        print("Cant overwrite pls play again")
                        continue
                    else:
                        R1[c-1]=" X "
                        break
                elif r==2:
                    if R2[c-1][1] in "XxOo" in "XxOo":
                        print("Cant overwrite pls play again")
                        continue
                    else:
                        R2[c-1]=" X "
                        break
                elif r==3:
                    if R3[c-1][1] in "XxOo" in "XxOo":
                        print("Cant overwrite pls play again")
                        continue
                    else:
                        R3[c-1]=" X "
                        break
                else:   
                    print("Row not defined")
            else:
                print("Column not defined")
       
        if R1==[" X "," X "," X ",1] or R2==[" X "," X "," X ",2] or R3==[" X "," X "," X ",3]:
            print("Player 1 wins")
            break
        elif R1[0]==" X " and R2[0]==" X " and R3[0]==" X ":
            print("Player 1 wins")
            break
        elif R1[1]==" X " and R2[1]==" X " and R3[1]==" X ":
            print("Player 1 wins")
            break
        elif R1[2]==" X " and R2[2]==" X " and R3[2]==" X ":
            print("Player 1 wins")
            break
        elif R1[0]==" X " and R2[1]==" X " and R3[2]==" X ":
            print("Player 1 wins")
            break
        elif R1[2]==" X " and R2[1]==" X " and R3[0]==" X ":
            print("Player 1 wins")
            break
        else:
            None
        for j in range(1):
                for i in range(1):
                    print("COMPUTER")
                    if R1[0]==" X " and R1[1]==" X ":
                        if R1[2][1] in "XxOo":
                            None
                        else:
                            R1[2]=" O "
                            break
                    if R1[1]==" X " and R1[2]==" X ":
                        if R1[0][1] in "XxOo":
                            None
                        else:            
                            R1[0]=" O "
                            break
                    if R1[0]==" X " and R1[2]==" X ":
                        if R1[1][1] in "XxOo":
                            None
                        else:
                            R1[1]=" O "
                            break
                    if R2[0]==" X " and R2[1]==" X ":
                        if R2[2][1] in "XxOo":
                            None
                        else:
                            R2[2]=" O "
                            break
                    if R2[1]==" X " and R2[2]==" X ":
                        if R2[0][1] in "XxOo":
                            None
                        else:
                            R2[0]=" O "
                            break
                    if R2[0]==" X " and R2[2]==" X ":
                        if R2[1][1] in "XxOo":
                            None
                        else:
                            R2[1]=" O "
                            break
                    if R3[0]==" X " and R3[1]==" X ":
                        if R3[2][1] in "XxOo":
                            None
                        else:
                            R3[2]=" O "
                            break
                    if R3[1]==" X " and R3[2]==" X ":
                        if R3[0][1] in "XxOo":
                            None
                        else:
                            R3[0]=" O "
                            break
                    if R3[0]==" X " and R3[2]==" X ":
                        if R3[1][1] in "XxOo":
                            None
                        else:
                            R3[1]=" O "
                            break
                    if R1[0]==" X " and R2[0]==" X ":
                        if R3[0][1] in "XxOo":
                            None
                        else:
                            R3[0]=" O "
                            break
                    if R1[0]==" X " and R3[0]==" X ":
                        if R2[0][1] in "XxOo":
                            None
                        else:
                            R2[0]=" O "
                            break
                    if R2[0]==" X " and R3[0]==" X ":
                        if R1[0][1] in "XxOo":
                            None
                        else:
                            R1[0]=" O "
                            break
                    if R1[1]==" X " and R2[1]==" X ":
                        if R3[1][1] in "XxOo":
                            None
                        else:
                            R3[1]=" O "
                            break
                    if R1[1]==" X " and R3[1]==" X ":
                        if R1[1][1] in "XxOo":
                            None
                        else:
                            R1[1]=" O "
                            break
                    if R2[1]==" X " and R3[1]==" X ":
                        if R1[1][1] in "XxOo":
                            None
                        else:
                            R1[1]=" O "
                            break
                    if R1[2]==" X " and R2[2]==" X ":
                        if R3[2][1] in "XxOo":
                            None
                        else:
                            R3[2]=" O "
                            break
                    if R1[2]==" X " and R3[2]==" X ":
                        if R2[2][1] in "XxOo":
                            None
                        else:
                            R2[2]=" O "
                            break
                    if R2[2]==" X " and R3[2]==" X ":
                        if R1[2][1] in "XxOo":
                            None
                        else:
                            R1[2]=" O "
                            break
                    if R1[0]==" X " and R2[1]==" X ":
                        if R3[2][1] in "XxOo":
                            None
                        else:
                            R3[2]=" O "
                            break
                    if R1[0]==" X " and R3[2]==" X ":
                        if R2[1][1] in "XxOo":
                            None
                        else:
                            R2[1]=" O "
                            break
                    if R2[1]==" X " and R3[2]==" X ":
                        if R1[0][1] in "XxOo":
                            None
                        else:
                            R1[0]=" O "
                            break
                    if R3[0]==" X " and R2[1]==" X ":
                        if R1[2][1] in "XxOo":
                            None
                        else:   
                            R1[2]=" O "
                            break
                    if R3[0]==" X " and R1[2]==" X ":
                        if R2[1][1] in "XxOo":
                            None
                        else:
                            R2[1]=" O "
                            break
                    if R2[1]==" X " and R1[2]==" X ":
                        if R3[1][1] in "XxOo":
                            None
                        else:   
                            R3[1]=" O "
                            break
                    if R1[0]==" X " and R2[1]==" X ":
                        if R3[2][1] in "XxOo":
                            None
                        else:
                            R3[2]=" O "
                            break
                    if R1[0]==" X " and R3[2]==" X ":
                        if R2[1][1] in "XxOo":
                            None
                        else:   
                            R2[1]=" O "
                            break
                    if R2[1]==" X " and R3[2]==" X ":
                        if R1[1][1] in "XxOo":
                            None
                        else:
                            R1[1]=" O "
                            break 
                    if R1[0]==" O " and R1[1]==" O ":
                        if R1[2][1] in "XxOo":
                            None
                        else:
                            R1[2]=" O "
                            break
                    if R1[1]==" O " and R1[2]==" O ":
                        if R1[0][1] in "XxOo":
                            None
                        else:            
                            R1[0]=" O "
                            break
                    if R1[0]==" O " and R1[2]==" O ":
                        if R1[1][1] in "XxOo":
                            None
                        else:
                            R1[1]=" O "
                            break
                    if R2[0]==" O " and R2[1]==" O ":
                        if R2[2][1] in "XxOo":
                            None
                        else:
                            R2[2]=" O "
                            break
                    if R2[1]==" O " and R2[2]==" O ":
                        if R2[0][1] in "XxOo":
                            None
                        else:
                            R2[0]=" O "
                            break
                    if R2[0]==" O " and R2[2]==" O ":
                        if R2[1][1] in "XxOo":
                            None
                        else:
                            R2[1]=" O "
                            break
                    if R3[0]==" O " and R3[1]==" O ":
                        if R3[2][1] in "XxOo":
                            None
                        else:
                            R3[2]=" O "
                            break
                    if R3[1]==" O " and R3[2]==" O ":
                        if R3[0][1] in "XxOo":
                            None
                        else:
                            R3[0]=" O "
                            break
                    if R3[0]==" O " and R3[2]==" O ":
                        if R3[1][1] in "XxOo":
                            None
                        else:
                            R3[1]=" O "
                            break
                    if R1[0]==" O " and R2[0]==" O ":
                        if R3[0][1] in "XxOo":
                            None
                        else:
                            R3[0]=" O "
                            break
                    if R1[0]==" O " and R3[0]==" O ":
                        if R2[0][1] in "XxOo":
                            None
                        else:
                            R2[0]=" O "
                            break
                    if R2[0]==" O " and R3[0]==" O ":
                        if R1[0][1] in "XxOo":
                            None
                        else:
                            R1[0]=" O "
                            break
                    if R1[1]==" O " and R2[1]==" O ":
                        if R3[1][1] in "XxOo":
                            None
                        else:
                            R3[1]=" O "
                            break
                    if R1[1]==" O " and R3[1]==" O ":
                        if R1[1][1] in "XxOo":
                            None
                        else:
                            R1[1]=" O "
                            break
                    if R2[1]==" O " and R3[1]==" O ":
                        if R1[1][1] in "XxOo":
                            None
                        else:
                            R1[1]=" O "
                            break
                    if R1[2]==" O " and R2[2]==" O ":
                        if R3[2][1] in "XxOo":
                            None
                        else:
                            R3[2]=" O "
                            break
                    if R1[2]==" O " and R3[2]==" O ":
                        if R2[2][1] in "XxOo":
                            None
                        else:
                            R2[2]=" O "
                            break
                    if R2[2]==" O " and R3[2]==" O ":
                        if R1[2][1] in "XxOo":
                            None
                        else:
                            R1[2]=" O "
                            break
                    if R1[0]==" O " and R2[1]==" O ":
                        if R3[2][1] in "XxOo":
                            None
                        else:
                            R3[2]=" O "
                            break
                    if R1[0]==" O " and R3[2]==" O ":
                        if R2[1][1] in "XxOo":
                            None
                        else:
                            R2[1]=" O "
                            break
                    if R2[1]==" O " and R3[2]==" O ":
                        if R1[0][1] in "XxOo":
                            None
                        else:
                            R1[0]=" O "
                            break
                    if R3[0]==" O " and R2[1]==" O ":
                        if R1[2][1] in "XxOo":
                            None
                        else:   
                            R1[2]=" O "
                            break
                    if R3[0]==" O " and R1[2]==" O ":
                        if R2[1][1] in "XxOo":
                            None
                        else:
                            R2[1]=" O "
                            break
                    if R2[1]==" O " and R1[2]==" O ":
                        if R3[1][1] in "XxOo":
                            None
                        else:   
                            R3[1]=" O "
                            break
                    if R1[0]==" O " and R2[1]==" O ":
                        if R3[2][1] in "XxOo":
                            None
                        else:
                            R3[2]=" O "
                            break
                    if R1[0]==" O " and R3[2]==" O ":
                        if R2[1][1] in "XxOo":
                            None
                        else:   
                            R2[1]=" O "
                            break
                    if R2[1]==" O " and R3[2]==" O ":
                        if R1[1][1] in "XxOo":
                            None
                        else:
                            R1[1]=" O "
                            break
                else:
                    while True:
                        r=random.randint(1,3)
                        c=random.randint(1,3)
                        if r==1:    
                            if R1[c-1][1] in "XxOo":
                                continue
                            else:
                                R1[c-1]=" O "
                                break
                        elif r==2:
                            if R2[c-1][1] in "XxOo":
                                continue
                            else:
                                R2[c-1]=" O "
                                break
                        elif r==3:
                            if R3[c-1][1] in "XxOo":
                                continue
                            else:
                                R3[c-1]=" O "
                                break
                        else:
                            None
                display(R1,R2,R3)   
                u=0
                if R1==[" O "," O "," O ",1] or R2==[" O "," O "," O ",2] or R3==[" O "," O "," O ",3]:
                    print("Computer wins")
                    u=1
                    break
                elif R1[0]==" O " and R2[0]==" O " and R3[0]==" O ":
                    print("Computer wins")
                    u=1
                    break
                elif R1[1]==" O " and R2[1]==" O " and R3[1]==" O ":
                    print("Computer wins")
                    u=1
                    break
                elif R1[2]==" O " and R2[2]==" O " and R3[2]==" O ":
                    print("Computer wins")
                    u=1
                    break
                elif R1[0]==" O " and R2[1]==" O " and R3[2]==" O ":
                    print("Computer wins")
                    u=1
                    break
                elif R1[2]==" O " and R2[1]==" O " and R3[0]==" O ":
                    print("Computer wins")
                    u=1
                    break
                else:
                    u=0
        if u==1:
            break
    else:
        print("Tie")
        #break
elif ch in "Mm":
    R1=["   ","   ","   ",1]
    R2=["   ","   ","   ",2]
    R3=["   ","   ","   ",3]
    display(R1,R2,R3)
    for i in range(4):
        while True:
            print("1st player")
            r=int(input("Enter rowno"))
            c=int(input("Enter column no"))
            if r==1:
                if R1[c-1][1] in "XxOo":
                    print("Cant overwrite pls play again")
                    continue
                else:
                    R1[c-1]=" X "
                    break
            elif r==2:
                if R2[c-1][1] in "XxOo":
                    print("Cant overwrite pls play again")
                    continue
                else:
                    R2[c-1]=" X "
                    break
            elif r==3:
                if R3[c-1][1] in "XxOo":
                    print("Cant overwrite pls play again")
                    continue
                else:
                    R3[c-1]=" X "
                    break
            else:
                print("Row or column not defined")
        display(R1,R2,R3)
        if R1==[" X "," X "," X ",1] or R2==[" X "," X "," X ",2] or R3==[" X "," X "," X ",3]:
            print("Player 1 wins")
            break
        elif R1[0]==" X " and R2[0]==" X " and R3[0]==" X ":
             print("Player 1 wins")
             break
        elif R1[1]==" X " and R2[1]==" X " and R3[1]==" X ":
             print("Player 1 wins")
             break
        elif R1[2]==" X " and R2[2]==" X " and R3[2]==" X ":
              print("Player 1 wins")
              break
        elif R1[0]==" X " and R2[1]==" X " and R3[2]==" X ":
              print("Player 1 wins")
              break
        elif R1[2]==" X " and R2[1]==" X " and R3[0]==" X ":
              print("Player 1 wins")
              break
        else:
             None
        while True:
             print("2nd player")
             r=int(input("Enter rowno"))
             c=int(input("Enter column no"))
             if r==1:
                if R1[c-1][1] in "XxOo":
                      print("Cant overwrite pls play again")
                      continue
                else:
                    R1[c-1]=" O "
                    break
             elif r==2:
                 if R2[c-1][1] in "XxOo":
                     print("Cant overwrite pls play again")
                     continue
                 else:
                      R2[c-1]=" O "
                      break
             elif r==3:
                if R3[c-1][1] in "XxOo":
                     print("Cant overwrite pls play again")
                     continue
                else:
                    R3[c-1]=" O "
                    break
             else:
                print("Row or column not defined")
        display(R1,R2,R3)
             
        if R1==[" O "," O "," O ",1] or R2==[" O "," O "," O ",2] or R3==[" O "," O "," O ",3]:
            print("Player 2 wins")
            break
        elif R1[0]==" O " and R2[0]==" O " and R3[0]==" O ":
            print("Player 2 wins")
            break
        elif R1[1]==" O " and R2[1]==" O " and R3[1]==" O ":
             print("Player 2 wins")
             break
        elif R1[2]==" O " and R2[2]==" O " and R3[2]==" O ":
             print("Player 2 wins")
             break
        elif R1[0]==" O " and R2[1]==" O " and R3[2]==" O ":
             print("Player 2 wins")
             break
        elif R1[2]==" O " and R2[1]==" O " and R3[0]==" O ":
             print("Player 2 wins")
             break
        else:
              None
    else:
        print("Tie")
