import pygame
import card
import gui_event_manager

pygame.init()

# Game Window
win_width, win_height = 1550, 800
win = pygame.display.set_mode((win_width, win_height))
# WINDOW = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
FPS = 60
pygame.display.set_caption("Shithead")
pygame.display.set_icon(pygame.image.load('img/game_icon.png'))
background = "b2"

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY_DARK = (96, 96, 96)
GREY_LIGHT = (220, 220, 220)
GREEN = (120, 215, 120)
BLUE = (50, 110, 160)

# CARD SETTINGS
card_height = 100
card_width = 75

# FONTS
font_playername = pygame.font.SysFont("Ubuntu", 20, True)

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
# USERNAMES
enemy_left_name = "enemy 1"
enemy_mid_name = "enemy 2"
enemy_right_name = "enemy 3"

# CHAT TAG
chat = font_playername.render("Chat", False, WHITE)


def rotate_and_center(x, y, image, angle):
    rotated = pygame.transform.rotate(image, angle)
    size = rotated.get_rect()
    win.blit(rotated, (x - size.center[0], y - size.center[1]))


def draw_card(card_shortcut, slot, face_up=False, rotation_angle=0, translation=(0, 0)):
    card_to_draw = card.Card(card_shortcut[0], card_shortcut[1])
    cx = slot.centerx
    cy = slot.centery
    if face_up:
        card_to_draw.turn()
    picture = pygame.image.load(card_to_draw.getFilename())
    if rotation_angle != 0:
        picture = pygame.transform.rotate(picture, rotation_angle)
    if translation[0] != 0:
        cx = cx + translation[0]
    if translation[1] != 0:
        cy = cy + translation[1]
    size = picture.get_rect()
    win.blit(picture, (cx - size.center[0], cy - size.center[1]))


def draw_window():
    # BACKGROUND
    win.blit(pygame.transform.scale(pygame.image.load("img/" + background + ".png"), (win.get_width(), win.get_height())), (0, 0))  # first fill Screen

    # CARD AREAS
    pygame.draw.rect(win, GREEN, player_area, 3, 8)
    pygame.draw.rect(win, BLUE, enemy1_area, 3, 8)
    pygame.draw.rect(win, BLUE, enemy2_area, 3, 8)
    pygame.draw.rect(win, BLUE, enemy3_area, 3, 8)
    pygame.draw.rect(win, WHITE, chat_area, 0, 8)
    pygame.draw.rect(win, GREY_DARK, deck_area, 3, 8)

    # SLOTS
    pygame.draw.rect(win, GREY_DARK, slot_enemy1_1, 3, 8)
    pygame.draw.rect(win, GREY_DARK, slot_enemy1_2, 3, 8)
    pygame.draw.rect(win, GREY_DARK, slot_enemy1_3, 3, 8)
    pygame.draw.rect(win, GREY_DARK, slot_enemy1_4, 3, 8)

    pygame.draw.rect(win, GREY_DARK, slot_enemy2_1, 3, 8)
    pygame.draw.rect(win, GREY_DARK, slot_enemy2_2, 3, 8)
    pygame.draw.rect(win, GREY_DARK, slot_enemy2_3, 3, 8)
    pygame.draw.rect(win, GREY_DARK, slot_enemy2_4, 3, 8)

    pygame.draw.rect(win, GREY_DARK, slot_enemy3_1, 3, 8)
    pygame.draw.rect(win, GREY_DARK, slot_enemy3_2, 3, 8)
    pygame.draw.rect(win, GREY_DARK, slot_enemy3_3, 3, 8)
    pygame.draw.rect(win, GREY_DARK, slot_enemy3_4, 3, 8)

    pygame.draw.rect(win, GREY_DARK, slot_d1, 3, 8)
    pygame.draw.rect(win, GREY_DARK, slot_d2, 3, 8)

    pygame.draw.rect(win, GREY_DARK, slot_p1, 3, 8)
    pygame.draw.rect(win, GREY_DARK, slot_p2, 3, 8)
    pygame.draw.rect(win, GREY_DARK, slot_p3, 3, 8)

    # USERNAMES
    # ENEMY TAGS
    enemy1 = font_playername.render(enemy_left_name, False, WHITE)
    enemy2 = font_playername.render(enemy_mid_name, False, WHITE)
    enemy3 = font_playername.render(enemy_right_name, False, WHITE)
    win.blit(enemy1, (enemy1_area.centerx - enemy1.get_width() / 2, enemy1_area_y - 10 - enemy1.get_height()))
    win.blit(enemy2, (enemy2_area.centerx - enemy2.get_width() / 2, enemy2_area_y - 10 - enemy2.get_height()))
    win.blit(enemy3, (enemy3_area.centerx - enemy3.get_width() / 2, enemy3_area_y - 10 - enemy3.get_height()))
    # CHAT
    win.blit(chat, (chat_area.x, chat_area_y - 10 - enemy3.get_height()))

    # CARDS
    # DEFAULT SET
    draw_card("1b", slot_enemy1_1)
    draw_card("1b", slot_enemy1_1, False, -5)
    draw_card("1b", slot_enemy1_1, False, 20)
    draw_card("1b", slot_enemy2_1)
    draw_card("1b", slot_enemy2_1, False, -10)
    draw_card("1b", slot_enemy2_1, False, 5)
    draw_card("1b", slot_enemy3_1)
    draw_card("1b", slot_enemy3_1, False, -10)
    draw_card("1b", slot_enemy3_1, False, 15)
    draw_card("1b", slot_d1)

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)  # 60 FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Clean Exit
                run = False
                print("Player has closed the Window")
            else:
                gui_event_manager.handleEvent(event)
        draw_window()

    # Clean Exit
    pygame.quit()


if __name__ == "__main__":
    main()
