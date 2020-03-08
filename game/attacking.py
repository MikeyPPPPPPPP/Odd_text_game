import random



class attack:
    def __init__(self,player,monster):
        self.you = player
        self.mons = monster


    def start(self):
        print('\n')
        self.mons.mhit(self.you)

        if self.you.health >= 0:
            if random.randint(0, 1) == '1':
                self.mons.mhit(self.you)
                return 3
            else:
                print('attack(y/n)')
                att = input(': ')
                if att == 'y':
                    self.you.phit(self.mons)
                    return 3
                else:
                    print('why')
                    return 3
        elif self.you.health <= 0 and self.mons.health != 0:
            print("you lose!")
            return 1

        elif self.you.health != 0 and self.mons.health <= 0:
            self.mons.reward(self.you)
            print('you won!')
            return 2

        else:
            self.mons.reward(self.you)
            print('you won!')
            return 3

