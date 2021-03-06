from pygame import *
import sys
import pygame


def menu_screen(Button,run_game):

    """make the screen for menu"""
    display.set_caption("Jet Mission")
    screen = pygame.display.set_mode((800, 600))

    # load button image for quit and start
    start_button = Button("start.png")
    quit_button = Button("exit.png")

    # load image for the menu's background
    bg_image=pygame.image.load("star.gif")

    # resize image
    bg_image=pygame.transform.scale(bg_image, (800, 600))

    # initialize all imported pygame modules
    pygame.init()

    while True:

        # create start button hit box
        rect_start= draw.rect(screen, (0, 0, 0), (250, 200, 300, 125))

        # create quit button hit box
        rect_quit = draw.rect(screen, (0, 0, 0), (250, 300, 300, 125))

        # print bg
        screen.blit(bg_image,(0,0))

        # print start button
        screen.blit(start_button.button,(250,200))

        # print quit button
        screen.blit(quit_button.button,(250,300))

        # wait for a key to be pressed
        ev=event.wait()

        # create a click able button for mouse
        if ev.type == MOUSEBUTTONDOWN:
            if rect_start.collidepoint(mouse.get_pos()):
                run_game()
            if rect_quit.collidepoint(mouse.get_pos()):
                sys.exit()

        # if user want to quit
        if ev.type == QUIT:
            pygame.quit()
            sys.exit()

        # render new frame
        display.update()


def pause_menu(Button,run_game):

    """pause_menu"""
    # make the screen display
    display.set_caption("Dank Mission")
    screen = pygame.display.set_mode((800, 600))

    pygame.init()

    paused = True
    while paused:

        # print bg
        screen.fill(pygame.Color(15, 77, 143))

        # create font
        font=pygame.font.Font("Minecraft.ttf",50)

        # print font
        text=font.render("Paused",True,(255,255,255))
        screen.blit(text,(320,280))

        # wait for a key to be pressed
        ev = event.wait()

        # press esc to resume
        if ev.type == K_ESCAPE:
            paused = False

        if ev.type == K_p:
            paused = False

        # if user want to quit
        if ev.type == QUIT:
            sys.exit()

        # render new frame
        display.update()


def lose_menu(Button,run_game,score):

    """make the screen for menu"""
    display.set_caption("Dank Mission")
    screen = pygame.display.set_mode((800, 600))

    # create font
    font=pygame.font.Font("Minecraft.ttf",50)

    # print font
    text=font.render("Haha you suck",True,(255,255,255))

    # print score
    score_text=font.render("Score: "+str(score),True,(255,255,255))

    # object button for quit and start
    start_button = Button("start.png")
    quit_button = Button("exit.png")

    # image for the menu's backgound
    bg_image = pygame.image.load("star.gif")
    bg_image = pygame.transform.scale(bg_image, (800, 600))

    # initialize all imported pygame modules
    pygame.init()

    while True:

        # create hit box for start and quit
        rect_start = draw.rect(screen, (0, 0, 0), (250, 200, 300, 150))
        rect_quit = draw.rect(screen, (0, 0, 0), (250, 300, 300, 150))

        # print bg
        screen.blit(bg_image, (0, 0))

        # print text
        screen.blit(text,(20,10))

        # print start and quit
        screen.blit(start_button.button, (250, 200))
        screen.blit(quit_button.button, (250, 300))

        # print score
        screen.blit(score_text,(20,100))

        # wait for
        ev = event.wait()

        # create a click able button for mouse
        if ev.type == MOUSEBUTTONDOWN:
            if rect_start.collidepoint(mouse.get_pos()):
                run_game()
            if rect_quit.collidepoint(mouse.get_pos()):
                sys.exit()

        # render new frame
        if ev.type == QUIT:
            sys.exit()

        # render new frame
        display.update()
