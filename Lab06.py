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
new_score = Player('Fernando', 'Torres', 'Chelsea')
torres = [0,0,1,0,1]
for i in range(len(torres)):
    torres_score = new_score.add_score ('011/07/09',torres[i])
print torres_score
new_score.total_score()
new_score.average_score()

