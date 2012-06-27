class Player:
    def __init__(self,firstname,lastname, team= None):
        self.first_name = firstname
        self.last_name = lastname
        self.score = []
        self.team = team
    def add_score(self, date, score):
        self.score.append(score)
        return self.score
        #print self.score
    def total_score (self):
        self.total = 0
        for i in range (len(self.score)):
            self.total = self.total + self.score[i]
        print self.total
    def average_score(self):
        len_score = float(len(self.score))
        self.average = float((self.total)/len_score)
        print self.average
torres= Player('Fernando', 'Torres', 'Chelsea')
new_score = [0,0,1,0,1]
for i in range(len(new_score)):
    torres_score = torres.add_score ('011/07/09',new_score[i])
print torres_score
torres.total_score()
torres.average_score()
print ''
print ''
#part III
class Team:
    def __init__(self, name, league, manager_name, points):
        self.name = name
        self.league = league
        self.manger_name = manager_name
        self.points = points
        self.players = []
    def add_player(self, player):
        self.players.append(player)
        print self.players
    def __str__(self):
       
        return 'the name of the team is '+self.name
    
        
spain = Team( 'spain', 'la liga', 'esta',51)
print spain
portugal = Team('portugal', 'epl', 'lizzy',46)
print portugal
torres= Player('Fernando', 'Torres', spain)
ronaldo = Player('Christiano', 'Ronaldo', portugal)
#print torres.first_name
#print ronaldo.team

spain.add_player('ronaldo')
portugal.add_player('torres')
class Match:
    def __init__(self, home_team, away_team, date):
        self.home_team = home_team
        self.away_team = away_team
        self.date = date
        self.home_scores = {}
        self.away_scores = {}
    def home_score(self):
        return sum(self.home_scores.values())
    def away_score(self):
        return sum(self.away_scores.values())
    def winner(self):
        if self.home_score() > self.away_score():
            return self.home_team.name
        elif self.home_score() < self.away_score():
            return self.away_team.name
        elif self.home_score() == self.away_score():
            return 'draw'
    def add_score(self, player, score):
        players_team = player.team
        if players_team == self.home_team:
            if player.last_name in  self.home_scores:
                self.home_scores[player.last_name] += score
            else:
                self.home_scores [player.last_name]= score
        elif players_team == self.away_team:
            if player.last_name in  self.away_scores:
                self.away_scores[player.last_name] += score
            else:
                self.away_scores [player.last_name]= score
euro_match_final = Match(spain, portugal,'2012/06/27')
euro_match_final.add_score(torres, 1)
euro_match_final.add_score(ronaldo, 1)
euro_match_final.add_score(torres, 1)
print euro_match_final.winner()




        
            
        




