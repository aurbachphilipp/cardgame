import pygame
import card

pygame.init()

# Game Window
win_width, win_height = 1550, 800

# WINDOW = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
FPS = 10
background = "b1"

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY_DARK = (96, 96, 96)
GREY_LIGHT = (220, 220, 220)
GREEN = (120, 215, 120)
BLUE = (50, 110, 160)

# CARD SETTINGS
card_height, card_width = 100, 75

# FONTS
font_playername = pygame.font.SysFont("Ubuntu", 20, True)
font_headline = pygame.font.SysFont("Ubuntu", 60, True)
font_rules = pygame.font.SysFont("Ubuntu", 18, True)
font_enemy_number_of_cards = pygame.font.SysFont("Ubuntu", 60, True)

# RULES PIC
SHITHEAD_TRUMPS = pygame.image.load('img/Shithead-trumps.png')
WERBUNG = pygame.image.load('img/raid.png')

# Areas
distance_between_cards_y = 30
distance_between_cards_x = 40
area_slot_offset = 10
enemy_area_y = 75
enemy_area_height = 2 * card_height + distance_between_cards_y + 2 * area_slot_offset
enemy_area_width = 3 * card_width + 2 * distance_between_cards_x + 2 * area_slot_offset
enemy_area_distance = 50

# ENEMY 1
enemy1_area_x = 50
enemy1_area_y = enemy_area_y
enemy1_area = pygame.Rect(enemy1_area_x, enemy1_area_y, enemy_area_width, enemy_area_height)

# ENEMY 2
enemy2_area_x = enemy1_area_x + enemy_area_distance + enemy_area_width
enemy2_area_y = enemy_area_y
enemy2_area = pygame.Rect(enemy2_area_x, enemy2_area_y, enemy_area_width, enemy_area_height)

# ENEMY 3
enemy3_area_x = enemy2_area_x + enemy_area_distance + enemy_area_width
enemy3_area_y = enemy_area_y
enemy3_area = pygame.Rect(enemy3_area_x, enemy3_area_y, enemy_area_width, enemy_area_height)

# PLAYER AREA
player_area = pygame.Rect(enemy1_area_x, win_height - enemy_area_height * 0.75,
                          3 * enemy_area_width + 2 * enemy_area_distance, enemy_area_height)

# CHAT
chat_area_height = player_area.top - enemy_area_y
chat_area_width = enemy_area_width
chat_area_x = enemy3_area.x + enemy_area_width + enemy_area_distance
chat_area_y = enemy3_area.y
chat_area = pygame.Rect(chat_area_x, chat_area_y, chat_area_width, chat_area_height)

# DECK AREA
deck_area_width = 2 * card_width + 3 * area_slot_offset
deck_area_height = card_height + 2 * area_slot_offset
deck_area = pygame.Rect(enemy2_area.centerx - deck_area_width / 2, 2 * enemy_area_y + enemy_area_height,
                        deck_area_width, deck_area_height)

# CARD SLOTS
slot_enemy1_1 = pygame.Rect(enemy1_area.x + area_slot_offset, enemy1_area_y + area_slot_offset,
                            card_width, card_height)
slot_enemy1_2 = pygame.Rect(enemy1_area.x + area_slot_offset,
                            enemy1_area_y + distance_between_cards_y + card_height + area_slot_offset,
                            card_width, card_height)
slot_enemy1_3 = pygame.Rect(slot_enemy1_2.x + card_width + distance_between_cards_x, slot_enemy1_2.y,
                            card_width, card_height)
slot_enemy1_4 = pygame.Rect(slot_enemy1_3.x + card_width + distance_between_cards_x, slot_enemy1_3.y,
                            card_width, card_height)

slot_enemy2_1 = pygame.Rect(slot_enemy1_1.x + enemy_area_width + enemy_area_distance, slot_enemy1_1.y, card_width,
                            card_height)
slot_enemy2_2 = pygame.Rect(slot_enemy1_2.x + enemy_area_width + enemy_area_distance, slot_enemy1_2.y, card_width,
                            card_height)
slot_enemy2_3 = pygame.Rect(slot_enemy1_3.x + enemy_area_width + enemy_area_distance, slot_enemy1_3.y, card_width,
                            card_height)
slot_enemy2_4 = pygame.Rect(slot_enemy1_4.x + enemy_area_width + enemy_area_distance, slot_enemy1_4.y, card_width,
                            card_height)

slot_enemy3_1 = pygame.Rect(slot_enemy2_1.x + enemy_area_width + enemy_area_distance, slot_enemy2_1.y, card_width,
                            card_height)
slot_enemy3_2 = pygame.Rect(slot_enemy2_2.x + enemy_area_width + enemy_area_distance, slot_enemy2_2.y, card_width,
                            card_height)
slot_enemy3_3 = pygame.Rect(slot_enemy2_3.x + enemy_area_width + enemy_area_distance, slot_enemy2_3.y, card_width,
                            card_height)
slot_enemy3_4 = pygame.Rect(slot_enemy2_4.x + enemy_area_width + enemy_area_distance, slot_enemy2_4.y, card_width,
                            card_height)

slot_d1 = pygame.Rect(deck_area.x + area_slot_offset, deck_area.y + area_slot_offset, card_width, card_height)
slot_d2 = pygame.Rect(deck_area.x + 2 * area_slot_offset + card_width, deck_area.y + area_slot_offset, card_width,
                      card_height)

slot_p1 = pygame.Rect(player_area.centerx - distance_between_cards_x - 1.5 * card_width,
                      player_area.y + area_slot_offset, card_width, card_height)
slot_p2 = pygame.Rect(player_area.centerx - 0.5 * card_width, player_area.y + area_slot_offset, card_width, card_height)
slot_p3 = pygame.Rect(player_area.centerx - distance_between_cards_x + 1.5 * card_width,
                      player_area.y + area_slot_offset, card_width, card_height)
# BUTTON START
slot_start = pygame.Rect(chat_area_x, chat_area_y + chat_area_height + 25, chat_area_width, 40)
text_start = font_playername.render("Start", False, WHITE)

# BUTTON RULES
slot_rules = pygame.Rect(slot_start.x, slot_start.y + slot_start.height + 10, chat_area_width, 40)
text_rules = font_playername.render("Rules", False, WHITE)

# BUTTON END TURN
slot_end_turn = pygame.Rect(slot_start.x, slot_start.y + 2 * slot_start.height + 20, chat_area_width, 40)
text_end_turn = font_playername.render("End turn", False, WHITE)

# CHAT TEXT
chat = font_playername.render("Werbung", False, WHITE)


class GUI:

    def __init__(self, clientobj):
        self.client = clientobj
        self.win = pygame.display.set_mode((win_width, win_height))
        pygame.display.set_caption("Shithead")
        pygame.display.set_icon(pygame.image.load('img/game_icon.png'))
        # ENEMY 1
        self.enemy1_name = "enemy 1"
        self.enemy1_name_text = font_playername.render(self.enemy1_name, False, WHITE)
        self.enemy1_number_of_cards = 0
        self.enemy1_number_of_cards_count = font_enemy_number_of_cards.render(
            str(self.enemy1_number_of_cards), False, BLACK)
        # ENEMY 2
        self.enemy2_name = "enemy 2"
        self.enemy2_name_text = font_playername.render(self.enemy2_name, False, WHITE)
        self.enemy2_number_of_cards = 0
        self.enemy2_number_of_cards_count = font_enemy_number_of_cards.render(
            str(self.enemy2_number_of_cards), False, BLACK)
        # ENEMY 3
        self.enemy3_name = "enemy 3"
        self.enemy3_name_text = font_playername.render(self.enemy3_name, False, WHITE)
        self.enemy3_number_of_cards = 0
        self.enemy3_number_of_cards_count = font_enemy_number_of_cards.render(
            str(self.enemy3_number_of_cards), False, BLACK)
        self.loop = True
        self.show_rule_window = False
        self.cards_of_slots = {}
        self.hovered_slot = None
        self.slots_hand_cards = []
        self.clock = pygame.time.Clock()
        self.update_window()

    def run(self):
        while self.loop:
            self.clock.tick(FPS)  # 30 FPS
            self.update_window()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Clean Exit
                    self.loop = False
                    print("Player has closed the Window")
                else:
                    self.handleEvent(event)
        # Clean Exit
        pygame.quit()

    def get_slot_of_player_and_card(self, player_counter, card_counter):
        if player_counter == 0:
            card_switcher = {
                1: slot_p1,
                2: slot_p2,
                3: slot_p3
            }
            return card_switcher.get(card_counter)
        elif player_counter == 1:
            card_switcher = {
                1: slot_enemy1_2,
                2: slot_enemy1_3,
                3: slot_enemy1_4
            }
            return card_switcher.get(card_counter)
        elif player_counter == 2:
            card_switcher = {
                1: slot_enemy2_2,
                2: slot_enemy2_3,
                3: slot_enemy2_4
            }
            return card_switcher.get(card_counter)
        elif player_counter == 3:
            card_switcher = {
                1: slot_enemy3_2,
                2: slot_enemy3_3,
                3: slot_enemy3_4
            }
            return card_switcher.get(card_counter)

    def get_card_of_slot(self, slot):
        return self.cards_of_slots[tuple(slot)]

    def rotate_and_center(self, x, y, image, angle):
        rotated = pygame.transform.rotate(image, angle)
        size = rotated.get_rect()
        self.win.blit(rotated, (x - size.center[0], y - size.center[1]))

    def draw_card(self, card_shortcut, slot, rotation_angle=0, translation=(0, 0)):
        self.cards_of_slots[tuple(slot)] = card_shortcut
        if card_shortcut == "0s":
            return
        card_to_draw = card.Card(card_shortcut[0], card_shortcut[1])
        cx = slot.centerx
        cy = slot.centery
        picture = pygame.image.load(card_to_draw.getFilename())
        if rotation_angle != 0:
            picture = pygame.transform.rotate(picture, rotation_angle)
        if translation[0] != 0:
            cx = cx + translation[0]
        if translation[1] != 0:
            cy = cy + translation[1]
        size = picture.get_rect()
        self.win.blit(picture, (cx - size.center[0], cy - size.center[1]))

    def show_rules(self):
        rule_window = pygame.Rect(30, 30, win_width - 60, 600)
        pygame.draw.rect(self.win, WHITE, rule_window, 0, 8)
        headline = font_headline.render("Rules", False, (0, 0, 0))
        self.win.blit(headline, (rule_window.x + 30, rule_window.y + 20))
        TITLE_TRUMPS = font_playername.render("TRUMPS", False, (0, 0, 0))
        self.win.blit(TITLE_TRUMPS, (rule_window.x + 30, rule_window.y + 100))
        self.win.blit(SHITHEAD_TRUMPS, (rule_window.x + 30, rule_window.y + 140))

        rules_1 = font_rules.render(
            "Play begins with only using your Hand cards. The Player with a 4 on Hand begins, else with lowest card.",
            False, (0, 0, 0))
        rules_2 = font_rules.render(
            "You should have at least 3 Cards on Hand. Else you must draw one from Deck until there are no cards left.",
            False, (0, 0, 0))
        rules_3 = font_rules.render(
            "If you can not play a higher or trump card then you must pick up all cards on the Pile", False, (0, 0, 0))
        rules_4 = font_rules.render("If you have multiples of the same card you can play them together #todo",
                                    False, (0, 0, 0))
        rules_5 = font_rules.render("If you have no cards in your Hand you can play your face up cards.", False,
                                    (0, 0, 0))
        rules_6 = font_rules.render(
            "All face up cards gone? Flip over one face down card. If you can not play the card, add it to your Hand",
            False, (0, 0, 0))
        rules_7 = font_rules.render("END of the game: Only one Player has cards left. He is now called Shithead",
                                    False, (0, 0, 0))

        RULES = [rules_1, rules_2, rules_3, rules_4, rules_5, rules_6, rules_7]

        for x in range(len(RULES)):
            self.win.blit(RULES[x],
                          (rule_window.x + SHITHEAD_TRUMPS.get_width() + 40, rule_window.y + 140 + x * 40))

    def update_slots_for_hand_cards(self, amount_of_cards):
        if amount_of_cards == 0:
            self.slots_hand_cards.clear()
            return
        area_width = player_area.width - 2 * area_slot_offset
        if area_width >= (amount_of_cards * card_width + (amount_of_cards - 1) * distance_between_cards_x):
            self.slots_hand_cards.clear()
            for i in range(amount_of_cards):
                self.slots_hand_cards.append(
                    pygame.Rect(player_area.x + area_slot_offset + i * (distance_between_cards_x + card_width),
                                player_area.bottom - card_height, card_width,
                                card_height))
        else:
            offset = ((area_width - amount_of_cards * card_width) / (amount_of_cards - 1)) + card_width
            self.slots_hand_cards.clear()
            for i in range(amount_of_cards):
                self.slots_hand_cards.append(
                    pygame.Rect(player_area.x + area_slot_offset + i * offset,
                                player_area.bottom - card_height,
                                card_width,
                                card_height))

    def update_window(self):
        # DRAW STATIC STUFF
        # BACKGROUND
        self.win.blit(pygame.transform.scale(pygame.image.load("img/" + background + ".png"),
                                             (self.win.get_width(), self.win.get_height())), (0, 0))

        # CARD AREA
        pygame.draw.rect(self.win, WHITE, chat_area, 0, 8)

        # WERBUNG
        self.win.blit(pygame.transform.scale(WERBUNG, (chat_area_width, chat_area_height)), (chat_area_x, chat_area_y))

        # DECK AREA
        pygame.draw.rect(self.win, GREY_DARK, deck_area, 3, 8)

        # SLOTS
        pygame.draw.rect(self.win, GREY_DARK, slot_d1, 3, 8)
        pygame.draw.rect(self.win, GREY_DARK, slot_d2, 3, 8)

        pygame.draw.rect(self.win, GREY_DARK, slot_p1, 3, 8)
        pygame.draw.rect(self.win, GREY_DARK, slot_p2, 3, 8)
        pygame.draw.rect(self.win, GREY_DARK, slot_p3, 3, 8)

        pygame.draw.rect(self.win, BLACK, slot_start, 0, 8)
        pygame.draw.rect(self.win, BLACK, slot_rules, 0, 8)

        # CHAT
        self.win.blit(chat, (chat_area.x, chat_area_y - 10 - self.enemy3_name_text.get_height()))

        self.win.blit(text_start, (
            slot_start.centerx - text_start.get_width() / 2, slot_start.centery - text_start.get_height() / 2))
        self.win.blit(text_rules, (
            slot_rules.centerx - text_rules.get_width() / 2, slot_rules.centery - text_rules.get_height() / 2))
        # USERNAMES
        # ENEMY TAGS

        # UPDATE GAMESTATE
        self.client.update_gamestate()

        # END TURN BUTTON
        if self.client.is_turn and self.client.game_started:
            end_turn_button_color = GREEN
        else:
            end_turn_button_color = BLACK
        pygame.draw.rect(self.win, end_turn_button_color, slot_end_turn, 0, 8)
        self.win.blit(text_end_turn, (
            slot_end_turn.centerx - text_end_turn.get_width() / 2,
            slot_end_turn.centery - text_end_turn.get_height() / 2))
        # SAFE GAMESTATE
        player_ids_sorted = []
        player_cards_sorted = []  # [own, next player in circle, next player in circle, next player in circle]
        number_of_player_cards_sorted = []
        # SORT PLAYERCARDS FOR BETTER STRUCTURE
        player_id = self.client.connection.id
        for counter in range(0, len(self.client.open_cards)):
            player_cards_sorted.append(self.client.open_cards[player_id])
            number_of_player_cards_sorted.append(self.client.number_of_handcards[player_id])
            player_ids_sorted.append(player_id)
            player_id += 1
            if player_id >= len(self.client.open_cards):
                player_id = 0

        # CARDs AND AREAS
        for counter in player_ids_sorted:
            # OWN
            if counter == 0:
                if player_ids_sorted[counter] == self.client.player_in_turn and self.client.game_started:
                    pygame.draw.rect(self.win, GREEN, player_area, 3, 8)
                else:
                    pygame.draw.rect(self.win, BLUE, player_area, 3, 8)
            elif counter == 1:
                # ENEMY 1
                if player_ids_sorted[counter] == self.client.player_in_turn and self.client.game_started:
                    pygame.draw.rect(self.win, GREEN, enemy1_area, 3, 8)
                else:
                    pygame.draw.rect(self.win, BLUE, enemy1_area, 3, 8)
                pygame.draw.rect(self.win, GREY_DARK, slot_enemy1_1, 3, 8)
                pygame.draw.rect(self.win, GREY_DARK, slot_enemy1_2, 3, 8)
                pygame.draw.rect(self.win, GREY_DARK, slot_enemy1_3, 3, 8)
                pygame.draw.rect(self.win, GREY_DARK, slot_enemy1_4, 3, 8)
                self.draw_card("1b", slot_enemy1_1)
                self.draw_card("1b", slot_enemy1_1, -5)
                self.draw_card("1b", slot_enemy1_1, 20)
                self.win.blit(self.enemy1_name_text, (
                    enemy1_area.centerx - self.enemy1_name_text.get_width() / 2,
                    enemy1_area_y - 10 - self.enemy1_name_text.get_height()))
            elif counter == 2:
                # ENEMY 2
                if player_ids_sorted[counter] == self.client.player_in_turn and self.client.game_started:
                    pygame.draw.rect(self.win, GREEN, enemy2_area, 3, 8)
                else:
                    pygame.draw.rect(self.win, BLUE, enemy2_area, 3, 8)
                pygame.draw.rect(self.win, GREY_DARK, slot_enemy2_1, 3, 8)
                pygame.draw.rect(self.win, GREY_DARK, slot_enemy2_2, 3, 8)
                pygame.draw.rect(self.win, GREY_DARK, slot_enemy2_3, 3, 8)
                pygame.draw.rect(self.win, GREY_DARK, slot_enemy2_4, 3, 8)
                self.draw_card("1b", slot_enemy2_1)
                self.draw_card("1b", slot_enemy2_1, -10)
                self.draw_card("1b", slot_enemy2_1, 5)
                self.win.blit(self.enemy2_name_text, (
                    enemy2_area.centerx - self.enemy2_name_text.get_width() / 2,
                    enemy2_area_y - 10 - self.enemy2_name_text.get_height()))
            elif counter == 3:
                # ENEMY 3
                if player_ids_sorted[counter] == self.client.player_in_turn and self.client.game_started:
                    pygame.draw.rect(self.win, GREEN, enemy3_area, 3, 8)
                else:
                    pygame.draw.rect(self.win, BLUE, enemy3_area, 3, 8)
                pygame.draw.rect(self.win, GREY_DARK, slot_enemy3_1, 3, 8)
                pygame.draw.rect(self.win, GREY_DARK, slot_enemy3_2, 3, 8)
                pygame.draw.rect(self.win, GREY_DARK, slot_enemy3_3, 3, 8)
                pygame.draw.rect(self.win, GREY_DARK, slot_enemy3_4, 3, 8)
                self.draw_card("1b", slot_enemy3_1)
                self.draw_card("1b", slot_enemy3_1, -10)
                self.draw_card("1b", slot_enemy3_1, 15)
                self.win.blit(self.enemy3_name_text, (
                    enemy3_area.centerx - self.enemy3_name_text.get_width() / 2,
                    enemy3_area_y - 10 - self.enemy3_name_text.get_height()))

        # DRAW CARDS
        # PILE
        for counter in range(0, 3):
            if self.client.pile_cards.count("0s") == 2:
                self.draw_card(str(self.client.pile_cards[counter]), slot_d2)
            elif self.client.pile_cards.count("0s") == 1:
                if self.hovered_slot == slot_d2:
                    if counter == 1:
                        self.draw_card(str(self.client.pile_cards[counter]), slot_d2)
                    else:
                        self.draw_card(str(self.client.pile_cards[counter]), slot_d2, 0, (20 * counter, 0))
                else:
                    self.draw_card(str(self.client.pile_cards[counter]), slot_d2)
            elif self.client.pile_cards.count("0s") == 0:
                if self.hovered_slot == slot_d2:
                    self.draw_card(str(self.client.pile_cards[counter]), slot_d2, 0, (20 * counter, 0))
                else:
                    self.draw_card(str(self.client.pile_cards[counter]), slot_d2)

        # CARDS OF PLAYERS IN FRONT
        player_counter = 0
        card_counter = 1
        for player_cards in player_cards_sorted:
            for shortcut in player_cards.split(","):
                self.draw_card(str(shortcut), self.get_slot_of_player_and_card(player_counter, card_counter))
                card_counter += 1
            player_counter += 1
            card_counter = 1

        # CARDS ON OWN HAND
        if self.client.hand_cards[0] == '0s':
            self.update_slots_for_hand_cards(0)
        else:
            self.update_slots_for_hand_cards(len(self.client.hand_cards))
            slot_counter = 0
            for slot in self.slots_hand_cards:
                pygame.draw.rect(self.win, GREY_DARK, slot, 3, 8)
                if self.hovered_slot == slot:
                    self.draw_card(self.client.hand_cards[slot_counter], slot, 0, (0, -25))
                else:
                    self.draw_card(self.client.hand_cards[slot_counter], slot)
                slot_counter += 1

        # DECK
        if self.client.deck_not_empty:
            self.draw_card("1b", slot_d1)

        # SHOW NUMBER OF ENEMY CARDS
        player_counter = 0
        for number_of_cards in number_of_player_cards_sorted:
            if player_counter == 1:
                self.enemy1_number_of_cards = number_of_cards
                # print("Karten Gegner 1:" + str(self.enemy1_number_of_cards))
                self.enemy1_number_of_cards_count = font_enemy_number_of_cards.render(str(self.enemy1_number_of_cards),
                                                                                      False, GREY_DARK)
                self.win.blit(self.enemy1_number_of_cards_count, (
                    slot_enemy1_3.left - self.enemy1_number_of_cards_count.get_width() / 2,
                    slot_enemy1_3.centery - distance_between_cards_y - card_height - self.enemy1_number_of_cards_count.get_height() / 2))
            elif player_counter == 2:
                self.enemy2_number_of_cards = number_of_cards
                # print("Karten Gegner 2:" + str(self.enemy2_number_of_cards))
                self.enemy2_number_of_cards_count = font_enemy_number_of_cards.render(str(self.enemy2_number_of_cards),
                                                                                      False, GREY_DARK)
                self.win.blit(self.enemy2_number_of_cards_count, (
                    slot_enemy2_3.left - self.enemy2_number_of_cards_count.get_width() / 2,
                    slot_enemy2_3.centery - distance_between_cards_y - card_height - self.enemy2_number_of_cards_count.get_height() / 2))
            elif player_counter == 3:
                self.enemy3_number_of_cards = number_of_cards
                # print("Karten Gegner 3:" + str(self.enemy3_number_of_cards))
                self.enemy3_number_of_cards_count = font_enemy_number_of_cards.render(str(self.enemy3_number_of_cards),
                                                                                      False, GREY_DARK)
                self.win.blit(self.enemy2_number_of_cards_count, (
                    slot_enemy3_3.left - self.enemy3_number_of_cards_count.get_width() / 2,
                    slot_enemy3_3.centery - distance_between_cards_y - card_height - self.enemy3_number_of_cards_count.get_height() / 2))
            player_counter += 1

        # RULES (LAST BEFORE WINDOW UPDATE)
        if self.show_rule_window:
            self.show_rules()

        # UPDATE WINDOW
        pygame.display.flip()
        pygame.display.update()

    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            print("Player pushed a Button")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                if self.client.game_started:
                    if not self.show_rule_window:
                        # CHECK HAND SLOTS
                        card_number = len(self.slots_hand_cards)
                        for slot in reversed(self.slots_hand_cards):
                            if slot.collidepoint(event.pos):
                                print("hand card: " + str(self.get_card_of_slot(slot)))
                                print("hc/" + str(card_number - 1))
                                self.client.connection.request_action("hc/" + str(card_number - 1))
                                break
                            card_number -= 1
                        # CHECK PILE
                        if slot_d2.collidepoint(event.pos):
                            if str(self.get_card_of_slot(slot_d2)) == "0s":
                                print("no card here, dont send action")
                            else:
                                print("pi/0")
                                self.client.connection.request_action("pi/0")
                        # CHECK PLAYER POSITION 1
                        elif slot_p1.collidepoint(event.pos):
                            print("position 1: " + str(self.get_card_of_slot(slot_p1)))
                            if str(self.get_card_of_slot(slot_p1)) == "0s":
                                print("no card here, dont send action")
                            else:
                                print("oc/0")
                                self.client.connection.request_action("oc/0")
                        # CHECK PLAYER POSITION 2
                        elif slot_p2.collidepoint(event.pos):
                            print("position 2: " + str(self.get_card_of_slot(slot_p2)))
                            if str(self.get_card_of_slot(slot_p2)) == "0s":
                                print("no card here, dont send action")
                            else:
                                print("oc/1")
                                self.client.connection.request_action("oc/1")
                        # CHECK PLAYER POSITION 3
                        elif slot_p3.collidepoint(event.pos):
                            print("position 3: " + str(self.get_card_of_slot(slot_p3)))
                            if str(self.get_card_of_slot(slot_p3)) == "0s":
                                print("no card here, dont send action")
                            else:
                                print("oc/2")
                                self.client.connection.request_action("oc/2")
                        # CHECK END TURN
                        elif slot_end_turn.collidepoint(event.pos):
                            self.client.connection.request_action("et/0")
                            print("et/0")
                            # CHECK RULES
                        elif slot_rules.collidepoint(event.pos):
                            if not self.show_rule_window:
                                self.show_rule_window = True
                    # RESET SHOWING RULES
                    else:
                        self.show_rule_window = False
                # GAME NOT STARTED
                else:
                    if not self.show_rule_window:
                        # CHECK START BUTTON
                        if slot_start.collidepoint(event.pos):
                            self.client.connection.request_start_game()
                            print("game started")
                        # CHECK RULES
                        elif slot_rules.collidepoint(event.pos):
                            if not self.show_rule_window:
                                self.show_rule_window = True
                    # RESET SHOWING RULES
                    else:
                        self.show_rule_window = False
        elif event.type == pygame.MOUSEMOTION:
            if not self.show_rule_window:
                slot_is_hovered = False
                # CHECK CARDS ON HAND
                for slot in reversed(self.slots_hand_cards):
                    if slot.collidepoint(event.pos):
                        self.hovered_slot = slot
                        slot_is_hovered = True
                        break

                        # CHECK PILE
                if slot_d2.collidepoint(event.pos):
                    self.hovered_slot = slot_d2
                    slot_is_hovered = True

                if not slot_is_hovered:
                    self.hovered_slot = None
