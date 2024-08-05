import gameState
import players
import stats


class Team:
    def __init__(self):
        self.batters = [players.players.Batter() for _ in range(9)]
        self.pitchers = [players.players.Pitcher() for _ in range(1)]


if __name__ == '__main__':
    home_team = Team()
    away_team = Team()

    total_stats = stats.Stats()

    print('Playing 4900 games')
    for iGame in range(4900):
        game = gameState.gamestate.GameState(home_team, away_team)
        stats_game = game.play_game()
        total_stats += stats_game
        if (iGame + 1) % 500 == 0:
            print(iGame + 1, 'Games Complete!')
    print('All Games Completed')
    print(total_stats)
