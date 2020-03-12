import pygame
import random
import constants
import levels
import objects
import player
from buttons import exit_button, music_play_button, music_skip_button, music_previous_button

verbose = True
MUSIC = True
INTRO = False
FPS = True

# TODO Death at bottom of world


def INSTRUCTION_PAGE():
    global done
    # Load Intro Page
    display_instructions = True
    instruction_page = 1

    Title_BG = pygame.image.load("BACKDROPS/joog_shooters_title.png").convert()
    Instructions_BG = pygame.image.load("BACKDROPS/joog_shooters_instructions.png").convert()

    # -------- Instruction Page Loop -----------
    while not done and display_instructions:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                instruction_page += 1
                if instruction_page == 3:
                    display_instructions = False

        screen.fill(constants.BLACK)

        if instruction_page == 1:
            screen.blit(Title_BG, [0, 0])
        if instruction_page == 2:
            screen.blit(Instructions_BG, [0, 0])

        # Limit to 5 frames per second
        clock.tick(5)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()


def PAUSE_GAME():
    global Paused, screen_pause_frame, playlist, playlist_que, music_paused

    # -------- Music control buttons and playback control---------
    global RsmBtn_img, MusicPlay_img, MusicSkip_img, MusicPrevious_img

    ExtBtn = exit_button(355, 280)
    MusicPlayBtn = music_play_button(375, 320)
    MusicSkipBtn = music_skip_button(420, 320)
    MusicPreviousBtn = music_previous_button(330, 320)

    RsmBtn_hover = pygame.image.load("SPRITES/RsmBtn_hover.png").convert_alpha()
    RsmBtn_not_hover = pygame.image.load("SPRITES/RsmBtn.png").convert_alpha()
    MusicPlay_hover = pygame.image.load("SPRITES/music_play_hover.png").convert_alpha()
    MusicPlay_not_hover = pygame.image.load("SPRITES/music_play.png").convert_alpha()
    MusicSkip_hover = pygame.image.load("SPRITES/music_skip_hover.png").convert_alpha()
    MusicSkip_not_hover = pygame.image.load("SPRITES/music_skip.png").convert_alpha()
    MusicPrevious_hover = pygame.image.load("SPRITES/music_previous_hover.png").convert_alpha()
    MusicPrevious_not_hover = pygame.image.load("SPRITES/music_previous.png").convert_alpha()
    menu_border = pygame.image.load('SPRITES/pause_menu_border.png').convert_alpha()

    RsmBtn_img = RsmBtn_not_hover
    MusicPlay_img = MusicPlay_not_hover
    MusicSkip_img = MusicSkip_not_hover
    MusicPrevious_img = MusicPrevious_not_hover

    while Paused:
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ExtBtn.isOver(mouse):
                    Paused = False
                    screen_pause_frame = 0
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
            if event.type == pygame.MOUSEMOTION:
                if ExtBtn.isOver(mouse):
                    RsmBtn_img = RsmBtn_hover
                if not ExtBtn.isOver(mouse):
                    RsmBtn_img = RsmBtn_not_hover
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
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
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
        screen.blit(menu_border, [25, 190])

        # Music and playback control
        screen.blit(RsmBtn_img, [350, 280])
        screen.blit(MusicPlay_img, [375, 320])
        screen.blit(MusicSkip_img, [420, 320])
        screen.blit(MusicPrevious_img, [330, 320])

        # Player's scores
        screen.blit(P1_img, [200, 250])
        score = font2.render("Score: " + str(P1_Score), True, constants.WHITE)
        screen.blit(score, [170, 300])
        screen.blit(P2_img, [575, 250])
        score = font2.render("Score: " + str(P2_Score), True, constants.WHITE)
        screen.blit(score, [545, 300])

        if music_paused:
            text = font2.render(playlist[playlist_que], True, constants.LIGHT_GRAY)
        else:
            text = font2.render(playlist[playlist_que], True, constants.WHITE)
        screen.blit(text, [110, 420])

        live_music()
        if FPS:
            display_fps()

        clock.tick(18)
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


def P1_SPAWN_WEAPON():
    x = player.WEAPON_X
    y = player.WEAPON_Y

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
        # print("<game.py> " + str(WEAPON))
        WEAPON.level = current_level
        WEAPON.rect.x = x
        WEAPON.rect.y = y
        WEAPON.update()
        active_weapon_list.add(WEAPON)


def P2_SPAWN_WEAPON():
    x = player.WEAPON_X
    y = player.WEAPON_Y

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
        WEAPON.rect.x = x
        WEAPON.rect.y = y
        WEAPON.update()
        active_weapon_list.add(WEAPON)


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
    x = player1.rect.x
    y = player1.rect.y
    if p1_has_gun:
        del Weapon_list[:]
        Weapon_list.append(objects.P1GUN())

        for WEAPON in Weapon_list:
            WEAPON.level = current_level
            WEAPON.rect.x = x
            WEAPON.rect.y = y
            WEAPON.update()
            active_weapon_list.add(WEAPON)
        p1_has_gun = False
        player1.lose_gun()
    if p1_has_sword:
        del Weapon_list[:]
        Weapon_list.append(objects.P1SWORD())

        for WEAPON in Weapon_list:
            WEAPON.level = current_level
            WEAPON.rect.x = x
            WEAPON.rect.y = y
            WEAPON.update()
            active_weapon_list.add(WEAPON)
        p1_has_sword = False
        player1.lose_sword()


def P2_THROW_WEAPON():
    global p2_has_gun, p2_has_sword, player2
    x = player2.rect.x
    y = player2.rect.y
    if p2_has_gun:
        del Weapon_list[:]
        Weapon_list.append(objects.P2GUN())

        for WEAPON in Weapon_list:
            WEAPON.level = current_level
            WEAPON.rect.x = x
            WEAPON.rect.y = y
            WEAPON.update()
            WEAPON.toss()
            active_weapon_list.add(WEAPON)
        p2_has_gun = False
        player2.lose_gun()
    if p2_has_sword:
        del Weapon_list[:]
        Weapon_list.append(objects.P2SWORD())

        for WEAPON in Weapon_list:
            WEAPON.level = current_level
            WEAPON.rect.x = x
            WEAPON.rect.y = y
            WEAPON.update()
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
                    player2.hit()
                    p1_score()
        # If bullet goes past player2 and within height of player2
        if player2.rect.x < player1.rect.x:
            if 12 >= (player2.rect.x - bullet.x) >= -15:
                if 0 > (player2.rect.y - bullet.y) > -32:
                    p1_bullets.pop(p1_bullets.index(bullet))
                    player2.hit()
                    p1_score()
        if constants.SCREEN_WIDTH > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            p1_bullets.pop(p1_bullets.index(bullet))
    for bullet in p2_bullets:
        bullet.draw(screen)
        # If bullet goes past player1 and within height of player1
        if player1.rect.x > player2.rect.x:
            if -12 <= (player1.rect.x - bullet.x) <= 0:
                if 0 > (player1.rect.y - bullet.y) > -32:
                    p2_bullets.pop(p2_bullets.index(bullet))
                    player1.hit()
                    p2_score()
        # If bullet goes past player1 and within height of player1
        if player1.rect.x < player2.rect.x:
            if 12 >= (player1.rect.x - bullet.x) >= -15:
                if 0 > (player1.rect.y - bullet.y) > -32:
                    p2_bullets.pop(p2_bullets.index(bullet))
                    player1.hit()
                    p2_score()
        if constants.SCREEN_WIDTH > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            p2_bullets.pop(p2_bullets.index(bullet))


def activate_turrets():
    global t1_alt
    if len(t1_bullets) < 3:
        t1_bullets.append(objects.turret_projectile(round(levels.T1_XY[0] + 15),
                                                    round(levels.T1_XY[1] + 8),
                                                    5,
                                                    constants.BULLET_RED,
                                                    t1_alt))
        t1_alt = t1_alt * -1


def turret_bullet_manager():
    for bullet in t1_bullets:
        bullet.draw(screen)
        if player1.rect.x > levels.T1_XY[0]:
            if -7 <= (player1.rect.x - bullet.x) <= 0:
                if 0 > (player1.rect.y - bullet.y) > -32:
                    t1_bullets.pop(t1_bullets.index(bullet))
                    player1.hit()
                    p2_score()
        if player1.rect.x < levels.T1_XY[0]:
            if 2 >= (player1.rect.x - bullet.x) >= -15:
                if 0 > (player1.rect.y - bullet.y) > -32:
                    t1_bullets.pop(t1_bullets.index(bullet))
                    player1.hit()
                    p2_score()
        if player2.rect.x > levels.T1_XY[0]:
            if -7 <= (player2.rect.x - bullet.x) <= 0:
                if 0 > (player2.rect.y - bullet.y) > -32:
                    t1_bullets.pop(t1_bullets.index(bullet))
                    player2.hit()
                    p1_score()
        if player2.rect.x < levels.T1_XY[0]:
            if 2 >= (player2.rect.x - bullet.x) >= -15:
                if 0 > (player2.rect.y - bullet.y) > -32:
                    t1_bullets.pop(t1_bullets.index(bullet))
                    player2.hit()
                    p1_score()
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
                    player1.hit()
                    p2_score()
        if player1.rect.x < levels.T2_XY[0]:
            if 2 >= (player1.rect.x - bullet.x) >= -15:
                if 0 > (player1.rect.y - bullet.y) > -32:
                    t2_bullets.pop(t2_bullets.index(bullet))
                    player1.hit()
                    p2_score()
        if player2.rect.x > levels.T2_XY[0]:
            if -7 <= (player2.rect.x - bullet.x) <= 0:
                if 0 > (player2.rect.y - bullet.y) > -32:
                    t2_bullets.pop(t2_bullets.index(bullet))
                    player2.hit()
                    p1_score()
        if player2.rect.x < levels.T2_XY[0]:
            if 2 >= (player2.rect.x - bullet.x) >= -15:
                if 0 > (player2.rect.y - bullet.y) > -32:
                    t2_bullets.pop(t2_bullets.index(bullet))
                    player2.hit()
                    p1_score()
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
                    player1.hit()
                    p2_score()
        if player1.rect.x < levels.T3_XY[0]:
            if 2 >= (player1.rect.x - bullet.x) >= -15:
                if 0 > (player1.rect.y - bullet.y) > -32:
                    t3_bullets.pop(t3_bullets.index(bullet))
                    player1.hit()
                    p2_score()
        if player2.rect.x > levels.T3_XY[0]:
            if -7 <= (player2.rect.x - bullet.x) <= 0:
                if 0 > (player2.rect.y - bullet.y) > -32:
                    t3_bullets.pop(t3_bullets.index(bullet))
                    player2.hit()
                    p1_score()
        if player2.rect.x < levels.T3_XY[0]:
            if 2 >= (player2.rect.x - bullet.x) >= -15:
                if 0 > (player2.rect.y - bullet.y) > -32:
                    t3_bullets.pop(t3_bullets.index(bullet))
                    player2.hit()
                    p1_score()
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
                    player1.hit()
                    p2_score()
        if player1.rect.x < levels.T4_XY[0]:
            if 2 >= (player1.rect.x - bullet.x) >= -15:
                if 0 > (player1.rect.y - bullet.y) > -32:
                    t4_bullets.pop(t4_bullets.index(bullet))
                    player1.hit()
                    p2_score()
        if player2.rect.x > levels.T4_XY[0]:
            if -7 <= (player2.rect.x - bullet.x) <= 0:
                if 0 > (player2.rect.y - bullet.y) > -32:
                    t4_bullets.pop(t4_bullets.index(bullet))
                    player2.hit()
                    p1_score()
        if player2.rect.x < levels.T4_XY[0]:
            if 2 >= (player2.rect.x - bullet.x) >= -15:
                if 0 > (player2.rect.y - bullet.y) > -32:
                    t4_bullets.pop(t4_bullets.index(bullet))
                    player2.hit()
                    p1_score()
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
                    player1.hit()
                    p2_score()
        if player1.rect.x < levels.T5_XY[0]:
            if 2 >= (player1.rect.x - bullet.x) >= -15:
                if 0 > (player1.rect.y - bullet.y) > -32:
                    t5_bullets.pop(t5_bullets.index(bullet))
                    player1.hit()
                    p2_score()
        if player2.rect.x > levels.T5_XY[0]:
            if -7 <= (player2.rect.x - bullet.x) <= 0:
                if 0 > (player2.rect.y - bullet.y) > -32:
                    t5_bullets.pop(t5_bullets.index(bullet))
                    player2.hit()
                    p1_score()
        if player2.rect.x < levels.T5_XY[0]:
            if 2 >= (player2.rect.x - bullet.x) >= -15:
                if 0 > (player2.rect.y - bullet.y) > -32:
                    t5_bullets.pop(t5_bullets.index(bullet))
                    player2.hit()
                    p1_score()
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
                    player1.hit()
                    p2_score()
        if player1.rect.x < levels.T6_XY[0]:
            if 2 >= (player1.rect.x - bullet.x) >= -15:
                if 0 > (player1.rect.y - bullet.y) > -32:
                    t6_bullets.pop(t6_bullets.index(bullet))
                    player1.hit()
                    p2_score()
        if player2.rect.x > levels.T6_XY[0]:
            if -7 <= (player2.rect.x - bullet.x) <= 0:
                if 0 > (player2.rect.y - bullet.y) > -32:
                    t6_bullets.pop(t6_bullets.index(bullet))
                    player2.hit()
                    p1_score()
        if player2.rect.x < levels.T6_XY[0]:
            if 2 >= (player2.rect.x - bullet.x) >= -15:
                if 0 > (player2.rect.y - bullet.y) > -32:
                    t6_bullets.pop(t6_bullets.index(bullet))
                    player2.hit()
                    p1_score()
        if constants.SCREEN_WIDTH > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            t6_bullets.pop(t6_bullets.index(bullet))


def end_level():
    global level_ending_layer
    global level_ending
    global auto_finish

    level_ending = True
    level_ending_layer = 0
    auto_finish = 0

    objects.active_weapon_list.empty()
    player.active_sprite_list.empty()

    player.p1_touching_weapon = None
    player.p2_touching_weapon = None


def new_level():
    global player1, player2, P1_img, P2_img
    global current_level
    global active_sprite_list, active_weapon_list
    global p1_has_gun, p2_has_gun, p1_has_sword, p2_has_sword
    global Weapon_list
    global level_starting_frame

    # Create the players
    player1 = player.Player1()
    player2 = player.Player2()
    P1_img = pygame.image.load("SPRITES/GM/FORWARD.png").convert_alpha()
    P2_img = pygame.image.load("SPRITES/PM/FORWARD.png").convert_alpha()

    # Create all the levels
    level_list = [levels.Level_01(player1), levels.Level_02(player1), levels.Level_03(player1),
                  levels.Level_04(player1), levels.Level_05(player1),
                  levels.Level_06(player1)
                  ]

    # Set the current level
    # Pick random level to begin with
    current_level_no = random.randint(0, 0)
    if verbose:
        print("<game.py> " + "Level " + str(current_level_no))
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    active_weapon_list = pygame.sprite.Group()
    player1.level = current_level
    player2.level = current_level

    # TODO start pos based on lvl
    player1.rect.x = 450
    player1.rect.y = 300
    player2.rect.x = 285
    player2.rect.y = 300

    active_sprite_list.add(player1)
    active_sprite_list.add(player2)

    player1.start()
    player2.start()

    p1_has_gun, p2_has_gun, p1_has_sword, p2_has_sword = False, False, False, False

    Weapon_list = []

    # Variable used to cause screen darken
    level_starting_frame = 250


def display_fps():
    fps = font2.render(str(int(clock.get_fps())), True, constants.COMP_GREEN)
    if Paused:
        screen.blit(fps, (710, 425))
    else:
        screen.blit(fps, (5, 5))


def main():
    pygame.init()

    # Game variables
    global clock
    global screen
    global done
    global Paused
    global font2
    global level_starting_frame, level_ending, level_ending_layer, auto_finish, screen_pause_frame

    # Player variables
    global P1_Score, P2_Score
    global P1_win, P2_win
    global p1_bullets, p2_bullets
    global t1_bullets, t2_bullets, t3_bullets, t4_bullets, t5_bullets, t6_bullets
    global t1_alt, t2_alt, t3_alt, t4_alt, t5_alt, t6_alt
    global p1_has_gun, p2_has_gun
    global p1_has_sword, p2_has_sword
    global p1_gun_direction, p2_gun_direction
    global P1_CALL_WEAPON, P2_CALL_WEAPON

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
    font2 = pygame.font.Font(None, 26)

    # Run instruction Page sequence
    if INTRO:
        INSTRUCTION_PAGE()
    pygame.mixer.music.stop()

    # Start playlist music
    if MUSIC:
        PLAYLIST()

    # -------- Main Program Loop -----------
    level_ending = False
    screen_pause_frame = 0

    P1_Score, P2_Score = 0, 0
    P1_win, P2_win = False, False
    p1_bullets, p2_bullets = [], []

    t1_bullets, t2_bullets, t3_bullets, t4_bullets, t5_bullets, t6_bullets = [], [], [], [], [], []
    t1_alt, t2_alt, t3_alt, t4_alt, t5_alt, t6_alt = 1, 1, 1, 1, 1, 1

    P1_CALL_WEAPON, P2_CALL_WEAPON = 0, 0
    turret_cooldown = 0

    new_level()

    while not done:
        # Detect user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    Paused = True
                    PAUSE_GAME()
                if event.key == pygame.K_UP:
                    player1.jump()
                    P1_CALL_WEAPON = 1
                if event.key == pygame.K_w:
                    player2.jump()
                    P2_CALL_WEAPON = 1
                if event.key == pygame.K_LEFT:
                    player1.go_left()
                if event.key == pygame.K_a:
                    player2.go_left()
                if event.key == pygame.K_RIGHT:
                    player1.go_right()
                if event.key == pygame.K_d:
                    player2.go_right()
                if event.key == pygame.K_PERIOD:
                    # TODO grab player
                    if player.p1_touching_weapon is not None:
                        P1_GRAB()
                    elif p1_has_gun or p1_has_sword:
                        P1_THROW_WEAPON()
                    else:
                        pass
                if event.key == pygame.K_TAB:
                    # TODO grab player
                    if player.p2_touching_weapon is not None:
                        P2_GRAB()
                    elif p2_has_gun or p2_has_sword:
                        P2_THROW_WEAPON()
                    else:
                        pass
                if event.key == pygame.K_SLASH:
                    if p1_has_gun:
                        if player1.direction == "R":
                            p1_gun_direction = 1
                        else:
                            p1_gun_direction = -1
                        if len(p1_bullets) < 5:
                            p1_bullets.append(objects.projectile(round(player1.rect.x + player1.width // 2),
                                                                 round((player1.rect.y + player1.height // 2) - 7),
                                                                 3,
                                                                 constants.BULLET_GREEN,
                                                                 p1_gun_direction))
                    if p1_has_sword:
                        # TODO sword attack
                        pass
                if event.key == pygame.K_q:
                    if p2_has_gun:
                        if player2.direction == "R":
                            p2_gun_direction = 1
                        else:
                            p2_gun_direction = -1
                        if len(p2_bullets) < 5:
                            p2_bullets.append(objects.projectile(round(player2.rect.x + player2.width // 2),
                                                                 round((player2.rect.y + player2.height // 2) - 7),
                                                                 3,
                                                                 constants.BULLET_BLUE,
                                                                 p2_gun_direction))
                    if p2_has_sword:
                        # TODO sword attack
                        pass

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player1.change_x < 0:
                    player1.stop()
                if event.key == pygame.K_a and player2.change_x < 0:
                    player2.stop()
                if event.key == pygame.K_RIGHT and player1.change_x > 0:
                    player1.stop()
                if event.key == pygame.K_d and player2.change_x > 0:
                    player2.stop()

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

        # ------- ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT -------
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        active_weapon_list.draw(screen)

        if turret_cooldown == 35:
            activate_turrets()
            turret_cooldown = 0
        turret_cooldown += 1

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
                    if level_ending_layer == 20:
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

                    continue_text = font2.render("Click to continue >>>", True, constants.WHITE)
                    screen.blit(continue_text, [600, 550])

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

                if auto_finish == 100:
                    level_ending = False
                    new_level()

                clock.tick(20)
                pygame.display.flip()

        if P1_CALL_WEAPON > 0:
            P1_CALL_WEAPON += 1
            if P1_CALL_WEAPON == 12:
                if verbose:
                    print("<game.py> Weapon_x = " + str(player.WEAPON_X) + " Weapon_y = " + str(player.WEAPON_Y))
                try:
                    P1_SPAWN_WEAPON()
                except:
                    if verbose:
                        print("<game.py> No Weapon")
                    pass
                P1_CALL_WEAPON = 0
                player.RESET_WEAPON_SPAWN()
        if P2_CALL_WEAPON > 0:
            P2_CALL_WEAPON += 1
            if P2_CALL_WEAPON == 12:
                if verbose:
                    print("<game.py> Weapon_x = " + str(player.WEAPON_X) + " Weapon_y = " + str(player.WEAPON_Y))
                try:
                    P2_SPAWN_WEAPON()
                except:
                    if verbose:
                        print("<game.py> " + "No Weapon")
                    pass
                P2_CALL_WEAPON = 0
                player.RESET_WEAPON_SPAWN()

        # ------- ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT --------

        live_music()
        if FPS:
            display_fps()

        # Limit to 60 frames per second
        clock.tick(0)
        # Update the screen with what was drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()


if __name__ == "__main__":
    main()
