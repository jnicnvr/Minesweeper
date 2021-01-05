import random
import os, sys
from stat import *

global rand1, rand2, rand3, rand4, rand5, rand6, rand7, rand8
flag1 = ''
flag2=''
flag3=''
flag4=''
flag5=''
flag6=''
flag7=''
flag8=''
move = ''

def setupPosition():
    
    with open('cs.txt') as fc:
       coordinates = fc.read().splitlines()
    with open('as.txt') as fa:
        acoordinates = fa.read().splitlines()
    with open('bs.txt') as f:
       bcoordinates = f.read().splitlines()
    with open('ds.txt') as fd:
       dcoordinates = fd.read().splitlines()
    with open('es.txt') as fe:
       ecoordinates = fe.read().splitlines()
    with open('fs.txt') as ff:
       fcoordinates = ff.read().splitlines()
    with open('gs.txt') as fg:
       gcoordinates = fg.read().splitlines()
    with open('hs.txt') as fh:
       hcoordinates = fh.read().splitlines()

    try:
       # for i in range(1):#

            rand1 = acoordinates[random.randint(0, 7)]  # flag1 #
            rand2 = bcoordinates[random.randint(0, 7)]  # flag2 #
            rand3 = coordinates[random.randint(0, 7)]   # flag3 #
            rand4 = dcoordinates[random.randint(0, 7)]  # flag4 #
            rand5 = ecoordinates[random.randint(0, 7)]  # flag5 #
            rand6 = fcoordinates[random.randint(0, 7)]  # flag6 #
            rand7 = gcoordinates[random.randint(0, 7)]  # flag7 #
            rand8 = hcoordinates[random.randint(0, 7)]  # flag8 #

# ====================== WRITE FLAGS ==========================#
            f = open('flags.txt', 'w')
            f.write(rand1 + '\n')
            f.write(rand2 + '\n')
            f.write(rand3 + '\n')
            f.write(rand4 + '\n')
            f.write(rand5 + '\n')
            f.write(rand6 + '\n')
            f.write(rand7 + '\n')
            f.write(rand8 + '\n')
            f.close()

            save_stateflag = open('save_state_flagsdata.txt', 'w')
            save_stateflag.write(rand1 + '\n')
            save_stateflag.write(rand2 + '\n')
            save_stateflag.write(rand3 + '\n')
            save_stateflag.write(rand4 + '\n')
            save_stateflag.write(rand5 + '\n')
            save_stateflag.write(rand6 + '\n')
            save_stateflag.write(rand7 + '\n')
            save_stateflag.write(rand8 + '\n')
            save_stateflag.close()
           
# =============================================================#            

    except Exception as e:
        print("Somethin went wrong: " + str(e))


def flagPositionLayout(move,flag1,flag2,flag3,flag4,flag5,flag6,flag7,flag8):
    #print("flagLayoutLoaded!")#
    with open('mines.txt') as f:
       minesCoordinates = f.read().splitlines()
       
    with open('playerdata.txt') as pd:
        playerdata = pd.read().splitlines()
    with open('save_state_flags.txt') as savestate:
        savedstate = savestate.read().splitlines()
    
    flagLeft = int(playerdata[0])
    score = int(playerdata[1])


   # print(flagLeft)#
    #print(score)#

    
    f = open('playerdata.txt', 'w')  

    save_state = open('save_state_flags.txt', 'r')
    lines = save_state.readlines()    
##    save_state = open('save_state_flags.txt', 'r')
##    contents = save_state.readlines()
##    save_state.close()
        
     
    #print("My Move ", move)#
    # print(move)#
    #print(flag8)#
    #print("Flag3 ",flag3)#
   
    try:
        while flagLeft != 0:
##            for x in range(len(savedstate)):
                for i in range(64):                                
                    if move == flag1 and flag1 == minesCoordinates[i]:
                        #print("█F█")#                   
                        flagLeft = flagLeft-1
                        score = score + 10
                        f.write(str(flagLeft) + '\n')
                        f.write(str(score) + '\n') 
                        f.close()
                        
                        #save_state.write(flag1 + '\n')#
                        
##                        contents.insert(0, flag1 + '\n')
##                        save_state = open('save_state_flags.txt', 'a+')
##                        contents = "".join(contents)
##                        save_state.seek(0)
##                        save_state.writelines('\n'+contents)

                        save_state = open('save_state_flags.txt', 'r')
                        lines=save_state.readlines()
                        lines[0]=flag1+'\n'
                        save_state.close()
                        
                        save_state = open('save_state_flags.txt', 'w')
                        save_state.writelines(lines)
                        save_state.close()
                      
                        
                        printBoard()
                        playerMove(move)
                        break

                    elif move == flag2 and flag2 == minesCoordinates[i]:
                        #print("█F█")#
                        flagLeft = flagLeft-1
                        score = score + 10
                        f.write(str(flagLeft) + '\n')
                        f.write(str(score) + '\n') 
                        f.close()
                        #save_state.write(flag2 + '\n')#

                        
##                        contents.insert(1, flag2+ '\n')
##                        save_state = open('save_state_flags.txt', 'a+')
##                        contents = "".join(contents)
##                        save_state.seek(0)
##                        save_state.writelines('\n'+contents)


                        save_state = open('save_state_flags.txt', 'r')
                        lines=save_state.readlines()
                        lines[0]=flag2+'\n'
                        lines[1]=flag1+'\n'
                        save_state.close()
                        
                        save_state = open('save_state_flags.txt', 'w')
                        save_state.writelines(lines)
                        save_state.close()
                                              
                                        
                        printBoard()
                        playerMove(move)
                        break

                    elif move == flag3 and flag3 == minesCoordinates[i]:
                        #print("█F█")#
                        flagLeft = flagLeft-1
                        score = score + 10
                        f.write(str(flagLeft) + '\n') 
                        f.write(str(score) + '\n')
                        f.close()
    
                        save_state = open('save_state_flags.txt', 'r')
                        lines=save_state.readlines()                       
                        save_state.close()

                        
                        lines[0]=flag3+'\n'
                        lines[1]=flag2+'\n'
                        lines[2]=flag1+'\n'
                        save_state = open('save_state_flags.txt', 'w')
                        save_state.writelines(lines)
                        save_state.close()
                        
                        printBoard()
                        playerMove(move)
                        break
                        
                    elif move == flag4 and flag4 == minesCoordinates[i]:
                        #print("█F█")#
                        flagLeft = flagLeft-1
                        score = score + 10
                        f.write(str(flagLeft) + '\n') 
                        f.write(str(score) + '\n')                    
                        f.close()
                        
                        save_state = open('save_state_flags.txt', 'r')
                        lines=save_state.readlines()
                        save_state.close()
                        
                        lines[0]=flag4+'\n'
                        lines[1]=flag3+'\n'
                        lines[2]=flag2+'\n'
                        lines[3]=flag1+'\n'
                        save_state = open('save_state_flags.txt', 'w')
                        save_state.writelines(lines)
                        save_state.close()

                        printBoard()
                        playerMove(move)
                        break
                      
                    elif move == flag5 and flag5 == minesCoordinates[i]:
                        #print("█F█")#
                        flagLeft = flagLeft-1
                        score = score + 10
                        f.write(str(flagLeft) + '\n')
                        f.write(str(score) + '\n')                        
                        f.close()
                        save_state = open('save_state_flags.txt', 'r')
                        lines=save_state.readlines()
                        save_state.close()
                        
                        lines[0]=flag5+'\n'
                        lines[1]=flag4+'\n'
                        lines[2]=flag3+'\n'
                        lines[3]=flag2+'\n'
                        lines[4]=flag1+'\n'
                        save_state = open('save_state_flags.txt', 'w')
                        save_state.writelines(lines)
                        save_state.close()

                        printBoard()                
                        playerMove(move)
                        break
                    
                    elif move == flag6 and flag6 == minesCoordinates[i]:
                       # print("█F█")#
                        flagLeft = flagLeft-1
                        score = score + 10
                        f.write(str(flagLeft) + '\n') 
                        f.write(str(score) + '\n')                       
                        f.close()
                        
                        save_state = open('save_state_flags.txt', 'r')
                        lines=save_state.readlines()
                        save_state.close()
                        
                        lines[0]=flag6+'\n'
                        lines[1]=flag5+'\n'
                        lines[2]=flag4+'\n'
                        lines[3]=flag3+'\n'
                        lines[4]=flag2+'\n'
                        lines[5]=flag1+'\n'
                        save_state = open('save_state_flags.txt', 'w')
                        save_state.writelines(lines)
                        save_state.close()

                        printBoard()
                        playerMove(move)
                        break

                    elif move == flag7 and flag7 == minesCoordinates[i]:
                        #print("█F█")#
                        flagLeft = flagLeft-1
                        score = score + 10
                        f.write(str(flagLeft) + '\n') 
                        f.write(str(score) + '\n')                        
                        f.close()
                        
                        save_state = open('save_state_flags.txt', 'r')
                        lines=save_state.readlines()
                        save_state.close()
                        
                        lines[0]=flag7+'\n'
                        lines[1]=flag6+'\n'
                        lines[2]=flag5+'\n'
                        lines[3]=flag4+'\n'
                        lines[4]=flag3+'\n'
                        lines[5]=flag2+'\n'
                        lines[6]=flag1+'\n'
                        save_state = open('save_state_flags.txt', 'w')
                        save_state.writelines(lines)
                        save_state.close()

                        printBoard()
                        playerMove(move)
                        break

                    elif move == flag8 and flag8 == minesCoordinates[i]:
                        #print("█F█")#
                        flagLeft = flagLeft-1
                        score = score + 10
                        f.write(str(flagLeft) + '\n') 
                        f.write(str(score) + '\n')                    
                        f.close()
                        
                        save_state = open('save_state_flags.txt', 'r')
                        lines=save_state.readlines()
                        save_state.close()
                        
                        lines[0]=flag8+'\n'
                        lines[1]=flag7+'\n'
                        lines[2]=flag6+'\n'
                        lines[3]=flag5+'\n'
                        lines[4]=flag4+'\n'
                        lines[5]=flag3+'\n'
                        lines[6]=flag2+'\n'
                        lines[7]=flag1+'\n'
                        save_state = open('save_state_flags.txt', 'w')
                        save_state.writelines(lines)
                        save_state.close()  

                        
                        printBoard()                
                        break                                                    
                    elif move!=flag1 and move != flag2 and move !=flag3 and move !=flag4 and move !=flag5 and move !=flag6 and move !=flag7 and move !=flag8:
                        print("█M█")
                        gameover()
                        exit()
                        break
##                    elif flagLeft == 0:
##                        print("You Win!")
##                        exit()
##                        break
                                            
##                    elif move == lines[0] or move == lines[1] or move == lines[2] or move == lines[3] or move == lines[4] or move == lines[5] or move == lines[6] or move == lines[7]:
##                       print("Already Moved")
##                       save_state.close()
##                       playerMove(move)
##                       break
            
    except Exception as e:
            print("Somethin went wrong: " + str(e))
        
def playerMove(move):
   
    with open('flags.txt') as f:
        flagsHint = f.read().splitlines()
    with open('playerdata.txt') as pd:
        playerdata = pd.read().splitlines()

        print('\n')
        print("Flags Left: ", playerdata[0])
        print("Player Score: ", playerdata[1])
        flagLeft = int(playerdata[0])

        #print(flagLeft)#
    if flagLeft == 0:
        print("You Win")
        exit()
    else:
   
##        print("My Flag1 ", flagsHint[0])
##        print("My Flag2 ", flagsHint[1])
##        print("My Flag3 ", flagsHint[2])
##        print("My Flag4 ", flagsHint[3])
##        print("My Flag5 ", flagsHint[4])
##        print("My Flag6 ", flagsHint[5])
##        print("My Flag7 ", flagsHint[6])
##        print("My Flag8 ", flagsHint[7])
        
        flag1 = flagsHint[0];
        flag2 = flagsHint[1];
        flag3 = flagsHint[2];
        flag4 = flagsHint[3];
        flag5 = flagsHint[4];
        flag6 = flagsHint[5];
        flag7 = flagsHint[6];
        flag8 = flagsHint[7];
   
       
        move = input("Player's Move: ")
        
       
        flagPositionLayout(move,flag1,flag2,flag3,flag4,flag5,flag6,flag7,flag8)

        

def gameover():
    print("Game is Over!")

def startofgame():
    with open('playerdata.txt') as pd:
        playerdata = pd.read().splitlines()
    file_size = os.stat('playerdata.txt').st_size
    
    if file_size == 0:
        f = open('playerdata.txt', 'w')
        f.write('8' + '\n') #edit#
        f.write('0'+ '\n') #edit#
        f.close();
    else:
        print("Flags Left: ", playerdata[0])
        print("Player Score: ", playerdata[1])
        flagLeft = int(playerdata[0])

    #print(flagLeft)#

    print("            _                                                        ")
    print("          /\/\ (_)_ __   ___ _____      _____  ___ _ __   ___ _ __   ")
    print("         /    \| | '_ \ / _ / __\ \ /\ / / _ \/ _ | '_ \ / _ | '__|  ")
    print("        / /\/\ | | | | |  __\__ \\ V  V |  __|  __| |_) |  __| |     ")
    print("        \/    \|_|_| |_|\___|___/ \_/\_/ \___|\___| .__/ \___|_|     ")
    print("                                                  |_|                ")

    
    print("                            [1] Start New Game")
    print("                            [2] Resume Game")

    selection = input("                                 Choice: ")

    if selection == '1':
          
            #print("Clear Saved Text ")#
            f = open('playerdata.txt', 'w')
            f.write('8' + '\n') #edit#
            f.write('0'+ '\n') #edit#
            f.close();

            fc = open('save_state_flags.txt', 'r+')
            fc.truncate(0)
            fc.close()

            fc = open('save_state_flags.txt', 'a')

            fc.write('0'+'\n')
            fc.write('0'+'\n')
            fc.write('0'+'\n')
            fc.write('0'+'\n')
            fc.write('0'+'\n')
            fc.write('0'+'\n')
            fc.write('0'+'\n')
            fc.write('0'+'\n')
            fc.close()
           
           
            setupPosition()
            playerMove(move)
      
    elif selection == '2':
        file_size = os.stat('save_state_flags.txt').st_size
    
        if file_size == 0:
            #print("The file is empty: " + str(file_size))#
            print("There is no saved data: Start New Game")
        elif flagLeft == 0:
            print("There is no saved data: Start New Game")                     
        else:
            printBoard()
            
    else:
            print("Invalid Selection")


def printBoard():            
    
    with open('save_state_flags.txt') as fc:
       move_save_state = fc.read().splitlines()
       
    with open('save_state_flagsdata.txt') as fc:
       flags_save_state = fc.read().splitlines()      

    #print(move_save_state)#
   # print("Move State", move_save_state[0])#
    file_size = os.stat('save_state_flags.txt').st_size
    for x in range(len(move_save_state)):
        if file_size == 0:            
            setupPosition()
            
# ============================================================ A ==========================================================#        
        elif move_save_state[x] == '0':
              
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break
        
        elif move_save_state[x] == 'A1':
              
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║  █F█  ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break
                
        elif move_save_state[x] == 'A2':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║  █F█  ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'A3':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║  █F█  ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'A4':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║  █F█  ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'A5':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║  █F█  ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break


        elif move_save_state[x] == 'A6':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║  █F█  ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'A7':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║  █F█  ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'A8':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║  █F█  ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

# ================================================================================================================ #



# ============================================================ B ==========================================================#        
        elif move_save_state[x] == 'B1':
            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║  █F█  ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break
                
        elif move_save_state[x] == 'B2':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║  █F█  ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'B3':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║  █F█  ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'B4':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║  █F█  ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'B5':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║  █F█  ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break


        elif move_save_state[x] == 'B6':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║  █F█  ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break
                
        elif move_save_state[x] == 'B7':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║  █F█  ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'B8':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║  █F█  ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

# ================================================================================================================ #



# ============================================================ C ==========================================================#        
        elif move_save_state[x] == 'C1':
            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║  █F█  ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break
                
        elif move_save_state[x] == 'C2':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║  █F█  ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'C3':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║  █F█  ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'C4':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║  █F█  ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'C5':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║  █F█  ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break


        elif move_save_state[x] == 'C6':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║  █F█  ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'C7':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║  █F█  ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'C8':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║  █F█  ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

# ================================================================================================================ #

# ============================================================ D ==========================================================#        
        elif move_save_state[x] == 'D1':
            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║  █F█  ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break
                
        elif move_save_state[x] == 'D2':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║  █F█  ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'D3':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║  █F█  ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'D4':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║  █F█  ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'D5':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║  █F█  ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break


        elif move_save_state[x] == 'D6':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║  █F█  ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'D7':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║  █F█  ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'D8':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║  █F█  ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

# ================================================================================================================ # 

# ============================================================ E ==========================================================#        
        elif move_save_state[x] == 'E1':
            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║  █F█  ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break
                
        elif move_save_state[x] == 'E2':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║  █F█  ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'E3':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║  █F█  ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'E4':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║  █F█  ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'E5':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║  █F█  ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break


        elif move_save_state[x] == 'E6':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║  █F█  ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'E7':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║  █F█  ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'E8':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║  █F█  ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

# ================================================================================================================ #

# ============================================================ F ==========================================================#        
        elif move_save_state[x] == 'F1':
            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║  █F█  ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break
                
        elif move_save_state[x] == 'F2':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║  █F█  ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'F3':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║  █F█  ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'F4':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║  █F█  ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'F5':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║  █F█  ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break


        elif move_save_state[x] == 'F6':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║  █F█  ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'F7':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║  █F█  ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'F8':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║  █F█  ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

# ================================================================================================================ #

# ============================================================ G ==========================================================#        
        elif move_save_state[x] == 'G1':
            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║  █F█  ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break
                
        elif move_save_state[x] == 'G2':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║  █F█  ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'G3':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║  █F█  ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'G4':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║  █F█  ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'G5':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║  █F█  ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break


        elif move_save_state[x] == 'G6':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║  █F█  ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'G7':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║  █F█  ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'G8':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║  █F█  ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

# ================================================================================================================ #


# ============================================================ H ==========================================================#        
        elif move_save_state[x] == 'H1':
            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║  █F█  ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break
                
        elif move_save_state[x] == 'H2':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║  █F█  ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'H3':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║  █F█  ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'H4':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║  █F█  ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'H5':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║  █F█  ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break


        elif move_save_state[x] == 'H6':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║  █F█  ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'H7':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║  █F█  ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

        elif move_save_state[x] == 'H8':
                            
                print("          ╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║  █F█  ║ 8")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 7")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 6")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 5")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 4")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 3")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 2")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║ 1")
                print("          ║       ║       ║       ║       ║       ║       ║       ║       ║  ")
                print("          ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝  ")
                print("              A       B        C      D       E       F       G       H      ")

                playerMove(move)
                break

# ================================================================================================================ #




                             
     
def main():
    global move

    startofgame()
    #printBoard()#
    #setupPosition()#
    #playerMove(move)#
    
    
if __name__ == '__main__':
    main()


         

