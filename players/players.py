import random


def batter(action_score, game):
    if action_score >= 19:
        game.homerun()
    elif action_score >= 18:
        game.triple()
    elif action_score >= 16:
        game.double()
    elif action_score >= 13:
        game.single()
    elif action_score >= 6:
        game.ball()
    else:
        game.foul()


def pitcher(action_score, game):
    if action_score >= 18:
        game.hit_into_double_play()
    elif action_score >= 16:
        game.hit_into_out()
    elif action_score >= 9:
        game.strike()
    else:
        game.foul()


def make_action_roll(game):
    batter_die = random.randint(1, 20)
    pitcher_die = random.randint(1, 20)
    if batter_die >= pitcher_die:
        # print('batter', batter_die- pitcher_die)
        batter(batter_die - pitcher_die, game)
    else:
        # print('pitcher', pitcher_die - batter_die)
        pitcher(pitcher_die - batter_die, game)
