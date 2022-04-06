from player import Player
from deck import Deck
from chatbox import Chatbox
from card import Card


class Game:
    # color = ["Clubs", "Spades", "Diamonds", "Hearts"]
    def __init__(self):
        self.card_deck = Deck()
        self.pile = []
        self.players = []  # evtl list comprehesion tbd
        self.round = 0
        self.turn = 0  # player 0 is active
        self.chatbox = Chatbox()
        self.last_card = Card(0, 'Spades')

        # for debugging end-game state:
        # for i in range(0, 25):
        #     self.card_deck._cards.pop(0)

    def action(self, player_id, data):

        # data = <Topf>/<Nummer im Array>
        # Topf: <oc> : <hc> : <st> : pi
        # data format:
        # <action_type>/<action_parameter>
        # data = "pos" + "Zahl"
        # pos = S(tack), (P)ile, H(and), O(pen), C(closed)
        # Zahl = Nummer der Karte in der Liste
        print(data)
        info = data.split("/")
        pos = int(info[1])
        action_type = info[0]
        if player_id == self.turn:

            if action_type == "et" and self.turn == player_id:
                if self.last_card.rank != 0:
                    self.next_turn()
                    self.draw_cards(player_id)
                    self.players[player_id].check_has_cards()


            if action_type == "pi":  # clicked on pile (ablage stapel)
                self.take_pile(player_id)
                self.next_turn()

            elif action_type == "hc":  # clicked on hand cards
                card_obj = self.players[player_id].hand[pos]
                rank = card_obj.rank
                if self.last_card.rank == 0 or self.last_card.rank == card_obj.rank:
                    if self.check_move(rank) == 1:
                        self.pile.append(self.players[player_id].hand.pop(pos))  # Karte im Game bewegt
                        self.last_card = self.pile[-1]
                        self.check_pile_burn(rank)

            elif action_type == "oc":  # clicked on face up cards
                #  check if faceup / check if not facedown
                if not self.players[player_id].hand:
                    if self.players[player_id].faceup[pos].get_shortcut() == '0s':
                        if self.players[player_id].facedown[pos].get_shortcut() == '0s':
                            # noCard Played
                            pass

                        else:  # facedown-Karte würde gespielt
                            if self.has_no_faceup(player_id) == 1:

                                card_obj = self.players[player_id].facedown[pos]
                                rank = card_obj.rank
                                if self.last_card.rank == 0 or self.last_card.rank == card_obj.rank:  # valid move
                                    if self.check_move(rank) == 1:
                                        self.pile.append(card_obj)
                                        self.last_card = self.pile[-1]
                                        # self.next_turn()
                                        self.check_pile_burn()

                                    else:
                                        self.pile.append(card_obj)
                                        self.last_card = self.pile[-1]
                                        self.take_pile(player_id)
                                        self.next_turn()

                                    self.players[player_id].facedown[pos] = Card(0, 'Spades')


                    else:  # faceup-Karte gespielt
                        card_obj = self.players[player_id].faceup[pos]
                        rank = card_obj.rank
                        if self.last_card.rank == 0 or self.last_card.rank == card_obj.rank:  # valid move
                            if self.check_move(rank) == 1:
                                self.pile.append(card_obj)  # Karte an die letzte Stelle des Pile
                                self.players[player_id].faceup[pos] = Card(0, 'Spades')
                                self.last_card = self.pile[-1]
                                self.check_pile_burn()

        return "success..."

    def draw_cards(self, player_id):
        while len(self.players[player_id].hand) < 3:
            if len(self.card_deck._cards) > 0:
                self.players[player_id].hand.append(self.card_deck.deal())
            else:
                break

    def next_turn(self):
        self.last_card = Card(0, 'Spades')
        self.turn += 1
        if self.turn >= len(self.players):
            self.turn = 0
        if self.players[self.turn].i_finished:
            self.next_turn()


    def has_no_faceup(self, player_id):
        for i in range(0, 3):
            if self.players[player_id].faceup[i].get_shortcut() == '0s':
                pass
            else:
                return 0  # Karte ungleich 0s -> faceup-Karte vorhanden -> return 0
        return 1  # 3x '0s' ausgelesen -> keine faceup-Karten vorhanden -> return 1

    def take_pile(self, player_id):

        for i in range(0, len(self.pile)):
            self.players[player_id].hand.append(self.pile.pop(0))

    #def get_card_rank(self, card_obj):
    #    return card_obj.rank

    # '''
    #         played_card = card_obj.get_shortcut()
    #
    #         if played_card[0] == "A":
    #             rank = 14
    #         elif played_card[0] == "K":
    #             rank = 13
    #         elif played_card[0] == "Q":
    #             rank = 12
    #         elif played_card[0] == "J":
    #             rank = 11
    #         elif played_card[0] == "T":
    #             rank = 10
    #         elif played_card[0] == "9":
    #             rank = 9
    #         elif played_card[0] == "8":
    #             rank = 8
    #         elif played_card[0] == "7":
    #             rank = 7
    #         elif played_card[0] == "6":
    #             rank = 6
    #         elif played_card[0] == "5":
    #             rank = 5
    #         elif played_card[0] == "4":
    #             rank = 4
    #         elif played_card[0] == "3":
    #             rank = 3
    #         elif played_card[0] == "2":
    #             rank = 2
    #         else:
    #             return 0
    #
    #         return rank
    # '''

    def check_move(self, rank):  # return 1 valid move; return 0 invalid move

        if rank == 2:  # 2 darf man immer legen
            return 1
        if rank == 3:  # 3 darf man immer legen
            return 1
        if rank == 10:  # T darf man immer legen
            return 1

        if self.pile:
            valid_pile = self.check_valid_pile()
            if rank >= valid_pile:  # tbd Gamestate attribut anlegen oder Abfrage des Piles
                return 1
            else:
                return 0
        else:
            return 1

    def check_valid_pile(self):

        for i in range (1,len(self.pile) +1):
            if self.pile[-i].rank == 3:
                pass
            else:
                return self.pile[-i].rank
        return 0 # nur gleiche Karten liegen im Moment am Pile

    def check_pile_burn(self,rank):

        if rank == 10: # 10 verbrennt den Stapel
            self.burn_pile()
            return 1
        elif len(self.pile) < 4:
            return 0
        else:
            for i in range (1,4):
                if self.pile[-1].rank == self.pile[-i-1].rank: # vier Karten gleichen Ranges am Ablagestapel brennt Stapel
                    pass
                else:
                    return 0
            self.burn_pile()
            return 1
    #        if self.gamestate == 7:
    #            if rank <= self.gamestate:
    #                return 1
    def burn_pile(self):
        self.pile.clear()

    def initiate_new_game(self, number_of_players):
        for i in range(0, number_of_players):
            self.players.append(Player())

        self.deal_cards(number_of_players)

    def deal_cards(self, number_of_players):
        self.card_deck.shuffle()

        # tbd: achtung, in zweiter Runde ist das self.card_deck nicht mehr voll...
        for i in range(0, number_of_players):
            # Handkarten verteilen
            self.players[i].hand = self.card_deck._cards[0:3]
            del self.card_deck._cards[0:3]

            # verdeckte Karten verteilen
            self.players[i].set_facedown(self.card_deck._cards[0:3])
            del self.card_deck._cards[0:3]

            # offene Karten verteilen
            self.players[i].set_faceup(self.card_deck._cards[0:3])
            del self.card_deck._cards[0:3]

    def get_gamestate_string2(self, id):
        return "0s,0s,9h/4h,1b,3h:1b,0s,1b:4h,5h,Th:0s,0s,0s/8,7,6,5/6h,7h,8h,8h/0/1/3:pures luck alda"

    def get_gamestate_string(self, player_id):
        # Segment 1: Pilestapel oberste 3 Karten senden
        if len(self.pile) == 0:  # Pile ist leer
            gamestring = '0s,0s,0s/'

        elif len(self.pile) == 1:
            gamestring = '0s,0s,'
            gamestring = gamestring + self.pile[-1].get_shortcut() + '/'

        elif len(self.pile) == 2:
            gamestring = '0s,'
            gamestring = gamestring + self.pile[-2].get_shortcut() + ',' + self.pile[-1].get_shortcut() + '/'

        elif len(self.pile) >= 3:
            gamestring = self.pile[-3].get_shortcut() + ',' + self.pile[-2].get_shortcut() + ',' + self.pile[
                -1].get_shortcut() + '/'
        else:
            gamestring = "0s,0s,0s/"

        # Segment 2: Opencards jedes Spielers senden
        # open und closed Card werden nicht gelöscht, sondern mit einer BlankoKarte ersetzt
        for i in range(0, len(self.players)):  # [0s, 0s, 0s] #4h,1b,3h:1b,0,1b:4h,5h,Th:0,0,0
            for card_pos in range(0, 3):
                if self.players[i].faceup[card_pos].get_shortcut() == '0s':
                    # Faceup-Karte ist weg
                    if self.players[i].facedown[card_pos].get_shortcut() == '0s':
                        # Facedown-Karte ist weg
                        gamestring = gamestring + '0s'  # Symbol für keine Karte Senden
                    else:  # facedown-Karte darstellen
                        gamestring = gamestring + '1b'  # Symbol für Facedown Karte senden

                else:  # faceup-Karte darstellen
                    gamestring = gamestring + self.players[i].faceup[card_pos].get_shortcut()  # faceup-KArte senden

                if card_pos < 2:  # entscheiden ob , angehängt wird
                    gamestring = gamestring + ','

            if i < (len(self.players) - 1):  # Zwischen : und / entscheiden
                gamestring = gamestring + ':'
            else:
                gamestring = gamestring + '/'

        # Segment 3: Anzahl Handkarten jedes Spielers senden
        for i in range(0, len(self.players)):
            if i < (len(self.players) - 1):  # nicht letztes String Segment
                gamestring = gamestring + str(len(self.players[i].hand)) + ','
            elif i == (len(self.players) - 1):  # letztes String Segment
                gamestring = gamestring + str(len(self.players[i].hand)) + '/'

        # Segment 4: Eigene Handkarten senden
        for i in range(0, len(self.players[player_id].hand)):
            if i < (len(self.players[player_id].hand) - 1):  # nicht letztes String Segment
                gamestring = gamestring + self.players[player_id].hand[i].get_shortcut() + ','
            if i == (len(self.players[player_id].hand) - 1):  # letztes String Segment
                gamestring = gamestring + self.players[player_id].hand[i].get_shortcut() + '/'
        if not self.players[player_id].hand:
            gamestring = gamestring + '0s/'

        # Segment 5: Flag Turn
        #     if self.turn == player_id:
        #         gamestring = gamestring + '1' + '/'
        #     else:
        #         gamestring = gamestring + '0' + '/'
        gamestring = gamestring + str(self.turn) + '/'

        # Segment 6: Flag Cards im Deck
        if len(self.card_deck._cards) > 0:  # len-operator is overloaded in class Deck
            gamestring = gamestring + '1'
        else:
            gamestring = gamestring + '0'

        players_active = len(self.players)
        for i in range(0, len(self.players)):
            if self.players[i].i_finished:
                players_active -= 1

        if players_active == 1:
            if not self.players[player_id].i_finished:
                gamestring = gamestring + "/you_lost_!"

        return gamestring