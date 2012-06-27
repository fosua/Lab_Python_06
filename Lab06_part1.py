"""
Lab_Python_06
Part 1
"""

"""
Whatever the datastructure you choose,
it should represent the following data:

player		| date		| score
_______________________________________
rooney		| 6/23/2012	| 2
rooney		| 6/25/2012	| 2
ronaldo		| 6/19/2012	| 0
ronaldo		| 6/20/2012	| 3
torres		| 6/21/2012	| 0
torres		| 6/21/2012	| 1
"""
import datetime
#create the player_stats data structure
player_stats = {datetime.date(2012,06,23):('rooney',2), datetime.date(2012,06,25):('rooney',2),
                datetime.date(2012,06,19):('ronaldo',0),datetime.date(2012,06,20):('ronaldo',3),
                datetime.date(2012,06,21):('torres', 1)}
#print player_stats

               
               
    

#implement highest_score
def highest_score(playee):
    highest = 0
    for i in player_stats.keys():
        scored_goals = player_stats[i]
        if (scored_goals[1]> highest):
            highest = scored_goals[1]
            name = scored_goals[0]
            date = i
    print '(',name,',',date,',',highest,')'
highest_score(player_stats)
print ''
            

#implement highest_score_for_player
def highest_score_for_player(player_stats,player):
    high = 0
    for i in player_stats.keys():
        player_goals = player_stats[i]
       
        if (player_goals[0] == player):
            if (player_goals[1] > high):
                high =player_goals [1]
                non = player_goals[0]
                print '(', non, ',', high, ')'
nam = str(raw_input('please enter the name of a player to see highest score'))

highest_score_for_player(player_stats,nam)
print ''    
    


#implement highest_scorer
def highest_scorer(player_stats):
    rooney_score = 0
    ronaldo_score = 0
    torres_score = 0
    high_scores = 0
    
    for i in player_stats.keys():
        player_score = player_stats[i]
        if (player_score[0] == 'ronaldo'):
            ronaldo_score = player_score[1] + ronaldo_score
            if ronaldo_score > high_scores:
               player_name = player_score[0]
              
        elif (player_score[0] == 'rooney'):
            rooney_score = player_score[1] + rooney_score
            if rooney_score > high_scores:
               player_name = player_score[0]
               
               
        elif (player_score[0] =='torres'):
            torres_score = player_score[1] + torres_score
            if torres_score > high_scores:
                player_name = player_score[0]
                
             
    print player_name
highest_scorer(player_stats)





        
    


