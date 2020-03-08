class player:
    def __init__(self, name):
        self.name = name
        self.strangth = 0
        self.health = 100
        self.level = 0
        self.hit = 2.5
        self.tools = []
        self.moved = []


    def showstats(self):
        print('nsame: ',self.name, 'strength: ',self.strangth,'health: ',self.health,'level: ', self.level, 'hit power', self.hit)

    def showtools(self):
        print('---tools---')
        for x in self.tools:
            print(x)

    def phit(self, attacking):
        attacking.health  -= self.hit

