import random
from ShowdownOutcomes import ShowdownOutcomes


class Batter:
    @staticmethod
    def take_action(action_score):
        if action_score >= 19:
            outcome = ShowdownOutcomes.TRIPLE
        elif action_score >= 18:
            outcome = ShowdownOutcomes.STOLENBASE
        elif action_score >= 17:
            outcome = ShowdownOutcomes.HOMERUN
        elif action_score >= 16:
            outcome = ShowdownOutcomes.DOUBLE
        elif action_score >= 14:
            outcome = ShowdownOutcomes.SINGLE
        elif action_score >= 6:
            outcome = ShowdownOutcomes.BALL
        else:
            outcome = ShowdownOutcomes.FOUL
        return outcome


class Pitcher:
    @staticmethod
    def take_action(action_score):
        if action_score >= 17:
            outcome = ShowdownOutcomes.HITINTODOUBLEPLAY
        elif action_score >= 15:
            outcome = ShowdownOutcomes.HITINTOOUT
        elif action_score >= 12:
            outcome = ShowdownOutcomes.SACRAFICE
        elif action_score >= 9:
            outcome = ShowdownOutcomes.STRIKE
        else:
            outcome = ShowdownOutcomes.FOUL
        return outcome


def make_action_roll(batter, pitcher) -> ShowdownOutcomes:
    batter_die = random.randint(1, 20)
    pitcher_die = random.randint(1, 20)
    if batter_die >= pitcher_die:
        # print('batter', batter_die- pitcher_die)
        outcome = batter.take_action(batter_die - pitcher_die)
    else:
        # print('pitcher', pitcher_die - batter_die)
        outcome = pitcher.take_action(pitcher_die - batter_die)
    return outcome

