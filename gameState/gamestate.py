import stats
import players
from ShowdownOutcomes import ShowdownOutcomes


class GameState:
    def __init__(self, visitor_team, home_team):
        self.verbose_pitch_prints = False
        self.bases = [0, 0, 0]
        self.count = (0, 0)
        self.outs = 0
        self.isTopOfInning = 1
        self.inning = 1
        self.score = (0, 0)
        self.stats = stats.Stats()
        self.visitor_team = visitor_team
        self.home_team = home_team
        self.iHome = 0
        self.iAway = 0

    def play_game(self):
        while not self.is_final():
            # print('Before:', self)
            if self.isTopOfInning:
                outcome = players.players.make_action_roll(self.visitor_team.batters[self.iAway], self.home_team.pitchers[0])
            else:
                outcome = players.players.make_action_roll(self.home_team.batters[self.iHome], self.visitor_team.pitchers[0])
            match outcome:
                case ShowdownOutcomes.HITINTODOUBLEPLAY:
                    self.hit_into_double_play()
                case ShowdownOutcomes.HITINTOOUT:
                    self.hit_into_out()
                case ShowdownOutcomes.SACRAFICE:
                    self.sacrifice()
                case ShowdownOutcomes.STRIKE:
                    self.strike()
                case ShowdownOutcomes.FOUL:
                    self.foul()
                case ShowdownOutcomes.BALL:
                    self.ball()
                case ShowdownOutcomes.SINGLE:
                    self.single()
                case ShowdownOutcomes.DOUBLE:
                    self.double()
                case ShowdownOutcomes.TRIPLE:
                    self.triple()
                case ShowdownOutcomes.HOMERUN:
                    self.homerun()
                case ShowdownOutcomes.STOLENBASE:
                    self.stolen_base()

            # print("After:", self)
        # print(self)
        return self.stats

    def __str__(self):
        final = ''
        if self.is_final():
            final = 'FINAL:'
        if self.isTopOfInning:
            return ' '.join([final, 'Score:', str(self.score),
                             'Top of the', str(self.inning),
                             ',', str(self.outs), 'outs, count is:', str(self.count)])
        else:
            return ' '.join([final, 'Score:', str(self.score),
                             'Bottom of the', str(self.inning),
                             ',', str(self.outs), 'outs, count is:', str(self.count)])

    def is_final(self):
        assert(0 <= self.outs <= 3)
        is_final = False
        if self.inning >= 9:
            if self.isTopOfInning and self.outs >= 3 and self.__is_home_team_winning():
                is_final = True
            elif not self.isTopOfInning and self.__is_home_team_winning():
                is_final = True
            elif not self.isTopOfInning and self.outs >= 3 and not self.__is_tie():
                is_final = True
        return is_final

    #########################
    # Defense - Outs

    def hit_into_double_play(self):
        if self.verbose_pitch_prints:
            print('Double Play Rolled...')
        self.stats.d.pitchCount += 1
        self.__out()
        if self.outs < 3:
            if self.bases[0] == 1:
                if self.verbose_pitch_prints:
                    print('Double Play!')
                self.stats.o.gdp += 1
                self.bases[0] = 0
                self.__out()
            elif self.bases[1] == 1:
                if self.verbose_pitch_prints:
                    print('Double Play!')
                self.stats.o.gdp += 1
                self.bases[1] = 0
                self.__out()
            elif self.bases[2] == 1:
                if self.verbose_pitch_prints:
                    print('Double Play!')
                self.stats.o.gdp += 1
                self.bases[2] = 0
                self.__out()
        if self.verbose_pitch_prints:
            print('Double Play fully resolved')

    def hit_into_out(self):
        if self.verbose_pitch_prints:
            print('Hit into out')
        self.stats.d.pitchCount += 1
        self.__out()

    def sacrifice(self):
        if self.verbose_pitch_prints:
            print('Sacrifice')
        self.stats.d.pitchCount += 1
        self.__out()
        if self.outs <= 2:
            self.__advance_runners(1)

    #########################
    # Offense - Hits

    def homerun(self):
        if self.verbose_pitch_prints:
            print('Home Run!')
        self.__hit(4)
        self.stats.o.hr += 1

    def triple(self):
        if self.verbose_pitch_prints:
            print('Triple')
        self.__hit(3)
        self.stats.o.b3 += 1

    def double(self):
        if self.verbose_pitch_prints:
            print('Double')
        self.__hit(2)
        self.stats.o.b2 += 1

    def single(self):
        if self.verbose_pitch_prints:
            print('Single')
        self.__hit(1)
        self.stats.o.b1 += 1

    def stolen_base(self):
        if self.verbose_pitch_prints:
            print('Stolen Base')
        self.__advance_runners(1)
        self.stats.o.sb += 1

    ##########################
    # Plate Appearance in Progress

    def ball(self):
        assert(0 <= self.count[0] <= 3)
        assert(0 <= self.count[1] <= 2)
        assert (0 <= self.outs <= 2)
        if self.verbose_pitch_prints:
            print('Ball')
        self.stats.d.pitchCount += 1
        self.stats.d.ball += 1
        self.count = (self.count[0] + 1, self.count[1])
        if self.count[0] == 4:
            self.__walk()

    def strike(self):
        assert (0 <= self.count[0] <= 3)
        assert (0 <= self.count[1] <= 2)
        assert (0 <= self.outs <= 2)
        if self.verbose_pitch_prints:
            print('Strike')
        self.stats.d.pitchCount += 1
        self.stats.d.strike += 1
        self.count = (self.count[0], self.count[1] + 1)
        if self.count[1] == 3:
            if self.verbose_pitch_prints:
                print('Strike Out')
            self.stats.o.so += 1
            self.__out()

    def foul(self):
        assert (0 <= self.count[0] <= 3)
        assert (0 <= self.count[1] <= 2)
        assert (0 <= self.outs <= 2)
        if self.verbose_pitch_prints:
            print('Foul')
        if self.count[1] < 2:
            self.strike()
        else:
            self.stats.d.pitchCount += 1

    ###########################
    # Internal Bookkeeping
    def __hit(self, num_bases):
        self.stats.d.pitchCount += 1
        self.stats.o.ab += 1
        self.stats.o.pa += 1
        self.stats.o.hits += 1
        self.stats.o.tb += num_bases
        self.__advance_runners(num_bases + 1)
        if num_bases < 4:
            self.bases[num_bases - 1] = 1
        else:
            self.__score_run()
        self.count = (0, 0)

    def __out(self):
        if self.verbose_pitch_prints:
            print('Out!')
        assert(self.outs < 3)
        self.outs += 1
        self.stats.d.out += 1
        self.stats.o.ab += 1
        self.stats.o.pa += 1
        if self.outs >= 3:
            self.__check_endgame_advance_and_reset_inning()
        else:
            self.count = (0, 0)

    def __walk(self):
        if self.verbose_pitch_prints:
            print('Walk')
        self.stats.o.bb += 1
        self.stats.o.pa += 1

        if self.bases[0] == 1:
            if self.bases[1] == 1:
                if self.bases[2] == 1:
                    self.__score_run()
                    self.stats.o.rbi += 1
                else:
                    # man aleady on first and second, add to third
                    self.bases[2] = 1
            else:
                # man already on first, just add to 2nd
                self.bases[1] = 1
        else:
            self.bases[0] = 1
        self.count = (0, 0)


    def __score_run(self):
        if self.verbose_pitch_prints:
            print('Run Scores')
        self.stats.o.runs += 1
        if self.isTopOfInning:
            self.score = (self.score[0] + 1, self.score[1])
        else:
            self.score = (self.score[0], self.score[1] + 1)

    def __advance_runners(self, num_bases):
        for _ in range(num_bases):
            if self.bases[2] == 1:
                self.__score_run()
            self.bases[1:2] = self.bases[0:1]
            self.bases[0] = 0
            if self.is_final():
                break

    def __check_endgame_advance_and_reset_inning(self):
        if self.verbose_pitch_prints:
            print('Checking Endgame')
        self.stats.o.lob += sum(self.bases)
        if self.is_final():
            return
        if self.isTopOfInning:
            self.isTopOfInning = 0
        else:
            self.isTopOfInning = 1
            self.inning += 1
        self.stats.o.lob += sum(self.bases)
        self.bases = [0, 0, 0]
        self.outs = 0
        self.count = (0, 0)

    def __is_tie(self):
        return self.score[0] == self.score[1]

    def __is_home_team_winning(self):
        return self.score[1] > self.score[0]
