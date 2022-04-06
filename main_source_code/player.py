class Player:
    def __init__(self):
        self.faceup = []        #[0s, 0s, 0s]
        self.facedown = []      #[0s, 0s, 0s]
        self.hand = []          #[]
        self.i_finished = False

    def set_faceup(self, cards):
        self.faceup = cards

    def set_facedown(self, cards):
        self.facedown = cards

    def set_hand(self, cards):
        self.hand = cards

    def check_has_cards(self):

        if not self.hand:
            for i in range(0, 3):
                if self.faceup[i].rank == 0:
                    if self.facedown[i].rank == 0:
                        pass
                    else:
                        return
                else:
                    return
        else:
            return
        
        self.i_finished = True
        return