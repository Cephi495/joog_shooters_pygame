import pygame
import constants
import objects
from platforms import MovingPlatform
from spritesheet_function import SpriteSheet

verbose = False

sprite_collided = False
WEAPON_X = None
WEAPON_Y = None
p1_touching_weapon, p2_touching_weapon = None, None
grab_p2, grab_p1 = False, False
p1_fell_to_death, p2_fell_to_death = False, False
active_sprite_list = pygame.sprite.Group()
sprite1_group = pygame.sprite.Group()
sprite2_group = pygame.sprite.Group()


def SPAWN_WEAPON(x, y):
    global WEAPON_X
    global WEAPON_Y

    WEAPON_X = x
    WEAPON_Y = y


def RESET_WEAPON_SPAWN():
    global WEAPON_X
    global WEAPON_Y

    WEAPON_X = None
    WEAPON_Y = None


class Player1(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player1
        controls. """

    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()
        active_sprite_list.add(self)
        sprite1_group.add(self)

        # -- Attributes
        self.width = 18
        self.height = 32
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        # This holds all the images for the animated walk left/right
        # of our player
        self.walking_frames_l = []
        self.walking_frames_r = []
        self.idle_walking_l = []
        self.idle_walking_r = []
        self.idle_forward_frame = []
        self.gun_frames_l = []
        self.gun_frames_r = []
        self.idle_gun_l = []
        self.idle_gun_r = []
        self.sword_frames_l = []
        self.sword_frames_r = []
        self.idle_sword_l = []
        self.idle_sword_r = []

        # For winning page
        self.Large = []
        sprite_sheet = SpriteSheet("SPRITES/Player1_Large.png")
        image = sprite_sheet.get_image(60, 96, 190, 384)
        self.Large.append(image)

        # What direction is the player facing?
        self.direction = "F"
        self.idling = True

        self.has_gun = False
        self.has_sword = False
        self.WEAPON = None

        # List of sprites we can bump against
        self.level = None
        sprite_sheet = SpriteSheet("SPRITES/Sprite1_sheet.png")

        # Load all the right facing walking images into a list
        image = sprite_sheet.get_image(54, 8, 18, 32)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(80, 8, 18, 32)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(54, 8, 18, 32)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(103, 8, 18, 32)
        self.walking_frames_r.append(image)

        image = sprite_sheet.get_image(30, 8, 18, 32)
        self.idle_walking_r.append(image)

        # Load all the right facing gun images into a list
        image = sprite_sheet.get_image(54, 88, 22, 32)
        self.gun_frames_r.append(image)
        image = sprite_sheet.get_image(80, 88, 22, 32)
        self.gun_frames_r.append(image)
        image = sprite_sheet.get_image(54, 88, 22, 32)
        self.gun_frames_r.append(image)
        image = sprite_sheet.get_image(103, 88, 22, 32)
        self.gun_frames_r.append(image)

        image = sprite_sheet.get_image(30, 88, 22, 32)
        self.idle_gun_r.append(image)

        # Load all the right facing sword images into a list
        image = sprite_sheet.get_image(54, 48, 21, 32)
        self.sword_frames_r.append(image)
        image = sprite_sheet.get_image(80, 48, 21, 32)
        self.sword_frames_r.append(image)
        image = sprite_sheet.get_image(54, 48, 21, 32)
        self.sword_frames_r.append(image)
        image = sprite_sheet.get_image(103, 48, 21, 32)
        self.sword_frames_r.append(image)

        image = sprite_sheet.get_image(30, 48, 21, 32)
        self.idle_sword_r.append(image)

        # Load all the left facing walking images, then flip them
        # to face left.
        image = sprite_sheet.get_image(54, 8, 18, 32)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(80, 8, 18, 32)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(54, 8, 18, 32)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(103, 8, 18, 32)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(30, 8, 18, 32)
        image = pygame.transform.flip(image, True, False)
        self.idle_walking_l.append(image)

        # Load all the left facing gun images, then flip them
        # to face left.
        image = sprite_sheet.get_image(54, 88, 22, 32)
        image = pygame.transform.flip(image, True, False)
        self.gun_frames_l.append(image)
        image = sprite_sheet.get_image(80, 88, 22, 32)
        image = pygame.transform.flip(image, True, False)
        self.gun_frames_l.append(image)
        image = sprite_sheet.get_image(54, 88, 22, 32)
        image = pygame.transform.flip(image, True, False)
        self.gun_frames_l.append(image)
        image = sprite_sheet.get_image(103, 88, 22, 32)
        image = pygame.transform.flip(image, True, False)
        self.gun_frames_l.append(image)

        image = sprite_sheet.get_image(30, 88, 22, 32)
        image = pygame.transform.flip(image, True, False)
        self.idle_gun_l.append(image)

        # Load all the left facing sword images, then flip them
        # to face left.
        image = sprite_sheet.get_image(54, 48, 21, 32)
        image = pygame.transform.flip(image, True, False)
        self.sword_frames_l.append(image)
        image = sprite_sheet.get_image(80, 48, 21, 32)
        image = pygame.transform.flip(image, True, False)
        self.sword_frames_l.append(image)
        image = sprite_sheet.get_image(54, 48, 21, 32)
        image = pygame.transform.flip(image, True, False)
        self.sword_frames_l.append(image)
        image = sprite_sheet.get_image(103, 48, 21, 32)
        image = pygame.transform.flip(image, True, False)
        self.sword_frames_l.append(image)

        image = sprite_sheet.get_image(30, 48, 21, 32)
        image = pygame.transform.flip(image, True, False)
        self.idle_sword_l.append(image)

        # Set the image the player starts with
        image = sprite_sheet.get_image(5, 8, 18, 32)
        self.idle_forward_frame.append(image)
        self.image = self.idle_forward_frame[0]

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

    def update(self):
        global p1_touching_weapon, p1_weapon_x, p1_weapon_y, sprite_collided, grab_p2

        """ Move the player1. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x
        pos = self.rect.x  # + self.level.world_shift

        if self.direction == "F":
            self.image = self.idle_forward_frame[0]

        if self.has_gun:
            if self.direction == "R":
                if self.idling:
                    self.image = self.idle_gun_r[0]
                else:
                    frame = (pos // 15) % len(self.gun_frames_r)
                    self.image = self.gun_frames_r[frame]
            else:
                if self.idling:
                    self.image = self.idle_gun_l[0]
                else:
                    frame = (pos // 15) % len(self.gun_frames_l)
                    self.image = self.gun_frames_l[frame]
        elif self.has_sword:
            if self.direction == "R":
                if self.idling:
                    self.image = self.idle_sword_r[0]
                else:
                    frame = (pos // 15) % len(self.sword_frames_r)
                    self.image = self.sword_frames_r[frame]
            else:
                if self.idling:
                    self.image = self.idle_sword_l[0]
                else:
                    frame = (pos // 15) % len(self.sword_frames_l)
                    self.image = self.sword_frames_l[frame]
        else:
            if self.direction == "R":
                if self.idling:
                    self.image = self.idle_walking_r[0]
                else:
                    frame = (pos // 15) % len(self.walking_frames_r)
                    self.image = self.walking_frames_r[frame]
            else:
                if self.idling:
                    self.image = self.idle_walking_l[0]
                else:
                    frame = (pos // 15) % len(self.walking_frames_l)
                    self.image = self.walking_frames_l[frame]

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
            if self.change_x > 0:
                self.rect.right = box.rect.left
            elif self.change_x < 0:
                self.rect.left = box.rect.right
        # For active weapons
        weapon_hit_list = pygame.sprite.spritecollide(self, objects.active_weapon_list, False)
        for weapon in weapon_hit_list:
            if not self.has_gun and not self.has_sword:
                if p1_touching_weapon is None:
                    p1_touching_weapon = weapon
                    self.WEAPON = weapon
            p1_weapon_x = weapon.rect.x
            p1_weapon_y = weapon.rect.y
            if self.change_x > 0:
                weapon.rect.left = self.rect.right
            elif self.change_x < 0:
                weapon.rect.right = self.rect.left
        # For active players
        player_hit_list = pygame.sprite.spritecollide(self, sprite2_group, False)
        for player in player_hit_list:
            if self.rect.x + self.width//2 > player.rect.x + player.width//2:
                self.rect.x += 1
            elif self.rect.x + self.width//2 < player.rect.x + player.width//2:
                self.rect.x -= 1
            sprite_collided = True

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
            if self.change_y > 0:
                self.rect.bottom = box.rect.top
            elif self.change_y < 0:
                SPAWN_WEAPON(box.rect.x, box.rect.y - 6)
                box.kill()
            self.change_y = 0
        # For weapons
        weapon_hit_list = pygame.sprite.spritecollide(self, objects.active_weapon_list, False)
        for weapon in weapon_hit_list:
            if not self.has_gun and not self.has_sword:
                if p1_touching_weapon is None:
                    p1_touching_weapon = weapon
                    self.WEAPON = weapon
            p1_weapon_x = weapon.rect.x
            p1_weapon_y = weapon.rect.y
            if verbose:
                print("<player.py> " + str(weapon))
            if self.change_y > 0:
                self.rect.bottom = weapon.rect.top
                self.change_y = 0
            elif self.change_y < 0:
                weapon.rect.bottom = self.rect.top

        if p1_touching_weapon is not None:
            if 40 < abs(abs(self.rect.x + self.width//2) - abs(p1_weapon_x + 8)):
                p1_touching_weapon = None
                if verbose:
                    print("<player.py> " + "P1 not touching weapon")

            elif 40 < abs(abs(self.rect.y + self.height//2) - abs(p1_weapon_y + 6)):
                p1_touching_weapon = None
                if verbose:
                    print("<player.py> " + "P1 not touching weapon ")

        if sprite_collided:
            player_hit_list = pygame.sprite.spritecollide(self, sprite2_group, False)
            if len(player_hit_list) < 1:
                sprite_collided = False
                if verbose:
                    print("<player.py> " + "P1 touching P2 " + str(sprite_collided))

    def calc_grav(self):
        """ Calculate effect of gravity. """
        global p1_fell_to_death
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .95

        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.kill()
            p1_fell_to_death = True

    def jump(self):
        """ Called when user hits 'jump' button. """
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        box_hit_list = pygame.sprite.spritecollide(self, self.level.query_box_list, False)
        weapon_hit_list = pygame.sprite.spritecollide(self, objects.active_weapon_list, False)
        self.rect.y -= 2
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or len(box_hit_list) > 0 or len(weapon_hit_list) > 0:
            if not grab_p2:
                self.change_y = -12
            else:
                self.change_y = -5

    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -3
        self.direction = "L"
        self.idling = False

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 3
        self.direction = "R"
        self.idling = False

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
        self.idling = True

    def start(self):
        self.direction = "F"
        if verbose:
            print("<player.py> " + "Player1 ready")

    def hit(self):
        pass

    def win(self):
        self.image = self.Large[0]

        if verbose:
            print("<player.py> " + "P2 WIN")

    def get_gun(self):
        self.has_gun = True
        self.has_sword = False

    def get_sword(self):
        self.has_sword = True
        self.has_gun = False

    def lose_gun(self):
        self.has_gun = False

    def lose_sword(self):
        self.has_sword = False

    def kill_weapon(self):
        self.WEAPON.kill()


class Player2(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player1
        controls. """

    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()
        active_sprite_list.add(self)
        sprite2_group.add(self)

        # -- Attributes
        self.width = 18
        self.height = 32
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        # This holds all the images for the animated walk left/right
        # of our player
        self.walking_frames_l = []
        self.walking_frames_r = []
        self.idle_walking_l = []
        self.idle_walking_r = []
        self.idle_forward_frame = []
        self.gun_frames_l = []
        self.gun_frames_r = []
        self.idle_gun_l = []
        self.idle_gun_r = []
        self.sword_frames_l = []
        self.sword_frames_r = []
        self.idle_sword_l = []
        self.idle_sword_r = []

        # For winning page
        self.Large = []
        sprite_sheet = SpriteSheet("SPRITES/Player2_Large.png")
        image = sprite_sheet.get_image(60, 96, 190, 384)
        self.Large.append(image)

        # What direction is the player facing?
        self.direction = "F"
        self.idling = True

        self.has_gun = False
        self.has_sword = False
        self.WEAPON = None

        # List of sprites we can bump against
        self.level = None
        sprite_sheet = SpriteSheet("SPRITES/Sprite2_sheet.png")

        # Load all the right facing walking images into a list
        image = sprite_sheet.get_image(54, 8, 18, 32)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(80, 8, 18, 32)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(54, 8, 18, 32)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(103, 8, 18, 32)
        self.walking_frames_r.append(image)

        image = sprite_sheet.get_image(30, 8, 18, 32)
        self.idle_walking_r.append(image)

        # Load all the right facing gun images into a list
        image = sprite_sheet.get_image(54, 88, 22, 32)
        self.gun_frames_r.append(image)
        image = sprite_sheet.get_image(80, 88, 22, 32)
        self.gun_frames_r.append(image)
        image = sprite_sheet.get_image(54, 88, 22, 32)
        self.gun_frames_r.append(image)
        image = sprite_sheet.get_image(103, 88, 22, 32)
        self.gun_frames_r.append(image)

        image = sprite_sheet.get_image(30, 88, 22, 32)
        self.idle_gun_r.append(image)

        # Load all the right facing sword images into a list
        image = sprite_sheet.get_image(54, 48, 21, 32)
        self.sword_frames_r.append(image)
        image = sprite_sheet.get_image(80, 48, 21, 32)
        self.sword_frames_r.append(image)
        image = sprite_sheet.get_image(54, 48, 21, 32)
        self.sword_frames_r.append(image)
        image = sprite_sheet.get_image(103, 48, 21, 32)
        self.sword_frames_r.append(image)

        image = sprite_sheet.get_image(30, 48, 21, 32)
        self.idle_sword_r.append(image)

        # Load all the left facing walking images, then flip them
        # to face left.
        image = sprite_sheet.get_image(54, 8, 18, 32)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(80, 8, 18, 32)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(54, 8, 18, 32)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(103, 8, 18, 32)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(30, 8, 18, 32)
        image = pygame.transform.flip(image, True, False)
        self.idle_walking_l.append(image)

        # Load all the left facing gun images, then flip them
        # to face left.
        image = sprite_sheet.get_image(54, 88, 22, 32)
        image = pygame.transform.flip(image, True, False)
        self.gun_frames_l.append(image)
        image = sprite_sheet.get_image(80, 88, 22, 32)
        image = pygame.transform.flip(image, True, False)
        self.gun_frames_l.append(image)
        image = sprite_sheet.get_image(54, 88, 22, 32)
        image = pygame.transform.flip(image, True, False)
        self.gun_frames_l.append(image)
        image = sprite_sheet.get_image(103, 88, 22, 32)
        image = pygame.transform.flip(image, True, False)
        self.gun_frames_l.append(image)

        image = sprite_sheet.get_image(30, 88, 22, 32)
        image = pygame.transform.flip(image, True, False)
        self.idle_gun_l.append(image)

        # Load all the left facing sword images, then flip them
        # to face left.
        image = sprite_sheet.get_image(54, 48, 21, 32)
        image = pygame.transform.flip(image, True, False)
        self.sword_frames_l.append(image)
        image = sprite_sheet.get_image(80, 48, 21, 32)
        image = pygame.transform.flip(image, True, False)
        self.sword_frames_l.append(image)
        image = sprite_sheet.get_image(54, 48, 21, 32)
        image = pygame.transform.flip(image, True, False)
        self.sword_frames_l.append(image)
        image = sprite_sheet.get_image(103, 48, 21, 32)
        image = pygame.transform.flip(image, True, False)
        self.sword_frames_l.append(image)

        image = sprite_sheet.get_image(30, 48, 21, 32)
        image = pygame.transform.flip(image, True, False)
        self.idle_sword_l.append(image)

        # Set the image the player starts with
        image = sprite_sheet.get_image(5, 8, 18, 32)
        self.idle_forward_frame.append(image)
        self.image = self.idle_forward_frame[0]

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

    def update(self):
        global p2_touching_weapon, p2_weapon_x, p2_weapon_y, sprite_collided, grab_p1

        """ Move the player2. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x
        pos = self.rect.x  # + self.level.world_shift
        if self.direction == "F":
            self.image = self.idle_forward_frame[0]

        if self.has_gun:
            if self.direction == "R":
                if self.idling:
                    self.image = self.idle_gun_r[0]
                else:
                    frame = (pos // 15) % len(self.gun_frames_r)
                    self.image = self.gun_frames_r[frame]
            else:
                if self.idling:
                    self.image = self.idle_gun_l[0]
                else:
                    frame = (pos // 15) % len(self.gun_frames_l)
                    self.image = self.gun_frames_l[frame]
        elif self.has_sword:
            if self.direction == "R":
                if self.idling:
                    self.image = self.idle_sword_r[0]
                else:
                    frame = (pos // 15) % len(self.sword_frames_r)
                    self.image = self.sword_frames_r[frame]
            else:
                if self.idling:
                    self.image = self.idle_sword_l[0]
                else:
                    frame = (pos // 15) % len(self.sword_frames_l)
                    self.image = self.sword_frames_l[frame]
        else:
            if self.direction == "R":
                if self.idling:
                    self.image = self.idle_walking_r[0]
                else:
                    frame = (pos // 15) % len(self.walking_frames_r)
                    self.image = self.walking_frames_r[frame]
            else:
                if self.idling:
                    self.image = self.idle_walking_l[0]
                else:
                    frame = (pos // 15) % len(self.walking_frames_l)
                    self.image = self.walking_frames_l[frame]

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
            if self.change_x > 0:
                self.rect.right = box.rect.left
            elif self.change_x < 0:
                self.rect.left = box.rect.right
        # For active weapons
        weapon_hit_list = pygame.sprite.spritecollide(self, objects.active_weapon_list, False)
        for weapon in weapon_hit_list:
            if not self.has_gun and not self.has_sword:
                if p2_touching_weapon is None:
                    p2_touching_weapon = weapon
                    self.WEAPON = weapon
            p2_weapon_x = weapon.rect.x
            p2_weapon_y = weapon.rect.y
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                weapon.rect.left = self.rect.right
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                weapon.rect.right = self.rect.left
        # For active players
        player_hit_list = pygame.sprite.spritecollide(self, sprite1_group, False)
        for player in player_hit_list:
            if self.rect.x + self.width // 2 > player.rect.x + player.width // 2:
                self.rect.x += 1
            elif self.rect.x + self.width // 2 < player.rect.x + player.width // 2:
                # Otherwise if we are moving left, do the opposite.
                self.rect.x -= 1
            sprite_collided = True

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
            if self.change_y > 0:
                self.rect.bottom = box.rect.top
            elif self.change_y < 0:
                SPAWN_WEAPON(box.rect.x, box.rect.y - 6)
                box.kill()
            self.change_y = 0
        # For weapons
        weapon_hit_list = pygame.sprite.spritecollide(self, objects.active_weapon_list, False)
        for weapon in weapon_hit_list:
            if not self.has_gun and not self.has_sword:
                if p2_touching_weapon is None:
                    p2_touching_weapon = weapon
                    self.WEAPON = weapon
            p2_weapon_x = weapon.rect.x
            p2_weapon_y = weapon.rect.y
            if verbose:
                print("<player.py> " + str(weapon))
            if self.change_y > 0:
                self.rect.bottom = weapon.rect.top
                self.change_y = 0
            elif self.change_y < 0:
                weapon.rect.bottom = self.rect.top

        if p2_touching_weapon is not None:
            if 40 < abs(abs(self.rect.x + self.width // 2) - abs(p2_weapon_x + 8)):
                p2_touching_weapon = None
                if verbose:
                    print("<player.py> " + "P2 not touching weapon")

            elif 40 < abs(abs(self.rect.y + self.height // 2) - abs(p2_weapon_y + 6)):
                p2_touching_weapon = None
                if verbose:
                    print("<player.py> " + "P2 not touching weapon")

        if sprite_collided:
            player_hit_list = pygame.sprite.spritecollide(self, sprite2_group, False)
            if len(player_hit_list) < 1:
                sprite_collided = False
                if verbose:
                    print("<player.py> " + "P2 touching P1 " + str(sprite_collided))

    def calc_grav(self):
        """ Calculate effect of gravity. """
        global p2_fell_to_death
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .95

        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.kill()
            p2_fell_to_death = True

    def jump(self):
        """ Called when user hits 'jump' button. """
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        box_hit_list = pygame.sprite.spritecollide(self, self.level.query_box_list, False)
        weapon_hit_list = pygame.sprite.spritecollide(self, objects.active_weapon_list, False)
        self.rect.y -= 2
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or len(box_hit_list) > 0 or len(weapon_hit_list) > 0:
            if not grab_p1:
                self.change_y = -12
            else:
                self.change_y = -5

    def go_left(self):
        """ Called when the user hits the left arrow. """

        self.change_x = -3
        self.direction = "L"
        self.idling = False

    def go_right(self):
        """ Called when the user hits the right arrow. """

        self.change_x = 3
        self.direction = "R"
        self.idling = False

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
        self.idling = True

    def start(self):
        self.direction = "F"

        if verbose:
            print("<player.py> " + "Player2 ready")

    def hit(self):
        pass

    def win(self):
        self.image = self.Large[0]

        if verbose:
            print("<player.py> " + "P2 WIN")

    def get_gun(self):
        self.has_gun = True
        self.has_sword = False

    def get_sword(self):
        self.has_sword = True
        self.has_gun = False

    def lose_gun(self):
        self.has_gun = False

    def lose_sword(self):
        self.has_sword = False

    def kill_weapon(self):
        self.WEAPON.kill()
