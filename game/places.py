import random
import time
import attacking
import monster
import os


def coolplace():
    print("cool place!")# add the town townNtree
    return 1

class houses:
    def __init__(self, playing, level=None, item=None):
        self.level = level
        self.item = item
        self.playing = playing

    def enter(self):
        if self.level-1 < self.playing.level:
            print("Hello chum, you must be new.")
            print("copy this:")

    def myhouse(self):
        print("House\n")
        print("you are in your room, do you want to sleep or leave(s,l)\n")
        get = input(':')
        if get == 's':
            self.playing.health += 10
            print('health', self.playing.health)
            return 1
        else:
            print('leaving.')
            return 0

class lake:
    def __init__(self, playing):
        self.playing = playing

    def lake(self):
        # print("Going to the Lake.\n")
        print("do you want to fish?")
        fishq = input('y/n: ')
        if fishq == 'y':
            t = 0
            while t == 0:
                a = random.randint(0, 1)
                if a == 1:
                    print("You got a fish")

                    print('new level: ', self.playing.level, ' to ', self.playing.level)
                    self.playing.level += 3  # .3
                    time.sleep(.5)
                    st = 1
                    while st != 0:

                        tryag = input("try again?: ")
                        if tryag == "y":
                            return 1
                        else:
                            return 0
            else:
                return 0
        else:
            return 0

class outside:
    def __init__(self, playing, graph,  lake, allhouses):
        self.graf = graph
        self.playing = playing
        self.lake = lake
        self.allhouses = allhouses

    def outside(self):




        print(self.graf.basmap)
        print("where to go (l, h, ?, t)m?: ")
        mov = input(':')
        if mov == 'h': ##############################3                  my_house
            self.playing.moved.append('h')
            a = 1
            while a == 1:
                # house(playing)
                print(self.graf.bahouse)  ######################             houses
                a = self.allhouses.myhouse()

            print('Outside')


        elif mov == 'l':####################################          lake
            a = 1
            print("Going to the Lake.\n")
            print(self.graf.atlake)
            while a == 1:
                self.playing.moved.append('l')
                a = self.lake.lake()
                if a != 0:
                    print("At the Lake.\n")
                    print(self.graf.atlake)
            print('Outside')


        elif mov == "?":  #                           ?
            if self.playing.level >= 7:
                self.playing.moved.append('?')
                print(self.graf.question)
                time.sleep(2)
                coolplace()
                #                                        add something here
            else:
                print('\nNot Level 7')
                print('your level', self.playing.level)
                time.sleep(2)
                m1 = monster.monster("basic", 1, 5, 2)
                attk = attacking.attack(self.playing, m1)

                while m1.health != 0 or m1.health <= 0:
                    print('\033[1;33mMONSTER !!!!!!!!!\033[1;m')
                    time.sleep(1)
                    s = self.playing.health
                    m = m1.health
                    if m1.health >= 0:
                        print('\033[1;36;48mYour life \033[1;m', self.playing.health)
                        print('\033[1;31;48mmonsters life:  \033[1;m', m1.health)
                        attk.start()
                        pass
                    else:
                        break

                m1.reward(self.playing)
                print("Rewarded! check level.")
                time.sleep(2)
                self.playing.showstats()
                time.sleep(1)
                pass

        elif mov == "?q":
            print(self.graf.question)
            coolplace()
            time.sleep(1)
        elif mov == "t":  #                                          town : make
            print(self.graf.waytown)
            self.playing.moved.append('t')
            time.sleep(2)
            print(self.graf.townNtree)
            towninp = input("Where to: (s t ?)")  # add a handeler
            print(towninp)
            return 1
        elif mov == "m": #                                            map
            if self.playing.level >= 7:
                print(self.graf.maps7)
            else:
                print(self.graf.maps)
        elif mov == "G":
            print('\033[1;32m---------Entering GOD Mode---------\033[1;31m')
            self.playing.strangth = 100
            self.playing.health = 100000
            self.playing.level = 1000
            self.playing.hit = 1000
            self.playing.showstats()



class town_N_tree(outside):
    def __init__(self, playing, graph,  lake, allhouses):
        self.graf = graph
        self.playing = playing
        self.lake = lake
        self.allhouses = allhouses

    def town_entrence(self):
        print(self.graf.basmap)
        print("where to go (l, h, ?, t)m?: ")
        mov = input(':')
        if mov == 'h':  ##############################3                  my_house
            self.allhouses.myhouse()




        elif mov == 'l':  ####################################          lake
            a = 1
            print("Going to the Lake.\n")
            print(self.graf.atlake)
            while a == 1:
                self.playing.moved.append('l')
                a = self.lake.lake()
                if a != 0:
                    print("At the Lake.\n")
                    print(self.graf.atlake)
            print('Outside')


        elif mov == "?":  # ?
            if self.playing.level >= 7:
                self.playing.moved.append('?')
                print(self.graf.question)
                time.sleep(2)
                ############################################
                return 123
            else:
                print('\nNot Level 7')
                print('your level', self.playing.level)
                time.sleep(2)
                m1 = monster.monster("basic", 1, 5, 2)
                attk = attacking.attack(self.playing, m1)

                while m1.health != 0 or m1.health <= 0:
                    print('\033[1;33mMONSTER !!!!!!!!!\033[1;m')
                    time.sleep(1)
                    s = self.playing.health
                    m = m1.health
                    if m1.health >= 0:
                        print('\033[1;36;48mYour life \033[1;m', self.playing.health)
                        print('\033[1;31;48mmonsters life:  \033[1;m', m1.health)
                        attk.start()
                        pass
                    else:
                        break

                m1.reward(self.playing)
                print("Rewarded! check level.")
                time.sleep(2)
                self.playing.showstats()
                time.sleep(1)
                pass

    def in_town(self):
        print(self.graf.townNtree)
        towninp = input("Where to: (s t ?)")
        if towninp == "s":
            print("severs")
            return 2
        elif towninp == "?":
            time.sleep(1)
            print(self.graf.question)
            return 1
        else:
            print("Town")
            return 3
