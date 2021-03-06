import pygame
import constants
import player
from platforms import MovingPlatform
from spritesheet_function import SpriteSheet

active_weapon_list = pygame.sprite.Group()
global p1_slash_frame, p2_slash_frame


def RESET_DATA():
    active_weapon_list.empty()


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
        self.vel = 7 * direction

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


class P1GUN(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        active_weapon_list.add(self)

        self.width = 16
        self.height = 11
        self.change_x = 0
        self.change_y = 0
        self.level = None

        self.image = pygame.image.load(constants.file_path + "SPRITES/SPRITES/GunIcon1.png").convert_alpha()
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

    def update(self):
        """ Move the weapon. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x

        self.image = pygame.image.load(constants.file_path + "SPRITES/SPRITES/GunIcon1.png").convert_alpha()

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
            self.change_x = 0
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
            self.change_x = 0
        # For active players
        player_hit_list = pygame.sprite.spritecollide(self, player.active_sprite_list, False)
        for sprite in player_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_x > 0:
                self.rect.right = sprite.rect.left
            elif self.change_x < 0:
                self.rect.left = sprite.rect.right
            self.change_x = 0

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
            self.change_x = 0
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
            self.change_x = 0
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
            self.change_x = 0
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
            self.kill()

    def toss_left(self):
        self.change_y = - 3
        self.change_x = - 7

    def toss_right(self):
        self.change_y = - 3
        self.change_x = 7


class P2GUN(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        active_weapon_list.add(self)

        self.width = 18
        self.height = 10
        # Set speed vector of weapon
        self.change_x = 0
        self.change_y = 0
        self.level = None

        self.image = pygame.image.load(constants.file_path + "SPRITES/GunIcon2.png").convert_alpha()
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

    def update(self):
        """ Move the weapon. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x

        self.image = pygame.image.load(constants.file_path + "SPRITES/GunIcon2.png").convert_alpha()

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
            self.change_x = 0
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
            self.change_x = 0
        # For active players
        player_hit_list = pygame.sprite.spritecollide(self, player.active_sprite_list, False)
        for sprite in player_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_x > 0:
                self.rect.right = sprite.rect.left
            elif self.change_x < 0:
                self.rect.left = sprite.rect.right
            self.change_x = 0

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
            self.change_x = 0
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
            self.change_x = 0
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
            self.change_x = 0
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
            self.kill()

    def toss_left(self):
        self.change_y = - 3
        self.change_x = - 7

    def toss_right(self):
        self.change_y = - 3
        self.change_x = 7


class P1SWORD(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        active_weapon_list.add(self)

        self.width = 15
        self.height = 15
        # Set speed vector of weapon
        self.change_x = 0
        self.change_y = 0
        self.level = None

        self.image = pygame.image.load(constants.file_path + "SPRITES/SwordIcon1.png").convert_alpha()
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

    def update(self):
        """ Move the weapon. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x

        self.image = pygame.image.load(constants.file_path + "SPRITES/SwordIcon2.png").convert_alpha()

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
            self.change_x = 0
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
            self.change_x = 0
        # For active players
        player_hit_list = pygame.sprite.spritecollide(self, player.active_sprite_list, False)
        for sprite in player_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_x > 0:
                self.rect.right = sprite.rect.left
            elif self.change_x < 0:
                self.rect.left = sprite.rect.right
            self.change_x = 0

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
            self.change_x = 0
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
            self.change_x = 0
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
            self.change_x = 0
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
            self.kill()

    def toss_left(self):
        self.change_y = - 3
        self.change_x = - 7

    def toss_right(self):
        self.change_y = - 3
        self.change_x = 7


class P2SWORD(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        active_weapon_list.add(self)

        self.width = 15
        self.height = 15
        # Set speed vector of weapon
        self.change_x = 0
        self.change_y = 0
        self.level = None

        self.image = pygame.image.load(constants.file_path + "SPRITES/SwordIcon2.png").convert_alpha()
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

    def update(self):
        """ Move the weapon. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x

        self.image = pygame.image.load(constants.file_path + "SPRITES/SwordIcon1.png").convert_alpha()

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
            self.change_x = 0
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
            self.change_x = 0
        # For active players
        player_hit_list = pygame.sprite.spritecollide(self, player.active_sprite_list, False)
        for sprite in player_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_x > 0:
                self.rect.right = sprite.rect.left
            elif self.change_x < 0:
                self.rect.left = sprite.rect.right
            self.change_x = 0

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
            self.change_x = 0
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
            self.change_x = 0
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
            self.change_x = 0
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
            self.kill()

    def toss_left(self):
        self.change_y = - 3
        self.change_x = - 7

    def toss_right(self):
        self.change_y = - 3
        self.change_x = 7


class P1SLASH(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 43
        self.height = 43
        self.direction = "R"
        self.slash_frame_r = []
        self.slash_frame_l = []
        self.slash_none = []
        sprite_sheet = SpriteSheet(constants.file_path + "SPRITES/p1_weapon_slash.png")

        # Load all the right facing walking images into a list
        image = sprite_sheet.get_image(107, 218, 43, 43)
        self.slash_frame_r.append(image)
        image = sprite_sheet.get_image(107, 173, 43, 43)
        self.slash_frame_r.append(image)
        image = sprite_sheet.get_image(107, 130, 43, 43)
        self.slash_frame_r.append(image)
        image = sprite_sheet.get_image(107, 86, 43, 43)
        self.slash_frame_r.append(image)
        image = sprite_sheet.get_image(107, 44, 43, 43)
        self.slash_frame_r.append(image)
        image = sprite_sheet.get_image(107, 0, 43, 43)
        self.slash_frame_r.append(image)

        # Load all the left facing walking images, then flip them
        # to face left.
        image = sprite_sheet.get_image(107, 218, 43, 43)
        image = pygame.transform.flip(image, True, False)
        self.slash_frame_l.append(image)
        image = sprite_sheet.get_image(107, 173, 43, 43)
        image = pygame.transform.flip(image, True, False)
        self.slash_frame_l.append(image)
        image = sprite_sheet.get_image(107, 130, 43, 43)
        image = pygame.transform.flip(image, True, False)
        self.slash_frame_l.append(image)
        image = sprite_sheet.get_image(107, 86, 43, 43)
        image = pygame.transform.flip(image, True, False)
        self.slash_frame_l.append(image)
        image = sprite_sheet.get_image(107, 44, 43, 43)
        image = pygame.transform.flip(image, True, False)
        self.slash_frame_l.append(image)
        image = sprite_sheet.get_image(107, 0, 43, 43)
        image = pygame.transform.flip(image, True, False)
        self.slash_frame_l.append(image)

        # Set a reference to the image rect.
        image = sprite_sheet.get_image(0, 0, 1, 1)
        self.slash_none.append(image)
        self.image = self.slash_none[0]
        self.rect = self.image.get_rect()

    def update(self):
        if p1_slash_frame < 6:
            if self.direction == "R":
                self.image = self.slash_frame_r[p1_slash_frame]

            if self.direction == "L":
                self.image = self.slash_frame_l[p1_slash_frame]
        else:
            self.kill()


class P2SLASH(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 43
        self.height = 43
        self.direction = "R"
        self.slash_frame_r = []
        self.slash_frame_l = []
        self.slash_none = []
        sprite_sheet = SpriteSheet(constants.file_path + "SPRITES/p2_weapon_slash.png")

        # Load all the right facing walking images into a list
        image = sprite_sheet.get_image(107, 218, 43, 43)
        self.slash_frame_r.append(image)
        image = sprite_sheet.get_image(107, 173, 43, 43)
        self.slash_frame_r.append(image)
        image = sprite_sheet.get_image(107, 130, 43, 43)
        self.slash_frame_r.append(image)
        image = sprite_sheet.get_image(107, 86, 43, 43)
        self.slash_frame_r.append(image)
        image = sprite_sheet.get_image(107, 44, 43, 43)
        self.slash_frame_r.append(image)
        image = sprite_sheet.get_image(107, 0, 43, 43)
        self.slash_frame_r.append(image)

        # Load all the left facing walking images, then flip them
        # to face left.
        image = sprite_sheet.get_image(107, 218, 43, 43)
        image = pygame.transform.flip(image, True, False)
        self.slash_frame_l.append(image)
        image = sprite_sheet.get_image(107, 173, 43, 43)
        image = pygame.transform.flip(image, True, False)
        self.slash_frame_l.append(image)
        image = sprite_sheet.get_image(107, 130, 43, 43)
        image = pygame.transform.flip(image, True, False)
        self.slash_frame_l.append(image)
        image = sprite_sheet.get_image(107, 86, 43, 43)
        image = pygame.transform.flip(image, True, False)
        self.slash_frame_l.append(image)
        image = sprite_sheet.get_image(107, 44, 43, 43)
        image = pygame.transform.flip(image, True, False)
        self.slash_frame_l.append(image)
        image = sprite_sheet.get_image(107, 0, 43, 43)
        image = pygame.transform.flip(image, True, False)
        self.slash_frame_l.append(image)

        # Set a reference to the image rect.
        image = sprite_sheet.get_image(0, 0, 1, 1)
        self.slash_none.append(image)
        self.image = self.slash_none[0]
        self.rect = self.image.get_rect()

    def update(self):
        if p2_slash_frame < 6:
            if self.direction == "R":
                self.image = self.slash_frame_r[p2_slash_frame]

            if self.direction == "L":
                self.image = self.slash_frame_l[p2_slash_frame]
        else:
            self.kill()
