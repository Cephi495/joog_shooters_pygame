import pygame
import os
import random
import math
import psutil
import constants
import levels
import objects
import player
import buttons

verbose = False
MUSIC = True
INTRO = False
FPS = False
STATS = False
GRID = False

FRAMES = 1
CPU = psutil.cpu_percent()


# BUG Jump free
# TODO Level optimization
# TODO High score page
# TODO Choose Sprite page
# TODO Intermission
# TODO Ducking
# TODO display playlist from pause
# BUG fix weapon colliding with sprites and platforms
# TODO bullets fired for activated turrets only
# TODO gun and sword level meter display
# TODO regenerate query boxes
# BUG p2 throw weapon from spawn spot glitch


def INSTRUCTION_PAGE():
    global done
    # Load Intro Page
    display_instructions = True
    instruction_page = 1

    Title_BG = pygame.image.load("BACKDROPS/joog_shooters_title.png").convert()
    Instructions_BG = pygame.image.load("BACKDROPS/joog_shooters_instructions.png").convert()
    Instructions2_BG = pygame.image.load("BACKDROPS/joog_shooters_instructions2.png").convert()

    # -------- Instruction Page Loop -----------
    while not done and display_instructions:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                instruction_page += 1
                if instruction_page == 4:
                    display_instructions = False

        screen.fill(constants.BLACK)

        if instruction_page == 1:
            screen.blit(Title_BG, [0, 0])
        if instruction_page == 2:
            screen.blit(Instructions_BG, [0, 0])
        if instruction_page == 3:
            screen.blit(Instructions2_BG, [0, 0])

        # Limit to 5 frames per second
        clock.tick(5)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()


def PAUSE_GAME():
    global Paused, screen_pause_frame, playlist, playlist_que, music_paused, Display_playlist, Display_Info, Display_Credits

    # -------- Music control buttons and playback control---------
    global RsmBtn_img, QuitBtn_img, RestartBtn_img, MusicPlay_img, MusicSkip_img, MusicPrevious_img

    ExtBtn = buttons.exit_button(362, 225)
    RestartBtn = buttons.restart_game_button(100, 340)
    QuitBtn = buttons.quit_game_button(600, 340)
    MusicPlayBtn = buttons.music_play_button(385, 280)
    MusicSkipBtn = buttons.music_skip_button(430, 280)
    MusicPreviousBtn = buttons.music_previous_button(340, 280)
    PlaylistBtn = buttons.playlist_button(80, 420)
    InfoBtn = buttons.info_button(40, 400)

    RsmBtn_hover = pygame.image.load("BUTTONS/RsmBtn_hover.png").convert_alpha()
    RsmBtn_not_hover = pygame.image.load("BUTTONS/RsmBtn.png").convert_alpha()
    RestartBtn_hover = pygame.image.load("BUTTONS/RestartBtn_hover.png").convert_alpha()
    RestartBtn_not_hover = pygame.image.load("BUTTONS/RestartBtn.png").convert_alpha()
    QuitGameBtn_hover = pygame.image.load("BUTTONS/QuitGameBtn_hover.png").convert_alpha()
    QuitGameBtn_not_hover = pygame.image.load("BUTTONS/QuitGameBtn.png").convert_alpha()
    MusicPlay_hover = pygame.image.load("BUTTONS/music_play_hover.png").convert_alpha()
    MusicPlay_not_hover = pygame.image.load("BUTTONS/music_play.png").convert_alpha()
    MusicSkip_hover = pygame.image.load("BUTTONS/music_skip_hover.png").convert_alpha()
    MusicSkip_not_hover = pygame.image.load("BUTTONS/music_skip.png").convert_alpha()
    MusicPrevious_hover = pygame.image.load("BUTTONS/music_previous_hover.png").convert_alpha()
    MusicPrevious_not_hover = pygame.image.load("BUTTONS/music_previous.png").convert_alpha()
    menu_border = pygame.image.load('SPRITES/pause_menu_border.png').convert_alpha()
    playlist_btn = pygame.image.load('BUTTONS/PlaylistBtn.png').convert_alpha()
    info_btn = pygame.image.load('BUTTONS/info_icon.png').convert_alpha()

    RsmBtn_img = RsmBtn_not_hover
    QuitBtn_img = QuitGameBtn_not_hover
    RestartBtn_img = RestartBtn_not_hover
    MusicPlay_img = MusicPlay_not_hover
    MusicSkip_img = MusicSkip_not_hover
    MusicPrevious_img = MusicPrevious_not_hover
    Display_playlist = False
    Display_Info = False
    Display_Credits = False

    while Paused:
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ExtBtn.isOver(mouse):
                    Paused = False
                    screen_pause_frame = 0
                if RestartBtn.isOver(mouse):
                    Paused = False
                    START_GAME()
                if QuitBtn.isOver(mouse):
                    pygame.quit()
                    quit()
                if MusicPlayBtn.isOver(mouse):
                    if music_paused:
                        pygame.mixer.music.unpause()
                        music_paused = False
                    else:
                        pygame.mixer.music.pause()
                        music_paused = True
                if MusicSkipBtn.isOver(mouse):
                    playlist_que += 1
                    music_paused = False
                    if playlist_que > 5:
                        playlist_que = 0
                    music_play()
                if MusicPreviousBtn.isOver(mouse):
                    playlist_que -= 1
                    music_paused = False
                    if playlist_que < 0:
                        playlist_que = 5
                    music_play()
                if PlaylistBtn.isOver(mouse):
                    Display_playlist = True
                    display_page()
                if InfoBtn.isOver(mouse):
                    Display_Info = True
                    display_page()
            if event.type == pygame.MOUSEMOTION:
                if ExtBtn.isOver(mouse):
                    RsmBtn_img = RsmBtn_hover
                if not ExtBtn.isOver(mouse):
                    RsmBtn_img = RsmBtn_not_hover
                if RestartBtn.isOver(mouse):
                    RestartBtn_img = RestartBtn_hover
                if not RestartBtn.isOver(mouse):
                    RestartBtn_img = RestartBtn_not_hover
                if QuitBtn.isOver(mouse):
                    QuitBtn_img = QuitGameBtn_hover
                if not QuitBtn.isOver(mouse):
                    QuitBtn_img = QuitGameBtn_not_hover
                if MusicPlayBtn.isOver(mouse):
                    MusicPlay_img = MusicPlay_hover
                if not MusicPlayBtn.isOver(mouse):
                    MusicPlay_img = MusicPlay_not_hover
                if MusicSkipBtn.isOver(mouse):
                    MusicSkip_img = MusicSkip_hover
                if not MusicSkipBtn.isOver(mouse):
                    MusicSkip_img = MusicSkip_not_hover
                if MusicPreviousBtn.isOver(mouse):
                    MusicPrevious_img = MusicPrevious_hover
                if not MusicPreviousBtn.isOver(mouse):
                    MusicPrevious_img = MusicPrevious_not_hover
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Paused = False
                    screen_pause_frame = 0

        # Prevent pause screen from going too dark
        if screen_pause_frame < 15:
            pause_layer = pygame.Surface((800, 600), pygame.SRCALPHA)  # per-pixel alpha
            pause_layer.fill((0, 0, 0, 25))  # notice the alpha value in the color
            screen.blit(pause_layer, (0, 0))
            screen_pause_frame += 1

        # ------- Blit all buttons and content in pause menu --------

        pygame.draw.rect(screen, (0, 0, 0, 0.5), (45, 200, 710, 200))
        screen.blit(menu_border, [25, 190])
        screen.blit(playlist_btn, [80, 420])
        screen.blit(info_btn, [40, 400])

        # Music and playback control
        screen.blit(RsmBtn_img, [362, 225])
        screen.blit(RestartBtn_img, [100, 340])
        screen.blit(QuitBtn_img, [600, 340])
        screen.blit(MusicPlay_img, [385, 280])
        screen.blit(MusicSkip_img, [430, 280])
        screen.blit(MusicPrevious_img, [340, 280])

        # Player's scores
        screen.blit(P1_img, [190, 250])
        score = font2.render("Score: " + str(P1_Score), True, constants.WHITE)
        screen.blit(score, [170, 300])
        screen.blit(P2_img, [590, 250])
        score = font2.render("Score: " + str(P2_Score), True, constants.WHITE)
        screen.blit(score, [570, 300])
        screen.blit(font2.render("More levels coming soon", True, constants.WHITE), [295, 350])

        if music_paused:
            text = font2.render(playlist[playlist_que], True, constants.LIGHT_GRAY)
        else:
            text = font2.render(playlist[playlist_que], True, constants.WHITE)
        screen.blit(text, [110, 420])

        live_music()
        if FPS:
            display_fps()

        clock.tick(15)
        pygame.display.flip()


def PLAYLIST():
    # --------- Creating Playlist ----------
    global playlist, playlist_que, music_paused, audio_path, audio_wav

    music_paused = False
    playlist_que = random.randint(0, 5)
    playlist = []
    audio_path = 'AUDIO/MUSIC/'
    audio_wav = '.wav'

    # Add songs to the playlist
    Big_Chillum = 'Big Chillum - David Starfire'
    playlist.append(Big_Chillum)
    Jumping_Off = 'Jumping Off - David Starfire'
    playlist.append(Jumping_Off)
    Knight_Riddum = 'Knight Riddum - David Starfire'
    playlist.append(Knight_Riddum)
    Rahu = 'Rahu - David Starfire'
    playlist.append(Rahu)
    Shiva_Lives = 'Shiva Lives - David Starfire'
    playlist.append(Shiva_Lives)
    The_One = 'The One (feat. Alex Grey and Joaqopelli) (Original Mix) - David Starfire'
    playlist.append(The_One)

    pygame.mixer.music.load(audio_path + playlist[playlist_que] + audio_wav)
    pygame.mixer.music.play(1)
    if verbose:
        print(str("<game.py> " + playlist[playlist_que]))


def music_play():
    pygame.mixer.music.load(audio_path + playlist[playlist_que] + audio_wav)
    pygame.mixer.music.play(1)


def live_music():
    # TODO detect if music ends so next song can start
    if pygame.mixer.Channel(0):
        pass


def display_page():
    global Display_playlist, Display_Info, Display_Credits, FPS, STATS, CheckBox1, CheckBox2

    context = font2.render("Coming in v1.2", True, constants.WHITE)
    checked = pygame.image.load("BUTTONS/checked_box-01.png").convert_alpha()
    unchecked = pygame.image.load("BUTTONS/unchecked_box-01.png").convert_alpha()
    X_btn_img = pygame.image.load("BUTTONS/X_Btn-01.png").convert_alpha()

    if FPS:
        CheckBox1 = checked
    else:
        CheckBox1 = unchecked
    if STATS:
        CheckBox2 = checked
    else:
        CheckBox2 = unchecked

    while Display_playlist:
        title = font2.render("PLAYLIST", True, constants.WHITE)
        X_Btn = buttons.X_button(90, 220)
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.draw.rect(screen, (0, 0, 0, 0.5), (80, 215, 645, 170))
                    Display_playlist = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if X_Btn.isOver(mouse):
                    pygame.draw.rect(screen, (0, 0, 0, 0.5), (80, 215, 645, 170))
                    Display_playlist = False
        if Display_playlist:
            pygame.draw.rect(screen, (0, 0, 0, 0.5), (80, 215, 645, 170))
            screen.blit(X_btn_img, (90, 220))
            screen.blit(title, (360, 218))
            screen.blit(context, (330, 300))
        clock.tick(15)
        pygame.display.flip()

    while Display_Info:
        title = font2.render("GAME INFO", True, constants.WHITE)
        checkbox1 = buttons.checkbox1(590, 280)
        checkbox2 = buttons.checkbox2(590, 320)
        X_Btn = buttons.X_button(90, 220)
        credits_Btn = buttons.Credits(645, 360)
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.draw.rect(screen, (0, 0, 0, 0.5), (80, 215, 645, 170))
                    Display_Info = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if X_Btn.isOver(mouse):
                    pygame.draw.rect(screen, (0, 0, 0, 0.5), (80, 215, 645, 170))
                    Display_Info = False
                if checkbox1.isOver(mouse):
                    if FPS:
                        FPS = False
                        CheckBox1 = unchecked
                    else:
                        FPS = True
                        CheckBox1 = checked
                if checkbox2.isOver(mouse):
                    if STATS:
                        STATS = False
                        CheckBox2 = unchecked
                    else:
                        STATS = True
                        CheckBox2 = checked
                if credits_Btn.isOver(mouse):
                    Display_Credits = True
                    display_credits()
        if Display_Info:
            pygame.draw.rect(screen, (0, 0, 0, 0.5), (80, 215, 645, 170))
            screen.blit(X_btn_img, (90, 220))
            screen.blit(title, (360, 218))
            screen.blit(CheckBox1, [590, 277])
            screen.blit(CheckBox2, [590, 317])
            screen.blit(font2.render("Display FPS", True, constants.WHITE), [200, 280])
            screen.blit(font2.render("Display STATS", True, constants.WHITE), [200, 320])
            screen.blit(font2.render("Credits", True, constants.WHITE), [650, 370])
        clock.tick(15)
        pygame.display.flip()


def display_credits():
    global Display_Credits

    c1a = font2.render("Created By:", True, constants.WHITE)
    c1b = font2.render("Music By:", True, constants.WHITE)
    c1c = font2.render("Sprite Art:", True, constants.WHITE)
    c1d = font2.render("Inspiration:", True, constants.WHITE)
    c2a = font2.render("Seay Zagar", True, constants.WHITE)
    c2b = font2.render("David Starfire", True, constants.WHITE)
    c2c = font2.render("Will Bercaw", True, constants.WHITE)
    c2d = font2.render("Duck Game", True, constants.WHITE)
    X_btn_img = pygame.image.load("BUTTONS/X_Btn-01.png").convert_alpha()
    title = font2.render("CREDITS", True, constants.WHITE)
    X_Btn = buttons.X_button(90, 220)
    while Display_Credits:
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.draw.rect(screen, (0, 0, 0, 0.5), (80, 215, 645, 170))
                    Display_Credits = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if X_Btn.isOver(mouse):
                    pygame.draw.rect(screen, (0, 0, 0, 0.5), (80, 215, 645, 170))
                    Display_Credits = False
        if Display_Credits:
            pygame.draw.rect(screen, (0, 0, 0, 0.5), (80, 215, 645, 170))
            screen.blit(X_btn_img, [90, 220])
            screen.blit(title, [360, 218])
            screen.blit(c1a, [270, 265])
            screen.blit(c1b, [270, 295])
            screen.blit(c1c, [270, 325])
            screen.blit(c1d, [270, 355])
            screen.blit(c2a, [450, 265])
            screen.blit(c2b, [450, 295])
            screen.blit(c2c, [450, 325])
            screen.blit(c2d, [450, 355])

        clock.tick(15)
        pygame.display.flip()
    pass


def display_grid():
    pygame.draw.rect(screen, (250, 250, 250), (50, 0, 1, 600))
    pygame.draw.rect(screen, (150, 150, 150), (100, 0, 1, 600))
    pygame.draw.rect(screen, (250, 250, 250), (150, 0, 1, 600))
    pygame.draw.rect(screen, (150, 150, 150), (200, 0, 1, 600))
    pygame.draw.rect(screen, (250, 250, 250), (250, 0, 1, 600))
    pygame.draw.rect(screen, (150, 150, 150), (300, 0, 1, 600))
    pygame.draw.rect(screen, (250, 250, 250), (350, 0, 1, 600))
    pygame.draw.rect(screen, (150, 150, 150), (400, 0, 1, 600))
    pygame.draw.rect(screen, (250, 250, 250), (450, 0, 1, 600))
    pygame.draw.rect(screen, (150, 150, 150), (500, 0, 1, 600))
    pygame.draw.rect(screen, (250, 250, 250), (550, 0, 1, 600))
    pygame.draw.rect(screen, (150, 150, 150), (600, 0, 1, 600))
    pygame.draw.rect(screen, (250, 250, 250), (650, 0, 1, 600))
    pygame.draw.rect(screen, (150, 150, 150), (700, 0, 1, 600))
    pygame.draw.rect(screen, (250, 250, 250), (750, 0, 1, 600))

    pygame.draw.rect(screen, (150, 150, 150), (0, 50, 800, 1))
    pygame.draw.rect(screen, (250, 250, 250), (0, 100, 800, 1))
    pygame.draw.rect(screen, (150, 150, 150), (0, 150, 800, 1))
    pygame.draw.rect(screen, (250, 250, 250), (0, 200, 800, 1))
    pygame.draw.rect(screen, (150, 150, 150), (0, 250, 800, 1))
    pygame.draw.rect(screen, (250, 250, 250), (0, 300, 800, 1))
    pygame.draw.rect(screen, (150, 150, 150), (0, 350, 800, 1))
    pygame.draw.rect(screen, (250, 250, 250), (0, 400, 800, 1))
    pygame.draw.rect(screen, (150, 150, 150), (0, 450, 800, 1))
    pygame.draw.rect(screen, (250, 250, 250), (0, 500, 800, 1))
    pygame.draw.rect(screen, (150, 150, 150), (0, 550, 800, 1))


def P1_SPAWN_WEAPON():
    del Weapon_list[:]

    weapon_type = random.randint(0, 3)
    if weapon_type == 0:
        Weapon_list.append(objects.P1GUN())
    if weapon_type == 1:
        Weapon_list.append(objects.P2GUN())
    if weapon_type == 2:
        Weapon_list.append(objects.P1SWORD())
    if weapon_type == 3:
        Weapon_list.append(objects.P2SWORD())

    for WEAPON in Weapon_list:
        WEAPON.level = current_level
        WEAPON.rect.x = player.P1_WEAPON_X
        WEAPON.rect.y = player.P1_WEAPON_Y
        WEAPON.update()
        active_weapon_list.add(WEAPON)

        player.P1_RESET_WEAPON_SPAWN()


def P2_SPAWN_WEAPON():
    del Weapon_list[:]

    weapon_type = random.randint(0, 3)
    if weapon_type == 0:
        Weapon_list.append(objects.P1GUN())
    if weapon_type == 1:
        Weapon_list.append(objects.P2GUN())
    if weapon_type == 2:
        Weapon_list.append(objects.P1SWORD())
    if weapon_type == 3:
        Weapon_list.append(objects.P2SWORD())

    for WEAPON in Weapon_list:
        WEAPON.level = current_level
        WEAPON.rect.x = player.P2_WEAPON_X
        WEAPON.rect.y = player.P2_WEAPON_Y
        WEAPON.update()
        active_weapon_list.add(WEAPON)

    player.P2_RESET_WEAPON_SPAWN()


def P1_GRAB():
    if verbose:
        print("<game.py> " + "P1_GRAB")
    global p1_has_gun, p1_has_sword
    if "P1GUN" in str(player.p1_touching_weapon):
        p1_has_gun = True
        p1_has_sword = False
        player1.kill_weapon()
        objects.active_weapon_list.remove(objects.P1GUN)
        player1.get_gun()
        player.p1_touching_weapon = None
    if "P2GUN" in str(player.p1_touching_weapon):
        p1_has_gun = True
        p1_has_sword = False
        player1.kill_weapon()
        objects.active_weapon_list.remove(objects.P2GUN)
        player1.get_gun()
        player.p1_touching_weapon = None
    if "P1SWORD" in str(player.p1_touching_weapon):
        p1_has_gun = False
        p1_has_sword = True
        player1.kill_weapon()
        objects.active_weapon_list.remove(objects.P1SWORD)
        player1.get_sword()
        player.p1_touching_weapon = None
    if "P2SWORD" in str(player.p1_touching_weapon):
        p1_has_gun = False
        p1_has_sword = True
        player1.kill_weapon()
        objects.active_weapon_list.remove(objects.P2SWORD)
        player1.get_sword()
        player.p1_touching_weapon = None


def P2_GRAB():
    if verbose:
        print("<game.py> " + "P2_GRAB")
    global p2_has_gun, p2_has_sword
    if "P1GUN" in str(player.p2_touching_weapon):
        p2_has_gun = True
        p2_has_sword = False
        player2.kill_weapon()
        objects.active_weapon_list.remove(objects.P1GUN)
        player2.get_gun()
        player.p2_touching_weapon = None
    if "P2GUN" in str(player.p2_touching_weapon):
        p2_has_gun = True
        p2_has_sword = False
        player2.kill_weapon()
        objects.active_weapon_list.remove(objects.P2GUN)
        player2.get_gun()
        player.p2_touching_weapon = None
    if "P1SWORD" in str(player.p2_touching_weapon):
        p2_has_gun = False
        p2_has_sword = True
        player2.kill_weapon()
        objects.active_weapon_list.remove(objects.P1SWORD)
        player2.get_sword()
        player.p2_touching_weapon = None
    if "P2SWORD" in str(player.p2_touching_weapon):
        p2_has_gun = False
        p2_has_sword = True
        player2.kill_weapon()
        objects.active_weapon_list.remove(objects.P2SWORD)
        player2.get_sword()
        player.p2_touching_weapon = None


def P1_THROW_WEAPON():
    global p1_has_gun, p1_has_sword, player1
    if p1_has_gun:
        del Weapon_list[:]
        Weapon_list.append(objects.P1GUN())
        for WEAPON in Weapon_list:
            WEAPON.level = current_level
            if player1.direction == "R":
                WEAPON.rect.x = player1.rect.x + 20
                WEAPON.rect.y = player1.rect.y + 6
                WEAPON.update()
                WEAPON.toss_right()
            elif player1.direction == "L":
                WEAPON.rect.x = player1.rect.x - 18
                WEAPON.rect.y = player1.rect.y + 6
                WEAPON.update()
                WEAPON.toss_left()
            active_weapon_list.add(WEAPON)
        p1_has_gun = False
        player1.lose_gun()
    if p1_has_sword:
        del Weapon_list[:]
        Weapon_list.append(objects.P1SWORD())
        for WEAPON in Weapon_list:
            WEAPON.level = current_level
            if player1.direction == "R":
                WEAPON.rect.x = player1.rect.x + 20
                WEAPON.rect.y = player1.rect.y + 6
                WEAPON.update()
                WEAPON.toss_right()
            elif player1.direction == "L":
                WEAPON.rect.x = player1.rect.x - 18
                WEAPON.rect.y = player1.rect.y + 6
                WEAPON.update()
                WEAPON.toss_left()
            active_weapon_list.add(WEAPON)
        p1_has_sword = False
        player1.lose_sword()


def P2_THROW_WEAPON():
    global p2_has_gun, p2_has_sword, player2
    if p2_has_gun:
        del Weapon_list[:]
        Weapon_list.append(objects.P2GUN())
        for WEAPON in Weapon_list:
            WEAPON.level = current_level
            if player2.direction == "R":
                WEAPON.rect.x = player2.rect.x + 20
                WEAPON.rect.y = player2.rect.y + 6
                WEAPON.update()
                WEAPON.toss_right()
            elif player2.direction == "L":
                WEAPON.rect.x = player2.rect.x - 18
                WEAPON.rect.y = player2.rect.y + 6
                WEAPON.update()
                WEAPON.toss_left()
            active_weapon_list.add(WEAPON)
        p2_has_gun = False
        player2.lose_gun()
    if p2_has_sword:
        del Weapon_list[:]
        Weapon_list.append(objects.P2SWORD())
        for WEAPON in Weapon_list:
            WEAPON.level = current_level
            if player2.direction == "R":
                WEAPON.rect.x = player2.rect.x + 20
                WEAPON.rect.y = player2.rect.y + 6
                WEAPON.update()
                WEAPON.toss_right()
            elif player2.direction == "L":
                WEAPON.rect.x = player2.rect.x - 18
                WEAPON.rect.y = player2.rect.y + 6
                WEAPON.update()
                WEAPON.toss_left()
            active_weapon_list.add(WEAPON)
        p2_has_sword = False
        player2.lose_sword()


def p1_score():
    global P1_Score, P1_win

    P1_Score += 1
    player1.rect.x = 325
    player1.rect.y = 600
    P1_win = True
    del p1_bullets[:]
    del p2_bullets[:]
    end_level()


def p2_score():
    global P2_Score, P2_win

    P2_Score += 1
    player2.rect.x = 325
    player2.rect.y = 600
    P2_win = True
    del p1_bullets[:]
    del p2_bullets[:]
    end_level()


def player_bullet_manager():
    for bullet in p1_bullets:
        bullet.draw(screen)
        # If bullet goes past player2 and within height of player2
        if player2.rect.x > player1.rect.x:
            if -12 <= (player2.rect.x - bullet.x) <= 0:
                if 0 > (player2.rect.y - bullet.y) > -32:
                    p1_bullets.pop(p1_bullets.index(bullet))
                    if player2.direction == "L" and P2_SLASH > 0:
                        pass
                    else:
                        player2.hit()
                        player.player_1_win = True
        # If bullet goes past player2 and within height of player2
        if player2.rect.x < player1.rect.x:
            if 12 >= (player2.rect.x - bullet.x) >= -15:
                if 0 > (player2.rect.y - bullet.y) > -32:
                    p1_bullets.pop(p1_bullets.index(bullet))
                    if player2.direction == "R" and P2_SLASH > 0:
                        pass
                    else:
                        player2.hit()
                        player.player_1_win = True
        if constants.SCREEN_WIDTH > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            p1_bullets.pop(p1_bullets.index(bullet))
    for bullet in p2_bullets:
        bullet.draw(screen)
        # If bullet goes past player1 and within height range of player1
        if player1.rect.x > player2.rect.x:
            if -12 <= (player1.rect.x - bullet.x) <= 0:
                if 0 > (player1.rect.y - bullet.y) > -32:
                    p2_bullets.pop(p2_bullets.index(bullet))
                    if player1.direction == "L" and P1_SLASH > 0:
                        pass
                    else:
                        player1.hit()
                        player.player_2_win = True
        # If bullet goes past player1 and within height range of player1
        if player1.rect.x < player2.rect.x:
            if 12 >= (player1.rect.x - bullet.x) >= -15:
                if 0 > (player1.rect.y - bullet.y) > -32:
                    p2_bullets.pop(p2_bullets.index(bullet))
                    if player1.direction == "R" and P1_SLASH > 0:
                        pass
                    else:
                        player1.hit()
                        player.player_2_win = True
        if constants.SCREEN_WIDTH > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            p2_bullets.pop(p2_bullets.index(bullet))


def grab_player_manager():
    global grab_p1, grab_p2, p1_escape, p2_escape
    if p1_escape == 20:
        grab_p2 = False
        player.grab_p2 = False
        player.sprite_collided = False
        p1_escape = 0
    if p2_escape == 20:
        grab_p1 = False
        player.grab_p1 = False
        player.sprite_collided = False
        p2_escape = 0
    # TODO jump free
    # print(str(grab_p2) + " " + str(grab_p1))
    if grab_p2:
        if player1.direction == "R":
            player2.rect.left = player1.rect.right
            player2.rect.y = player1.rect.y - 4
            player2.direction = "R"
        if player1.direction == "L":
            player2.rect.right = player1.rect.left
            player2.rect.y = player1.rect.y - 4
            player2.direction = "L"
    if grab_p1:
        if player2.direction == "R":
            player1.rect.left = player2.rect.right
            player1.rect.y = player2.rect.y - 4
            player1.direction = "R"
        if player2.direction == "L":
            player1.rect.right = player2.rect.left
            player1.rect.y = player2.rect.y - 4
            player1.direction = "L"


def activate_turrets():
    global t1_alt, t2_alt, t3_alt, t4_alt, t5_alt, t6_alt
    if len(t1_bullets) < 3 and levels.active_turret_list.__contains__(int(60)):
        t1_bullets.append(objects.turret_projectile(round(levels.T1_XY[0] + 15),
                                                    round(levels.T1_XY[1] + 8),
                                                    5,
                                                    constants.BULLET_RED,
                                                    t1_alt))
        t1_alt = t1_alt * -1
    if len(t2_bullets) < 3 and levels.active_turret_list.__contains__(int(160)):
        t2_bullets.append(objects.turret_projectile(round(levels.T2_XY[0] + 15),
                                                    round(levels.T2_XY[1] + 8),
                                                    5,
                                                    constants.BULLET_RED,
                                                    t2_alt))
        t2_alt = t2_alt * -1
    if len(t3_bullets) < 3 and levels.active_turret_list.__contains__(int(230)):
        t3_bullets.append(objects.turret_projectile(round(levels.T3_XY[0] + 15),
                                                    round(levels.T3_XY[1] + 8),
                                                    5,
                                                    constants.BULLET_RED,
                                                    t3_alt))
        t3_alt = t3_alt * -1
    if len(t4_bullets) < 3 and levels.active_turret_list.__contains__(int(360)):
        t4_bullets.append(objects.turret_projectile(round(levels.T4_XY[0] + 15),
                                                    round(levels.T4_XY[1] + 8),
                                                    5,
                                                    constants.BULLET_RED,
                                                    t4_alt))
        t4_alt = t4_alt * -1
    if len(t5_bullets) < 3 and levels.active_turret_list.__contains__(int(440)):
        t5_bullets.append(objects.turret_projectile(round(levels.T5_XY[0] + 15),
                                                    round(levels.T5_XY[1] + 8),
                                                    5,
                                                    constants.BULLET_RED,
                                                    t5_alt))
        t5_alt = t5_alt * -1
    if len(t6_bullets) < 3 and levels.active_turret_list.__contains__(int(510)):
        t6_bullets.append(objects.turret_projectile(round(levels.T6_XY[0] + 15),
                                                    round(levels.T6_XY[1] + 8),
                                                    5,
                                                    constants.BULLET_RED,
                                                    t6_alt))
        t6_alt = t6_alt * -1


def turret_bullet_manager():
    for bullet in t1_bullets:
        bullet.draw(screen)
        if player1.rect.x > levels.T1_XY[0]:
            if -7 <= (player1.rect.x - bullet.x) <= 0:
                if 0 > (player1.rect.y - bullet.y) > -32:
                    t1_bullets.pop(t1_bullets.index(bullet))
                    if player1.direction == "L" and P1_SLASH > 0:
                        pass
                    else:
                        player1.hit()
                        player.player_2_win = True
        if player1.rect.x < levels.T1_XY[0]:
            if 2 >= (player1.rect.x - bullet.x) >= -15:
                if 0 > (player1.rect.y - bullet.y) > -32:
                    t1_bullets.pop(t1_bullets.index(bullet))
                    if player1.direction == "R" and P1_SLASH > 0:
                        pass
                    else:
                        player1.hit()
                        player.player_2_win = True
        if player2.rect.x > levels.T1_XY[0]:
            if -7 <= (player2.rect.x - bullet.x) <= 0:
                if 0 > (player2.rect.y - bullet.y) > -32:
                    t1_bullets.pop(t1_bullets.index(bullet))
                    if player2.direction == "L" and P2_SLASH > 0:
                        pass
                    else:
                        player2.hit()
                        player.player_1_win = True
        if player2.rect.x < levels.T1_XY[0]:
            if 2 >= (player2.rect.x - bullet.x) >= -15:
                if 0 > (player2.rect.y - bullet.y) > -32:
                    t1_bullets.pop(t1_bullets.index(bullet))
                    if player2.direction == "R" and P2_SLASH > 0:
                        pass
                    else:
                        player2.hit()
                        player.player_1_win = True
        if constants.SCREEN_WIDTH > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            t1_bullets.pop(t1_bullets.index(bullet))
    for bullet in t2_bullets:
        bullet.draw(screen)
        if player1.rect.x > levels.T2_XY[0]:
            if -7 <= (player1.rect.x - bullet.x) <= 0:
                if 0 > (player1.rect.y - bullet.y) > -32:
                    t2_bullets.pop(t2_bullets.index(bullet))
                    if player1.direction == "L" and P1_SLASH > 0:
                        pass
                    else:
                        player1.hit()
                        player.player_2_win = True
        if player1.rect.x < levels.T2_XY[0]:
            if 2 >= (player1.rect.x - bullet.x) >= -15:
                if 0 > (player1.rect.y - bullet.y) > -32:
                    t2_bullets.pop(t2_bullets.index(bullet))
                    if player1.direction == "R" and P1_SLASH > 0:
                        pass
                    else:
                        player1.hit()
                        player.player_2_win = True
        if player2.rect.x > levels.T2_XY[0]:
            if -7 <= (player2.rect.x - bullet.x) <= 0:
                if 0 > (player2.rect.y - bullet.y) > -32:
                    t2_bullets.pop(t2_bullets.index(bullet))
                    if player2.direction == "L" and P2_SLASH > 0:
                        pass
                    else:
                        player2.hit()
                        player.player_1_win = True
        if player2.rect.x < levels.T2_XY[0]:
            if 2 >= (player2.rect.x - bullet.x) >= -15:
                if 0 > (player2.rect.y - bullet.y) > -32:
                    t2_bullets.pop(t2_bullets.index(bullet))
                    if player2.direction == "R" and P2_SLASH > 0:
                        pass
                    else:
                        player2.hit()
                        player.player_1_win = True
        if constants.SCREEN_WIDTH > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            t2_bullets.pop(t2_bullets.index(bullet))
    for bullet in t3_bullets:
        bullet.draw(screen)
        if player1.rect.x > levels.T3_XY[0]:
            if -7 <= (player1.rect.x - bullet.x) <= 0:
                if 0 > (player1.rect.y - bullet.y) > -32:
                    t3_bullets.pop(t3_bullets.index(bullet))
                    if player1.direction == "L" and P1_SLASH > 0:
                        pass
                    else:
                        player1.hit()
                        player.player_2_win = True
        if player1.rect.x < levels.T3_XY[0]:
            if 2 >= (player1.rect.x - bullet.x) >= -15:
                if 0 > (player1.rect.y - bullet.y) > -32:
                    t3_bullets.pop(t3_bullets.index(bullet))
                    if player1.direction == "R" and P1_SLASH > 0:
                        pass
                    else:
                        player1.hit()
                        player.player_2_win = True
        if player2.rect.x > levels.T3_XY[0]:
            if -7 <= (player2.rect.x - bullet.x) <= 0:
                if 0 > (player2.rect.y - bullet.y) > -32:
                    t3_bullets.pop(t3_bullets.index(bullet))
                    if player2.direction == "L" and P2_SLASH > 0:
                        pass
                    else:
                        player2.hit()
                        player.player_1_win = True
        if player2.rect.x < levels.T3_XY[0]:
            if 2 >= (player2.rect.x - bullet.x) >= -15:
                if 0 > (player2.rect.y - bullet.y) > -32:
                    t3_bullets.pop(t3_bullets.index(bullet))
                    if player2.direction == "R" and P2_SLASH > 0:
                        pass
                    else:
                        player2.hit()
                        player.player_1_win = True
        if constants.SCREEN_WIDTH > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            t3_bullets.pop(t3_bullets.index(bullet))
    for bullet in t4_bullets:
        bullet.draw(screen)
        if player1.rect.x > levels.T4_XY[0]:
            if -7 <= (player1.rect.x - bullet.x) <= 0:
                if 0 > (player1.rect.y - bullet.y) > -32:
                    t4_bullets.pop(t4_bullets.index(bullet))
                    if player1.direction == "L" and P1_SLASH > 0:
                        pass
                    else:
                        player1.hit()
                        player.player_2_win = True
        if player1.rect.x < levels.T4_XY[0]:
            if 2 >= (player1.rect.x - bullet.x) >= -15:
                if 0 > (player1.rect.y - bullet.y) > -32:
                    t4_bullets.pop(t4_bullets.index(bullet))
                    if player1.direction == "R" and P1_SLASH > 0:
                        pass
                    else:
                        player1.hit()
                        player.player_2_win = True
        if player2.rect.x > levels.T4_XY[0]:
            if -7 <= (player2.rect.x - bullet.x) <= 0:
                if 0 > (player2.rect.y - bullet.y) > -32:
                    t4_bullets.pop(t4_bullets.index(bullet))
                    if player2.direction == "L" and P2_SLASH > 0:
                        pass
                    else:
                        player2.hit()
                        player.player_1_win = True
        if player2.rect.x < levels.T4_XY[0]:
            if 2 >= (player2.rect.x - bullet.x) >= -15:
                if 0 > (player2.rect.y - bullet.y) > -32:
                    t4_bullets.pop(t4_bullets.index(bullet))
                    if player2.direction == "R" and P2_SLASH > 0:
                        pass
                    else:
                        player2.hit()
                        player.player_1_win = True
        if constants.SCREEN_WIDTH > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            t4_bullets.pop(t4_bullets.index(bullet))
    for bullet in t5_bullets:
        bullet.draw(screen)
        if player1.rect.x > levels.T5_XY[0]:
            if -7 <= (player1.rect.x - bullet.x) <= 0:
                if 0 > (player1.rect.y - bullet.y) > -32:
                    t5_bullets.pop(t5_bullets.index(bullet))
                    if player1.direction == "L" and P1_SLASH > 0:
                        pass
                    else:
                        player1.hit()
                        player.player_2_win = True
        if player1.rect.x < levels.T5_XY[0]:
            if 2 >= (player1.rect.x - bullet.x) >= -15:
                if 0 > (player1.rect.y - bullet.y) > -32:
                    t5_bullets.pop(t5_bullets.index(bullet))
                    if player1.direction == "R" and P1_SLASH > 0:
                        pass
                    else:
                        player1.hit()
                        player.player_2_win = True
        if player2.rect.x > levels.T5_XY[0]:
            if -7 <= (player2.rect.x - bullet.x) <= 0:
                if 0 > (player2.rect.y - bullet.y) > -32:
                    t5_bullets.pop(t5_bullets.index(bullet))
                    if player2.direction == "L" and P2_SLASH > 0:
                        pass
                    else:
                        player2.hit()
                        player.player_1_win = True
        if player2.rect.x < levels.T5_XY[0]:
            if 2 >= (player2.rect.x - bullet.x) >= -15:
                if 0 > (player2.rect.y - bullet.y) > -32:
                    t5_bullets.pop(t5_bullets.index(bullet))
                    if player2.direction == "R" and P2_SLASH > 0:
                        pass
                    else:
                        player2.hit()
                        player.player_1_win = True
        if constants.SCREEN_WIDTH > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            t5_bullets.pop(t5_bullets.index(bullet))
    for bullet in t6_bullets:
        bullet.draw(screen)
        if player1.rect.x > levels.T6_XY[0]:
            if -7 <= (player1.rect.x - bullet.x) <= 0:
                if 0 > (player1.rect.y - bullet.y) > -32:
                    t6_bullets.pop(t6_bullets.index(bullet))
                    if player1.direction == "L" and P1_SLASH > 0:
                        pass
                    else:
                        player1.hit()
                        player.player_2_win = True
        if player1.rect.x < levels.T1_XY[0]:
            if 2 >= (player1.rect.x - bullet.x) >= -15:
                if 0 > (player1.rect.y - bullet.y) > -32:
                    t6_bullets.pop(t6_bullets.index(bullet))
                    if player1.direction == "R" and P1_SLASH > 0:
                        pass
                    else:
                        player1.hit()
                        player.player_2_win = True
        if player2.rect.x > levels.T1_XY[0]:
            if -7 <= (player2.rect.x - bullet.x) <= 0:
                if 0 > (player2.rect.y - bullet.y) > -32:
                    t6_bullets.pop(t6_bullets.index(bullet))
                    if player2.direction == "L" and P2_SLASH > 0:
                        pass
                    else:
                        player2.hit()
                        player.player_1_win = True
        if player2.rect.x < levels.T1_XY[0]:
            if 2 >= (player2.rect.x - bullet.x) >= -15:
                if 0 > (player2.rect.y - bullet.y) > -32:
                    t6_bullets.pop(t6_bullets.index(bullet))
                    if player2.direction == "R" and P2_SLASH > 0:
                        pass
                    else:
                        player2.hit()
                        player.player_1_win = True
        if constants.SCREEN_WIDTH > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            t6_bullets.pop(t6_bullets.index(bullet))


def turret_cooldown_repeater():
    global turret_cooldown
    if turret_cooldown == 60:
        activate_turrets()
        turret_cooldown = 0
    turret_cooldown += 1


def win_checker():
    if player.player_2_win:
        p2_score()
    if player.player_1_win:
        p1_score()


def display_fps():
    fps = font2.render(str(int(clock.get_fps())), True, constants.COMP_GREEN)
    if Paused:
        screen.blit(fps, (710, 425))
    else:
        screen.blit(fps, (5, 5))


def display_stats():
    active_weapons = objects.active_weapon_list
    active_players = active_sprite_list
    CPU_usage = str(round(CPU/FRAMES, 1))
    memory = psutil.Process(os.getpid())
    MEM_usage = str(round(memory.memory_info()[0]/1000000, 1))
    if Paused:
        pass
    else:
        screen.blit(font1.render("CPU: " + CPU_usage + "%", True, constants.WHITE), (35, 5))
        screen.blit(font1.render("RAM: " + MEM_usage + " MB", True, constants.WHITE), (35, 20))
        for sprite in active_players:
            screen.blit(font1.render(str(sprite.rect.x) + " " + str(sprite.rect.y), True, constants.LIGHT_BLUE), (sprite.rect.x - 16, 5))
        for weapon in active_weapons:
            screen.blit(font1.render(str(weapon.rect.x) + " " + str(weapon.rect.y), True, constants.LIGHT_BLUE), (weapon.rect.x - 20, 580))


def end_level():
    global game_ready
    global level_ending_layer
    global level_ending
    global auto_finish
    global active_weapon_list, p1_slash_group, p2_slash_group

    game_ready = False

    level_ending = True
    level_ending_layer = 0
    auto_finish = 0

    active_weapon_list.empty()
    p1_slash_group.empty()
    p2_slash_group.empty()


def new_level():
    global game_ready
    global player1, player2, P1_img, P2_img
    global current_level
    global active_sprite_list, active_weapon_list, p1_slash_group, p2_slash_group
    global level_starting_frame

    active_sprite_list = pygame.sprite.Group()
    active_weapon_list = pygame.sprite.Group()
    p1_slash_group = pygame.sprite.Group()
    p2_slash_group = pygame.sprite.Group()

    RESET_DATA()
    player.RESET_DATA()
    objects.RESET_DATA()

    # Create the players
    player1 = player.Player1()
    player2 = player.Player2()
    P1_img = pygame.image.load("SPRITES/GM/FORWARD.png").convert_alpha()
    P2_img = pygame.image.load("SPRITES/PM/FORWARD.png").convert_alpha()

    # Create all the levels
    level_list = [levels.Level_01(player1, player2),# levels.Level_02(), levels.Level_03(),
                  #levels.Level_04(), levels.Level_05(), levels.Level_06()
                  ]

    # Set the current level
    # Pick random level to begin with
    current_level_no = random.randint(0, 0)
    current_level = level_list[current_level_no]
    if verbose:
        print("<game.py> " + "Level " + str(current_level_no))

    player1.level = current_level
    player2.level = current_level

    active_sprite_list.add(player1)
    active_sprite_list.add(player2)

    player1.start()
    player2.start()

    # Variable used to cause screen darken
    level_starting_frame = 250

    # TODO start pos based on lvl
    player1.rect.x = 480
    player1.rect.y = 120
    player2.rect.x = 300
    player2.rect.y = 120

    game_ready = True


def RESET_DATA():
    global p1_has_gun, p2_has_gun, p1_has_sword, p2_has_sword, grab_p1, grab_p2, p1_escape, p2_escape
    global P1_win, P2_win
    global turret_cooldown
    global P1_CALL_WEAPON, P2_CALL_WEAPON
    global P1_SLASH, P2_SLASH
    global Weapon_list

    p1_has_gun, p2_has_gun, p1_has_sword, p2_has_sword, grab_p2, grab_p1 = False, False, False, False, False, False
    P1_win, P2_win = False, False
    p1_escape, p2_escape = 0, 0
    turret_cooldown = 0
    P1_CALL_WEAPON, P2_CALL_WEAPON = 0, 0
    P1_SLASH, P2_SLASH = 0, 0

    Weapon_list = []

    active_sprite_list.empty()
    active_weapon_list.empty()
    p1_slash_group.empty()
    p2_slash_group.empty()


def START_GAME():
    pygame.init()

    # Game variables
    global clock
    global FRAMES, CPU
    global screen
    global done
    global Paused
    global font1, font2
    global level_starting_frame, level_ending, level_ending_layer, auto_finish, screen_pause_frame
    global music_paused

    # Player variables
    global P1_Score, P2_Score, P1_win, P2_win
    global p1_bullets, p2_bullets
    global t1_bullets, t2_bullets, t3_bullets, t4_bullets, t5_bullets, t6_bullets
    global t1_alt, t2_alt, t3_alt, t4_alt, t5_alt, t6_alt
    global p1_has_gun, p2_has_gun
    global p1_has_sword, p2_has_sword
    global p1_gun_direction, p2_gun_direction
    global P1_CALL_WEAPON, P2_CALL_WEAPON
    global P1_SLASH, P2_SLASH
    global grab_p2, grab_p1, p1_escape, p2_escape
    global active_sprite_list

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    # Window title
    pygame.display.set_caption("Joog Shooters")
    # Play Music
    pygame.mixer.music.load('AUDIO/MUSIC/Rahu - David Starfire.wav')
    pygame.mixer.music.play(-1)
    # Loop until the user clicks the close button.
    done = False
    Paused = False

    # Text font
    font1 = pygame.font.Font(None, 18)
    font2 = pygame.font.Font(None, 26)

    # Run instruction Page sequence
    if INTRO:
        INSTRUCTION_PAGE()
    pygame.mixer.music.stop()

    # Start playlist music
    PLAYLIST()

    # -------- Main Program Loop -----------
    level_ending = False
    screen_pause_frame = 0

    P1_Score, P2_Score = 0, 0
    p1_bullets, p2_bullets = [], []
    t1_bullets, t2_bullets, t3_bullets, t4_bullets, t5_bullets, t6_bullets = [], [], [], [], [], []
    t1_alt, t2_alt, t3_alt, t4_alt, t5_alt, t6_alt = 1, 1, 1, 1, 1, 1

    p1_slash = objects.P1SLASH()
    p2_slash = objects.P2SLASH()

    new_level()

    while not done:
        # Detect user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if game_ready:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        Paused = True
                        PAUSE_GAME()
                    if event.key == pygame.K_UP:
                        if not grab_p1:
                            player1.jump()
                        if grab_p1:
                            p1_escape += 1
                            print(str(p1_escape))
                    if event.key == pygame.K_w:
                        if not grab_p2:
                            player2.jump()
                        if grab_p2:
                            p2_escape += 1
                            print(str(p2_escape))
                    if event.key == pygame.K_DOWN:
                        if player.p1_in_air:
                            player.p1_down_btn = True
                            P1_CALL_WEAPON = 1
                        else:
                            pass
                    if event.key == pygame.K_s:
                        if player.p2_in_air:
                            player.p2_down_btn = True
                            P2_CALL_WEAPON = 1
                        else:
                            pass
                    if event.key == pygame.K_LEFT:
                        if not grab_p1:
                            player1.go_left()
                    if event.key == pygame.K_a:
                        if not grab_p2:
                            player2.go_left()
                    if event.key == pygame.K_RIGHT:
                        if not grab_p1:
                            player1.go_right()
                    if event.key == pygame.K_d:
                        if not grab_p2:
                            player2.go_right()
                    if event.key == pygame.K_PERIOD:
                        # TODO jump free
                        if p1_has_gun or p1_has_sword:
                            P1_THROW_WEAPON()
                        elif player.p1_touching_weapon is not None:
                            P1_GRAB()
                        elif not p1_has_gun and not p1_has_sword:
                            if player.sprite_collided and not grab_p1:
                                grab_p2 = True
                                player.grab_p2 = True
                        else:
                            pass
                    if event.key == pygame.K_TAB:
                        # TODO jump free
                        if p2_has_gun or p2_has_sword:
                            P2_THROW_WEAPON()
                        elif player.p2_touching_weapon is not None:
                            P2_GRAB()
                        elif not p2_has_gun and not p2_has_sword:
                            if player.sprite_collided and not grab_p2:
                                grab_p1 = True
                                player.grab_p1 = True
                        else:
                            pass
                    if event.key == pygame.K_SLASH:
                        if p1_has_gun:
                            if player1.direction == "R":
                                p1_gun_direction = 1
                            else:
                                p1_gun_direction = -1
                            if len(p1_bullets) < 4:
                                p1_bullets.append(objects.projectile(round(player1.rect.x + player1.width // 2),
                                                                     round((player1.rect.y + player1.height // 2) - 7),
                                                                     3,
                                                                     constants.BULLET_GREEN,
                                                                     p1_gun_direction))
                                player1.ammo -= 1
                                if player1.ammo == 0:
                                    player1.lose_gun()
                                    p1_has_gun = False
                                    player1.ammo = 10
                        if p1_has_sword:
                            if P1_SLASH == 0:
                                p1_slash_group.add(p1_slash)
                                P1_SLASH = 1
                                player1.swing -= 1
                                if player1.swing == 0:
                                    player1.lose_sword()
                                    p1_has_sword = False
                                    player1.swing = 10
                    if event.key == pygame.K_q:
                        if p2_has_gun:
                            if player2.direction == "R":
                                p2_gun_direction = 1
                            else:
                                p2_gun_direction = -1
                            if len(p2_bullets) < 4:
                                p2_bullets.append(objects.projectile(round(player2.rect.x + player2.width // 2),
                                                                     round((player2.rect.y + player2.height // 2) - 7),
                                                                     3,
                                                                     constants.BULLET_BLUE,
                                                                     p2_gun_direction))
                                player2.ammo -= 1
                                if player2.ammo == 0:
                                    player2.lose_gun()
                                    p2_has_gun = False
                                    player2.ammo = 10
                        if p2_has_sword:
                            if P2_SLASH == 0:
                                p2_slash_group.add(p2_slash)
                                P2_SLASH = 1
                                player2.swing -= 1
                                if player2.swing == 0:
                                    player2.lose_sword()
                                    p2_has_sword = False
                                    player2.swing = 10
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and player1.change_x < 0:
                        player1.stop()
                    if event.key == pygame.K_d and player2.change_x > 0:
                        player2.stop()
                    if event.key == pygame.K_RIGHT and player1.change_x > 0:
                        player1.stop()
                    if event.key == pygame.K_a and player2.change_x < 0:
                        player2.stop()
                    if event.key == pygame.K_DOWN:
                        player.p1_down_btn = False
                    if event.key == pygame.K_s:
                        player.p2_down_btn = False
                    if event.key == pygame.K_PERIOD:
                        if grab_p2:
                            grab_p2 = False
                            player.grab_p2 = False
                            player.sprite_collided = False
                    if event.key == pygame.K_TAB:
                        if grab_p1:
                            grab_p1 = False
                            player.grab_p1 = False
                            player.sprite_collided = False
        # Update the players.
        active_sprite_list.update()
        active_weapon_list.update()
        # Update items in the level
        current_level.update()
        # If the player1 gets near the right side, shift the world left (-x)
        if player1.rect.right > constants.SCREEN_WIDTH:
            player1.rect.right = constants.SCREEN_WIDTH
        if player2.rect.right > constants.SCREEN_WIDTH:
            player2.rect.right = constants.SCREEN_WIDTH
        # If the player1 gets near the left side, shift the world right (+x)
        if player1.rect.left < 0:
            player1.rect.left = 0
        if player2.rect.left < 0:
            player2.rect.left = 0
        grab_player_manager()
        turret_cooldown_repeater()
        win_checker()
        # ------- ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT -------
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        active_weapon_list.draw(screen)
        # --------- bullet manager ---------
        player_bullet_manager()
        turret_bullet_manager()
        # -----------------------------------
        if level_starting_frame > 0:  # Also transparency value
            screen_layer = pygame.Surface((800, 600), pygame.SRCALPHA)  # per-pixel alpha
            screen_layer.fill((0, 0, 0, level_starting_frame))  # notice the alpha value in the color
            screen.blit(screen_layer, (0, 0))
            # Speed of screen layer fade
            level_starting_frame -= 8
        if level_ending:
            while level_ending:
                if verbose:
                    print("<game.py> " + str(level_ending_layer))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                        pygame.quit()
                        quit()
                    if level_ending_layer > 10:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if P1_win:
                                P1_win = False

                                if verbose:
                                    print("<game.py> " + "P1 Win Reset")
                            if P2_win:
                                P2_win = False

                                if verbose:
                                    print("<game.py> " + "P2 Win Reset")
                            level_ending = False
                            active_sprite_list.empty()
                            new_level()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                if P1_win:
                                    P1_win = False

                                    if verbose:
                                        print("<game.py> " + "P1 Win Reset")
                                if P2_win:
                                    P2_win = False

                                    if verbose:
                                        print("<game.py> " + "P2 Win Reset")
                                level_ending = False
                                active_sprite_list.empty()
                                new_level()

                if level_ending_layer < 20:
                    screen_layer = pygame.Surface((800, 600), pygame.SRCALPHA)  # per-pixel alpha
                    screen_layer.fill((0, 0, 0, level_ending_layer + 10))  # notice the alpha value in the color
                    screen.blit(screen_layer, (0, 0))

                    # Player's scores
                    screen.blit(P1_img, [200, 250])
                    score = font2.render("Score: " + str(P1_Score), True, constants.WHITE)
                    screen.blit(score, [170, 300])
                    screen.blit(P2_img, [575, 250])
                    score = font2.render("Score: " + str(P2_Score), True, constants.WHITE)
                    screen.blit(score, [545, 300])

                    continue_text = font2.render("Click or SPACE to continue >>>", True, constants.WHITE)
                    screen.blit(continue_text, [515, 550])

                    level_ending_layer += 1

                if auto_finish < 100:
                    auto_finish += 1
                    if P1_win:
                        player1.win()
                        player1.rect.y = player1.rect.y - 2
                        active_sprite_list.draw(screen)

                        if verbose:
                            print("<game.py> " + "P1 Win")
                    if P2_win:
                        player2.win()
                        player2.rect.y = player2.rect.y - 2
                        active_sprite_list.draw(screen)

                        if verbose:
                            print("<game.py> " + "P2 Win")
                if auto_finish == 80:
                    if P1_win:
                        P1_win = False

                        if verbose:
                            print("<game.py> " + "P1 Win Reset")
                    if P2_win:
                        P2_win = False

                        if verbose:
                            print("<game.py> " + "P2 Win Reset")
                    active_sprite_list.empty()
                if auto_finish == 100:
                    level_ending = False
                    new_level()

                clock.tick(20)
                pygame.display.flip()
        if player.P1_WEAPON_X is not None:
            P1_SPAWN_WEAPON()
        if player.P2_WEAPON_X is not None:
            P2_SPAWN_WEAPON()
        if P1_SLASH > 0:
            if -35 < player1.rect.x - player2.rect.x < 40 and -35 < player1.rect.y - player2.rect.y < 55:
                player.player_1_win = True
            p1_slash.rect.y = player1.rect.y - 12
            if player1.direction == "R":
                p1_slash.direction = "R"
                p1_slash.rect.x = player1.rect.x
            elif player1.direction == "L":
                p1_slash.direction = "L"
                p1_slash.rect.x = player1.rect.x - 21
            objects.p1_slash_frame = math.floor(P1_SLASH / 2)
            p1_slash_group.update()
            p1_slash_group.draw(screen)
            P1_SLASH += 1
            if P1_SLASH == 20:
                P1_SLASH = 0
                p1_slash_group.empty()
        if P2_SLASH > 0:
            if -35 < player2.rect.x - player1.rect.x < 40 and -35 < player2.rect.y - player1.rect.y < 55:
                player.player_2_win = True
            p2_slash.rect.y = player2.rect.y - 12
            if player2.direction == "R":
                p2_slash.direction = "R"
                p2_slash.rect.x = player2.rect.x
            elif player2.direction == "L":
                p2_slash.direction = "L"
                p2_slash.rect.x = player2.rect.x - 21
            objects.p2_slash_frame = math.floor(P2_SLASH / 2)
            p2_slash_group.update()
            p2_slash_group.draw(screen)
            P2_SLASH += 1
            if P2_SLASH == 20:
                P2_SLASH = 0
                p2_slash_group.empty()
        if FPS:
            display_fps()
        if STATS:
            display_stats()
        if GRID:
            display_grid()
        # ------- ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT --------

        live_music()


        # Limit to 60 frames per second
        clock.tick(0)
        FRAMES += 1
        CPU += psutil.cpu_percent()
        # Update the screen with what was drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()


if __name__ == "__main__":
    START_GAME()
