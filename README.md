# Dice Baseball
## TLDR
Trying to match statistics of a baseball game to real MLB statistics.
## Background
My son loves baseball and baseball cards.  I have heard of people inventing games to play with baseball cards and so I helped hiim to invent a game he could play with the cards.  At first we made a pretty simple game with two D6 dice, one for the pitcher and one for the batter.  You would roll both and subtract the two.  If the pitcher was higher and the difference was 5, double play.  If the batter was higher and the difference was 5, homerun!  If it was a tie, foul ball.  We filled in the rest with singles, strikes, and balls.

As he grew familiar with the game he was interested to add more actions, base on balls, steals, sacrafice hits.  So we replaced D6 dice with D20 dice and made a much bigger action table.  We filled it in according to how 'good' or 'exciting' outcomes seemed to be for the defense and offense, but gamaes were going on forever and the scoring was out of control.

I thought I would work to see if I could define actions based on the dice difference that would match the real MLB statistics.  I wrote this simulation so I could quickly run hundreds of games to see if the statistics of the game match the real MLB.
## Reference
I took target statistics for different outcomes from this website: https://www.baseball-reference.com/leagues/majors/bat.shtml
## Current State
The simulation run successfully.  It tracks players on base and game statistics.  I believe it appropriately accounts for all end of game scenarios, i.e. home team wins in top of 9th, walk-off, away team wins.  Also statistics are well matched for singles, a bit high for doubles, triples, and homeruns, and as a result, unsurprising, total bases.  Surprisingly the runs are coming in quite short.  Not sure if there is an error in the simulator or if using all identically average players is accounting for the discrepency in runs.
## Example output is:
Playing 4900 games
500 Games Complete!
1000 Games Complete!
1500 Games Complete!
2000 Games Complete!
2500 Games Complete!
3000 Games Complete!
3500 Games Complete!
4000 Games Complete!
4500 Games Complete!
All Games Completed

Statistics are Per Game Per Team: 
---------------------------------
Runs Per Game (4.07-4.86): 2.88 
Games Played: 4900 
Plate Appearances (37.03-38.80): 40.65 
At Bats (32.87-34.51): 37.58 
Runs (4.07-4.86): 2.88 
Hits (8.04-9.28): 9.77 
1B (5.06-6.15): 5.66 
2B (1.57-1.89): 2.06 
3B (0.13-0.20): 0.50 
HR (0.89-1.39): 1.54 
SB (0.57-0.72): 1.04 
BB (2.88-3.39): 3.07 
SO (6.52-8.37): 8.51 
BA (.243-.269): 0.260 
TB (13-35-14.59): 17.47 
GDP (.68-.82): 0.76
