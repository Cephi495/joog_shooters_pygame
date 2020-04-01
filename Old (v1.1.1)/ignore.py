import pygame
import random
import sys

# Global constants

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Player1(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player1
        controls. """

    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        width = 25
        height = 32
        self.image = pygame.Surface([width, height], pygame.SRCALPHA)
        self.image.set_alpha(128)
        # self.image.fill(RED)

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

        # Set speed vector of player1
        self.change_x = 0
        self.change_y = 0

        # List of sprites we can bump against
        self.level = None

    def update(self):
        """ Move the player1. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .65

        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump(self):
        """ Called when user hits 'jump' button. """
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -8

    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -3

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 3

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0


class Player2(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player2
        controls. """

    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        width = 25
        height = 32
        self.image = pygame.Surface([width, height], pygame.SRCALPHA)
        self.image.set_alpha(128)

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

        # Set speed vector of player2
        self.change_x = 0
        self.change_y = 0

        # List of sprites we can bump against
        self.level = None

    def update(self):
        """ Move the player2. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .65

        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump(self):
        """ Called when user hits 'jump' button. """
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -8

    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -3

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 3

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0


class Platform(pygame.sprite.Sprite):
    # TODO Create platform textures
    """ Platform the user can jump on """

    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super().__init__()

        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill((0, 100, 255, 155))

        self.rect = self.image.get_rect()


class Level(object):
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    def __init__(self, player1):
        """ Constructor. Pass in a handle to player1. Needed for when moving platforms
            collide with the player1. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player1 = player1

        # Background image
        self.background = None

    # Update everything on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw all the sprite lists that we have
        screen.fill(BLACK)
        self.platform_list.draw(screen)


# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player1):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player1)

        # Array with width, height, x, and y of platform
        level = [
            [150, 10, 50, 50], [150, 10, 300, 50], [150, 10, 550, 50],
            [150, 10, 50, 150], [150, 10, 300, 150], [150, 10, 550, 150],
            [150, 10, 50, 250], [150, 10, 300, 250], [150, 10, 550, 250],
            [150, 10, 50, 350], [150, 10, 300, 350], [150, 10, 550, 350],
            [150, 10, 50, 450], [150, 10, 300, 450], [150, 10, 550, 450],
            [150, 10, 50, 550], [150, 10, 300, 550], [150, 10, 550, 550],
            [150, 10, 50, 650], [150, 10, 300, 650], [150, 10, 550, 650],
            [150, 10, 50, 750], [150, 10, 300, 750], [150, 10, 550, 750],

            [150, 10, 175, 100], [150, 10, 425, 100],
            [150, 10, 175, 200], [150, 10, 425, 200],
            [150, 10, 175, 300], [150, 10, 425, 300],
            [150, 10, 175, 400], [150, 10, 425, 400],
            [150, 10, 175, 500], [150, 10, 425, 500],
            [150, 10, 175, 600], [150, 10, 425, 600],
        ]

        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player1 = self.player1
            self.platform_list.add(block)


class Level_02(Level):
    """ Definition for level 1. """

    def __init__(self, player1):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player1)

        # Array with width, height, x, and y of platform
        level = [
            [150, 10, 50, 50], [150, 10, 300, 50], [150, 10, 550, 50],
            [150, 10, 50, 250], [150, 10, 300, 250], [150, 10, 550, 250],
            [150, 10, 50, 450], [150, 10, 300, 450], [150, 10, 550, 450],
            [150, 10, 50, 650], [150, 10, 300, 650], [150, 10, 550, 650],
        ]

        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player1 = self.player1
            self.platform_list.add(block)


class Level_03(Level):
    """ Definition for level 1. """

    def __init__(self, player1):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player1)

        # Array with width, height, x, and y of platform
        level = [
            [150, 10, 50, 50], [150, 10, 300, 50], [150, 10, 550, 50],
            [150, 10, 50, 150], [150, 10, 300, 150], [150, 10, 550, 150],
            [150, 10, 50, 250], [150, 10, 300, 250], [150, 10, 550, 250],
            [150, 10, 50, 350], [150, 10, 300, 350], [150, 10, 550, 350],
            [150, 10, 50, 450], [150, 10, 300, 450], [150, 10, 550, 450],
            [150, 10, 50, 550], [150, 10, 300, 550], [150, 10, 550, 550],
            [150, 10, 50, 650], [150, 10, 300, 650], [150, 10, 550, 650],
            [150, 10, 50, 750], [150, 10, 300, 750], [150, 10, 550, 750],

            [150, 10, 175, 100], [150, 10, 425, 100],
            [150, 10, 175, 200], [150, 10, 425, 200],
            [150, 10, 175, 300], [150, 10, 425, 300],
            [150, 10, 175, 400], [150, 10, 425, 400],
            [150, 10, 175, 500], [150, 10, 425, 500],
            [150, 10, 175, 600], [150, 10, 425, 600],
        ]

        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player1 = self.player1
            self.platform_list.add(block)


class Level_04(Level):
    """ Definition for level 1. """

    def __init__(self, player1):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player1)

        # Array with width, height, x, and y of platform
        level = [
            [150, 10, 50, 50], [150, 10, 300, 50], [150, 10, 550, 50],
            [150, 10, 50, 250], [150, 10, 300, 250], [150, 10, 550, 250],
            [150, 10, 50, 450], [150, 10, 300, 450], [150, 10, 550, 450],
            [150, 10, 50, 650], [150, 10, 300, 650], [150, 10, 550, 650],
        ]

        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player1 = self.player1
            self.platform_list.add(block)


class Level_05(Level):
    """ Definition for level 1. """

    def __init__(self, player1):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player1)

        # Array with width, height, x, and y of platform
        level = [
            [150, 10, 50, 50], [150, 10, 300, 50], [150, 10, 550, 50],
            [150, 10, 50, 150], [150, 10, 300, 150], [150, 10, 550, 150],
            [150, 10, 50, 250], [150, 10, 300, 250], [150, 10, 550, 250],
            [150, 10, 50, 350], [150, 10, 300, 350], [150, 10, 550, 350],
            [150, 10, 50, 450], [150, 10, 300, 450], [150, 10, 550, 450],
            [150, 10, 50, 550], [150, 10, 300, 550], [150, 10, 550, 550],
            [150, 10, 50, 650], [150, 10, 300, 650], [150, 10, 550, 650],
            [150, 10, 50, 750], [150, 10, 300, 750], [150, 10, 550, 750],

            [150, 10, 175, 100], [150, 10, 425, 100],
            [150, 10, 175, 200], [150, 10, 425, 200],
            [150, 10, 175, 300], [150, 10, 425, 300],
            [150, 10, 175, 400], [150, 10, 425, 400],
            [150, 10, 175, 500], [150, 10, 425, 500],
            [150, 10, 175, 600], [150, 10, 425, 600],
        ]

        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player1 = self.player1
            self.platform_list.add(block)


class Level_06(Level):
    """ Definition for level 1. """

    def __init__(self, player1):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player1)

        # Array with width, height, x, and y of platform
        level = [
            [150, 10, 50, 50], [150, 10, 300, 50], [150, 10, 550, 50],
            [150, 10, 50, 250], [150, 10, 300, 250], [150, 10, 550, 250],
            [150, 10, 50, 450], [150, 10, 300, 450], [150, 10, 550, 450],
            [150, 10, 50, 650], [150, 10, 300, 650], [150, 10, 550, 650],
        ]

        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player1 = self.player1
            self.platform_list.add(block)


# TODO Create Levels 3-6 here


def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    # Window title
    pygame.display.set_caption("Joog Shooters")

    # This is a font we use to draw text on the screen (size 36)
    font = pygame.font.Font(None, 36)

    # Load Intro Page
    display_instructions = True
    instruction_page = 1

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    pygame.mixer.music.load('AUDIO/MUSIC/Rahu - David Starfire.wav')
    pygame.mixer.music.play(-1)

    # -------- Instruction Page Loop -----------
    while not done and display_instructions:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                instruction_page += 1
                if instruction_page == 3:
                    display_instructions = False

        screen.fill(BLACK)

        if instruction_page == 1:
            # Draw instructions, page 1

            text = font.render("Page 1/2", True, WHITE)
            screen.blit(text, [10, 10])

            text = font.render("Game Title IMG", True, WHITE)
            screen.blit(text, [300, 250])

        if instruction_page == 2:
            # Draw instructions, page 2
            text = font.render("Page 2/2", True, WHITE)
            screen.blit(text, [10, 10])

            text = font.render("Instructions IMG", True, WHITE)
            screen.blit(text, [300, 250])

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    pygame.mixer.music.stop()
    # TODO Start background program to play music here

    # Create the player1
    player1 = Player1()
    player2 = Player2()

    # Create all the levels
    level_list = [Level_01(player1), Level_01(player2), Level_02(player1), Level_02(player2), Level_03(player1),
                  Level_03(player2), Level_04(player1), Level_04(player2), Level_05(player1), Level_05(player2),
                  Level_06(player1), Level_06(player2)]

    # Set the current level
    # TODO choose level by random and triggered by player win

    """def new_lvl():
    new_lvl()"""

    Game_level = random.randint(1, 6)

    current_level_no = Game_level
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player1.level = current_level
    player2.level = current_level

    # TODO start pos based on lvl
    player1.rect.x = 450
    player1.rect.y = 300
    player2.rect.x = 285
    player2.rect.y = 300

    active_sprite_list.add(player1)
    active_sprite_list.add(player2)

    # Backgrounds
    BG1 = pygame.image.load('BACKDROPS/synth-wave-retro-city-landscape.png').convert()
    BG2 = pygame.image.load('BACKDROPS/Pixel-Art-BackGround1.png').convert()
    BG3 = pygame.image.load('BACKDROPS/synth-wave-retro-city-landscape.png').convert()
    BG4 = pygame.image.load('BACKDROPS/Pixel-Art-BackGround1.png').convert()
    BG5 = pygame.image.load('BACKDROPS/synth-wave-retro-city-landscape.png').convert()
    BG6 = pygame.image.load('BACKDROPS/Pixel-Art-BackGround1.png').convert()

    # Sprite Costumes
    GM_FORWARD = pygame.image.load('SPRITES/GM/FORWARD.png').convert_alpha()
    GM_Gun = pygame.image.load('SPRITES/GM/Gun.png').convert_alpha()
    GM_Idle = pygame.image.load('SPRITES/GM/Idle.png').convert_alpha()
    GM_LeftGun = pygame.image.load('SPRITES/GM/LeftGun.png').convert_alpha()
    GM_LeftStep = pygame.image.load('SPRITES/GM/LeftStep.png').convert_alpha()
    GM_LeftSword = pygame.image.load('SPRITES/GM/LeftSword.png').convert_alpha()
    GM_MiddleGun = pygame.image.load('SPRITES/GM/MiddleGun.png').convert_alpha()
    GM_MiddleStep = pygame.image.load('SPRITES/GM/MiddleStep.png').convert_alpha()
    GM_Point = pygame.image.load('SPRITES/GM/Point.png').convert_alpha()
    GM_RightGun = pygame.image.load('SPRITES/GM/RightGun.png').convert_alpha()
    GM_RightStep = pygame.image.load('SPRITES/GM/RightStep.png').convert_alpha()
    GM_RightSword = pygame.image.load('SPRITES/GM/RightSword.png').convert_alpha()
    GM_Sword = pygame.image.load('SPRITES/GM/Sword.png').convert_alpha()

    PM_FORWARD = pygame.image.load('SPRITES/PM/FORWARD.png').convert_alpha()
    PM_Gun = pygame.image.load('SPRITES/PM/Gun.png').convert_alpha()
    PM_Idle = pygame.image.load('SPRITES/PM/Idle.png').convert_alpha()
    PM_LeftGun = pygame.image.load('SPRITES/PM/LeftGun.png').convert_alpha()
    PM_LeftStep = pygame.image.load('SPRITES/PM/LeftStep.png').convert_alpha()
    PM_LeftSword = pygame.image.load('SPRITES/PM/LeftSword.png').convert_alpha()
    PM_MiddleGun = pygame.image.load('SPRITES/PM/MiddleGun.png').convert_alpha()
    PM_MiddleStep = pygame.image.load('SPRITES/PM/MiddleStep.png').convert_alpha()
    # PM_Point = pygame.image.load('SPRITES/PM/Point.png').convert_alpha()
    PM_RightGun = pygame.image.load('SPRITES/PM/RightGun.png').convert_alpha()
    PM_RightStep = pygame.image.load('SPRITES/PM/RightStep.png').convert_alpha()
    PM_RightSword = pygame.image.load('SPRITES/PM/RightSword.png').convert_alpha()
    PM_Sword = pygame.image.load('SPRITES/PM/Sword.png').convert_alpha()

    # -------- Main Program Loop -----------
    sys.stdout.write('Game started\n')
    global GM_Step
    global PM_Step
    global GM_Jump
    global PM_Jump
    global GM_Costume
    global PM_Costume
    GM_Step = 2
    PM_Step = 2
    GM_Jump = 0
    PM_Jump = 0
    P1changed = 0
    P2changed = 0
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player1.go_left()
                    GM_Step = 0
                if event.key == pygame.K_RIGHT:
                    player1.go_right()
                    GM_Step = 1
                if event.key == pygame.K_UP and GM_Step == 1:
                    player1.jump()
                    GM_Jump = 1
                if event.key == pygame.K_UP and GM_Step == 0:
                    player1.jump()
                    GM_Jump = 2
                if event.key == pygame.K_a:
                    player2.go_left()
                    PM_Step = 0
                if event.key == pygame.K_d:
                    player2.go_right()
                    PM_Step = 1
                if event.key == pygame.K_w and PM_Step == 1:
                    player2.jump()
                    PM_Jump = 1
                if event.key == pygame.K_w and PM_Step == 0:
                    player2.jump()
                    PM_Jump = 2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player1.change_x < 0:
                    player1.stop()
                    GM_Step = -2
                if event.key == pygame.K_RIGHT and player1.change_x > 0:
                    player1.stop()
                    GM_Step = -1
                if event.key == pygame.K_UP:
                    GM_Jump = 0
                if event.key == pygame.K_a and player2.change_x < 0:
                    player2.stop()
                    PM_Step = -2
                if event.key == pygame.K_d and player2.change_x > 0:
                    player2.stop()
                    PM_Step = -1
                if event.key == pygame.K_w:
                    PM_Jump = 0

        # Update the players.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        # If the player1 gets near the right side, shift the world left (-x)
        if player1.rect.right > SCREEN_WIDTH:
            player1.rect.right = SCREEN_WIDTH

        if player2.rect.right > SCREEN_WIDTH:
            player2.rect.right = SCREEN_WIDTH

        # If the player1 gets near the left side, shift the world right (+x)
        if player1.rect.left < 0:
            player1.rect.left = 0

        if player2.rect.left < 0:
            player2.rect.left = 0

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        # Sprites
        if GM_Jump == 0:
            if GM_Step == -1:
                GM_Costume = GM_Idle
            if GM_Step == -2:
                GM_Costume = pygame.transform.flip(GM_Idle, True, False)
            if GM_Step == 0:
                if P1changed < 6:
                    P1changed = P1changed + 1
                    GM_Costume = pygame.transform.flip(GM_LeftStep, True, False)
                if 12 > P1changed >= 6:
                    P1changed = P1changed + 1
                    GM_Costume = pygame.transform.flip(GM_MiddleStep, True, False)
                if 18 > P1changed >= 12:
                    P1changed = P1changed + 1
                    GM_Costume = pygame.transform.flip(GM_RightStep, True, False)
                if 24 > P1changed >= 18:
                    P1changed = P1changed + 1
                    GM_Costume = pygame.transform.flip(GM_MiddleStep, True, False)
                if P1changed >= 24:
                    P1changed = 0
            if GM_Step == 1:
                if P1changed <= 6:
                    P1changed = P1changed + 1
                    GM_Costume = GM_LeftStep
                if 12 > P1changed >= 6:
                    P1changed = P1changed + 1
                    GM_Costume = GM_MiddleStep
                if 18 > P1changed >= 12:
                    P1changed = P1changed + 1
                    GM_Costume = GM_RightStep
                if 24 > P1changed >= 18:
                    P1changed = P1changed + 1
                    GM_Costume = GM_MiddleStep
                if P1changed >= 24:
                    P1changed = 0
        if GM_Jump == 1:
            GM_Costume = GM_MiddleStep
        if GM_Jump == 2:
            GM_Costume = pygame.transform.flip(GM_MiddleStep, True, False)
        if GM_Step == 2:
            GM_Costume = GM_FORWARD

        if PM_Jump == 0:
            if PM_Step == -1:
                PM_Costume = PM_Idle
            if PM_Step == -2:
                PM_Costume = pygame.transform.flip(PM_Idle, True, False)
            if PM_Step == 0:
                if P2changed < 6:
                    PM_Costume = pygame.transform.flip(PM_LeftStep, True, False)
                    P2changed = P2changed + 1
                if 12 > P2changed >= 6:
                    PM_Costume = pygame.transform.flip(PM_MiddleStep, True, False)
                    P2changed = P2changed + 1
                if 18 > P2changed >= 12:
                    PM_Costume = pygame.transform.flip(PM_RightStep, True, False)
                    P2changed = P2changed + 1
                if 24 > P2changed >= 18:
                    PM_Costume = pygame.transform.flip(PM_MiddleStep, True, False)
                    P2changed = P2changed + 1
                if P2changed >= 24:
                    P2changed = 0
            if PM_Step == 1:
                if P2changed < 6:
                    PM_Costume = PM_LeftStep
                    P2changed = P2changed + 1
                if 12 > P2changed >= 6:
                    PM_Costume = PM_MiddleStep
                    P2changed = P2changed + 1
                if 18 > P2changed >= 12:
                    PM_Costume = PM_RightStep
                    P2changed = P2changed + 1
                if 24 > P2changed >= 18:
                    PM_Costume = PM_MiddleStep
                    P2changed = P2changed + 1
                if P2changed >= 24:
                    P2changed = 0
        if PM_Jump == 1:
            PM_Costume = PM_MiddleStep
        if PM_Jump == 2:
            PM_Costume = pygame.transform.flip(PM_MiddleStep, True, False)
        if PM_Step == 2:
            PM_Costume = PM_FORWARD

        player1.image.blit(GM_Costume, [0, -8])
        player2.image.blit(PM_Costume, [0, -8])

        # Backgrounds
        '''if current_level_no == 1:
            screen.blit(BG1, [0, 0])

        if current_level_no == 2:
            screen.blit(BG2, [0, 0])

        if current_level_no == 3:
            screen.blit(BG3, [0, 0])

        if current_level_no == 4:
            screen.blit(BG4, [0, 0])

        if current_level_no == 5:
            screen.blit(BG5, [0, 0])

        if current_level_no == 6:
            screen.blit(BG6, [0, 0])'''

        current_level.draw(screen)
        active_sprite_list.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()


if __name__ == "__main__":
    main()
