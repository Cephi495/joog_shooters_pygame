import pygame
import constants
import player
from platforms import MovingPlatform

active_weapon_list = pygame.sprite.Group()


class projectile(object):
    def __init__(self, x, y, radius, color, direction):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.direction = direction
        self.vel = 8 * direction

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


class turret_projectile(object):
    def __init__(self, x, y, radius, color, direction):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.direction = direction
        self.vel = 4 * direction

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


class P1GUN(pygame.sprite.Sprite):
    def __init__(self):
        """ Platform constructor. Assumes constructed with user passing in
                    an array of 5 numbers like what's defined at the top of this
                    code. """
        super().__init__()
        active_weapon_list.add(self)

        self.width = 16
        self.height = 11
        # Set speed vector of weapon
        self.change_x = 0
        self.change_y = 0
        self.level = None

        self.image = pygame.image.load("SPRITES/GunIcon1.png").convert_alpha()
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

    def update(self):
        """ Move the weapon. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x

        self.image = pygame.image.load("SPRITES/GunIcon1.png").convert_alpha()

        # See if we hit anything
        # For platforms
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
        # For query boxes
        box_hit_list = pygame.sprite.spritecollide(self, self.level.query_box_list, False)
        for box in box_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = box.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = box.rect.right
        # For active players
        player_hit_list = pygame.sprite.spritecollide(self, player.active_sprite_list, False)
        for sprite in player_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_x > 0:
                self.rect.right = sprite.rect.left
            elif self.change_x < 0:
                self.rect.left = sprite.rect.right
            # Stop our vertical movement
            self.change_y = 0

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        # For platforms
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
            # Stop our vertical movement
            self.change_y = 0
            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x
        # For query boxes
        box_hit_list = pygame.sprite.spritecollide(self, self.level.query_box_list, False)
        for box in box_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = box.rect.top
            elif self.change_y < 0:
                self.rect.top = box.rect.bottom
            # Stop our vertical movement
            self.change_y = 0
        # For active players
        player_hit_list = pygame.sprite.spritecollide(self, player.active_sprite_list, False)
        for sprite in player_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = sprite.rect.top
            elif self.change_y < 0:
                self.rect.top = sprite.rect.bottom
            # Stop our vertical movement
            self.change_y = 0
            if self.rect.bottom == sprite.rect.top:
                self.rect.x += sprite.change_x

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .95

        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    def toss(self):
        self.change_y = -4


class P2GUN(pygame.sprite.Sprite):
    def __init__(self):
        """ Platform constructor. Assumes constructed with user passing in
                    an array of 5 numbers like what's defined at the top of this
                    code. """
        super().__init__()
        active_weapon_list.add(self)

        self.width = 16
        self.height = 11
        # Set speed vector of weapon
        self.change_x = 0
        self.change_y = 0
        self.level = None
        self.level = None

        self.image = pygame.image.load("SPRITES/GunIcon1.png").convert_alpha()
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

    def update(self):
        """ Move the weapon. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x

        self.image = pygame.image.load("SPRITES/GunIcon1.png").convert_alpha()

        # See if we hit anything
        # For platforms
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
        # For query boxes
        box_hit_list = pygame.sprite.spritecollide(self, self.level.query_box_list, False)
        for box in box_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = box.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = box.rect.right
        # For active players
        player_hit_list = pygame.sprite.spritecollide(self, player.active_sprite_list, False)
        for sprite in player_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_x > 0:
                self.rect.right = sprite.rect.left
            elif self.change_x < 0:
                self.rect.left = sprite.rect.right
            # Stop our vertical movement
            self.change_y = 0

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        # For platforms
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
            # Stop our vertical movement
            self.change_y = 0
            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x
        # For query boxes
        box_hit_list = pygame.sprite.spritecollide(self, self.level.query_box_list, False)
        for box in box_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = box.rect.top
            elif self.change_y < 0:
                self.rect.top = box.rect.bottom
            # Stop our vertical movement
            self.change_y = 0
        # For active players
        player_hit_list = pygame.sprite.spritecollide(self, player.active_sprite_list, False)
        for sprite in player_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = sprite.rect.top
            elif self.change_y < 0:
                self.rect.top = sprite.rect.bottom
            # Stop our vertical movement
            self.change_y = 0
            if self.rect.bottom == sprite.rect.top:
                self.rect.x += sprite.change_x

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .95

        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    def toss(self):
        """ Called when user hits 'jump' button. """
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -4


class P1SWORD(pygame.sprite.Sprite):
    def __init__(self):
        """ Platform constructor. Assumes constructed with user passing in
                    an array of 5 numbers like what's defined at the top of this
                    code. """
        super().__init__()
        active_weapon_list.add(self)

        self.width = 15
        self.height = 15
        # Set speed vector of weapon
        self.change_x = 0
        self.change_y = 0
        self.level = None
        self.level = None

        self.image = pygame.image.load("SPRITES/SwordIcon1.png").convert_alpha()
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

    def update(self):
        """ Move the weapon. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x

        self.image = pygame.image.load("SPRITES/SwordIcon2.png").convert_alpha()

        # See if we hit anything
        # For platforms
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
        # For query boxes
        box_hit_list = pygame.sprite.spritecollide(self, self.level.query_box_list, False)
        for box in box_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = box.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = box.rect.right
        # For active players
        player_hit_list = pygame.sprite.spritecollide(self, player.active_sprite_list, False)
        for sprite in player_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_x > 0:
                self.rect.right = sprite.rect.left
            elif self.change_x < 0:
                self.rect.left = sprite.rect.right
            # Stop our vertical movement
            self.change_y = 0

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        # For platforms
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
            # Stop our vertical movement
            self.change_y = 0
            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x
        # For query boxes
        box_hit_list = pygame.sprite.spritecollide(self, self.level.query_box_list, False)
        for box in box_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = box.rect.top
            elif self.change_y < 0:
                self.rect.top = box.rect.bottom
            # Stop our vertical movement
            self.change_y = 0
        # For active players
        player_hit_list = pygame.sprite.spritecollide(self, player.active_sprite_list, False)
        for sprite in player_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = sprite.rect.top
            elif self.change_y < 0:
                self.rect.top = sprite.rect.bottom
            # Stop our vertical movement
            self.change_y = 0
            if self.rect.bottom == sprite.rect.top:
                self.rect.x += sprite.change_x

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .95

        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    def toss(self):
        """ Called when user hits 'jump' button. """
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -4


class P2SWORD(pygame.sprite.Sprite):
    def __init__(self):
        """ Platform constructor. Assumes constructed with user passing in
                    an array of 5 numbers like what's defined at the top of this
                    code. """
        super().__init__()
        active_weapon_list.add(self)

        self.width = 15
        self.height = 15
        # Set speed vector of weapon
        self.change_x = 0
        self.change_y = 0
        self.level = None
        self.level = None

        self.image = pygame.image.load("SPRITES/SwordIcon2.png").convert_alpha()
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

    def update(self):
        """ Move the weapon. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x

        self.image = pygame.image.load("SPRITES/SwordIcon1.png").convert_alpha()

        # See if we hit anything
        # For platforms
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
        # For query boxes
        box_hit_list = pygame.sprite.spritecollide(self, self.level.query_box_list, False)
        for box in box_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = box.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = box.rect.right
        # For active players
        player_hit_list = pygame.sprite.spritecollide(self, player.active_sprite_list, False)
        for sprite in player_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_x > 0:
                self.rect.right = sprite.rect.left
            elif self.change_x < 0:
                self.rect.left = sprite.rect.right
            # Stop our vertical movement
            self.change_y = 0

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        # For platforms
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
            # Stop our vertical movement
            self.change_y = 0
            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x
        # For query boxes
        box_hit_list = pygame.sprite.spritecollide(self, self.level.query_box_list, False)
        for box in box_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = box.rect.top
            elif self.change_y < 0:
                self.rect.top = box.rect.bottom
            # Stop our vertical movement
            self.change_y = 0
        # For active players
        player_hit_list = pygame.sprite.spritecollide(self, player.active_sprite_list, False)
        for sprite in player_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = sprite.rect.top
            elif self.change_y < 0:
                self.rect.top = sprite.rect.bottom
            # Stop our vertical movement
            self.change_y = 0
            if self.rect.bottom == sprite.rect.top:
                self.rect.x += sprite.change_x

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .95

        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    def toss(self):
        """ Called when user hits 'jump' button. """
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -4
