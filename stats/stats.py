class Stats:
    def __init__(self):
        self.o = OffenseStatistics()
        self.d = DefenseStatistics()

    def __add__(self, other):
        
        self.o.ab += other.o.ab
        self.o.pa += other.o.pa
        self.o.ab += other.o.ab
        self.o.hits += other.o.hits
        self.o.bb += other.o.bb
        self.o.tb += other.o.tb
        self.o.runs += other.o.runs
        self.o.lob += other.o.lob
        self.o.rbi = other.o.rbi
        self.o.gdp = other.o.gdp
        self.d.pitchCount += other.d.pitchCount
        self.d.strike += other.d.strike
        self.d.ball += other.d.ball
        self.d.out += other.d.out
        self.d.er += other.d.er

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
        self.gdp = 0


class DefenseStatistics:
    def __init__(self):
        self.pitchCount = 0
        self.strike = 0
        self.ball = 0
        self.out = 0
        self.er = 0
