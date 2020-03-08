from player import player
from monster import monster
import places
import graphics
import random
import time
import os

lev1mon = monster('monster', 1, 5, 2)

def starting(playing):
    playing.level = random.randint(1,5)
    playing.strangth = random.randint(1,5)


def coolplace(playing):
    print("cool place!")# add the town townNtree
    return 1


def rand():
    a = random.randint(1, 2)
    if a == '1':
        return 1
    else:
        return 0


def intersec(playing):
    graf = graphics.graphic()
    allhouses = places.houses(playing)
    lake = places.lake(playing)
    outsid = places.outside(playing, graf, lake, allhouses)
    return outsid.outside()





def town_intersect(playing):
    graf = graphics.graphic()
    allhouses = places.houses(playing)
    lake = places.lake(playing)
    towninter = places.town_N_tree(playing, graf, lake, allhouses)
    return towninter.in_town()







def getin(me):
    h = ("cmd: stats")
    i = input('h for help >>>')
    if i == 'stats':
        me.showstats()
        return 1
    else:
        print("dont want to see items? Ok")
        return 0

def menu():
    print('\033[1;32m+----menu----+\033[1;31m')
    print('\033[1;32m|\033[1;31m \033[1;31m   1.play  \033[1;m\033[1;32m|\033[1;31m')
    print('\033[1;32m|\033[1;31m \033[1;31m   2.exit  \033[1;m\033[1;32m|\033[1;31m')
    print('\033[1;32m+------------+\033[1;m')
    getins = input(': ')
    if getins == '1':
        thegame()
    else:
        print('exiting')

def contin(playing):
    con = input('\ncontinue(y/n): ')
    if con == 'y':
        intersec(playing)
    else:
        sho = getin(playing)
        if sho == 1:
            print(1)
            #gameset += 1
        elif sho == 0:
            gameset = 0

        else:
            print("error")

def thegame():

    gameset = 0
    cont = 0 # continue
    tow  = 0
    me = player('michael')

    starting(me)
    print("\nstarting stats\n")
    me.showstats()

    while cont != 1:
        while gameset == 0:

            con = input('\ncontinue(y/n): ')
            if con == 'y':
                os.system('cls')
                intersec(me)
            else:
                sho = getin(me)
                if sho == 1:
                    print(1)
                    # gameset += 1
                elif sho == 0:
                    gameset = 0

                else:
                    print("error")

            a = intersec(me)# outside
            if a == 1:
                gameset = 1

        while tow == 0:
            os.system('cls')
            s = town_intersect(me)

            if a == 1:
                gameset = 0
                tow += 1
            elif a == 2:
                print("serer")
            elif a == 3:
                print("town")
            else:
                print("not real")
        print("finally!")




if __name__=='__main__':
    menu()
