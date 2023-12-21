import time

print("-----------WELCOME TO PUBG MOBILE-----------")
name=input("enter your name: ")
print("Hi!", name , "welocome to the game")
def lobby():
    print("Heres the lobby ")
    print("1.Maps")
    print("2.inventory")
    print("3.missions")
    print("4.invite friends")
    print("5.quit")

def school():
    kills=0
    alive=100
    print("you are landed on top of the school building")
    mode=input("enemy started hitting bullets on you! select jump/stay: ").lower()
    if mode=='stay':
        print("you are dead! with {0} kills".format(kills))
    elif mode=='jump':
        print("you had entered into room and equiped m416,vest and helmet")
        mode1=input("you witnessed the footsteps beside you and enemy is infront of you? select fire/calm: ")
        if mode1=="calm":
            print("enemy killed you!, you dead! with {0} kills", format(kills))
        elif mode1=="fire":
            print("you had killed the enemy with m416")
            kills+=1
            alive-=1
            print("total kills =", kills)
            print("alive =", alive)
            direction=input("now move left/right: ")
            if direction=="left":
                print("full squad rushed on you!  and killed you :(")
                alive-=1
                print("total kills =", kills)
                print("alive =", alive)
                maps()
            elif direction=="right":
                print("you killed full squad and equiped AWM gun with few supplies")
                kills+=4
                alive-=4
                print("total kills =", kills)
                print("alive =", alive)
                direction1=input("now move left/right: ")
                if direction1=="left":
                    print("you killed by m24 from long shot :(")
                    alive-=1
                    print("total kills =", kills)
                    print("alive =", alive)
                    print("start new match.....")
                elif direction1=="right":
                    print("you killed by akm from top of the school building :(")
                    alive-=1
                    print("total kills =", kills)
                    print("alive =", alive)
                    print("start new match.....")
                else:
                    print("select the correct option")

            else:
                print("select the correct option")
        else:
           print("select the correct option") 
    else:
        print("select the correct option")
        school()
        
    
def pochinki():
    kills=0
    alive=100
    print("you are landed on top of the squad house")
    mode=input("enemy started hitting bullets on you! select jump/stay: ").lower()
    if mode=='stay':
        print("you are dead! with {0} kills".format(kills))
    elif mode=='jump':
        print("you had entered into room and equiped ump45,vest and pan")
        mode1=input("you witnessed the footsteps beside you and enemy is infront of you? select fire/calm: ")
        if mode1=="calm":
            print("enemy killed you!, you dead! with {0} kills", format(kills))
        elif mode1=="fire":
            print("you had killed the enemy with ump45")
            kills+=1
            alive-=1
            print("total kills =", kills)
            print("alive =", alive)
            direction=input("now move left/right: ").lower()
            if direction=="left":
                print("you had equiped flare gun")
                use_flare=input("use flare gun yes/no:")
                if use_flare=="yes":
                    print("u shooted flare gun and waiting for air drop")
                    print("......air drop landing.......")
                    print(".")
                    print(".")
                    print(".")
                    print(".")
                    print("finally air drop is infront of you :)")
                    open_crate=input("r you ready to open airdrop yes/no : ").lower()
                    if open_crate=="yes":
                        print("you had looted AWM , Lv3 vest, Lv3 helmet :) ")
                    elif open_crate=="no":
                        print("skipped the drop and waiting for enemy")
                        time.sleep(60)
                        enemy1=input("enemy spotted infront of u fire/wait: ").lower()
                        if enemy1=="fire":
                            print("you killed enemy")
                            kills+=1
                            alive-=1
                            print("total kills =", kills)
                            print("alive =", alive)
                        elif enemy1=="wait":
                            print("he looted your drop and killed you :(")
                            alive-=1
                            print("total kills =", kills)
                            print("alive =", alive)
                    else:
                        print("select correct option")                        
                elif use_flare=="no":
                    print("you had droped flare gun")
                else:
                    print("select the correct option")
                
            elif direction=="right":
                print("you killed full squad and equiped flare gun with few supplies")
                kills+=4
                alive-=4
                print("total kills =", kills)
                print("alive =", alive)
                direction1=input("now move left/right: ").lower()
                if direction1=="left":
                    print("you killed by kar98 from long shot :(")
                    alive-=1
                    print("total kills =", kills)
                    print("alive =", alive)
                    print("start new match.....")
                elif direction1=="right":
                    print("you killed by vector from 2nd building :(")
                    alive-=1
                    print("total kills =", kills)
                    print("alive =", alive)
                    print("start new match.....")
                else:
                    print("select the correct option")

            else:
                print("select the correct option")
        else:
           print("select the correct option") 
    else:
        print("select the correct option")
        pochinki()
def military_base():
    kills=0
    alive=100
    print("you are landed on top of the c-building")
    mode=input("enemy started hitting bullets on you! select jump/stay: ").lower()
    if mode=='stay':
        print("you are dead! with {0} kills".format(kills))
    elif mode=='jump':
        print("you had entered into room and equiped thompson and uzi")
        mode1=input("you witnessed the footsteps beside you and enemy is infront of you? select fire/calm: ").lower()
        if mode1=="calm":
            print("enemy killed you!, you dead! with {0} kills", format(kills))
        elif mode1=="fire":
            print("you had killed the enemy with uzi")
            kills+=1
            alive-=1
            print("total kills =", kills)
            print("alive =", alive)
            direction=input("now move left/right: ").lower()
            if direction=="left":
                print("two enemies rushed on you!  and killed you :(")
                alive-=1
                print("total kills =", kills)
                print("alive =", alive)
                maps()
            elif direction=="right":
                print("you killed 3 enemies and equiped their supplies")
                kills+=3
                alive-=3
                print("total kills =", kills)
                print("alive =", alive)
                direction1=input("now move left/right: ").lower()
                if direction1=="left":
                    print("you killed by vss from long shot :(")
                    alive-=1
                    print("total kills =", kills)
                    print("alive =", alive)
                    print("start new match.....")
                elif direction1=="right":
                    print("you have killed by enemy with m416 using red-dot")
                    alive-=1
            
                    print("total kills =", kills)
                    print("alive =", alive)
                else:
                    print("select the correct option")

            else:
                print("select the correct option")
        else:
           print("select the correct option") 
    else:
        print("select the correct option")
        military_base()
def erangle():
    print("Erangle map welcomes you",name)
    print("present your are on plane, select the place you need to land \n 1.school \n 2.pochinki\n 3.military base")
    place_choice=int(input("enter choice:"))
    if place_choice==1:
        school()
    elif place_choice==2:
        pochinki()
    elif place_choice==3:
        military_base()

def power_plant():
    kills=0
    alive=100
    print("you are landed on top of the plant building")
    mode=input("enemy started hitting bullets on you! select jump/stay: ").lower()
    if mode=='stay':
        print("you are dead! with {0} kills".format(kills))
    elif mode=='jump':
        print("you had entered into room and equiped m416,vest and helmet")
        mode1=input("you witnessed the footsteps beside you and enemy is infront of you? select fire/calm: ").lower()
        if mode1=="calm":
            print("enemy killed you!, you dead! with {0} kills", format(kills))
        elif mode1=="fire":
            print("you had killed the enemy with m416")
            kills+=1
            alive-=1
            print("total kills =", kills)
            print("alive =", alive)
            direction=input("now move left/right: ").lower()
            if direction=="left":
                print("full squad rushed on you!  and killed you :(")
                alive-=1
                print("total kills =", kills)
                print("alive =", alive)
                maps()
            elif direction=="right":
                print("you killed full squad and equiped AWM gun with few supplies")
                kills+=4
                alive-=4
                print("total kills =", kills)
                print("alive =", alive)
                direction1=input("now move left/right: ").lower()
                if direction1=="left":
                    print("you killed by m24 from long shot :(")
                    alive-=1
                    print("total kills =", kills)
                    print("alive =", alive)
                    print("start new match.....")
                elif direction1=="right":
                    print("you killed by akm from top of the plant building :(")
                    alive-=1
                    print("total kills =", kills)
                    print("alive =", alive)
                    print("start new match.....")
                else:
                    print("select the correct option")

            else:
                print("select the correct option")
        else:
           print("select the correct option") 
    else:
        print("select the correct option")
        power_plant()
        
    
def hot_springs():
    kills=0
    alive=100
    print("you are landed in hotsprings")
    mode=input("enemy started hitting bullets on you! select move/stay: ").lower()
    if mode=='stay':
        print("you are dead! with {0} kills".format(kills))
    elif mode=='move':
        print("you had entered into room and equiped ump45,vest and pan")
        mode1=input("you witnessed the footsteps beside you and enemy is infront of you? select fire/calm: ").lower()
        if mode1=="calm":
            print("enemy killed you!, you dead! with {0} kills", format(kills))
        elif mode1=="fire":
            print("you had killed the enemy with ump45")
            kills+=1
            alive-=1
            print("total kills =", kills)
            print("alive =", alive)
            direction=input("now move left/right: ").lower()
            if direction=="left":
                print("you had equiped flare gun")
                use_flare=input("use flare gun yes/no:")
                if use_flare=="yes":
                    print("u shooted flare gun and waiting for air drop")
                elif use_flare=="no":
                    print("you had droped flare gun")
                else:
                    print("select the correct option")
                
            elif direction=="right":
                print("you killed full squad and equiped flare gun with few supplies")
                kills+=4
                alive-=4
                print("total kills =", kills)
                print("alive =", alive)
                direction1=input("now move left/right: ").lower()
                if direction1=="left":
                    print("you killed by kar98 from long shot :(")
                    alive-=1
                    print("total kills =", kills)
                    print("alive =", alive)
                    print("start new match.....")
                elif direction1=="right":
                    print("you killed by vector from 2nd building :(")
                    alive-=1
                    print("total kills =", kills)
                    print("alive =", alive)
                    print("start new match.....")
                else:
                    print("select the correct option")

            else:
                print("select the correct option")
        else:
           print("select the correct option") 
    else:
        print("select the correct option")
        hot_springs()
def midstein():
    kills=0
    alive=100
    print("you are landed on top of the building")
    mode=input("enemy started hitting bullets on you! select jump/stay: ").lower()
    if mode=='stay':
        print("you are dead! with {0} kills".format(kills))
    elif mode=='jump':
        print("you had entered into room and equiped thompson and uzi")
        mode1=input("you witnessed the footsteps beside you and enemy is infront of you? select fire/calm: ").lower()
        if mode1=="calm":
            print("enemy killed you!, you dead! with {0} kills", format(kills))
        elif mode1=="fire":
            print("you had killed the enemy with uzi")
            kills+=1
            alive-=1
            print("total kills =", kills)
            print("alive =", alive)
            direction=input("now move left/right: ").lower()
            if direction=="left":
                print("two enemies rushed on you!  and killed you :(")
                alive-=1
                print("total kills =", kills)
                print("alive =", alive)
                maps()
            elif direction=="right":
                print("you killed 3 enemies and equiped their supplies")
                kills+=3
                alive-=3
                print("total kills =", kills)
                print("alive =", alive)
                direction1=input("now move left/right: ").lower()
                if direction1=="left":
                    print("you killed by vss from long shot :(")
                    alive-=1
                    print("total kills =", kills)
                    print("alive =", alive)
                    print("start new match.....")
                elif direction1=="right":
                    print("you have killed 1 enemy with m416 using red-dot")
                    alive-=1
                    kills+=1
                    print("total kills =", kills)
                    print("alive =", alive)
                else:
                    print("select the correct option")

            else:
                print("select the correct option")
        else:
           print("select the correct option") 
    else:
        print("select the correct option")
        midstein()
def livic():
    print("Livic map welcomes you",name)
    print("present your are on plane, select the place you need to land \n 1.power plant \n 2.hot springs\n 3.midstein")
    place_choice=int(input("enter choice:"))
    if place_choice==1:
        power_plant()
    elif place_choice==2:
        hot_springs()
    elif place_choice==3:
        midstein()
def shanok():
    pass
def miramar():
    pass

def maps():
    print("-------list of maps----------------")
    print("1.erangle")
    print("2.livic")
    print("3.shanok")
    print("4.miramar")
    print("-----------------------------------")
    map_choice=int(input("select your map: "))
    if map_choice==1:
        erangle()
    elif map_choice==2:
        livic()
    elif map_choice==3:
        shanok()
    elif map_choice==4:
        miramar()
def inventory():
    print("---------------------------------------------------")
    print("its your first game so u dont have any items yet :)")
    print("---------------------------------------------------")
def missions():
    print("---------------------------------------------------")
    print("mission1: kill 50 enemies with m416")
    print("mission2: kill 50 enemies with akm")
    print("mission3: collect cocktail for 15 times")
    print("mission4: kill 10 enemies with AWM")
    print("mission5: loot 5 air drops")
    print("---------------------------------------------------")

def invite_friends():
    pass
while True:
    lobby()
    choice=int(input("enter your choice as per options: "))
    if choice==1:
        maps()
    elif choice==2:
        inventory()
    elif choice==3:
        missions()
    elif choice==4:
        invite_friends()
    elif choice==5:
        quit()
    else:
        print("please enter the correct options")
