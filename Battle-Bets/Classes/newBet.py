

class NewBet:

    def __init__(self, user, bet, points, time, mentions):
        self.Id = Id # generate random id
        self.user = user
        self.bet = bet
        self.points = points
        self.mentions = []
        self.status = 1 # 0 for inactive; 1 for active

    def saveBet(self):
        ...
    
    