import pygame
import constants
import platforms

"""

SHORT       2000    x   50
MEDIUM      400     x   50
LONG        600     x   50

"""
T1_XY = [390, 235]
T2_XY = [0, 5]
T3_XY = [0, 5]
T4_XY = [0, 5]
T5_XY = [0, 5]
T6_XY = [0, 5]


class Level(object):
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    def __init__(self, player1):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """

        # Lists of sprites used in all levels. Add or remove
        # lists as needed for your game.

        # Background image
        self.background = None

        self.world_shift = 0
        self.platform_list = pygame.sprite.Group()
        self.query_box_list = pygame.sprite.Group()
        self.turret_list = pygame.sprite.Group()
        self.player = player1

    # Update everything on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.query_box_list.update()
        self.turret_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """
        screen.fill(constants.BLACK)
        screen.blit(self.background, [0, 0])

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.query_box_list.draw(screen)
        self.turret_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x
        for box in self.query_box_list:
            box.rect.x += shift_x
        for turret in self.turret_list:
            turret.rect.x += shift_x


# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player1):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player1)

        self.background = pygame.image.load("BACKDROPS/Pixelated_BG1.png").convert()
        self.background.set_colorkey(constants.WHITE)

        # TODO Update platform data
        # Array with type of platform, and x, y location of the platform.
        level = [[platforms.SHORT_PLATFORM, 50, 66],
                 [platforms.SHORT_PLATFORM, 550, 66],
                 [platforms.MEDIUM_PLATFORM, 200, 133],
                 [platforms.SHORT_PLATFORM, 550, 266],
                 [platforms.SHORT_PLATFORM, 50, 266],
                 [platforms.LONG_PLATFORM, 100, 200],
                 [platforms.LONG_PLATFORM, 100, 333],
                 [platforms.SHORT_PLATFORM, 50, 400],
                 [platforms.SHORT_PLATFORM, 550, 400],
                 [platforms.MEDIUM_PLATFORM, 200, 466],
                 [platforms.SHORT_PLATFORM, 50, 533],
                 [platforms.SHORT_PLATFORM, 550, 533],
                 ]

        m_level = [[platforms.SHORT_PLATFORM, 500, 400, 350, 550, 1]]

        boxes = [[platforms.QUERY_BOX, 300, 33],
                 [platforms.QUERY_BOX, 480, 33],
                 [platforms.QUERY_BOX, 10, 140],
                 [platforms.QUERY_BOX, 770, 140],
                 ]

        turrets = [[platforms.TURRET, 390, 235],
                   ]

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for moving_platform in m_level:
            block = platforms.MovingPlatform(moving_platform[0])
            block.rect.x = moving_platform[1]
            block.rect.y = moving_platform[2]
            block.boundary_left = moving_platform[3]
            block.boundary_right = moving_platform[4]
            block.change_x = moving_platform[5]
            block.player = self.player
            block.level = self
            # self.platform_list.add(block)

        for query_box in boxes:
            block = platforms.Query_Box(query_box[0])
            block.rect.x = query_box[1]
            block.rect.y = query_box[2]
            block.player = self.player
            self.query_box_list.add(block)

        for turret in turrets:
            block = platforms.Turret(turret[0])
            block.rect.x = turret[1]
            block.rect.y = turret[2]
            block.player = self.player
            self.turret_list.add(block)


class Level_02(Level):
    """ Definition for level 1. """

    def __init__(self, player1):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player1)

        self.background = pygame.image.load("BACKDROPS/Pixelated_BG2.png").convert()
        self.background.set_colorkey(constants.BLACK)

        # TODO Update platform data
        # Array with type of platform, and x, y location of the platform.
        level = [[platforms.SHORT_PLATFORM, 300, 250],
                 [platforms.MEDIUM_PLATFORM, 250, 300],
                 [platforms.LONG_PLATFORM, 100, 500],
                 ]

        box = [[platforms.QUERY_BOX, 200, 400],
               [platforms.QUERY_BOX, 300, 400],
               [platforms.QUERY_BOX, 450, 350],
               ]

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for query_box in box:
            block = platforms.Query_Box(query_box[0])
            block.rect.x = query_box[1]
            block.rect.y = query_box[2]
            block.player = self.player
            self.query_box_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.SHORT_PLATFORM)
        block.rect.x = 500
        block.rect.y = 400
        block.boundary_left = 350
        block.boundary_right = 550
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


class Level_03(Level):
    """ Definition for level 1. """

    def __init__(self, player1):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player1)

        self.background = pygame.image.load("BACKDROPS/Pixelated_BG3.png").convert()
        self.background.set_colorkey(constants.BLACK)

        # TODO Update platform data
        # Array with type of platform, and x, y location of the platform.
        level = [[platforms.SHORT_PLATFORM, 300, 250],
                 [platforms.MEDIUM_PLATFORM, 250, 300],
                 [platforms.LONG_PLATFORM, 100, 500],
                 ]

        box = [[platforms.QUERY_BOX, 200, 400],
               [platforms.QUERY_BOX, 300, 400],
               [platforms.QUERY_BOX, 450, 350],
               ]

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for query_box in box:
            block = platforms.Query_Box(query_box[0])
            block.rect.x = query_box[1]
            block.rect.y = query_box[2]
            block.player = self.player
            self.query_box_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.SHORT_PLATFORM)
        block.rect.x = 500
        block.rect.y = 400
        block.boundary_left = 350
        block.boundary_right = 550
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


class Level_04(Level):
    """ Definition for level 1. """

    def __init__(self, player1):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player1)

        self.background = pygame.image.load("BACKDROPS/Smooth_pixel_BG.png").convert()
        self.background.set_colorkey(constants.BLACK)

        # TODO Update platform data
        # Array with type of platform, and x, y location of the platform.
        level = [[platforms.SHORT_PLATFORM, 300, 250],
                 [platforms.MEDIUM_PLATFORM, 250, 300],
                 [platforms.LONG_PLATFORM, 100, 500],
                 ]

        box = [[platforms.QUERY_BOX, 200, 400],
               [platforms.QUERY_BOX, 300, 400],
               [platforms.QUERY_BOX, 450, 350],
               ]

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for query_box in box:
            block = platforms.Query_Box(query_box[0])
            block.rect.x = query_box[1]
            block.rect.y = query_box[2]
            block.player = self.player
            self.query_box_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.SHORT_PLATFORM)
        block.rect.x = 500
        block.rect.y = 400
        block.boundary_left = 350
        block.boundary_right = 550
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


class Level_05(Level):
    """ Definition for level 1. """

    def __init__(self, player1):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player1)

        self.background = pygame.image.load("BACKDROPS/synth-wave-retro-city-landscape.png").convert()
        self.background.set_colorkey(constants.BLACK)

        # TODO Update platform data
        # Array with type of platform, and x, y location of the platform.
        level = [[platforms.SHORT_PLATFORM, 300, 250],
                 [platforms.MEDIUM_PLATFORM, 250, 300],
                 [platforms.LONG_PLATFORM, 100, 500],
                 ]

        box = [[platforms.QUERY_BOX, 200, 400],
               [platforms.QUERY_BOX, 300, 400],
               [platforms.QUERY_BOX, 450, 350],
               ]

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for query_box in box:
            block = platforms.Query_Box(query_box[0])
            block.rect.x = query_box[1]
            block.rect.y = query_box[2]
            block.player = self.player
            self.query_box_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.SHORT_PLATFORM)
        block.rect.x = 500
        block.rect.y = 400
        block.boundary_left = 350
        block.boundary_right = 550
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


class Level_06(Level):
    """ Definition for level 1. """

    def __init__(self, player1):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player1)

        self.background = pygame.image.load("BACKDROPS/Pixel-Art-BackGround1.png").convert()
        self.background.set_colorkey(constants.BLACK)

        # TODO Update platform data
        # Array with type of platform, and x, y location of the platform.
        level = [[platforms.SHORT_PLATFORM, 300, 250],
                 [platforms.MEDIUM_PLATFORM, 250, 300],
                 [platforms.LONG_PLATFORM, 100, 500],
                 ]

        box = [[platforms.QUERY_BOX, 200, 400],
               [platforms.QUERY_BOX, 300, 400],
               [platforms.QUERY_BOX, 450, 350],
               ]

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for query_box in box:
            block = platforms.Query_Box(query_box[0])
            block.rect.x = query_box[1]
            block.rect.y = query_box[2]
            block.player = self.player
            self.query_box_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.SHORT_PLATFORM)
        block.rect.x = 500
        block.rect.y = 400
        block.boundary_left = 350
        block.boundary_right = 550
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
