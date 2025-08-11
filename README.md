# Dice Baseball

## Introduction

This project is a dice-based baseball game simulation. The goal is to create a game where dice rolls determine outcomes, and then verify that the resulting game statistics closely match real Major League Baseball (MLB) statistics.

## Background

My son loves baseball and collecting baseball cards. Inspired by how some people invent games using baseball cards, we created a simple dice game for him. Originally, we used two six-sided dice (D6) — one representing the batter and one the pitcher. The difference in dice rolls determined outcomes like strikeouts, singles, doubles, home runs, and more. For example, a difference of 5 in favor of the pitcher might mean a double play, and the same difference favoring the batter could mean a home run.

As the game evolved, we expanded the dice to 20-sided dice (D20) and added more possible outcomes such as walks, stolen bases, and sacrifice hits. However, the game became overly long and scoring became unrealistic.

To improve the game, I wrote this simulation to test and refine the outcome probabilities based on dice rolls, aiming to match real MLB statistics more closely. This helps us tune the game for better realism and balanced gameplay.

## Reference Data

The target statistics are taken from this authoritative source:
[Baseball Reference - MLB Batting Stats](https://www.baseball-reference.com/leagues/majors/bat.shtml)

## Current State

The simulation runs successfully and produces offensive statistics that are reasonably close to real MLB data, though the offense is currently a bit high.

## Example Output

```
Playing 4900 games  
500 Games Complete!  
1000 Games Complete!  
...  
All Games Completed  

Statistics are Per Game Per Team:  
---------------------------------  
Runs Per Game (4.07-4.86): 5.61  
Games Played: 4900  
Plate Appearances (37.03-38.80): 39.27  
At Bats (32.87-34.51): 36.31  
Runs (4.07-4.86): 5.61  
Hits (8.04-9.28): 9.45  
1B (5.06-6.15): 5.50  
2B (1.57-1.89): 1.98  
3B (0.13-0.20): 0.50  
HR (0.89-1.39): 1.46  
SB (0.57-0.72): 0.98  
BB (2.88-3.39): 2.96  
SO (6.52-8.37): 8.24  
BA (.243-.269): 0.260  
TB (13-35-14.59): 16.83  
GDP (.68-.82): 0.74  
```

## How to Use

1. Run `main.py` to simulate 4,900 games between two teams.
2. Review the statistics printed at the end to compare the simulated game outcomes with real MLB stats.
3. Use the code to experiment with different outcome tables, dice rules, or player attributes to tune gameplay realism.
