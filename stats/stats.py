class Stats:
    def __init__(self):
        self.o = OffenseStatistics()
        self.d = DefenseStatistics()
        self.games_played = 0

    def __iadd__(self, other):
        self.o.pa += other.o.pa
        self.o.ab += other.o.ab
        self.o.hits += other.o.hits
        self.o.bb += other.o.bb
        self.o.tb += other.o.tb
        self.o.runs += other.o.runs
        self.o.lob += other.o.lob
        self.o.rbi += other.o.rbi
        self.o.sb += other.o.sb
        self.o.gdp += other.o.gdp
        self.o.so += other.o.so
        self.o.b1 += other.o.b1
        self.o.b2 += other.o.b2
        self.o.b3 += other.o.b3
        self.o.hr += other.o.hr
        self.d.pitchCount += other.d.pitchCount
        self.d.strike += other.d.strike
        self.d.ball += other.d.ball
        self.d.out += other.d.out
        self.d.er += other.d.er
        self.games_played += 1
        return self

    def __str__(self):
        return ' '.join(['\nStatistics are Per Game Per Team:',
                         '\n---------------------------------'
                         '\nRuns Per Game (4.07-4.86):', "{:3.2f}".format(self.o.runs / self.games_played / 2),
                         '\nGames Played:', str(self.games_played),
                         '\nPlate Appearances (37.03-38.80):', "{:3.2f}".format(self.o.pa / self.games_played / 2),
                         '\nAt Bats (32.87-34.51):', "{:3.2f}".format(self.o.ab / self.games_played / 2),
                         '\nRuns (4.07-4.86):', "{:3.2f}".format(self.o.runs / self.games_played / 2),
                         '\nHits (8.04-9.28):', "{:3.2f}".format(self.o.hits / self.games_played / 2),
                         '\n1B (5.06-6.15):', "{:3.2f}".format(self.o.b1 / self.games_played / 2),
                         '\n2B (1.57-1.89):', "{:3.2f}".format(self.o.b2 / self.games_played / 2),
                         '\n3B (0.13-0.20):', "{:3.2f}".format(self.o.b3 / self.games_played / 2),
                         '\nHR (0.89-1.39):', "{:3.2f}".format(self.o.hr / self.games_played / 2),
                         '\nSB (0.57-0.72):', "{:3.2f}".format(self.o.sb / self.games_played / 2),
                         '\nBB (2.88-3.39):', "{:3.2f}".format(self.o.bb / self.games_played / 2),
                         '\nSO (6.52-8.37):', "{:3.2f}".format(self.o.so / self.games_played / 2),
                         '\nBA (.243-.269):', "{:3.3f}".format(self.o.hits / self.o.ab),
                         '\nTB (13-35-14.59):', "{:3.2f}".format(self.o.tb / self.games_played / 2),
                         '\nGDP (.68-.82):', "{:3.2f}".format(self.o.gdp / self.games_played / 2),
                         ])


class OffenseStatistics:
    def __init__(self):
        self.pa = 0
        self.ab = 0
        self.hits = 0
        self.bb = 0
        self.tb = 0
        self.runs = 0
        self.lob = 0
        self.rbi = 0
        self.sb = 0
        self.gdp = 0
        self.so = 0
        self.b1 = 0
        self.b2 = 0
        self.b3 = 0
        self.hr = 0


class DefenseStatistics:
    def __init__(self):
        self.pitchCount = 0
        self.strike = 0
        self.ball = 0
        self.out = 0
        self.er = 0
