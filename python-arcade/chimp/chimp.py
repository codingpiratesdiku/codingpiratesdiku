import arcade
import pathlib

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 480
BG_COLOR_RGB = (170, 238, 187)
SCREEN_TITLE = 'Monkey Fever'
MOTIVATING_TEXT = 'Pummel The Chimp, And Win $$$'
CHIMP_SPEED = 20
CHIMP_SCALE = 4
LINE_HEIGHT = 45
FONT_SIZE = 30
FIST_PUNCH_X = 15
FIST_PUNCH_Y = 25


def resource_path(fname):
    """Helper to load resources (images, sounds) from this files directory"""
    this_dir = pathlib.Path(__file__).parent.resolve()
    return this_dir / 'data' / fname


class Chimp(arcade.Sprite):
    """Custom sprite for representing the punchable chimp"""
    def __init__(self):
        super().__init__()

        # Set the default position, direction and size of the chimp sprite
        self.position = (150, 200)
        self.change_x = CHIMP_SPEED
        self.scale = CHIMP_SCALE

        # The chimp can face either left or right so use different
        # textures for that
        self.right_texture = arcade.load_texture(resource_path('chimp.png'))
        self.left_texture = arcade.load_texture(resource_path('chimp.png'),
                                                flipped_horizontally=True)
        self.texture = self.right_texture

        # This chimp has not been hit yet so is not dizzy
        self.dizzy = False

    def update(self):
        """Called when the game needs to update so update the chimp state"""
        if self.dizzy:
            # If the chimp has been hit and is dizzy update its rotation
            self.angle += 10
            # If it has rotated one complete circle stop it from rotating again
            if self.angle == 360:
                self.angle = 0
                self.dizzy = False
        else:
            # Move the chimp normally
            self.center_x += self.change_x

            # Has the chimp reaced the right edge of the screen?
            if self.right >= SCREEN_WIDTH:
                # Make the chimp move left on each update
                self.change_x *= -1
                # And make the chimp image face left
                self.texture = self.left_texture
            # Has the chimp reaced the left edge of the screen?
            elif self.left <= 0:
                # Make the chimp move right on each update
                self.change_x *= -1
                # And make the chimp image face right
                self.texture = self.right_texture

    def punched(self):
        """Called when the chimp has been hit"""
        # The chimp is now dizzy
        self.dizzy = True


class ChimpGame(arcade.Window):
    """Main game class. Manages all of the game elements (sprites, sounds...)"""
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(BG_COLOR_RGB)
        # Hide the deafult mouse cursor. The fist will move with the
        # mouse instead
        self.set_mouse_visible(False)

        # Initialize our sprites
        self.chimp = Chimp()
        self.fist = arcade.Sprite(resource_path('fist.png'))

        # Load our sounds
        self.whiff_sound = arcade.Sound(resource_path('whiff.wav'))
        self.punch_sound = arcade.Sound(resource_path('punch.wav'))

    def draw_title(self):
        """Draw the motivating text"""
        start_x = 0
        start_y = SCREEN_HEIGHT - LINE_HEIGHT
        arcade.draw_text(MOTIVATING_TEXT,
                         start_x,
                         start_y,
                         arcade.color.BLACK,
                         FONT_SIZE,
                         width=SCREEN_WIDTH,
                         align='center',
                         bold=True)

    def on_update(self, delta_time):
        """Called when the game needs to update"""
        # Currently only the chimp sprite needs to update
        self.chimp.update()

    def on_draw(self):
        """Called when the screen needs to be redrawn"""
        # Clear all screen contents to get rid of old sprites etc.
        self.clear()
        # Draw our motivating text and sprites
        self.draw_title()
        self.chimp.draw()
        self.fist.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        """Called when the mouse has been moved"""
        # Move the fist to the position of the mouse
        self.fist.position = (x, y)

    def on_mouse_press(self, x, y, button, modifiers):
        """Called when the mouse has been clicked"""
        # Move the fist a bit to give a punching effect
        self.fist.center_x += FIST_PUNCH_X
        self.fist.center_y += FIST_PUNCH_Y
        # Did the fist collide with the monkey when the mouse was pressed?
        if arcade.check_for_collision(self.fist, self.chimp):
            # If so play then punching sound
            self.punch_sound.play()
            # And let the chimp know it was hit
            self.chimp.punched()
        else:
            # Chimp missed. Play missed sound
            self.whiff_sound.play()

    def on_mouse_release(self, x, y, button, modifiers):
        """Called when the mouse button has been released"""
        # Move the fist back to its original position
        self.fist.center_x -= FIST_PUNCH_X
        self.fist.center_y -= FIST_PUNCH_Y


def main():
    """The game entry point"""
    # Create our main game class
    ChimpGame()
    # Run the game until the window is closed
    arcade.run()


# This calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()
