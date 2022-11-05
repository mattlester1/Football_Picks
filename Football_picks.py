#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 12:20:51 2022

@author: mattlester
"""


import pandas as pd
from Football_utility import *

game_winner = 0
matt_picks = 0
andrew_picks = 0 
dad_picks = 0
paul_picks = 0
matts_weeklyTally = []
Players = ["Dad", "Matthew", "Andrew", "Paul"]
dad_weekly = []
matt_weekly = []
andrew_weekly = []
paul_weekly = []
weeklyWinTally = [dad_weekly , matt_weekly , andrew_weekly , paul_weekly]
        
# main program:
    
w_w = pd.read_csv("weekly_winners.csv")
m_picks = pd.read_csv("matts_picks.csv")
a_picks = pd.read_csv("andrews_picks.csv")
d_picks = pd.read_csv("dads_picks.csv")
p_picks = pd.read_csv("pauls_picks.csv")

weekly_winners = list_convert(w_w, game_winner)
m_week_picks = list_convert(m_picks, matt_picks)
a_week_picks = list_convert(a_picks, andrew_picks)
d_week_picks = list_convert(d_picks, dad_picks)
p_week_picks = list_convert(p_picks, paul_picks)

matt_wins = win_count(weekly_winners, m_week_picks)
andrew_wins = win_count(weekly_winners, a_week_picks)
dad_wins = win_count(weekly_winners, d_week_picks)
paul_wins = win_count(weekly_winners, p_week_picks)

forWeeklyTally = [d_week_picks, m_week_picks, a_week_picks, p_week_picks]
playerTotalWins = [dad_wins, matt_wins, andrew_wins, paul_wins]

weeklyWins(dad_weekly, forWeeklyTally[0], weekly_winners)
weeklyWins(matt_weekly, forWeeklyTally[1], weekly_winners)
weeklyWins(andrew_weekly, forWeeklyTally[2], weekly_winners)
weeklyWins(paul_weekly, forWeeklyTally[3], weekly_winners)

print_function_Total(Players, playerTotalWins)
print_function_weekly(Players, weeklyWinTally)


