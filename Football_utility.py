from datetime import date
 
def list_convert(file, dict_name):
    dict_name = {}
    for i in range(5,18):
        dict_name[f"w{i}"] = file[f"week{i}"].tolist()
    return dict_name

def weekly_results(check, picks):
    week_wins = 0
    
    for i in range(len(check)):
        if picks[i] in check:
            week_wins += 1
    return week_wins

def win_count(week_winners, week_picks):
    num_wins = 0
    total_wins = 0
    for i in range (5, len(week_winners)):
        
        person_list = week_picks[f"w{i}"] 
        check_list = week_winners[f"w{i}"]
        
        for j in range(len(check_list)):
            if person_list[j] in check_list:
                num_wins += 1
                
    total_wins = total_wins + num_wins    
    return total_wins

def weeklyWins (player, playerPicks, weekly_winners):  # update the range as weeks progress
    for i in range(5,weekNumber()):
        player.append( weekly_results(weekly_winners.get(f"w{i}"), playerPicks.get(f"w{i}")))
                 
def print_function_weekly (players , playerWins):

    week = int(input("Enter the week number: "))
    print()
    
    for i in range (len(players)):
        person = playerWins[i]
        print (f"{players[i]} has {person[week - 5]} wins this week")
    
    print()

def print_function_Total (players, playerWins):
    
    for i in range(len(players)):
        print(f"{players[i]} has {playerWins[i]} wins total")
        
    print()

def weekNumber():
    date1 = date(2022, 10, 8)
    date2 = date.today()
    weekOffset = 6
    
    days = abs(date1 - date2).days
    
    return (days // 7) + weekOffset
    
    
 
    


# def list_convert(file, dict_name):
#     dict_name = {}
#     for i in range(5,18):
#         dict_name[f"w{i}"] = file[f"week{i}"].tolist()
#     return dict_name


# def weekly_results(check, picks):
#     week_wins = 0
    
#     for i in range(len(check)):
#         if picks[i] in check:
#             week_wins += 1
#     return week_wins

        
# def weeklyWins (player, playerPicks):  # update the range as weeks progress
#     for i in range(5,9):
#         player.append( weekly_results(weekly_winners.get(f"w{i}"), playerPicks.get(f"w{i}")))
         

# def win_count(week_winners, week_picks):
#     num_wins = 0
#     total_wins = 0
#     for i in range (5, len(week_winners)):
        
#         person_list = week_picks[f"w{i}"] 
#         check_list = week_winners[f"w{i}"]
        
#         for j in range(len(check_list)):
#             if person_list[j] in check_list:
#                 num_wins += 1
                
#     total_wins = total_wins + num_wins    
#     return total_wins

        
        
        
# def print_function_weekly (players , playerWins):

#     week = int(input("Enter the week number: "))
#     print()
    
#     for i in range (len(Players)):
#         person = playerWins[i]
#         print (f"{players[i]} has {person[week - 5]} wins this week")
    
#     print()



# def print_function_Total (players, playerWins):
    
#     for i in range(len(Players)):
#         print(f"{Players[i]} has {playerWins[i]} wins total")
        
#     print()
        