import gui
import pygame

def handleEvent(event):
    if event.type == pygame.KEYDOWN:
        print("Player pushed a Button")
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == pygame.BUTTON_LEFT:
            if gui.slot_d1.collidepoint(event.pos):
                print("Stapel gedrückt")
            if gui.slot_p1.collidepoint(event.pos):
                print("Position1 gedrückt")
            if gui.slot_p2.collidepoint(event.pos):
                print("Position2 gedrückt")
            if gui.slot_p3.collidepoint(event.pos):
                print("Position3 gedrückt")
