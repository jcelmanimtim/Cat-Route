import sys

import numpy as num
import random
import pygame.mixer
from prettytable import PrettyTable
from pygame import mixer
import pygame

pygame.mixer.init()


isrunning = True
menu = 1
score = 0
indicator = "\N{cat}"
lose_sound = pygame.mixer.Sound("Project_Sounds_Lose.wav")
win_sound = pygame.mixer.Sound("Project_Sounds_Win.wav")
earn_sound = pygame.mixer.Sound("Project_Sounds_Heal.wav")

lose_sound.set_volume(0.6)
earn_sound.set_volume(0.3)
win_sound.set_volume(100)


while (isrunning == True):
    print(""" 
                                                    -----------------------------------------------------------------------------
                                                    |           The cat is hungry, seek out a place with plenty of food.        |
                                                    |                      The goal is to fill Ryan's tummy.                    |
                                                    |                                                       ./\\.../\\.           |
                                                    |                              0 : To Start             ='@ . @'=           |  
                                                    |                              1 : To Exit                .♥**♥.            |    
                                                    |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _| """)
    print("\n")
    choices = (input("                                                        Enter Choice: "))
    if choices == "0":
        print("""                                                                            ~WELCOME TO CAT ROUTES~
                                                   -----------------------------------------------------------------------------
                                                   |                                                                           |
                                                   |                          INSTRUCTION:                                     |
                                                   |            To fill Ryan tummy,                                            |
                                                   |            you need to find a food in any location.                       |
                                                   |            The system will randomized your location.                      |
                                                   |            The system will also recommend shortest route to take.         |
                                                   |            Each location has its own history.                             |
                                                   |            Solve the riddle and get the food for Ryan's tummy.            |
                                                   |            Earn 100 tummy points to win the game.                         |
                                                   |            Good luck and enjoy the journey!...FIGHTING...                 |
                                                   |                                                                           |
                                                   -----------------------------------------------------------------------------""")
        break
    elif choices == "1":
        print("Thank you for trying.")
        exit()
    else:
        print("Invalid Input.Please try again.")
print("\n")

def AtoS():
    global location
    global score
    global loc1
    if location == "Abandon_house" and loc1 == "3":  # Abandon_house to Store

        print("                                                              - - - - - - - - - - - - -")
        print("                                                              Tummy Points: | ", {score})
        print("                                                              - - - - - - - - - - - - - \n")


        duration = A_S / 6.00  # path1
        add = A_P + P_HB + HA_HB + S_HA  # path2
        duration1 = round(add / 6.00)
        add1 = A_B + B_M + HB_M + HA_HB + S_HA  # path3
        duration2 = round(add1 / 6.00)
        add2 = A_B + P_B + P_HB + HA_HB + S_HA  # path4
        duration3 = round(add2 / 6.00)

        table = PrettyTable()
        table.field_names = ["", "Possible Routes To Be Taken", "Distance per meter's", "Time Duration"]
        table.add_row([1, "From Abandon_house to Store                                    ", f"{A_S} meters", f"{duration} hrs"])
        table.add_row([2, "From Abandon_House to Pond to Home B to Home A to Store           ", f"{add} meters", f"{duration1} hrs"])
        table.add_row([3, "From Abandon_House to Bridge to Market to Home B to Home A to Store", f"{add1} meters", f"{duration2} hrs"])
        table.add_row([4, "From Abandon_House to Bridge to Pond to Home B to Home A to Store  ", f"{add2} meters", f"{duration3} hrs"])
        print(table)
        print("\n")


        distanceList = []
        for i in range(4):
            distanceList.append(A_S)
            distanceList.append(add)
            distanceList.append(add1)
            distanceList.append(add2)

        print("\n")
        print(f"The shortest path should be taken is {route[distanceList.index(min(distanceList))]}")

        print("\n")
        print('''------------------------------------------------------------------------------------
                        Answer the following Riddle in order for you to get the Tummy points:
                 ------------------------------------------------------------------------------------ \n''')
        print('''-------------------------------------------------------------------------------------------------------
                        Where are the lakes always empty, the mountains always flat and the rivers always still? 
                 ------------------------------------------------------------------------------------------------------- \n''')
        print('''                                 a.) map    b.) darkness                           \n''')
        answer = input('''Your answer should be in lowercase: '''  )
        if answer == "a":
            print("\n")
            print('''-------------------------------------------------------------------------------------------------------
                       Congratulations! You have successfully earned [Bread, milk cat food] equivalent to 30 Tummy points! 
                     ------------------------------------------------------------------------------------------------------- \n''' )
            print('''                                                          
                                                                                      _ _ _ _ _ _ _ _
                                                _________                            /_______________\\            
                                              /         \\                            I  ##         I                 _____________   
                                             /--/--|--\--\\          v                I  ##   ___   I                |_____________|    
                                               | #       |                            I_______I_I___I                 | #  #  # # |
                                    - - - - -  |         |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ HOME B _ _ _ _ _ _ _ _ _  | #  ___  # |                      
                                  |   _ _ _ _  |_______|_|  _ _ _ _ _ _ _ _ _ _ _ _       _ _ _ _ _ _ _ _ _ _ _ _ _ _ |____| |____|                
                                  |  |            HOME A                            |  |                        MARKET   |    |             
                                  |  |                                vv            |  |                                 |    |             
                                  |  |                                              |  |                                 |    |             
                                  |  |                                            + |  |                                 |    |            
                                  |  |                       '^   ^                ~+ ~`~ + - - - - - - - - - - - - - -       - - - - -                     
                                  |  |                       (>^.^<)                 ~.+ POND ~`~ - - - - - - - - - - - - - - - - -      |   
                               ^ ^ ^ ^ ^ ^ ^                ''/   \\                |  ~'.~  ~                                      |    |
                             / = = = = = = \\                (_____)____            |  |                                            |    |              
                              |           |                                         |  |                          |~~~~~~~~|        |    |
                              |  \N{cat}STORE  |- - - - - - - - - - - -                   ___                     |- - - - |        |    |  
                              |___________|- - - - - - - - - -     |               //   \\\\                     - BRIDGE- - - - -       |                            
                                                               |   |              //     \\\\                    |    _ _ _ _ _ _ _ _ _ _                           
                                                               |   |             //-------\\\\                   |    |      
                                                               |   |              |       |                      |    |
                                        v                      |   |              |____#__|                      |    |         vvv
                                                         vvv   |     - - - - - - - ABANDON HOUSE - - - - - - - -      | vv
                                                                 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _                    \n''')  # MAP
            score += 30
            earn_sound.play()
            print(f'''                                                 ---   Your current score is {score}   ---''' )

        else:
            print("\n")
            print('''--------------------------------------------------------------------------------
                                  Wrong Answer! You have failed to earn a Tummy points.
                     --------------------------------------------------------------------------------''')
            lose_sound.play()

def AtoHA():
    global location
    global score
    global loc1
    if location == "Abandon_house" and loc1 == '1':  # Abandon_house to Home A
        print("                                                            - - - - - - - - - - - - -")
        print("                                                            Tummy Points: | ", {score})
        print("                                                            - - - - - - - - - - - - - \n")
        add3 = A_S + S_HA  # path1
        duration4 = round(add3 / 6.00)
        add4 = A_P + P_HB + HA_HB  # path2
        duration5 = round(add4 / 6.00)
        add5 = A_P + P_M + HB_M + HA_HB  # path3
        duration6 = round(add5 / 6.00)
        add6 = A_B + P_B + P_HB + HA_HB  # path4
        duration7 = round(add6 / 6.00)
        add7 = A_B + B_M + HB_M + HA_HB  # path5
        duration8 = round(add7 / 6.00)

        table = PrettyTable()
        table.field_names = ["", "Possible Routes To Be Taken", "Distance per meter's", "Time Duration"]
        table.add_row([1, "From Abandon_house to Store to Home A                  ", f"{add3} meters", f"{duration4} hrs"])
        table.add_row([2, "From Abandon_house to Pond to Home B to Home A          ", f"{add4} meters", f"{duration5} hrs"])
        table.add_row([3, "From Abandon_house to Pond to Market to Home B to Home A ", f"{add5} meters", f"{duration6} hrs"])
        table.add_row([4, "From Abandon_house to Bridge to Pond to Home B to Home A  ", f"{add6} meters", f"{duration7} hrs"])
        table.add_row(
            [5, "Abandon_house - Bridge - Market - Home B - Home A", f"{add7} meters", f"{duration8} hrs"])
        print(table)

        distanceList1 = []
        for i in range(5):
            distanceList1.append(add3)
            distanceList1.append(add4)
            distanceList1.append(add5)
            distanceList1.append(add6)
            distanceList1.append(add7)

        print(f"The shortest path should be taken is {route[distanceList1.index(min(distanceList1))]}")

        print("\n")
        print('''------------------------------------------------------------------------------------
                       Answer the following Riddle in order for you to get the Tummy points:
                 ------------------------------------------------------------------------------------ \n''' )
        print('''------------------------------------------------------------------------------------
                                      What has thirteen hearts, but no other organs? 
                 ------------------------------------------------------------------------------------ \n ''' )
        print('''                         a.) footsteps    b.) deck of cards                           \n''' )
        answer1 = input('''Your answer should be in lowercase: ''' )
        if answer1 == "b":
            print("\n")
            print('''-------------------------------------------------------------------------------------------------------
                       Congratulations! You have successfully earned [Bread, milk cat food] equivalent to 10 Tummy points! 
                     ------------------------------------------------------------------------------------------------------- \n''' )
            print('''                                                          
                                                                                         _ _ _ _ _ _ _ _
                                                   _________                            /_______________\\            
                                                 /         \\                            I  ##         I                 _____________   
                                                /--/--|--\--\\          v                I  ##   ___   I                |_____________|    
                                                  | #       |                            I_______I_I___I                 | #  #  # # |
                                       - - - - -  |         |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ HOME B _ _ _ _ _ _ _ _ _  | #  ___  # |                      
                                     |   _ _ _ _  |_______|_|  _ _ _ _ _ _ _ _ _ _ _ _       _ _ _ _ _ _ _ _ _ _ _ _ _ _ |____| |____|                
                                     |  |          \N{cat}HOME A                            |  |                        MARKET   |    |             
                                     |  |                                vv            |  |                                 |    |             
                                     |  |                                              |  |                                 |    |             
                                     |  |                                            + |  |                                 |    |            
                                     |  |                       '^   ^                ~+ ~`~ + - - - - - - - - - - - - - -       - - - - -                     
                                     |  |                       (>^.^<)                 ~.+ POND ~`~ - - - - - - - - - - - - - - - - -       |   
                                  ^ ^ ^ ^ ^ ^ ^                ''/   \\                |  ~'.~  ~                                       |    |
                                 / = = = = = = \\               (_____)____            |  |                                             |    |              
                                  |           |                                        |  |                           |~~~~~~~~|        |    |
                                  |   STORE   |- - - - - - - - - - - -                   ___                          |- - - - |        |    |  
                                  |___________|- - - - - - - - - -     |               //   \\\\                       - BRIDGE- - - - -     |                            |
                                                                   |   |              //     \\\\                    |    _ _ _ _ _ _ _ _ _ _                           
                                                                   |   |             //-------\\\\                   |    |      
                                                                   |   |              |       |                      |    |
                                            v                      |   |              |____#__|                      |    |         vvv
                                                             vvv   |     - - - - - - - ABANDON HOUSE - - - - - - - -      | vv
                                                                     _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _                    \n''')  # MAP
            score += 10
            print(f'''                                                  ---   Your current score is {score}   ---''' )
            earn_sound.play()
        else:
            print("\n")
            print('''--------------------------------------------------------------------------------
                                  Wrong Answer! You have failed to earn a Tummy points.
                     --------------------------------------------------------------------------------''' )
            lose_sound.play()

def AtoHB():
    global location
    global score
    global loc1
    if location == "Abandon_house" and loc1 == '2':  # Abandon_house to Home B
        print("                                                           - - - - - - - - - - - - -")
        print("                                                           Tummy Points: | ", {score})
        print("                                                           - - - - - - - - - - - - - \n")

        add8 = A_P + P_HB  # path1
        duration9 = round(add8 / 6.00)
        add9 = A_S + S_HA + HA_HB  # path2
        duration10 = round(add9 / 6.00)
        add10 = A_B + P_B + P_HB  # path3
        duration11 = round(add10 / 6.00)
        add11 = A_B + B_M + HB_M
        duration12 = round(add11 / 6.00)

        table = PrettyTable()
        table.field_names = ["", "Possible Routes To Be Taken", "Distance per meter's", "Time Duration"]
        table.add_row([1, "From Abandon_house to Pond to Home B           ", f"{add8} meters", f"{duration9} hrs"])
        table.add_row([2, "From Abandon_house to Store to Home A to Home B ", f"{add9} meters", f"{duration10} hrs"])
        table.add_row([3, "From Abandon_house to Bridge to Pond to Home B  ", f"{add10} meters", f"{duration11} hrs"])
        table.add_row([4, "From Abandon_house to Bridge to Market to Home B", f"{add11} meters", f"{duration12} hrs"])
        print(table)

        distanceList2 = []
        for i in range(4):
            distanceList2.append(add8)
            distanceList2.append(add9)
            distanceList2.append(add10)
            distanceList2.append(add11)

        print(f"The shortest path should be taken is {route[distanceList2.index(min(distanceList2))]}")

        print("\n")
        print('''------------------------------------------------------------------------------------
                        Answer the following Riddle in order for you to get the Tummy points:
                 ------------------------------------------------------------------------------------ \n''' )
        print('''------------------------------------------------------------------------------------
                             The more you take, the more you leave behind. What are they? 
                 ------------------------------------------------------------------------------------ \n''' )
        print('''                          a.) all of them    b.) footsteps                           \n''' )
        answer2 = input('''Your answer should be in lowercase: ''' )
        if answer2 == "b":
            print("\n")
            print('''---------------------------------------------------------------------------------------------
                        Congratulations! You have successfully earned [rice,egg] equivalent to 15 Tummy points! 
                     --------------------------------------------------------------------------------------------- \n''' )
            print('''                                                          
                                                                                            _ _ _ _ _ _ _ _
                                                     _________                            /_______________\\            
                                                    /         \\                            I  ##         I                 _____________   
                                                   /--/--|--\--\\          v                I  ##   ___   I                |_____________|    
                                                     | #       |                            I_______I_I___I                 | #  #  # # |
                                          - - - - -  |         |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\N{cat}HOME B _ _ _ _ _ _ _ _ _  | #  ___  # |                      
                                        |   _ _ _ _  |_______|_|  _ _ _ _ _ _ _ _ _ _ _ _       _ _ _ _ _ _ _ _ _ _ _ _ _ _ |____| |____|                
                                        |  |            HOME A                            |  |                        MARKET   |    |             
                                        |  |                                vv            |  |                                 |    |             
                                        |  |                                              |  |                                 |    |             
                                        |  |                                            + |  |                                 |    |            
                                        |  |                       '^   ^                ~+ ~`~ + - - - - - - - - - - - - - -       - - - - -                     
                                        |  |                       (>^.^<)                 ~.+ POND ~`~ - - - - - - - - - - - - - - - - -       |   
                                     ^ ^ ^ ^ ^ ^ ^                ''/   \\                |  ~'.~  ~                                       |    |
                                   / = = = = = = \\                (_____)____            |  |                                             |    |              
                                     |           |                                        |  |                           |~~~~~~~~|        |    |
                                     |   STORE   |- - - - - - - - - - - -                   ___                          |- - - - |        |    |  
                                     |___________|- - - - - - - - - -     |               //   \\\\                       - BRIDGE- - - - -     |                            |
                                                                      |   |              //     \\\\                    |    _ _ _ _ _ _ _ _ _ _                           
                                                                      |   |             //-------\\\\                   |    |      
                                                                      |   |              |       |                      |    |
                                                               v      |   |              |____#__|                      |    |         vvv
                                                                vvv   |     - - - - - - - ABANDON HOUSE - - - - - - - -      | vv
                                                                        _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _                    \n''')  # MAP
            score += 15
            print(f'''                                                      ---   Your current score is {score}   ---''' )
            earn_sound.play()
        else:
            print("\n")
            print('''--------------------------------------------------------------------------------
                                 Wrong Answer! You have failed to earn a Tummy points.
                     --------------------------------------------------------------------------------''' )
            lose_sound.play()


def AtoM():
    global location
    global score
    global loc1
    if location == "Abandon_house" and loc1 == '4':  # Abandon_house to Market
        print("                                                           - - - - - - - - - - - - -")
        print("                                                           Tummy Points: | ", {score})
        print("                                                           - - - - - - - - - - - - - \n")

        add12 = A_P + P_M  # path1
        duration13 = round(add12 / 6.00)
        add13 = A_B + B_M  # path2
        duration14 = round(add13 / 6.00)
        add14 = A_P + P_HB + HB_M  # path3
        duration15 = round(add14 / 6.00)
        add15 = A_S + S_HA + HA_HB + HB_M  # path4
        duration16 = round(add15 / 6.00)

        table = PrettyTable()
        table.field_names = ["", "Possible Routes To Be Taken", "Distance per meter's", "Time Duration"]
        table.add_row([1, "From Abandon_house to Pond to Market                   ", f"{add12} meters", f"{duration13} hrs"])
        table.add_row([2, "From Abandon_house to Bridge to Market                 ", f"{add13} meters", f"{duration14} hrs"])
        table.add_row([3, "From Abandon_house to Pond to Home B to Market          ", f"{add14} meters", f"{duration15} hrs"])
        table.add_row([4, "From Abandon_house to Store to Home A to Home B to Market", f"{add15} meters", f"{duration16} hrs"])
        print(table)

        distanceList3 = []
        for i in range(4):
            distanceList3.append(add12)
            distanceList3.append(add13)
            distanceList3.append(add14)
            distanceList3.append(add15)

        print(f"The shortest path should be taken is {route[distanceList3.index(min(distanceList3))]}")

        print("\n")
        print('''------------------------------------------------------------------------------------
                        Answer the following Riddle in order for you to get the Tummy points:
                 ------------------------------------------------------------------------------------ \n''' )
        print('''---------------------------------------------------------------------------------------------
                   The healthier you are, the bigger I get. The bigger I get, the more I'm hated. What am I?
                 --------------------------------------------------------------------------------------------- \n''' )
        print('''                              a.) age    b.) an envelope                          \n''' )
        answer3 = input("Your answer should be in lowercase: ")
        if answer3 == "a":
            print("\n")
            print('''---------------------------------------------------------------------------------------------------------
                       Congratulations! You have successfully earned [fish, pork, vegetable] equivalent to 40 Tummy points! 
                     --------------------------------------------------------------------------------------------------------- \n''' )
            print('''                                                          
                                                                                             _ _ _ _ _ _ _ _
                                                      _________                            /_______________\\            
                                                     /         \\                            I  ##         I                 _____________   
                                                    /--/--|--\--\\          v                I  ##   ___   I                |_____________|    
                                                      | #       |                            I_______I_I___I                 | #  #  # # |
                                           - - - - -  |         |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ HOME B _ _ _ _ _ _ _ _ _  | #  ___  # |                      
                                         |   _ _ _ _  |_______|_|  _ _ _ _ _ _ _ _ _ _ _ _       _ _ _ _ _ _ _ _ _ _ _ _ _ _ |____| |____|                
                                         |  |            HOME A                            |  |                       \N{cat}MARKET   |    |             
                                         |  |                                vv            |  |                                 |    |             
                                         |  |                                              |  |                                 |    |             
                                         |  |                                            + |  |                                 |    |            
                                         |  |                       '^   ^                ~+ ~`~ + - - - - - - - - - - - - - -       - - - - -                     
                                         |  |                       (>^.^<)                 ~.+ POND ~`~ - - - - - - - - - - - - - - - - -        |   
                                      ^ ^ ^ ^ ^ ^ ^                ''/   \\                |  ~'.~  ~                                        |    |
                                     / = = = = = = \\               (_____)____            |  |                                              |    |              
                                       |           |                                       |  |                            |~~~~~~~~|        |    |
                                       |   STORE   |- - - - - - - - - - - -                   ___                          |- - - - |        |    |  
                                       |___________|- - - - - - - - - -     |               //   \\\\                       - BRIDGE- - - - -     |                            |
                                                                        |   |              //     \\\\                    |    _ _ _ _ _ _ _ _ _ _                           
                                                                        |   |             //-------\\\\                   |    |      
                                                                        |   |              |       |                      |    |
                                                               v        |   |              |____#__|                      |    |         vvv
                                                                  vvv   |     - - - - - - - ABANDON HOUSE - - - - - - - -      | vv
                                                                          _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _                    \n''')  # MAP
            score += 40
            print(f'''                                                      ---   Your current score is {score}   ---''' )
            earn_sound.play()
        else:
            print("\n")
            print('''--------------------------------------------------------------------------------
                                Wrong Answer! You have failed to earn a Tummy points.
                     --------------------------------------------------------------------------------''' )
            lose_sound.play()

def StoHA():
    global location
    global score
    global loc1
    if location == "Store" and loc1 == "1":  # Store to Home A
        print("                                                           - - - - - - - - - - - - -")
        print("                                                           Tummy Points: | ", {score})
        print("                                                           - - - - - - - - - - - - - \n")
        duration17 = round(S_HA / 6.00)  # path1
        add16 = A_S + A_P + P_HB + HA_HB  # path2
        duration18 = round(add16 / 6.00)
        add17 = A_S + A_B + B_M + HB_M + HA_HB  # path3
        duration19 = round(add17 / 6.00)
        add18 = A_S + A_B + P_B + P_HB + HA_HB  # path4
        duration20 = round(add18 / 6.00)

        table = PrettyTable()
        table.field_names = ["", "Possible Routes To Be Taken", "Distance per meter's", "Time Duration"]
        table.add_row([1, "From Store to Home A                                          ", f"{S_HA} meters", f"{duration17} hrs"])
        table.add_row([2, "From Store to Abandon_house to Pond to Home B to Home A         ", f"{add16} meters", f"{duration18} hrs"])
        table.add_row([3, "From Store to Abandon_house to Bridge to Market to Home B to Home A", f"{add17} meters", f"{duration19} hrs"])
        table.add_row([4, "From Store to Abandon_house to Bridge to Pond to Home B to Home A", f"{add18} meters", f"{duration20} hrs"])
        print(table)

        distanceList4 = []
        for i in range(4):
            distanceList4.append(S_HA)
            distanceList4.append(add16)
            distanceList4.append(add17)
            distanceList4.append(add18)

        print(f"The shortest path should be taken is {route[distanceList4.index(min(distanceList4))]}")

        print("\n")
        print('''------------------------------------------------------------------------------------
                        Answer the following Riddle in order for you to get the Tummy points:
                 ------------------------------------------------------------------------------------ \n''' )
        print('''------------------------------------------------------------------------------------
                                            How many months have 28 days?
                 ------------------------------------------------------------------------------------ \n''')
        print('''                          a.) all of them    b.) february                          \n''')
        answer4 = input('''Your answer should be in lowercase: ''')
        if answer4 == "a":
            print("\n")
            print('''----------------------------------------------------------------------------------------------
                       Congratulations! You have successfully earned [fish, rice] equivalent to 10 Tummy points! 
                     ----------------------------------------------------------------------------------------------\n''')
            print('''                                                          
                                                                                                _ _ _ _ _ _ _ _
                                                         _________                            /_______________\\            
                                                       /         \\                            I  ##         I                 _____________   
                                                      /--/--|--\--\\          v                I  ##   ___   I                |_____________|    
                                                        | #       |                            I_______I_I___I                 | #  #  # # |
                                             - - - - -  |         |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ HOME B _ _ _ _ _ _ _ _ _  | #  ___  # |                      
                                           |   _ _ _ _  |_______|_|  _ _ _ _ _ _ _ _ _ _ _ _       _ _ _ _ _ _ _ _ _ _ _ _ _ _ |____| |____|                
                                           |  |           \N{cat}HOME A                            |  |                        MARKET   |    |             
                                           |  |                                vv            |  |                                 |    |             
                                           |  |                                              |  |                                 |    |             
                                           |  |                                            + |  |                                 |    |            
                                           |  |                       '^   ^                ~+ ~`~ + - - - - - - - - - - - - - -       - - - - -                     
                                           |  |                       (>^.^<)                 ~.+ POND ~`~ - - - - - - - - - - - - - - - - -        |   
                                        ^ ^ ^ ^ ^ ^ ^                ''/   \\                |  ~'.~  ~                                        |    |
                                       / = = = = = = \\               (_____)____            |  |                                              |    |              
                                         |           |                                       |  |                            |~~~~~~~~|        |    |
                                         |   STORE   |- - - - - - - - - - - -                   ___                          |- - - - |        |    |  
                                         |___________|- - - - - - - - - -     |               //   \\\\                       - BRIDGE- - - - -     |                            |
                                                                          |   |              //     \\\\                    |    _ _ _ _ _ _ _ _ _ _                           
                                                                          |   |             //-------\\\\                   |    |      
                                                                          |   |              |       |                      |    |
                                                               v          |   |              |____#__|                      |    |         vvv
                                                                    vvv   |     - - - - - - - ABANDON HOUSE - - - - - - - -      | vv
                                                                            _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _                    \n''')  # MAP
            score += 10
            print(f'''                                                       ---   Your current score is {score}   ---''')
            earn_sound.play()
        else:
            print("\n")
            print('''--------------------------------------------------------------------------------
                                  Wrong Answer! You have failed to earn a Tummy points.
                     --------------------------------------------------------------------------------''')
            lose_sound.play()

def StoA():
    global location
    global score
    global loc1
    if location == "Store" and loc1 == "0":  # Store to Abandon_house
        print("                                                           - - - - - - - - - - - - -")
        print("                                                           Tummy Points: | ", {score})
        print("                                                           - - - - - - - - - - - - - \n")
        duration21 = round(A_S / 6.00)  # path1
        add19 = S_HA + HA_HB + P_HB + A_P
        duration22 = round(add19 / 6.00)  # path2
        add20 = S_HA + HA_HB + P_HB + P_B + A_B  # path3
        duration23 = round(add20 / 6.00)
        add21 = S_HA + HA_HB + HB_M + B_M + A_B  # path4
        duration24 = round(add21 / 6.00)

        table = PrettyTable()
        table.field_names = ["", "Possible Routes To Be Taken", "Distance per meter's", "Time Duration"]
        table.add_row([1, "From Store to Abandon_house         ", f"{A_S} meters", f"{duration21} hrs"])
        table.add_row([2, "From Store to Home A to Home B to Pond to Abandon_house  ", f"{add19} meters", f"{duration22} hrs"])
        table.add_row([3, "From Store to Home A to Home B to Pond to Bridge to Abandon_house", f"{add20} meters", f"{duration23} hrs"])
        table.add_row([4, "From Store to Home A to Home B to Market to Bridge to Abandon_house  ", f"{add21} meters",f"{duration24} hrs"])
        print(table)

        distanceList5 = []
        for i in range(4):
            distanceList5.append(A_S)
            distanceList5.append(add19)
            distanceList5.append(add20)
            distanceList5.append(add21)

        print(f"The shortest path should be taken is {route[distanceList5.index(min(distanceList5))]}")

        print("\n")
        print('''------------------------------------------------------------------------------------
                        Answer the following Riddle in order for you to get the Tummy points:
                 ------------------------------------------------------------------------------------ \n''')
        print('''------------------------------------------------------------------------------------
                                The more there is, the less you see. What is it? 
                 ------------------------------------------------------------------------------------ \n''')
        print('''                           a.) darkness    b.) dim                         \n''')
        answer5 = input('''Your answer should be in lowercase: ''')
        if answer5 == "a":
            print("\n")
            print('''------------------------------------------------------------------------------------------
                        Congratulations! You have successfully earned [spices] equivalent to 5 Tummy points! 
                     ------------------------------------------------------------------------------------------ \n''')
            print('''                                                          
                                                                                                  _ _ _ _ _ _ _ _
                                                            _________                            /_______________\\            
                                                           /         \\                           I  ##         I                 _____________   
                                                          /--/--|--\--\\          v               I  ##   ___   I                |_____________|    
                                                           | #       |                            I_______I_I___I                 | #  #  # # |
                                                - - - - -  |         |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ HOME B _ _ _ _ _ _ _ _ _  | #  ___  # |                      
                                              |   _ _ _ _  |_______|_|  _ _ _ _ _ _ _ _ _ _ _ _       _ _ _ _ _ _ _ _ _ _ _ _ _ _ |____| |____|                
                                              |  |            HOME A                            |  |                        MARKET   |    |             
                                              |  |                                vv            |  |                                 |    |             
                                              |  |                                              |  |                                 |    |             
                                              |  |                                            + |  |                                 |    |            
                                              |  |                       '^   ^                ~+ ~`~ + - - - - - - - - - - - - - -       - - - - -                     
                                              |  |                       (>^.^<)                 ~.+ POND ~`~ - - - - - - - - - - - - - - - - -       |   
                                           ^ ^ ^ ^ ^ ^ ^                ''/   \\                |  ~'.~  ~                                       |    |
                                          / = = = = = = \\               (_____)____            |  |                                             |    |              
                                           |           |                                        |  |                           |~~~~~~~~|        |    |
                                           |   STORE   |- - - - - - - - - - - -                   ___                          |- - - - |        |    |  
                                           |___________|- - - - - - - - - -     |               //   \\\\                       - BRIDGE- - - - -     |                            |
                                                                            |   |              //     \\\\                    |    _ _ _ _ _ _ _ _ _ _                           
                                                                            |   |             //-------\\\\                   |    |      
                                                                            |   |              |       |                      |    |
                                                               v            |   |              |____#__|                      |    |         vvv
                                                                      vvv   |     - - - - - - -\N{cat}ABANDON HOUSE - - - - - -    | vv
                                                                                _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _                    \n''')  # MAP
            score += 5
            print(f'''                                                         ---   Your current score is {score}   ---''')
            earn_sound.play()
        else:
            print("\n")
            print('''--------------------------------------------------------------------------------
                                   Wrong Answer! You have failed to earn a Tummy points.
                     --------------------------------------------------------------------------------''')
            lose_sound.play()

def StoHB():
    global location
    global score
    global loc1
    if location == "Store" and loc1 == "2":  # Store to Home B
        print("                                                           - - - - - - - - - - - - -")
        print("                                                           Tummy Points: | ", {score})
        print("                                                           - - - - - - - - - - - - - \n")

        add22 = S_HA + HA_HB  # path1
        duration25 = round(add22 / 6.00)
        add23 = A_S + A_P + P_HB  # path2
        duration26 = round(add23 / 6.00)
        add24 = A_S + A_B + P_B + P_HB  # path3
        duration27 = round(add24 / 6.00)
        add25 = A_S + A_B + B_M + HB_M  # path4
        duration28 = round(add25 / 6.00)

        table = PrettyTable()
        table.field_names = ["", "Possible Routes To Be Taken", "Distance per meter's", "Time Duration"]
        table.add_row([1, "From Store to Home A to Home B                         ", f"{add22} meters", f"{duration25} hrs"])
        table.add_row([2, "From Store to Abandon_house to Pond to Home B           ", f"{add23} meters", f"{duration26} hrs"])
        table.add_row([3, "From Store to Abandon_house to Bridge to Pond to Home B  ", f"{add24} meters", f"{duration27} hrs"])
        table.add_row([4, "From Store to Abandon_house to Bridge to Market to Home B", f"{add25} meters", f"{duration28} hrs"])
        print(table)

        distanceList6 = []
        for i in range(4):
            distanceList6.append(add22)
            distanceList6.append(add23)
            distanceList6.append(add24)
            distanceList6.append(add25)

        print(f"The shortest path should be taken is {route[distanceList6.index(min(distanceList6))]}")

        print("\n")
        print('''------------------------------------------------------------------------------------
                         Answer the following Riddle in order for you to get the Tummy points:
                 ------------------------------------------------------------------------------------ \n''')
        print('''------------------------------------------------------------------------------------
                            The more you take, the more you leave behind. What are they? 
                 ------------------------------------------------------------------------------------ \n''')
        print('''                           a.) bag    b.) footsteps                        \n''')
        answer6 = input('''Your answer should be in lowercase: ''')
        if answer6 == "b":
            print("\n")
            print('''----------------------------------------------------------------------------------------------
                        Congratulations! You have successfully earned [rice, egg] equivalent to 15 Tummy points! 
                     ---------------------------------------------------------------------------------------------- \n''')
            print('''                                                          
                                                                                                    _ _ _ _ _ _ _ _
                                                             _________                            /_______________\\            
                                                            /         \\                            I  ##         I                 _____________   
                                                           /--/--|--\--\\          v                I  ##   ___   I                |_____________|    
                                                            | #       |                             I_______I_I___I                 | #  #  # # |
                                                 - - - - -  |         |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\N{cat}HOME B _ _ _ _ _ _ _ _ _  | #  ___  # |                      
                                               |   _ _ _ _  |_______|_|  _ _ _ _ _ _ _ _ _ _ _ _       _ _ _ _ _ _ _ _ _ _ _ _ _ _ |____| |____|                
                                               |  |            HOME A                            |  |                        MARKET   |    |             
                                               |  |                                vv            |  |                                 |    |             
                                               |  |                                              |  |                                 |    |             
                                               |  |                                            + |  |                                 |    |            
                                               |  |                       '^   ^                ~+ ~`~ + - - - - - - - - - - - - - -       - - - - -                     
                                               |  |                       (>^.^<)                 ~.+ POND ~`~ - - - - - - - - - - - - - - - - -        |   
                                            ^ ^ ^ ^ ^ ^ ^                ''/   \\                |  ~'.~  ~                                        |    |
                                           / = = = = = = \\               (_____)____            |  |                                              |    |              
                                             |           |                                       |  |                            |~~~~~~~~|        |    |
                                             |   STORE   |- - - - - - - - - - - -                   ___                          |- - - - |        |    |  
                                             |___________|- - - - - - - - - -     |               //   \\\\                       - BRIDGE- - - - -     |                            |
                                                                              |   |              //     \\\\                    |    _ _ _ _ _ _ _ _ _ _                           
                                                                              |   |             //-------\\\\                   |    |      
                                                                              |   |              |       |                      |    |
                                                               v              |   |              |____#__|                      |    |         vvv
                                                                        vvv   |     - - - - - - - ABANDON HOUSE - - - - - - - -      | vv
                                                                                 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _                    \n''')  # MAP
            score += 15
            print(f'''                                                             ---   Your current score is {score}   ---''')
            earn_sound.play()
        else:
            print("\n")
            print('''--------------------------------------------------------------------------------
                                    Wrong Answer! You have failed to earn a Tummy points.
                     --------------------------------------------------------------------------------''')
            lose_sound.play()

def StoM():
    global location
    global score
    global loc1
    if location == "Store" and loc1 == "4":  # Store to Market
        print("                                                           - - - - - - - - - - - - -")
        print("                                                           Tummy Points: | ", {score})
        print("                                                           - - - - - - - - - - - - - \n")

        add26 = S_HA + HA_HB + HB_M  # path1
        duration29 = round(add26 / 6.00)
        add27 = S_HA + HA_HB + P_HB + P_M  # path2
        duration30 = round(add27 / 6.00)
        add28 = A_S + A_P + P_M  # path3
        duration31 = round(add28 / 6.00)
        add29 = A_S + A_B + B_M  # path4
        duration32 = round(add29 / 6.00)

        table = PrettyTable()
        table.field_names = ["", "Possible Routes To Be Taken", "Distance per meter's", "Time Duration"]
        table.add_row([1, "From Store to Home A to Home B to Market               ", f"{add26} meters", f"{duration29} hrs"])
        table.add_row([2, "From Store to Home A to Home B to Pond to Market", f"{add27} meters", f"{duration30} hrs"])
        table.add_row([3, "From Store to Abandon_house to Pond to Market          ", f"{add28} meters", f"{duration31} hrs"])
        table.add_row([4, "From Store to Abandon_house to Bridge to Market", f"{add29} meters", f"{duration32} hrs"])
        print(table)

        distanceList7 = []
        for i in range(4):
            distanceList7.append(add26)
            distanceList7.append(add27)
            distanceList7.append(add28)
            distanceList7.append(add29)

        print(f"The shortest path should be taken is {route[distanceList7.index(min(distanceList7))]}")

        print("\n")
        print('''------------------------------------------------------------------------------------
                        Answer the following Riddle in order for you to get the Tummy points:
                 ------------------------------------------------------------------------------------ \n''')
        print('''-------------------------------------------------------------------------------------------
                                   What building has the most stories in the world?
                 ------------------------------------------------------------------------------------------- \n''')
        print('''                            a.) library    b.) museum                          \n''')
        answer7 = input('''Your answer should be in lowercase: ''')
        if answer7 == "a":
            print("\n")
            print('''-----------------------------------------------------------------------------------------------------------
                         Congratulations! You have successfully earned [Fish, pork, vegetable] equivalent to 40 Tummy points! 
                     ----------------------------------------------------------------------------------------------------------- \n''')
            print('''                                                          
                                                                                                 _ _ _ _ _ _ _ _
                                                          _________                            /_______________\\            
                                                         /         \\                           I  ##         I                 _____________   
                                                        /--/--|--\--\\          v               I  ##   ___   I                |_____________|    
                                                         | #       |                            I_______I_I___I                 | #  #  # # |
                                              - - - - -  |         |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ HOME B _ _ _ _ _ _ _ _ _  | #  ___  # |                      
                                            |   _ _ _ _  |_______|_|  _ _ _ _ _ _ _ _ _ _ _ _       _ _ _ _ _ _ _ _ _ _ _ _ _ _ |____| |____|                
                                            |  |            HOME A                            |  |                       \N{cat}MARKET   |    |             
                                            |  |                                vv            |  |                                 |    |             
                                            |  |                                              |  |                                 |    |             
                                            |  |                                            + |  |                                 |    |            
                                            |  |                       '^   ^                ~+ ~`~ + - - - - - - - - - - - - - -       - - - - -                     
                                            |  |                       (>^.^<)                 ~.+ POND ~`~ - - - - - - - - - - - - - - - - -       |   
                                         ^ ^ ^ ^ ^ ^ ^                ''/   \\                |  ~'.~  ~                                       |    |
                                       / = = = = = = \\                (_____)____            |  |                                             |    |              
                                         |           |                                        |  |                           |~~~~~~~~|        |    |
                                         |   STORE   |- - - - - - - - - - - -                   ___                          |- - - - |        |    |  
                                         |___________|- - - - - - - - - -     |               //   \\\\                       - BRIDGE- - - - -     |                            |
                                                                          |   |              //     \\\\                    |    _ _ _ _ _ _ _ _ _ _                           
                                                                          |   |             //-------\\\\                   |    |      
                                                                          |   |              |       |                      |    |
                                                               v          |   |              |____#__|                      |    |         vvv
                                                                    vvv   |     - - - - - - - ABANDON HOUSE - - - - - - - -      | vv
                                                                             _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _                    \n''')  # MAP
            score += 40
            print(f'''                                                         ---   Your current score is {score}   ---''')
            earn_sound.play()
        else:
            print("\n")
            print('''--------------------------------------------------------------------------------
                                 Wrong Answer! You have failed to earn a Tummy points.
                     --------------------------------------------------------------------------------''')
            lose_sound.play()

def HAtoHB():
    global location
    global score
    global loc1
    if location == "Home A" and loc1 == "2":  # Home A to Home B
        print("                                                           - - - - - - - - - - - - -")
        print("                                                           Tummy Points: | ", {score})
        print("                                                           - - - - - - - - - - - - - \n")

        duration33 = round(HA_HB / 6.00)  # path1
        add30 = S_HA + A_S + A_P + P_HB  # path2
        duration34 = round(add30 / 6.00)
        add31 = S_HA + A_S + A_B + P_B + P_HB  # path3
        duration35 = round(add31 / 6.00)
        add32 = S_HA + A_S + A_B + B_M + HB_M  # path4
        duration36 = round(add32 / 6.00)

        table = PrettyTable()
        table.field_names = ["", "Possible Routes To Be Taken", "Distance per meter's", "Time Duration"]
        table.add_row([1, "From Home A to Home B                                           ", f"{HA_HB} meters",f"{duration33} hrs"])
        table.add_row([2, "From Home A to Store to Abandon_house to Pond to Home B            ", f"{add30} meters",f"{duration34} hrs"])
        table.add_row([3, "From Home A to Store to Abandon_house to Bridge to Pond to Home B   ", f"{add31} meters",f"{duration35} hrs"])
        table.add_row([4, "From Home A to Store to Abandon_house to Bridge to Market to Home B ", f"{add32} meters",f"{duration36} hrs"])
        print(table)

        distanceList8 = []
        for i in range(4):
            distanceList8.append(HA_HB)
            distanceList8.append(add30)
            distanceList8.append(add31)
            distanceList8.append(add32)

        print(f"The shortest path should be taken is {route[distanceList8.index(min(distanceList8))]}")

        print("\n")
        print('''------------------------------------------------------------------------------------
                        Answer the following Riddle in order for you to get the Tummy points:
                 ------------------------------------------------------------------------------------ \n''')
        print('''------------------------------------------------------------------------------------
                                What belongs to you, but is used by everyone else? 
                 ------------------------------------------------------------------------------------ \n''')
        print('''                         a.) clothes    b.) your name                          \n''')
        answer8 = input('''Your answer should be in lowercase: ''')
        if answer8 == "b":
            print("\n")
            print('''-----------------------------------------------------------------------------------------------
                         Congratulations! You have successfully earned [rice, egg] equivalent to 15 Tummy points! 
                     ----------------------------------------------------------------------------------------------- \n''')
            print('''                                                          
                                                                                                 _ _ _ _ _ _ _ _
                                                          _________                            /_______________\\            
                                                         /         \\                           I  ##         I                 _____________   
                                                        /--/--|--\--\\          v               I  ##   ___   I                |_____________|    
                                                         | #       |                            I_______I_I___I                 | #  #  # # |
                                              - - - - -  |         |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\N{cat}HOME B _ _ _ _ _ _ _ _ _  | #  ___  # |                      
                                            |   _ _ _ _  |_______|_|  _ _ _ _ _ _ _ _ _ _ _ _       _ _ _ _ _ _ _ _ _ _ _ _ _ _ |____| |____|                
                                            |  |            HOME A                            |  |                        MARKET   |    |             
                                            |  |                                vv            |  |                                 |    |             
                                            |  |                                              |  |                                 |    |             
                                            |  |                                            + |  |                                 |    |            
                                            |  |                       '^   ^                ~+ ~`~ + - - - - - - - - - - - - - -       - - - - -                     
                                            |  |                       (>^.^<)                 ~.+ POND ~`~ - - - - - - - - - - - - - - - - -       |   
                                         ^ ^ ^ ^ ^ ^ ^                ''/   \\                |  ~'.~  ~                                       |    |
                                       / = = = = = = \\                (_____)____            |  |                                             |    |              
                                         |           |                                        |  |                           |~~~~~~~~|        |    |
                                         |   STORE   |- - - - - - - - - - - -                   ___                          |- - - - |        |    |  
                                         |___________|- - - - - - - - - -     |               //   \\\\                       - BRIDGE- - - - -     |                            |
                                                                          |   |              //     \\\\                    |    _ _ _ _ _ _ _ _ _ _                           
                                                                          |   |             //-------\\\\                   |    |      
                                                                          |   |              |       |                      |    |
                                                               v          |   |              |____#__|                      |    |         vvv
                                                                   vvv    |     - - - - - - - ABANDON HOUSE - - - - - - - -      | vv
                                                                            _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _                    \n''')  # MAP
            score += 15
            print(f'''                                                       ---   Your current score is {score}   ---''')
            earn_sound.play()
        else:
            print("\n")
            print('''--------------------------------------------------------------------------------
                                  Wrong Answer! You have failed to earn a Tummy points.
                     --------------------------------------------------------------------------------''')
            lose_sound.play()

def HAtoS():
    global location
    global score
    global loc1
    if location == "Home A" and loc1 == "3":  # Home A to Store
        print("                                                           - - - - - - - - - - - - -")
        print("                                                           Tummy Points: | ", {score})
        print("                                                           - - - - - - - - - - - - - \n")

        duration37 = round(S_HA / 6.00)  # path1
        add33 = HA_HB + P_HB + A_P + A_S  # path2
        duration38 = round(add33 / 6.00)
        add34 = HA_HB + HB_M + P_M + A_P + A_S  # path3
        duration39 = round(add34 / 6.00)
        add35 = HA_HB + HB_M + B_M + A_B + A_S  # path4
        duration40 = round(add35 / 6.00)

        table = PrettyTable()
        table.field_names = ["", "Possible Routes To Be Taken", "Distance per meter's", "Time Duration"]
        table.add_row([1, "From Home A to Store                                            ", f"{S_HA} meters",f"{duration37} hrs"])
        table.add_row([2, "From Home A to Home B to Pond to Abandon_house to Store            ", f"{add33} meters",f"{duration38} hrs"])
        table.add_row([3, "From Home A to Home B to Market to Pond to Abandon_house to Store   ", f"{add34} meters",f"{duration39} hrs"])
        table.add_row([4, "From Home A to Home B to Market to Bridge to Abandon_house to Store ", f"{add35} meters",f"{duration40} hrs"])
        print(table)

        distanceList9 = []
        for i in range(4):
            distanceList9.append(S_HA)
            distanceList9.append(add33)
            distanceList9.append(add34)
            distanceList9.append(add35)

        print(f"The shortest path should be taken is {route[distanceList9.index(min(distanceList9))]}")

        print("\n")
        print('''------------------------------------------------------------------------------------
                        Answer the following Riddle in order for you to get the Tummy points:
                 ------------------------------------------------------------------------------------ \n''')
        print('''----------------------------------------------------------------------------------------------
                        You see it once in June, three times in September and never in May. What is it? 
                 ---------------------------------------------------------------------------------------------- \n''')
        print('''                          a.) the letter E    b.) the 31st day                         \n''')
        answer9 = input('''Your answer should be in lowercase: ''')
        if answer9 == "a":
            print("\n")
            print('''--------------------------------------------------------------------------------------------------------
                       Congratulations! You have successfully earned [bread, milk, cat food] equivalent to 30 Tummy points! 
                     -------------------------------------------------------------------------------------------------------- \n''')
            print('''                                                          
                                                                                                  _ _ _ _ _ _ _ _
                                                           _________                            /_______________\\            
                                                          /         \\                           I  ##         I                 _____________   
                                                         /--/--|--\--\\          v               I  ##   ___   I                |_____________|    
                                                          | #       |                            I_______I_I___I                 | #  #  # # |
                                               - - - - -  |         |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ HOME B _ _ _ _ _ _ _ _ _  | #  ___  # |                      
                                             |   _ _ _ _  |_______|_|  _ _ _ _ _ _ _ _ _ _ _ _       _ _ _ _ _ _ _ _ _ _ _ _ _ _ |____| |____|                
                                             |  |            HOME A                            |  |                        MARKET   |    |             
                                             |  |                                vv            |  |                                 |    |             
                                             |  |                                              |  |                                 |    |             
                                             |  |                                            + |  |                                 |    |            
                                             |  |                       '^   ^                ~+ ~`~ + - - - - - - - - - - - - - -       - - - - -                     
                                             |  |                       (>^.^<)                 ~.+ POND ~`~ - - - - - - - - - - - - - - - - -        |   
                                          ^ ^ ^ ^ ^ ^ ^                ''/   \\                |  ~'.~  ~                                        |    |
                                         / = = = = = = \\               (_____)____            |  |                                              |    |              
                                           |           |                                       |  |                            |~~~~~~~~|        |    |
                                           |  \N{cat}STORE  |- - - - - - - - - - - -                   ___                     |- - - - |        |    |  
                                           |___________|- - - - - - - - - -     |               //   \\\\                       - BRIDGE- - - - -     |                            |
                                                                            |   |              //     \\\\                    |    _ _ _ _ _ _ _ _ _ _                           
                                                                            |   |             //-------\\\\                   |    |      
                                                                            |   |              |       |                      |    |
                                                               v            |   |              |____#__|                      |    |         vvv
                                                                      vvv   |     - - - - - - - ABANDON HOUSE - - - - - - - -      | vv
                                                                               _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _                    \n''')  # MAP
            score += 30
            print(f'''                                                          ---   Your current score is {score}   ---''')
            earn_sound.play()
        else:
            print("\n")
            print('''--------------------------------------------------------------------------------
                                  Wrong Answer! You have failed to earn a Tummy points.
                     --------------------------------------------------------------------------------''')
            lose_sound.play()

def HAtoA():
    global location
    global score
    global loc1
    if location == "Home A" and loc1 == "0":  # Home A to Abandon_house
        print("                                                           - - - - - - - - - - - - -")
        print("                                                           Tummy Points: | ", {score})
        print("                                                           - - - - - - - - - - - - - \n")
        add36 = S_HA + A_S  # path1
        duration41 = round(add36 / 6.00)
        add37 = HA_HB + P_HB + A_P  # path2
        duration42 = round(add37 / 6.00)
        add38 = HA_HB + HB_M + P_M + A_P  # path3
        duration43 = round(add38 / 6.00)
        add39 = HA_HB + HB_M + B_M + A_B  # path4
        duration44 = round(add39 / 6.00)

        table = PrettyTable()
        table.field_names = ["", "Possible Routes To Be Taken", "Distance per meter's", "Time Duration"]
        table.add_row([1, "From Home A to Store to Abandon_house                    ", f"{add36} meters", f"{duration41} hrs"])
        table.add_row([2, "From Home A to Home B to Pond to Abandon_House          ", f"{add37} meters", f"{duration42} hrs"])
        table.add_row([3, "From Home A to Home B to Market to Pond to Abandon_house   ", f"{add38} meters", f"{duration43} hrs"])
        table.add_row([4, "From Home A to Home B to Market to Bridge to Abandon_house ", f"{add39} meters", f"{duration44} hrs"])
        print(table)

        distanceList10 = []
        for i in range(4):
            distanceList10.append(add36)
            distanceList10.append(add37)
            distanceList10.append(add38)
            distanceList10.append(add39)

        print(f"The shortest path should be taken is {route[distanceList10.index(min(distanceList10))]}")

        print("\n")
        print('''------------------------------------------------------------------------------------
                        Answer the following Riddle in order for you to get the Tummy points:
                 ------------------------------------------------------------------------------------ \n''')
        print('''------------------------------------------------------------------------------------
                                     What word is spelled wrong in dictionary?
                 ------------------------------------------------------------------------------------ \n''')
        print('''                             a.) none    b.) wrong                       \n''')
        answer10 = input('''Your answer should be in lowercase: ''')
        if answer10 == "b":
            print("\n")
            print('''------------------------------------------------------------------------------------------
                        Congratulations! You have successfully earned [spices] equivalent to 5 Tummy points! 
                     ------------------------------------------------------------------------------------------ \n''')
            print('''                                                          
                                                                                              _ _ _ _ _ _ _ _
                                                        _________                            /_______________\\            
                                                       /         \\                           I  ##         I                 _____________   
                                                      /--/--|--\--\\          v               I  ##   ___   I                |_____________|    
                                                       | #       |                            I_______I_I___I                 | #  #  # # |
                                            - - - - -  |         |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ HOME B _ _ _ _ _ _ _ _ _  | #  ___  # |                      
                                          |   _ _ _ _  |_______|_|  _ _ _ _ _ _ _ _ _ _ _ _       _ _ _ _ _ _ _ _ _ _ _ _ _ _ |____| |____|                
                                          |  |            HOME A                            |  |                        MARKET   |    |             
                                          |  |                                vv            |  |                                 |    |             
                                          |  |                                              |  |                                 |    |             
                                          |  |                                            + |  |                                 |    |            
                                          |  |                       '^   ^                ~+ ~`~ + - - - - - - - - - - - - - -       - - - - -                     
                                          |  |                       (>^.^<)                 ~.+ POND ~`~ - - - - - - - - - - - - - - - - -        |   
                                       ^ ^ ^ ^ ^ ^ ^                ''/   \\                |  ~'.~  ~                                        |    |
                                      / = = = = = = \\               (_____)____            |  |                                              |    |              
                                        |           |                                       |  |                            |~~~~~~~~|        |    |
                                        |   STORE   |- - - - - - - - - - - -                   ___                          |- - - - |        |    |  
                                        |___________|- - - - - - - - - -     |               //   \\\\                       - BRIDGE- - - - -     |                            |
                                                                         |   |              //     \\\\                    |    _ _ _ _ _ _ _ _ _ _                           
                                                                         |   |             //-------\\\\                   |    |      
                                                                         |   |              |       |                      |    |
                                                               v         |   |              |____#__|                      |    |         vvv
                                                                   vvv   |     - - - - - - -\N{cat}ABANDON HOUSE - - - - - - - -      | vv
                                                                           _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _                    \n''')  # MAP
            score += 5
            print(f'''                                                       ---   Your current score is {score}   ---''')
            earn_sound.play()
        else:
            print("\n")
            print('''--------------------------------------------------------------------------------
                                  Wrong Answer! You have failed to earn a Tummy points.
                     --------------------------------------------------------------------------------''')
            lose_sound.play()

def HAtoM():
    global location
    global score
    global loc1
    if location == "Home A" and loc1 == "4":  # Home A to Market
        print("                                                           - - - - - - - - - - - - -")
        print("                                                           Tummy Points: | ", {score})
        print("                                                           - - - - - - - - - - - - -\n")

        add40 = HA_HB + HB_M  # path1
        duration45 = round(add40 / 6.000)
        add41 = HA_HB + P_HB + P_M  # path2
        duration46 = round(add41 / 6.00)
        add42 = S_HA + A_S + A_B + B_M  # path3
        duration47 = round(add42 / 6.00)
        add43 = S_HA + A_S + A_P + P_M
        duration48 = round(add43 / 6.00)

        table = PrettyTable()
        table.field_names = ["", "Possible Routes To Be Taken", "Distance per meter's", "Time Duration"]
        table.add_row([1, "From Home A to Home B to Market                        ", f"{add40} meters", f"{duration45} hrs"])
        table.add_row([2, "From Home A to Home B to Pond to Market                 ", f"{add41} meters", f"{duration46} hrs"])
        table.add_row([3, "From Home A to Store to Abandon_house to Bridge to Market", f"{add42} meters", f"{duration47} hrs"])
        table.add_row([4, "From Home A to Store to Abandon_house to Pond to Market  ", f"{add43} meters", f"{duration48} hrs"])
        print(table)

        distanceList11 = []
        for i in range(4):
            distanceList11.append(add40)
            distanceList11.append(add41)
            distanceList11.append(add42)
            distanceList11.append(add43)

        print(f"The shortest path should be taken is {route[distanceList11.index(min(distanceList11))]}")

        print("\n")
        print('''------------------------------------------------------------------------------------
                        Answer the following Riddle in order for you to get the Tummy points:
                 ------------------------------------------------------------------------------------ \n''')
        print('''-------------------------------------------------------------------------------------------------
                                   If you speak its name, you break it. What is it?
                 ------------------------------------------------------------------------------------------------- \n''')
        print('''                              a.) silence    b.) vase                      \n''')
        answer11 = input('''Your answer should be in lowercase: ''')
        if answer11 == "a":
            print("\n")
            print('''-----------------------------------------------------------------------------------------------------------
                        Congratulations! You have successfully earned [fish, pork, vegetables] equivalent to 40 Tummy points! 
                     ----------------------------------------------------------------------------------------------------------- \n''')
            print('''                                                         
                                                                                                _ _ _ _ _ _ _ _
                                                          _________                            /_______________\\            
                                                         /         \\                           I  ##         I                 _____________   
                                                        /--/--|--\--\\          v               I  ##   ___   I                |_____________|    
                                                         | #       |                            I_______I_I___I                 | #  #  # # |
                                              - - - - -  |         |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ HOME B _ _ _ _ _ _ _ _ _  | #  ___  # |                      
                                            |   _ _ _ _  |_______|_|  _ _ _ _ _ _ _ _ _ _ _ _       _ _ _ _ _ _ _ _ _ _ _ _ _ _ |____| |____|                
                                            |  |            HOME A                            |  |                       \N{cat}MARKET   |    |             
                                            |  |                                vv            |  |                                 |    |             
                                            |  |                                              |  |                                 |    |             
                                            |  |                                            + |  |                                 |    |            
                                            |  |                       '^   ^                ~+ ~`~ + - - - - - - - - - - - - - -       - - - - -                     
                                            |  |                       (>^.^<)                 ~.+ POND ~`~ - - - - - - - - - - - - - - - - -        |   
                                         ^ ^ ^ ^ ^ ^ ^                ''/   \\                |  ~'.~  ~                                        |    |
                                        / = = = = = = \\               (_____)____            |  |                                              |    |              
                                          |           |                                       |  |                            |~~~~~~~~|        |    |
                                          |   STORE   |- - - - - - - - - - - -                   ___                          |- - - - |        |    |  
                                          |___________|- - - - - - - - - -     |               //   \\\\                       - BRIDGE- - - - -     |                            |
                                                                           |   |              //     \\\\                    |    _ _ _ _ _ _ _ _ _ _                           
                                                                           |   |             //-------\\\\                   |    |      
                                                                           |   |              |       |                      |    |
                                                               v           |   |              |____#__|                      |    |         vvv
                                                                     vvv   |     - - - - - - - ABANDON HOUSE - - - - - - - -      | vv
                                                                              _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _                    \n''')  # MAP
            score += 40
            print(f'''                                                          ---   Your current score is {score}   ---''')
            earn_sound.play()

        else:
            print("\n")
            print('''--------------------------------------------------------------------------------
                                  Wrong Answer! You have failed to earn a Tummy points.
                     --------------------------------------------------------------------------------''')
            lose_sound.play()


def HBtoM():
    global location
    global score
    global loc1
    if location == "Home B" and loc1 == "4":
        print("                                                           - - - - - - - - - - - - -")
        print("                                                           Tummy Points: | ", {score})
        print("                                                           - - - - - - - - - - - - - \n")

        duration49 = round(HB_M / 6.00)  # path1
        add44 = P_HB + P_M  # path2
        duration50 = round(add44 / 6.00)
        add45 = P_HB + A_P + A_B + B_M  # path3
        duration51 = round(add45 / 6.00)
        add46 = HA_HB + S_HA + A_S + A_P + P_M  # path4
        duration52 = round(add46 / 6.00)
        add47 = HA_HB + S_HA + A_S + A_B + B_M  # path5
        duration53 = round(add47 / 6.00)

        table = PrettyTable()
        table.field_names = ["", "Possible Routes To Be Taken", "Distance per meter's", "Time Duration"]
        table.add_row([1, "From Home B to Market                                         ", f"{HB_M} meters", f"{duration49} hrs"])
        table.add_row([2, "From Home B to Pond to Market                                  ", f"{add44} meters", f"{duration50} hrs"])
        table.add_row([3, "From Home B to Pond to Abandon_house to  Bridge to Market        ", f"{add45} meters", f"{duration51} hrs"])
        table.add_row([4, "From Home B to Home A to Store to Abandon_house to Pond to Market ", f"{add46} meters", f"{duration52} hrs"])
        table.add_row([5, "From Home B to Home A to Store to Abandon_house to Bridge to Market", f"{add47} meters",f"{duration53} hrs"])
        print(table)

        distanceList12 = []
        for i in range(5):
            distanceList12.append(HB_M)
            distanceList12.append(add44)
            distanceList12.append(add45)
            distanceList12.append(add46)
            distanceList12.append(add47)

        print(f"The shortest path should be taken is {route[distanceList12.index(min(distanceList12))]}")

        print("\n")
        print('''------------------------------------------------------------------------------------
                        Answer the following Riddle in order for you to get the Tummy points:
                 ------------------------------------------------------------------------------------ \n''')
        print('''-------------------------------------------------------------------------------------------------
                                      What kind of band never plays music? 
                 -------------------------------------------------------------------------------------------------\n''')
        print('''                        a.) rubber band    b.) pop band                         \n''')
        answer12 = input('''Your answer should be in lowercase: ''')
        if answer12 == "a":
            print("\n")
            print('''-----------------------------------------------------------------------------------------------------------
                        Congratulations! You have successfully earned [fish, pork, vegetables] equivalent to 40 Tummy points!
                     ----------------------------------------------------------------------------------------------------------- \n''')
            print('''                                                          
                                                                                                    _ _ _ _ _ _ _ _
                                                              _________                            /_______________\\            
                                                             /         \\                           I  ##         I                 _____________   
                                                            /--/--|--\--\\          v               I  ##   ___   I                |_____________|    
                                                             | #       |                            I_______I_I___I                 | #  #  # # |
                                                  - - - - -  |         |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ HOME B _ _ _ _ _ _ _ _ _  | #  ___  # |                      
                                                |   _ _ _ _  |_______|_|  _ _ _ _ _ _ _ _ _ _ _ _       _ _ _ _ _ _ _ _ _ _ _ _ _ _ |____| |____|                
                                                |  |            HOME A                            |  |                       \N{cat}MARKET   |    |             
                                                |  |                                vv            |  |                                 |    |             
                                                |  |                                              |  |                                 |    |             
                                                |  |                                            + |  |                                 |    |            
                                                |  |                       '^   ^                ~+ ~`~ + - - - - - - - - - - - - - -       - - - - -                     
                                                |  |                       (>^.^<)                 ~.+ POND ~`~ - - - - - - - - - - - - - - - - -       |   
                                             ^ ^ ^ ^ ^ ^ ^                ''/   \\                |  ~'.~  ~                                       |    |
                                           / = = = = = = \\                (_____)____            |  |                                             |    |              
                                             |           |                                        |  |                           |~~~~~~~~|        |    |
                                             |   STORE   |- - - - - - - - - - - -                   ___                          |- - - - |        |    |  
                                             |___________|- - - - - - - - - -     |               //   \\\\                       - BRIDGE- - - - -     |                            |
                                                                              |   |              //     \\\\                    |    _ _ _ _ _ _ _ _ _ _                           
                                                                              |   |             //-------\\\\                   |    |      
                                                                              |   |              |       |                      |    |
                                                               v              |   |              |____#__|                      |    |         vvv
                                                                        vvv   |     - - - - - - - ABANDON HOUSE - - - - - - - -      | vv
                                                                                 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _                    \n''')  # MAP
            score += 40
            print(f'''                                                             ---   Your current score is {score}   ---''')
            earn_sound.play()
        else:
            print("\n")
            print('''--------------------------------------------------------------------------------
                                Wrong Answer! You have failed to earn a Tummy points.
                     --------------------------------------------------------------------------------''')
            lose_sound.play()

def HBtoHA():
    global location
    global score
    global loc1
    if location == "Home B" and loc1 == "1":  # Home B to Home A
        print("                                                           - - - - - - - - - - - - -")
        print("                                                           Tummy Points: | ", {score})
        print("                                                           - - - - - - - - - - - - - \n")

        duration54 = round(HA_HB / 6.00)  # path1
        add48 = P_HB + A_P + A_S + S_HA  # path2
        duration55 = round(add48 / 6.00)
        add49 = HB_M + P_M + A_P + A_S + S_HA  # path3
        duration56 = round(add49 / 6.00)
        add50 = HB_M + B_M + A_B + A_S + S_HA
        duration57 = round(add50 / 6.00)

        table = PrettyTable()
        table.field_names = ["", "Possible Routes To Be Taken", "Distance per meter's", "Time Duration"]
        table.add_row([1, "From Home B to Home A                                           ", f"{HA_HB} meters",f"{duration54} hrs"])
        table.add_row([2, "From Home B to Pond to Abandon_house to Store to Home A            ", f"{add48} meters",f"{duration55} hrs"])
        table.add_row([3, "From Home B to Market to Pond to Abandon_house to Store to Home A   ", f"{add49} meters",f"{duration56} hrs"])
        table.add_row([4, "From Home B to Market to Bridge to Abandon_house to Store to Home A ", f"{add50} meters",f"{duration57} hrs"])
        print(table)

        distanceList13 = []
        for i in range(4):
            distanceList13.append(HA_HB)
            distanceList13.append(add48)
            distanceList13.append(add49)
            distanceList13.append(add50)

        print(f"The shortest path should be taken is {route[distanceList13.index(min(distanceList13))]}")

        print("\n")
        print('''------------------------------------------------------------------------------------
                       Answer the following Riddle in order for you to get the Tummy points:
                 ------------------------------------------------------------------------------------ \n''')
        print('''---------------------------------------------------------------------------------------------------------
                    At night, they come without being fetched. By day they are lost without being stolen. What are they?
                 ---------------------------------------------------------------------------------------------------------  \n''')
        print('''                                       a.) moon    b.) stars                         \n''')
        answer13 = input('''Your answer should be in lowercase: ''')
        if answer13 == "b":
            print("\n")
            print('''-----------------------------------------------------------------------------------------------
                        Congratulations! You have successfully earned [fish, rice] equivalent to 10 Tummy points!
                     ----------------------------------------------------------------------------------------------- \n''')
            print('''                                                          
                                                                                                    _ _ _ _ _ _ _ _
                                                              _________                            /_______________\\            
                                                             /         \\                           I  ##         I                 _____________   
                                                            /--/--|--\--\\          v               I  ##   ___   I                |_____________|    
                                                             | #       |                            I_______I_I___I                 | #  #  # # |
                                                  - - - - -  |         |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ HOME B _ _ _ _ _ _ _ _ _  | #  ___  # |                      
                                                |   _ _ _ _  |_______|_|  _ _ _ _ _ _ _ _ _ _ _ _       _ _ _ _ _ _ _ _ _ _ _ _ _ _ |____| |____|                
                                                |  |           \N{cat}HOME A                            |  |                        MARKET   |    |             
                                                |  |                                vv            |  |                                 |    |             
                                                |  |                                              |  |                                 |    |             
                                                |  |                                            + |  |                                 |    |            
                                                |  |                       '^   ^                ~+ ~`~ + - - - - - - - - - - - - - -       - - - - -                     
                                                |  |                       (>^.^<)                 ~.+ POND ~`~ - - - - - - - - - - - - - - - - -        |   
                                             ^ ^ ^ ^ ^ ^ ^                ''/   \\                |  ~'.~  ~                                        |    |
                                            / = = = = = = \\               (_____)____            |  |                                              |    |              
                                              |           |                                       |  |                            |~~~~~~~~|        |    |
                                              |   STORE   |- - - - - - - - - - - -                   ___                          |- - - - |        |    |  
                                              |___________|- - - - - - - - - -     |               //   \\\\                       - BRIDGE- - - - -     |                            |
                                                                               |   |              //     \\\\                    |    _ _ _ _ _ _ _ _ _ _                           
                                                                               |   |             //-------\\\\                   |    |      
                                                                               |   |              |       |                      |    |
                                                               v               |   |              |____#__|                      |    |         vvv
                                                                         vvv   |     - - - - - - - ABANDON HOUSE - - - - - - - -      | vv
                                                                                  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _                     \n''')  # MAP
            score += 10
            print(f'''                                                              ---   Your current score is {score}   ---''')
            earn_sound.play()
        else:
            print("\n")
            print('''--------------------------------------------------------------------------------
                                  Wrong Answer! You have failed to earn a Tummy points.
                     --------------------------------------------------------------------------------''')
            lose_sound.play()


def HBtoS():
    global location
    global score
    global loc1
    if location == "Home B" and loc1 == "3":  # Home B to Store
        print("                                                           - - - - - - - - - - - - -")
        print("                                                           Tummy Points: | ", {score})
        print("                                                           - - - - - - - - - - - - - \n")

        add51 = HA_HB + S_HA  # path1
        duration58 = round(add51 / 6.00)
        add52 = P_HB + A_P + A_S  # path2
        duration59 = round(add52 / 6.00)
        add53 = HB_M + P_M + A_P + A_S  # path3
        duration60 = round(add53 / 6.00)
        add54 = HB_M + B_M + A_B + A_S  # path4
        duration61 = round(add54 / 6.00)

        table = PrettyTable()
        table.field_names = ["", "Possible Routes To Be Taken", "Distance per meter's", "Time Duration"]
        table.add_row([1, "From Home B to Home A to Store                         ", f"{add51} meters", f"{duration58} hrs"])
        table.add_row([2, "From Home B to Pond to Abandon_house to Store           ", f"{add52} meters", f"{duration59} hrs"])
        table.add_row([3, "From Home B to Market to Pond to Abandon_house to Store        ", f"{add53} meters", f"{duration60} hrs"])
        table.add_row([4, "From Home B to Market to Bridge to Abandon_house to Store", f"{add54} meters", f"{duration61} hrs"])
        print(table)

        distanceList14 = []
        for i in range(4):
            distanceList14.append(add51)
            distanceList14.append(add52)
            distanceList14.append(add53)
            distanceList14.append(add54)

        print(f"The shortest path should be taken is {route[distanceList14.index(min(distanceList14))]}")

        print("\n")
        print('''------------------------------------------------------------------------------------
                        Answer the following Riddle in order for you to get the Tummy points:
                 ------------------------------------------------------------------------------------ \n''')
        print('''------------------------------------------------------------------------------------------------
                                  What runs around the whole yard without moving?
                 ------------------------------------------------------------------------------------------------ \n''')
        print('''                             a.) fence    b.)plant                       \n''')
        answer14 = input('''Your answer should be in lowercase: ''')
        if answer14 == "a":
            print("\n")
            print('''---------------------------------------------------------------------------------------------------------
                        Congratulations! You have successfully earned [bread, milk, cat food] equivalent to 30 Tummy points!
                     --------------------------------------------------------------------------------------------------------- \n''')
            print('''                                                          
                                                                                                    _ _ _ _ _ _ _ _
                                                              _________                            /_______________\\            
                                                             /         \\                           I  ##         I                 _____________   
                                                            /--/--|--\--\\          v               I  ##   ___   I                |_____________|    
                                                             | #       |                            I_______I_I___I                 | #  #  # # |
                                                  - - - - -  |         |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ HOME B _ _ _ _ _ _ _ _ _  | #  ___  # |                      
                                                |   _ _ _ _  |_______|_|  _ _ _ _ _ _ _ _ _ _ _ _       _ _ _ _ _ _ _ _ _ _ _ _ _ _ |____| |____|                
                                                |  |            HOME A                            |  |                        MARKET   |    |             
                                                |  |                                vv            |  |                                 |    |             
                                                |  |                                              |  |                                 |    |             
                                                |  |                                            + |  |                                 |    |            
                                                |  |                       '^   ^                ~+ ~`~ + - - - - - - - - - - - - - -       - - - - -                     
                                                |  |                       (>^.^<)                 ~.+ POND ~`~ - - - - - - - - - - - - - - - - -        |   
                                             ^ ^ ^ ^ ^ ^ ^                ''/   \\                |  ~'.~  ~                                        |    |
                                            / = = = = = = \\               (_____)____            |  |                                              |    |              
                                              |           |                                       |  |                            |~~~~~~~~|        |    |
                                              |  \N{cat}STORE  |- - - - - - - - - - - -                   ___                     |- - - - |        |    |  
                                              |___________|- - - - - - - - - -     |               //   \\\\                       - BRIDGE- - - - -     |                            |
                                                                               |   |              //     \\\\                    |    _ _ _ _ _ _ _ _ _ _                           
                                                                               |   |             //-------\\\\                   |    |      
                                                                               |   |              |       |                      |    |
                                                               v               |   |              |____#__|                      |    |         vvv
                                                                         vvv   |     - - - - - - - ABANDON HOUSE - - - - - - - -      | vv
                                                                                 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _                    \n''')  # MAP
            score += 30
            print(f'''                                                            ---   Your current score is {score}   ---''')
            earn_sound.play()
        else:
            print("\n")
            print('''--------------------------------------------------------------------------------
                                 Wrong Answer! You have failed to earn a Tummy points.
                     --------------------------------------------------------------------------------''')
            lose_sound.play()

def HBtoA():
    global location
    global score
    global loc1
    if location == "Home B" and loc1 == "0":  # Home B - Abandon_house
        print("                                                           - - - - - - - - - - - - -")
        print("                                                           Tummy Points: | ", {score})
        print("                                                           - - - - - - - - - - - - - \n")

        add55 = P_HB + A_P  # path1
        duration62 = round(add55 / 6.00)
        add56 = HA_HB + S_HA + A_S  # path2
        duration63 = round(add56 / 6.00)
        add57 = HB_M + P_M + A_P  # path3
        duration64 = round(add57 / 6.00)
        add58 = HB_M + B_M + A_B  # path4
        duration65 = round(add58 / 6.00)

        table = PrettyTable()
        table.field_names = ["", "Possible Routes To Be Taken", "Distance per meter's", "Time Duration"]
        table.add_row([1, "From Home B to Pond to Abandon_house           ", f"{add55} meters", f"{duration62} hrs"])
        table.add_row([2, "From Home B to Home A to Store to Abandon_house ", f"{add56} meters", f"{duration63} hrs"])
        table.add_row([3, "From Home B to Market to Pond to Abandon_house  ", f"{add57} meters", f"{duration64} hrs"])
        table.add_row([4, "From Home B to Market to Bridge to Abandon_house", f"{add58} meters", f"{duration65} hrs"])
        print(table)

        distanceList15 = []
        for i in range(4):
            distanceList15.append(add55)
            distanceList15.append(add56)
            distanceList15.append(add57)
            distanceList15.append(add58)

        print(f"The shortest path should be taken is {route[distanceList15.index(min(distanceList15))]}")

        print("\n")
        print('''------------------------------------------------------------------------------------
                        Answer the following Riddle in order for you to get the Tummy points:
                 ------------------------------------------------------------------------------------ \n''')
        print('''------------------------------------------------------------------------------------ 
                                     What has one head, one foot, and four legs?
                 ------------------------------------------------------------------------------------ \n''')
        print('''                              a.) table    b.) bed                       \n''')
        answer15 = input('''Your answer should be in lowercase: ''')
        if answer15 == "b":
            print("\n")
            print('''------------------------------------------------------------------------------------------
                        Congratulations! You have successfully earned [spices] equivalent to 5 Tummy points!
                     ------------------------------------------------------------------------------------------ \n''')
            print('''                                                          
                                                                                                    _ _ _ _ _ _ _ _
                                                              _________                            /_______________\\            
                                                             /         \\                           I  ##         I                 _____________   
                                                            /--/--|--\--\\          v               I  ##   ___   I                |_____________|    
                                                             | #       |                            I_______I_I___I                 | #  #  # # |
                                                  - - - - -  |         |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ HOME B _ _ _ _ _ _ _ _ _  | #  ___  # |                      
                                                |   _ _ _ _  |_______|_|  _ _ _ _ _ _ _ _ _ _ _ _       _ _ _ _ _ _ _ _ _ _ _ _ _ _ |____| |____|                
                                                |  |            HOME A                            |  |                        MARKET   |    |             
                                                |  |                                vv            |  |                                 |    |             
                                                |  |                                              |  |                                 |    |             
                                                |  |                                            + |  |                                 |    |            
                                                |  |                       '^   ^                ~+ ~`~ + - - - - - - - - - - - - - -       - - - - -                     
                                                |  |                       (>^.^<)                 ~.+ POND ~`~ - - - - - - - - - - - - - - - - -        |   
                                             ^ ^ ^ ^ ^ ^ ^                ''/   \\                |  ~'.~  ~                                        |    |
                                            / = = = = = = \\               (_____)____            |  |                                              |    |              
                                              |           |                                       |  |                            |~~~~~~~~|        |    |
                                              |   STORE   |- - - - - - - - - - - -                   ___                          |- - - - |        |    |  
                                              |___________|- - - - - - - - - -     |               //   \\\\                       - BRIDGE- - - - -     |                            |
                                                                               |   |              //     \\\\                      |    _ _ _ _ _ _ _ _ _ _                           
                                                                               |   |             //-------\\\\                     |    |      
                                                                               |   |              |       |                        |    |
                                                               v               |   |              |____#__|                        |    |         vvv
                                                                         vvv   |     - - - - - - -\N{cat}ABANDON HOUSE - - - - - -      | vv
                                                                                  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _                    \n''')  # MAP
            score += 5
            print(f'''                                                              ---   Your current score is {score}   ---''')
            earn_sound.play()
        else:
            print("\n")
            print('''--------------------------------------------------------------------------------
                                 Wrong Answer! You have failed to earn a Tummy points.
                     --------------------------------------------------------------------------------''')
            lose_sound.play()


def MtoA():
    global location
    global score
    global loc1
    if location == "Market" and loc1 == "0":
        print("                                                           - - - - - - - - - - - - -")
        print("                                                           Tummy Points: | ", {score})
        print("                                                           - - - - - - - - - - - - - \n")

        add59 = B_M + A_B  # path1
        duration66 = round(add59 / 6.00)
        add60 = P_M + A_P  # path2
        duration67 = round(add60 / 6.00)
        add61 = HB_M + P_HB + A_P  # path3
        duration68 = round(add61 / 6.00)
        add62 = HB_M + HA_HB + S_HA + A_S  # path4
        duration69 = round(add62 / 6.00)

        table = PrettyTable()
        table.field_names = ["", "Possible Routes To Be Taken", "Distance per meter's", "Time Duration"]
        table.add_row([1, "From Market to Bridge to Abandon_house                 ", f"{add59} meters", f"{duration66} hrs"])
        table.add_row([2, "From Market to Pond to Abandon_house                   ", f"{add60} meters", f"{duration67} hrs"])
        table.add_row([3, "From Market to Home B to Pond to Abandon_house          ", f"{add61} meters", f"{duration68} hrs"])
        table.add_row([4, "From Market to Home B to Home A to Store to Abandon_house", f"{add62} meters", f"{duration69} hrs"])
        print(table)

        distanceList16 = []
        for i in range(4):
            distanceList16.append(add59)
            distanceList16.append(add60)
            distanceList16.append(add61)
            distanceList16.append(add62)

        print(f"The shortest path should be taken is {route[distanceList16.index(min(distanceList16))]}")

        print("\n")
        print('''------------------------------------------------------------------------------------
                       Answer the following Riddle in order for you to get the Tummy points:
                 ------------------------------------------------------------------------------------ \n''')
        print('''-------------------------------------------------------------------------------------------------------------------
                    There is nothing outside, nothing on the insidelight as the feather, yet ten men cannot lift it. What is it?
                 ------------------------------------------------------------------------------------------------------------------- \n''')
        print('''                                          a.) feather    b.)bubble                        \n''')
        answer16 = input('''Your answer should be in lowercase: ''')
        if answer16 == "b":
            print("\n")
            print('''------------------------------------------------------------------------------------------
                        Congratulations! You have successfully earned [spices] equivalent to 5 Tummy points!
                     ------------------------------------------------------------------------------------------ \n''')
            print('''                                                          
                                                                                                    _ _ _ _ _ _ _ _
                                                             _________                            /_______________\\            
                                                            /         \\                           I  ##         I                 _____________   
                                                           /--/--|--\--\\          v               I  ##   ___   I                |_____________|    
                                                            | #       |                            I_______I_I___I                 | #  #  # # |
                                                 - - - - -  |         |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ HOME B _ _ _ _ _ _ _ _ _  | #  ___  # |                      
                                               |   _ _ _ _  |_______|_|  _ _ _ _ _ _ _ _ _ _ _ _       _ _ _ _ _ _ _ _ _ _ _ _ _ _ |____| |____|                
                                               |  |            HOME A                            |  |                        MARKET   |    |             
                                               |  |                                vv            |  |                                 |    |             
                                               |  |                                              |  |                                 |    |             
                                               |  |                                            + |  |                                 |    |            
                                               |  |                       '^   ^                ~+ ~`~ + - - - - - - - - - - - - - -       - - - - -                     
                                               |  |                       (>^.^<)                 ~.+ POND ~`~ - - - - - - - - - - - - - - - - -        |   
                                            ^ ^ ^ ^ ^ ^ ^                ''/   \\                |  ~'.~  ~                                        |    |
                                           / = = = = = = \\               (_____)____            |  |                                              |    |              
                                             |           |                                       |  |                            |~~~~~~~~|        |    |
                                             |   STORE   |- - - - - - - - - - - -                   ___                          |- - - - |        |    |  
                                             |___________|- - - - - - - - - -     |               //   \\\\                       - BRIDGE- - - - -     |                            |
                                                                              |   |              //     \\\\                      |    _ _ _ _ _ _ _ _ _                           
                                                                              |   |             //-------\\\\                     |    |      
                                                                              |   |              |       |                        |    |
                                                               v              |   |              |____#__|                        |    |         vvv
                                                                        vvv   |     - - - - - - -\N{cat}ABANDON HOUSE - - - - - - - -  | vv
                                                                                   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _                    \n''')  # MAP
            score += 5
            print(f'''                                                               ---   Your current score is {score}   ---''')
            earn_sound.play()
        else:
            print("\n")
            print('''--------------------------------------------------------------------------------
                             Wrong Answer! You have failed to earn a Tummy points.
                     --------------------------------------------------------------------------------''')
            lose_sound.play()

def MtoHB():
    global location
    global score
    global loc1
    if location == "Market" and loc1 == "2":  # market to home B
        print("                                                           - - - - - - - - - - - - -")
        print("                                                           Tummy Points: | ", {score})
        print("                                                           - - - - - - - - - - - - - \n")
        duration70 = round(HB_M / 6.00)  # path1
        add63 = P_M + P_HB  # path2
        duration71 = round(add63 / 6.00)
        add64 = B_M + A_B + A_P + P_HB  # path3
        duration72 = round(add64 / 6.00)
        add65 = B_M + A_B + A_S + S_HA + HA_HB  # path4
        duration73 = round(add65 / 6.00)

        table = PrettyTable()
        table.field_names = ["", "Possible Routes To Be Taken", "Distance per meter's", "Time Duration"]
        table.add_row([1, "From Market to Home B                                          ", f"{HB_M} meters", f"{duration70} hrs"])
        table.add_row([2, "From Market to Pond to Home B                                   ", f"{add63} meters",f"{duration71} hrs"])
        table.add_row([3, "From Market to Bridge to Abandon_house to Pond to Home B          ", f"{add64} meters",f"{duration72} hrs"])
        table.add_row([4, "From Market to Bridge to Abandon_house to Store to Home A to Home B", f"{add65} meters",f"{duration73} hrs"])
        print(table)

        distanceList17 = []
        for i in range(4):
            distanceList17.append(HB_M)
            distanceList17.append(add63)
            distanceList17.append(add64)
            distanceList17.append(add65)

        print(f"The shortest path should be taken is {route[distanceList17.index(min(distanceList17))]}")

        print("\n")
        print('''------------------------------------------------------------------------------------
                         Answer the following Riddle in order for you to get the Tummy points:
                 ------------------------------------------------------------------------------------ \n''')
        print('''------------------------------------------------------------------------------------------------------------
                    I stand in the corner of a building and never leave. Yet, my children travel everywhere. What am I?
                 ------------------------------------------------------------------------------------------------------------ \n''')
        print('''                                      a.) bench    b.) mailbox                      \n''')
        answer17 = input('''Your answer should be in lowercase: ''')
        if answer17 == "b":
            print("\n")
            print('''----------------------------------------------------------------------------------------------
                        Congratulations! You have successfully earned [rice, egg] equivalent to 15 Tummy points!
                     ---------------------------------------------------------------------------------------------- \n''')
            print('''                                                          
                                                                                                     _ _ _ _ _ _ _ _
                                                               _________                            /_______________\\            
                                                              /         \\                           I  ##         I                 _____________   
                                                             /--/--|--\--\\          v               I  ##   ___   I                |_____________|    
                                                              | #       |                            I_______I_I___I                 | #  #  # # |
                                                   - - - - -  |         |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\N{cat}HOME B _ _ _ _ _ _ _ _ _  | #  ___  # |                      
                                                 |   _ _ _ _  |_______|_|  _ _ _ _ _ _ _ _ _ _ _ _       _ _ _ _ _ _ _ _ _ _ _ _ _ _ |____| |____|                
                                                 |  |            HOME A                            |  |                        MARKET   |    |             
                                                 |  |                                vv            |  |                                 |    |             
                                                 |  |                                              |  |                                 |    |             
                                                 |  |                                            + |  |                                 |    |            
                                                 |  |                       '^   ^                ~+ ~`~ + - - - - - - - - - - - - - -       - - - - -                     
                                                 |  |                       (>^.^<)                 ~.+ POND ~`~ - - - - - - - - - - - - - - - - -       |   
                                              ^ ^ ^ ^ ^ ^ ^                ''/   \\                |  ~'.~  ~                                       |    |
                                            / = = = = = = \\                (_____)____            |  |                                             |    |              
                                              |           |                                        |  |                           |~~~~~~~~|        |    |
                                              |   STORE   |- - - - - - - - - - - -                   ___                          |- - - - |        |    |  
                                              |___________|- - - - - - - - - -     |               //   \\\\                       - BRIDGE- - - - -     |                            |
                                                                               |   |              //     \\\\                    |    _ _ _ _ _ _ _ _ _ _                           
                                                                               |   |             //-------\\\\                   |    |      
                                                                               |   |              |       |                      |    |
                                                               v               |   |              |____#__|                      |    |         vvv
                                                                         vvv   |     - - - - - - - ABANDON HOUSE - - - - - - - -      | vv
                                                                                 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _                   \n ''')  # MAP
            score += 15
            print(f'''                                                             ---   Your current score is {score}   ---''')
            earn_sound.play()
        else:
            print("\n")
            print('''--------------------------------------------------------------------------------
                                  Wrong Answer! You have failed to earn a Tummy points.
                     --------------------------------------------------------------------------------''')
            lose_sound.play()


def MtoHA():
    global location
    global score
    global loc1
    if location == "Market" and loc1 == "1":  # market to home A
        print("                                                           - - - - - - - - - - - - -")
        print("                                                           Tummy Points: | ", {score})
        print("                                                           - - - - - - - - - - - - - \n")

        add66 = HB_M + HA_HB  # path1
        duration74 = round(add66 / 6.00)
        add67 = P_M + P_HB + HA_HB  # path2
        duration75 = round(add67 / 6.00)
        add68 = P_M + A_P + A_S + S_HA  # path3
        duration76 = round(add68 / 6.00)
        add69 = B_M + A_B + A_S + S_HA  # path4
        duration77 = round(add69 / 6.00)
        add70 = B_M + A_B + A_P + P_HB + HA_HB  # path5
        duration78 = round(add69 / 6.00)

        table = PrettyTable()
        table.field_names = ["", "Possible Routes To Be Taken", "Distance per meter's", "Time Duration"]
        table.add_row([1, "From Market to Home B to Home A                                ", f"{add66} meters", f"{duration74} hrs"])
        table.add_row([2, "From Market to Pond to Home B to Home A                         ", f"{add67} meters", f"{duration75} hrs"])
        table.add_row([3, "From Market to Pond to Abandon_house to Store to Home A          ", f"{add68} meters", f"{duration76} hrs"])
        table.add_row([4, "From Market to Bridge to Abandon_house to Store to Home A        ", f"{add69} meters", f"{duration77} hrs"])
        table.add_row([5, "From Market to Bridge to Abandon_house to Pond to Home B to Home A", f"{add70} meters", f"{duration78} hrs"])
        print(table)

        distanceList18 = []
        for i in range(5):
            distanceList18.append(add66)
            distanceList18.append(add67)
            distanceList18.append(add68)
            distanceList18.append(add69)
            distanceList18.append(add70)

        print(f"The shortest path should be taken is {route[distanceList18.index(min(distanceList18))]}")

        print("\n")
        print('''------------------------------------------------------------------------------------
                       Answer the following Riddle in order for you to get the Tummy points:
                 ------------------------------------------------------------------------------------ \n''')
        print('''------------------------------------------------------------------------------------
                                      What kind of cheese is made backward?
                 ------------------------------------------------------------------------------------ \n''')
        print('''                             a.) eden    b.) edam                       \n''')
        answer18 = input('''Your answer should be in lowercase: ''')
        if answer18 == "b":
            print("\n")
            print('''-----------------------------------------------------------------------------------------------
                        Congratulations! You have successfully earned [fish, rice] equivalent to 10 Tummy points!
                     ----------------------------------------------------------------------------------------------- \n''')
            print('''                                                          
                                                                                                   _ _ _ _ _ _ _ _
                                                            _________                            /_______________\\            
                                                           /         \\                           I  ##         I                 _____________   
                                                          /--/--|--\--\\          v               I  ##   ___   I                |_____________|    
                                                           | #       |                            I_______I_I___I                 | #  #  # # |
                                                - - - - -  |         |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ HOME B _ _ _ _ _ _ _ _ _  | #  ___  # |                      
                                              |   _ _ _ _  |_______|_|  _ _ _ _ _ _ _ _ _ _ _ _       _ _ _ _ _ _ _ _ _ _ _ _ _ _ |____| |____|                
                                              |  |           \N{cat}HOME A                            |  |                        MARKET   |    |             
                                              |  |                                vv            |  |                                 |    |             
                                              |  |                                              |  |                                 |    |             
                                              |  |                                            + |  |                                 |    |            
                                              |  |                       '^   ^                ~+ ~`~ + - - - - - - - - - - - - - -       - - - - -                     
                                              |  |                       (>^.^<)                 ~.+ POND ~`~ - - - - - - - - - - - - - - - - -        |   
                                           ^ ^ ^ ^ ^ ^ ^                ''/   \\                |  ~'.~  ~                                        |    |
                                          / = = = = = = \\               (_____)____            |  |                                              |    |              
                                            |           |                                       |  |                            |~~~~~~~~|        |    |
                                            |   STORE   |- - - - - - - - - - - -                   ___                          |- - - - |        |    |  
                                            |___________|- - - - - - - - - -     |               //   \\\\                       - BRIDGE- - - - -     |                            |
                                                                             |   |              //     \\\\                    |    _ _ _ _ _ _ _ _ _ _                           
                                                                             |   |             //-------\\\\                   |    |      
                                                                             |   |              |       |                      |    |
                                                               v             |   |              |____#__|                      |    |         vvv
                                                                       vvv   |     - - - - - - - ABANDON HOUSE - - - - - - - -      | vv
                                                                                _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _                    \n''')  # MAP
            score += 10
            print(f'''                                                             ---   Your current score is {score}   ---''')
            earn_sound.play()
        else:
            print("\n")
            print('''--------------------------------------------------------------------------------
                                Wrong Answer! You have failed to earn a Tummy points.
                     --------------------------------------------------------------------------------''')
            lose_sound.play()

def MtoS():
    global location
    global score
    global loc1
    if location == "Market" and loc1 == "3":  # market to Store
        print("                                                           - - - - - - - - - - - - -")
        print("                                                           Tummy Points: | ", {score})
        print("                                                           - - - - - - - - - - - - - \n")

        add71 = HB_M + HA_HB + S_HA  # path1
        duration79 = round(add71 / 6.00)
        add72 = P_M + P_HB + HA_HB + S_HA  # path2
        duration80 = round(add72 / 6.00)
        add73 = P_M + A_P + A_S  # path3
        duration81 = round(add73 / 6.00)
        add74 = B_M + A_B + A_S  # path4
        duration82 = round(add74 / 6.00)

        table = PrettyTable()
        table.field_names = ["", "Possible Routes To Be Taken", "Distance per meter's", "Time Duration"]
        table.add_row([1, "From Market to Home B to Home A to Store       ", f"{add71} meters", f"{duration79} hrs"])
        table.add_row([2, "From Market to Pond to Home B to Home A - Store", f"{add72} meters", f"{duration80} hrs"])
        table.add_row([3, "From Market to Pond to Abandon_house to Store  ", f"{add73} meters", f"{duration81} hrs"])
        table.add_row([4, "From Market to Bridge to Abandon_house to Store", f"{add74} meters", f"{duration82} hrs"])
        print(table)

        distanceList19 = []
        for i in range(4):
            distanceList19.append(add71)
            distanceList19.append(add72)
            distanceList19.append(add73)
            distanceList19.append(add74)

        print(f"The shortest path should be taken is {route[distanceList19.index(min(distanceList19))]}")

        print("\n")
        print('''------------------------------------------------------------------------------------
                       Answer the following Riddle in order for you to get the Tummy points:
                 ------------------------------------------------------------------------------------ \n''')
        print('''-------------------------------------------------------------------------------------------------
                                         What has 18 legs and catches flies?
                 ------------------------------------------------------------------------------------------------- \n''')
        print('''                          a.) baseball team    b.) spider                         \n''')
        answer19 = input('''Your answer should be in lowercase: ''')
        if answer19 == "a":
            print("\n")
            print('''----------------------------------------------------------------------------------------------------------
                        Congratulations! You have successfully earned [bread, milk, cat food] equivalent to 30 Tummy points!
                     ---------------------------------------------------------------------------------------------------------- \n''')
            print('''                                                          
                                                                                                     _ _ _ _ _ _ _ _
                                                              _________                            /_______________\\            
                                                             /         \\                           I  ##         I                 _____________   
                                                            /--/--|--\--\\          v               I  ##   ___   I                |_____________|    
                                                             | #       |                            I_______I_I___I                 | #  #  # # |
                                                  - - - - -  |         |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ HOME B _ _ _ _ _ _ _ _ _  | #  ___  # |                      
                                                |   _ _ _ _  |_______|_|  _ _ _ _ _ _ _ _ _ _ _ _       _ _ _ _ _ _ _ _ _ _ _ _ _ _ |____| |____|                
                                                |  |            HOME A                            |  |                        MARKET   |    |             
                                                |  |                                vv            |  |                                 |    |             
                                                |  |                                              |  |                                 |    |             
                                                |  |                                            + |  |                                 |    |            
                                                |  |                       '^   ^                ~+ ~`~ + - - - - - - - - - - - - - -       - - - - -                     
                                                |  |                       (>^.^<)                 ~.+ POND ~`~ - - - - - - - - - - - - - - - - -      |   
                                             ^ ^ ^ ^ ^ ^ ^                ''/   \\                |  ~'.~  ~                                      |    |
                                            / = = = = = = \\               (_____)____            |  |                                            |    |              
                                              |           |                                       |  |                            |~~~~~~~~|      |    |
                                              |  \N{cat}STORE  |- - - - - - - - - - - -                   ___                     |- - - - |      |    |  
                                              |___________|- - - - - - - - - -     |               //   \\\\                        - BRIDGE- - - -    |                            |
                                                                               |   |              //     \\\\                    |    _ _ _ _ _ _ _ _ _                          
                                                                               |   |             //-------\\\\                   |    |      
                                                                               |   |              |       |                      |    |
                                                               v               |   |              |____#__|                      |    |         vvv
                                                                         vvv   |     - - - - - - - ABANDON HOUSE - - - - - - - -      | vv
                                                                                  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _                    \n''')  # MAP
            score += 30
            print(f'''                                                              ---   Your current score is {score}   ---''')
            earn_sound.play()
        else:
            print("\n")
            print('''--------------------------------------------------------------------------------
                                   Wrong Answer! You have failed to earn a Tummy points.
                     --------------------------------------------------------------------------------''')
            lose_sound.play()

while (menu < 2):
    proceed = input('''                                                         CONTINUE [Y|N]: ''')
    if proceed.lower() == "y":

        print('''
    
                                                       _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _           
                                                       | Place Discription:                                                       |
                                                       |  AN ABANDON PLACE:                                                       | 
                                                       |     Ten years ago, this location was well-known for selling spices       |
                                                       |     that were shipped around the city, but an unforeseen event caused    |
                                                       |     the owners to close the business.                                    |
                                                       |     Visit this location to find out what happened.                       |
                                                                : [spices] = 5 tummy points
                                                       |  HOME A:                                                                 |
                                                       |     Normal family in day but become different at night.                  |
                                                       |     Will you still willing to go?                                        |
                                                                 : [Fish,Rice] = 10 tummy points
                                                       |  HOME B:                                                                 |
                                                       |     Only has a simply food but it's safe here.ps(Not sure)               |
                                                                 : [Rice, Egg] = 15 tummy points
                                                       |  MARKET:                                                                 |
                                                       |     A market has a random thing that you need. Your favorite             |
                                                       |     food is here.                                                        |
                                                                 : [Fish, Pork, Vegetable] = 40 tummy points
                                                       |  STORE:                                                                  |
                                                       |      The store has a pack of food.                                       |
                                                                 : [Bread, milk,cat food] = 30 tummy points          
    
                                                        - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -        
                                       ''') # PLACE DISCRIPTION
        global loc1
        global location

        list1 = ["Abandon_house", "Home A", "Home B", "Store", "Market"] # List of location to randomize.
        route = ["Route 1", "Route 2", "Route 3", "Route 4", "Route 5"]
        distance = [55, 60, 45, 35, 95]
        distance1 = [10, 13, 15, 16, 20, 18]
        random.shuffle(distance)
        random.shuffle(distance1)
        # Randomize distance
        print('''                                                                  - - - - - - - - - - - - - - - - - - - - - - - - -                             
                                                                                Distance per meter's''')  # Variable type to use in making a formula.
        S_HA = distance[0]
        HA_HB = distance[1]
        HB_M = distance[2]
        M_A = distance[3]
        A_S = distance[4]
        A_P = distance1[0]
        P_HB = distance1[1]
        A_B = distance1[2]
        B_M = distance1[3]
        P_B = distance1[4]
        P_M = distance1[5]
        print('''                                                                   - - - - - - - - - - - - - - - - - - - - - - - - -  ''')
        # Distance relating Bridge and Pond, also use in formula.

        print(f'''                                                              |          Store to Home A         : {S_HA} meters              |
                                                              |          Home A to Home B        : {HA_HB} meters              |
                                                              |          Home B to Market        : {HB_M} meters              |
                                                              |          Market to Abandon       : {M_A} meters              |
                                                              |          Abandon to Store        : {A_S} meters              |
                                                              |                         ~Intersection~                    |
                                                              |          Abandon_house to Pond   : {A_P} meters              |
                                                              |          Pond to Home B          : {P_HB} meters              |
                                                              |          Abandon_house to Bridge : {A_B} meters              |
                                                              |          Bridge to Market        : {B_M} meters              |
                                                              |          Pond to Bridge          : {P_B} meters              |
                                                              |          Pond to Market          : {P_M} meters              |
                                                                                                 ''')
        location = random.choice(list1)  # Randomize current possition.
        if location == "Abandon_house":
            print(f'''                                            ::::::::::::::::::::::::::::::::::::::::::::::::::::::            
                                                                  ::::'## ::::::: ##  :::: ### ::::: ## ## ## ::::::::;
                                                               :::::: '## ##   ## ## :::: ## ##  ::: ## ::: ##  :::::::::
                                                            :::::::::: ##.:## ##: ## ::  ## : ##  :: ## ::: ##  :::::::::::::
                                                           ::::::::::: ## .  ##   ## :  #########  : ## ## ## ::::::::::::::
                                                            :::::::::: ## ::::::: ## .: ## ':: ## :: ## ::::::::::::::......
                                                               ::::::: ##: :::::: ##..: ## :::;## :  ##  ::::::::::;:...
                                                                  ::::::::::::::::::::::::::::::::::::::::::::::::::;

                                                                                                   _ _ _ _ _ _ _ _
                                                             _________                            /_______________\\            
                                                            /         \\                           I  ##         I                 _____________   
                                                           /--/--|--\--\\          v               I  ##   ___   I                |_____________|    
                                                            | #       |                            I_______I_I___I                 | #  #  # # |
                                                 - - - - -  |         |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ HOME B _ _ _ _ _ _ _ _ _  | #  ___  # |                      
                                               |   _ _ _ _  |_______|_|  _ _ _ _ _ _ _ _ _ _ _ _       _ _ _ _ _ _ _ _ _ _ _ _ _ _ |____| |____|                
                                               |  |            HOME A                            |  |                        MARKET   |    |             
                                               |  |                                vv            |  |                                 |    |             
                                               |  |                                              |  |                                 |    |             
                                               |  |                                            + |  |                                 |    |            
                                               |  |                       '^   ^                ~+ ~`~ + - - - - - - - - - - - - - -           - - - - -                     
                                               |  |                       (>^.^<)                 ~.+ POND ~`~ - - - - - - - - - - - - - - - - -        |   
                                            ^ ^ ^ ^ ^ ^ ^                  ''/   \\              |  ~'.~  ~                                        |    |
                                          / = = = = = = \\                  (_____)____          |  |                                              |    |              
                                           |           |                                         |  |                          |~~~~~~~~|          |    |
                                           |   STORE   |- - - - - - - - - - - -                   ___                          |- - - - |          |    |  
                                           |___________|- - - - - - - - - -     |               //   \\\\                       - BRIDGE- - - - -       |                            
                                                                            |   |              //     \\\\                    |    _ _ _ _ _ _ _ _ _ _                           
                                                                            |   |             //-------\\\\                   |    |      
                                                                            |   |              |       |                      |    |
                                                                  v         |   |              |____#__|                      |    |         vvv
                                                                      vvv   |     - - - - - - {indicator}ABANDON HOUSE - - - - - - - -      | vv
                                                                              _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _                    \n''')  # MAP
        elif location == "Home A":
            print(f'''                                            ::::::::::::::::::::::::::::::::::::::::::::::::::::::            
                                                                  ::::'## ::::::: ##  :::: ### ::::: ## ## ## ::::::::;
                                                               :::::: '## ##   ## ## :::: ## ##  ::: ## ::: ##  :::::::::
                                                            :::::::::: ##.:## ##: ## ::  ## : ##  :: ## ::: ##  :::::::::::::
                                                           ::::::::::: ## .  ##   ## :  #########  : ## ## ## ::::::::::::::
                                                            :::::::::: ## ::::::: ## .: ## ':: ## :: ## ::::::::::::::......
                                                               ::::::: ##: :::::: ##..: ## :::;## :  ##  ::::::::::;:...
                                                                   ::::::::::::::::::::::::::::::::::::::::::::::::::;

                                                                                                  _ _ _ _ _ _ _ _
                                                            _________                            /_______________\\            
                                                           /         \\                           I  ##         I                 _____________   
                                                          /--/--|--\--\\          v               I  ##   ___   I                |_____________|    
                                                           | #       |                            I_______I_I___I                 | #  #  # # |
                                                - - - - -  |         |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ HOME B _ _ _ _ _ _ _ _ _  | #  ___  # |                      
                                              |   _ _ _ _  |_______|_|  _ _ _ _ _ _ _ _ _ _ _ _       _ _ _ _ _ _ _ _ _ _ _ _ _ _ |____| |____|                
                                              |  |         {indicator}                          |  |                        MARKET   |    |             
                                              |  |           Home A           vv                |  |                                 |    |             
                                              |  |                                              |  |                                 |    |             
                                              |  |                                            + |  |                                 |    |            
                                              |  |                         '^   ^                ~+ ~`~ + - - - - - - - - - - - - - -           - - - -                      
                                              |  |                         (>^.^<)                 ~.+ POND ~`~ - - - - - - - - - - - - - - - - -      |   
                                           ^ ^ ^ ^ ^ ^ ^                  ''/   \\              |  ~'.~  ~                                        |    |
                                         / = = = = = = \\                  (_____)____          |  |                                              |    |              
                                           |           |                                        |  |                          |~~~~~~~~|          |    |
                                           |   STORE   |- - - - - - - - - - - -                   ___                          |- - - - |         |    |  
                                           |___________|- - - - - - - - - -     |               //   \\\\                       - BRIDGE- - - - -      |                            
                                                                            |   |              //     \\\\                    |    _ _ _ _ _ _ _ _ _ _                           
                                                                            |   |             //-------\\\\                   |    |      
                                                                            |   |              |       |                      |    |
                                                                v           |   |              |____#__|                      |    |         vvv
                                                                      vvv   |     - - - - - - - - - - - - - - - - - - - - - -      | vv
                                                                             _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _                 \n''')  # MAPP
        elif location == "Home B":
            print(f'''                                            ::::::::::::::::::::::::::::::::::::::::::::::::::::::            
                                                                  ::::'## ::::::: ##  :::: ### ::::: ## ## ## ::::::::;
                                                               :::::: '## ##   ## ## :::: ## ##  ::: ## ::: ##  :::::::::
                                                            :::::::::: ##.:## ##: ## ::  ## : ##  :: ## ::: ##  :::::::::::::
                                                           ::::::::::: ## .  ##   ## :  #########  : ## ## ## ::::::::::::::
                                                            :::::::::: ## ::::::: ## .: ## ':: ## :: ## ::::::::::::::......
                                                               ::::::: ##: :::::: ##..: ## :::;## :  ##  ::::::::::;:...
                                                                  ::::::::::::::::::::::::::::::::::::::::::::::::::;  

                                                                                                  _ _ _ _ _ _ _ _
                                                            _________                            /_______________\\            
                                                           /         \\                           I  ##         I                 _____________   
                                                          /--/--|--\--\\          v               I  ##   ___   I                |_____________|    
                                                           | #       |                            I_______I_I___I                 | #  #  # # |
                                                 - - - - - |         |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ {indicator}HOME B _ _ _ _ _ _ _ _ _  | #  ___  # |                      
                                              |   _ _ _ _  |_______|_|  _ _ _ _ _ _ _ _ _ _ _ _       _ _ _ _ _ _ _ _ _ _ _ _ _ _ |____| |____|                
                                              |  |            HOME A                            |  |                        MARKET   |    |             
                                              |  |                                vv            |  |                                 |    |             
                                              |  |                                              |  |                                 |    |             
                                              |  |                                            + |  |                                 |    |            
                                              |  |                       '^   ^                ~+ ~`~ + - - - - - - - - - - - - - -       - - - - -                     
                                              |  |                       (>^.^<)                 ~.+ POND ~`~ - - - - - - - - - - - - - - - - -       |   
                                           ^ ^ ^ ^ ^ ^ ^                  ''/   \\              |  ~'.~  ~                                       |    |
                                         / = = = = = = \\                  (_____)____          |  |                                             |    |              
                                           |           |                                        |  |                          |~~~~~~~~|         |    |
                                           |   STORE   |- - - - - - - - - - - -                   ___                          |- - - - |        |    |  
                                           |___________|- - - - - - - - - -     |               //   \\\\                       - BRIDGE- - - - -     |                            
                                                                            |   |              //     \\\\                      |    _ _ _ _ _ _ _ _ _                          
                                                                            |   |             //-------\\\\                     |    |      
                                                                            |   |              |       |                        |    |
                                                                  v         |   |              |____#__|                        |    |         vvv
                                                                     vvv    |     - - - - - - - ABANDON HOUSE - - - - - - - -        | vv
                                                                              _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _                    \n''')  # MAP
        elif location == "Store":
            print(f'''                                            ::::::::::::::::::::::::::::::::::::::::::::::::::::::            
                                                                  ::::'## ::::::: ##  :::: ### ::::: ## ## ## ::::::::;
                                                               :::::: '## ##   ## ## :::: ## ##  ::: ## ::: ##  :::::::::
                                                            :::::::::: ##.:## ##: ## ::  ## : ##  :: ## ::: ##  :::::::::::::
                                                           ::::::::::: ## .  ##   ## :  #########  : ## ## ## ::::::::::::::
                                                            :::::::::: ## ::::::: ## .: ## ':: ## :: ## ::::::::::::::......
                                                               ::::::: ##: :::::: ##..: ## :::;## :  ##  ::::::::::;:...
                                                                  ::::::::::::::::::::::::::::::::::::::::::::::::::;          

                                                                                                  _ _ _ _ _ _ _ _
                                                            _________                            /_______________\\            
                                                           /         \\                           I  ##         I                 _____________   
                                                          /--/--|--\--\\          v               I  ##   ___   I                |_____________|    
                                                           | #       |                            I_______I_I___I                 | #  #  # # |
                                                - - - - -  |         |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ HOME B _ _ _ _ _ _ _ _ _  | #  ___  # |                      
                                              |   _ _ _ _  |_______|_|  _ _ _ _ _ _ _ _ _ _ _ _       _ _ _ _ _ _ _ _ _ _ _ _ _ _ |____| |____|                
                                              |  |            HOME A                            |  |                        MARKET   |    |             
                                              |  |                                vv            |  |                                 |    |             
                                              |  |                                              |  |                                 |    |             
                                              |  |                                            + |  |                                 |    |            
                                              |  |                       '^   ^                ~+ ~`~ + - - - - - - - - - - - - - -       - - - - -                     
                                              |  |                       (>^.^<)                 ~.+ POND ~`~ - - - - - - - - - - - - - - - - -       |   
                                           ^ ^ ^ ^ ^ ^ ^                  ''/   \\              |  ~'.~  ~                                       |    |
                                         / = = = = = = \\                  (_____)____          |  |                                             |    |              
                                           |           |                                        |  |                          |~~~~~~~~|         |    |
                                           |{indicator} STORE|- - - - - - - - - - - -                   ___                          |- - - - |        |    |  
                                           |___________|- - - - - - - - - -     |               //   \\\\                       - BRIDGE- - - - -     |                            
                                                                            |   |              //     \\\\                      |    _ _ _ _ _ _ _ _ _                         
                                                                            |   |             //-------\\\\                     |    |      
                                                                            |   |              |       |                        |    |
                                                                  v         |   |              |____#__|                        |    |         vvv
                                                                 vvv        |     - - - - - - - ABANDON HOUSE - - - - - - - -        | vv
                                                                               _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _                    \n''')  # MAP
        elif location == "Market":
            print(f'''                                           ::::::::::::::::::::::::::::::::::::::::::::::::::::::            
                                                                 ::::'## ::::::: ##  :::: ### ::::: ## ## ## ::::::::;
                                                              :::::: '## ##   ## ## :::: ## ##  ::: ## ::: ##  :::::::::
                                                           :::::::::: ##.:## ##: ## ::  ## : ##  :: ## ::: ##  :::::::::::::
                                                          ::::::::::: ## .  ##   ## :  #########  : ## ## ## ::::::::::::::
                                                           :::::::::: ## ::::::: ## .: ## ':: ## :: ## ::::::::::::::......
                                                              ::::::: ##: :::::: ##..: ## :::;## :  ##  ::::::::::;:...
                                                                 ::::::::::::::::::::::::::::::::::::::::::::::::::;        

                                                                                                 _ _ _ _ _ _ _ _
                                                           _________                            /_______________\\            
                                                          /         \\                           I  ##         I                 _____________   
                                                         /--/--|--\--\\          v               I  ##   ___   I                |_____________|    
                                                          | #       |                            I_______I_I___I                 | #  #  # # |
                                               - - - - -  |         |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ HOME B _ _ _ _ _ _ _ _ _  | #  ___  # |                      
                                             |   _ _ _ _  |_______|_|  _ _ _ _ _ _ _ _ _ _ _ _       _ _ _ _ _ _ _ _ _ _ _ _ _ _ |____| |____|                
                                             |  |            HOME A                            |  |                      {indicator}MARKET   |    |             
                                             |  |                                vv            |  |                                 |    |             
                                             |  |                                              |  |                                 |    |             
                                             |  |                                            + |  |                                 |    |            
                                             |  |                       '^   ^                ~+ ~`~ + - - - - - - - - - - - - - -       - - - - -                     
                                             |  |                       (>^.^<)                 ~.+ POND ~`~ - - - - - - - - - - - - - - - - -      |   
                                          ^ ^ ^ ^ ^ ^ ^                  ''/   \\              |  ~'.~  ~                                      |    |
                                        / = = = = = = \\                  (_____)____          |  |                                            |    |              
                                         |           |                                         |  |                          |~~~~~~~~|        |    |
                                         |   STORE   |- - - - - - - - - - - -                   ___                          |- - - - |        |    |  
                                         |___________|- - - - - - - - - -     |               //   \\\\                       - BRIDGE- - - - -     |                            
                                                                          |   |              //     \\\\                      |    _ _ _ _ _ _ _ _ _                           
                                                                          |   |             //-------\\\\                     |    |      
                                                                          |   |              |       |                        |    |
                                                                  v       |   |              |____#__|                        |    |         vvv
                                                                    vvv   |     - - - - - - - ABANDON HOUSE - - - - - - - -        | vv
                                                                             _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _                    \n''')  # MAP

        print('''                                                              - - - - - - - - - - - - - - - - - - - - - - - - -''')
        print('''                                                                      Your Current location is''', location)

        data = {'distance': [55, 60, 45, 35, 95],
                'duration': ['55 minutes', '1 hour', '45 minutes', '35 minutes', '1:35 minutes']}
        # ABANDON HOUSE
        print('''                                                              - - - - - - - - - - - - - - - - - - - - - - - - -''')
        print('''                                                                              Choices Location:
                                                                                [0] Abandon_house
                                                                                [1] Home A
                                                                                [2] Home B
                                                                                [3] Store
                                                                                [4] Market  ''')
        print('''                                                               - - - - - - - - - - - - - - - - - - - - - - - - - \n''')
        loc1 = (input('''                                                   Input a place you want to visit: '''))
        if location == "Abandon_house" and loc1 == "0" or location == "Home A" and loc1 == "1" or location == "Home B" and loc1 == "2" or location == "Store" and loc1 == "3" or location == "Market" and loc1 == "4":
            print('''                                                               You are already at your desired destination.''')


        AtoS()
        AtoHA()
        AtoM()
        AtoHB()
        StoA()
        StoM()
        StoHA()
        StoHB()
        HAtoM()
        HAtoA()
        HAtoS()
        HAtoHB()
        HBtoM()
        HBtoHA()
        HBtoA()
        HBtoS()
        MtoS()
        MtoHA()
        MtoHB()
        MtoA()

        if score == 100:
            win_sound.play()
            print(
                '''                                       Congratulations! You successfully earned 100 points, you win the game :>>''')
            menu += 1

        elif score > 100:
            win_sound.play()
            print('''                                                      ~CONGRATULATIONS! YOU WON THE GAME~ \n
                                                             Ryan have now enough tummy points to fill in his hungry stomach. 
                                                             However, you can still continue to play the game! \n''')
    elif proceed == "N":
        quit("                                                                 Thank you for trying.")


    else:
        quit("Bye")




