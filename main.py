import gameState
import players
import stats

if __name__ == '__main__':
    stats_total = stats.Stats()
    for iGame in range(1000):
        game = gameState.gamestate.GameState()
        while not game.is_final():
            # print('Before:', game[iGame])
            players.players.make_action_roll(game)
            # print("After:", game[iGame])
        print(game)
        if stats_total is None or game.stats is None:
            print('Bad')
        stats_total = stats_total + game.stats
        if (iGame + 1) % 10000 == 0:
            print(iGame + 1, 'Games Complete!')
    print('All Games Completed')
    print(stats_total)
