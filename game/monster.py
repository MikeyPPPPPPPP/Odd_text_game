import scoring_alg


class monster:
    def __init__(self, type, level, health, hit):
        self.type = type
        self.level = level
        self.health = health
        self.hit = hit

    def showstats(self):
        print('nsame: ', 'health: ', self.health, 'level: ', self.level,
              'hit power', self.hit)
        return self.health

    def mhit(self, attacking):
        attacking.health -= self.hit

    def reward(self, killed_by):
        killed_by.level += 8
        killed_by.strangth += scoring_alg.scor_stren(killed_by.level, self.level)