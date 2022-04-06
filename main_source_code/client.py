from game import Chatbox
from connection import Connection
from gui import GUI
import pygame

'''
# decode variables - used for frontend info:
is_turn = False
deck_not_empty = True
pile_cards = []
open_cards = []             # ["4h,1b,3h","fd,0,fd","4h,5h,3h","0,0,0"]
number_of_handcards = []
hand_cards = []
'''

class Client:
    def __init__(self, host_address, port):
        self.host_address = host_address
        self.port = port
        self.connection = Connection(host_address, port)
        self.chatbox = Chatbox()
        self.deck_not_empty = True
        self.is_turn = False
        self.player_in_turn = -1
        self.game_started = False
        self.pile_cards = []
        self.hand_cards = []
        self.open_cards = []
        self.number_of_handcards = []
        self.i_lost = False
        self.i_won = False
        self.game_gui = GUI(self)
        self.game_gui.run()


    # def check_winner(self, gamestate):
    #     if self.game_started:
    #         return
    #     # sets the parameter "i_lost" and "i_won" accordingly when the game has finished
    #     # game has finished when one client has zero hand cards and zero open cards
    #     # "3s,3s,9h/4h,1b,3h:1b,0,1b:4h,5h,Th:0,0,0/8,7,6,5/6h,7h,8h,8h/0/1/3:pures luck alda"
    #     open_cards = gamestate.split()
    #
    #     pass

    def update_gamestate(self):
        gamestate = self.connection.request_gamestate()
        #print("Gamestate Augabe: " +  gamestate)
        self.decode_gamestate_string(gamestate)

        # self.decode_gamestate_string("3s,3s,9h/4h,1b,3h:1b,0,1b:4h,5h,Th:0,0,0/8,7,6,5/6h,7h,8h,8h/0/1/3:pures luck alda")

    def decode_gamestate_string(self, gamestate):
        #global is_turn, deck_not_empty, pile_cards, open_cards, hand_cards

        # Format of gamestate:
        # "<pile>/<open_card>/<number_hand_cards>/<hand_cards>/<turn>/<deck>/<message>"
        # "<3_pile_top_cards>/<open_cards:id0>:<id1>:<id2>:<id3>/<number_of_handcards_id0>,<id1>,<id2>,id3>/<hand_cards_self>/<flag_is_turn>/<flag_deck_is_not_empty>/<message>"
        # Example:
        # gamestate = "0,3s,9h/4h,1b,3h:1b,0,1b:4h,5h,Th:0,0,0/8,7,6,5/6h,7h,8h,8h/0/1/3:pures luck alda"
        # Content:
        # <3_pile_top_cards>    = 0,3s,9h   # two cards in pile, top card is 9 of hearts
        # <open_cards:id0>      = 4h,1b,3h  # open cards of player 0, fd means "face down"
        #  ...
        # <flag_is_turn>            = 0     # it is not the players turn
        # <flag_deck_is_not_empty>  = 1     # the deck is not empty, card needs to be displayed
        # <message>                 = 3:pures luck alda     # if no message is given the lenght of the string array is one time smaller

        base = gamestate.split("/")
        length = len(base)
        print("Gamestate as base: " + gamestate)
        self.pile_cards = base[0].split(",")  # ["0","3s","9h"]
        self.open_cards = base[1].split(":")  # ["4h,fd,3h","fd,0,fd", ...]
        self.number_of_handcards = base[2].split(",")  # ["8","7","6","5"]
        self.hand_cards = base[3].split(",")  # ["6h","7h","8h","8h"]

        self.player_in_turn = int(base[4]) # safe player in turn
        if base[4] == str(self.connection.id):  # reading turn state
            self.is_turn = True
        else:
            self.is_turn = False

        if base[5] == "1":  # reading deck state
            self.deck_not_empty = True
        else:
            self.deck_not_empty = False

        if length == 7:  # call chat-box to insert new string (message)
            if base[6] == "game_started":
                self.game_started = True
            if base[6] == "you_lost_!":
                self.i_lost = True
            else:
                pass
                # call chat-box operator            # tbd: implement chatbox methods in gui!
                # parameter is base[6]
                # f.e. gui.chatbox.append(base[6])