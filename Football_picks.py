#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 12:20:51 2022

@author: mattlester
"""


import pandas as pd
from Football_utility import *

dict_googleDocID = {"matt": "1PA-StzhJWqxBB4P1RdT3aS7pXRgAu-Bvd6EZyhRA6_s",
                        "dad": "1wRiKC8sU9W5JzNcgmAAO6DMhz13hxk7T_4o-u4XYGD0",
                        "andrew": "15cS19HdL1ZOPJSiC0FRyUd05LVIPh7_gXjoshB0ZyiA",
                        "paul": "19MHO7HGH-Cl-RH22axAsQNdSxHYRKP-ZTOhcB7qmSQo",
                        "mom": "1ed-14dAxFPgxPBprhZ60jW8Fkeb0Q27RCoqqsCE8FPg",
                        "jenn": "1596xwbfjhs3qdkdLGHYngeyDTSJ4D2Cl-hpjiEen2X4",
                        "natalie": "1WXcAAaPJPpGVv4Cn6s43q8VDDQ2mNU0QoQeAlcSrq38",
                        "outcomes": "1FBaKidqQlBbWm7VJ0DGJK4sik3pQTU_1zGB3IMZh2a0"}

Players = ["Dad", "Matthew", "Andrew", "Paul", "Mom", "Natalie"]
dad_weekly = []
matt_weekly = []
andrew_weekly = []
paul_weekly = []
mom_weekly = []
natalie_weekly = []
weeklyWinTally = [dad_weekly, matt_weekly , andrew_weekly , paul_weekly, mom_weekly, natalie_weekly]
url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet=Sheet1"
        
# main program:

w_w = pd.read_csv(url.format(dict_googleDocID.get("outcomes")))
m_picks = pd.read_csv(url.format(dict_googleDocID.get("matt")))
a_picks = pd.read_csv(url.format(dict_googleDocID.get("andrew")))
d_picks = pd.read_csv(url.format(dict_googleDocID.get("dad")))
p_picks = pd.read_csv(url.format(dict_googleDocID.get("paul")))
mom_csv = pd.read_csv(url.format(dict_googleDocID.get("mom")))
natalie_picks = pd.read_csv(url.format(dict_googleDocID.get("natalie")))

weekly_winners = list_convert(w_w)
m_week_picks = list_convert(m_picks)
a_week_picks = list_convert(a_picks)
d_week_picks = list_convert(d_picks)
p_week_picks = list_convert(p_picks)
mom_week_picks = list_convert(mom_csv)
n_week_picks = list_convert(mom_csv)


matt_wins = win_count(weekly_winners, m_week_picks)
andrew_wins = win_count(weekly_winners, a_week_picks)
dad_wins = win_count(weekly_winners, d_week_picks)
paul_wins = win_count(weekly_winners, p_week_picks)
mom_wins = win_count(weekly_winners, mom_week_picks)
natalie_wins = win_count(weekly_winners, n_week_picks)

forWeeklyTally = [d_week_picks, m_week_picks, a_week_picks, p_week_picks, mom_week_picks, n_week_picks]
playerTotalWins = [dad_wins, matt_wins, andrew_wins, paul_wins, mom_wins, natalie_wins]

weeklyWins(dad_weekly, forWeeklyTally[0], weekly_winners)
weeklyWins(matt_weekly, forWeeklyTally[1], weekly_winners)
weeklyWins(andrew_weekly, forWeeklyTally[2], weekly_winners)
weeklyWins(paul_weekly, forWeeklyTally[3], weekly_winners)
weeklyWins(mom_weekly, forWeeklyTally[4], weekly_winners)
weeklyWins(natalie_weekly, forWeeklyTally[5], weekly_winners)

print_function_Total(Players, playerTotalWins)
print_function_weekly(Players, weeklyWinTally)


