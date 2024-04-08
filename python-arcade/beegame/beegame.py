#!/usr/bin/env python3

# Se https://api.arcade.academy/en/latest/install/index.html for hjælp til installation.
import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Bee game"

PLAYER_SCALING = 1  # Spilleren er normal størrelse.
PLAYER_MOVEMENT_SPEED = 5

BEE_SCALING = 2  # Bien er dobbelt størrelse.
BEE_MOVEMENT_SPEED = 3

TILE_SCALING = 0.5  # Græs og kasser er halv størrelse.


class BeeGame(arcade.Window):
    def __init__(self):
        # Lav et vindue.
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        # Sæt baggrundsfarven.
        arcade.set_background_color(arcade.csscolor.OLIVE)

    def setup(self):
        # Hold styr på scoren.
        self.score = 0

        # Understøt tekst.
        self.gui_camera = arcade.Camera(self.width, self.height)

        # Lav græsset.
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        for x in range(0, 1250, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

        # Lav kasser.
        crates_coordinates = [[64 - 32, 96], [64 * 15 + 40 - 32, 96]]
        for coordinate in crates_coordinates:
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", TILE_SCALING)
            wall.position = coordinate
            self.wall_list.append(wall)

        # Lav spilleren.
        image_source = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
        self.player_sprite = arcade.Sprite(image_source, PLAYER_SCALING)
        self.player_sprite.center_x = 64 * 3
        self.player_sprite.center_y = 64 * 2
        self.player_physics = arcade.PhysicsEngineSimple(self.player_sprite, walls=self.wall_list)

        # Lav bien.
        self.bee_sprite = arcade.Sprite(':resources:images/enemies/bee.png', BEE_SCALING)
        self.all_bee_sprites = arcade.SpriteList()
        self.all_bee_sprites.append(self.bee_sprite)
        self.bee_sprite.center_x = 64 * 6
        self.bee_sprite.center_y = 64 * 8
        self.bee_physics = arcade.PhysicsEnginePlatformer(
            self.bee_sprite, gravity_constant=1, walls=self.wall_list)

    def on_key_press(self, key, modifiers):
        # Tryk på en tast.
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        # Giv slip på en tast.
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        # Reagér på tyngdekraft og change_x.
        self.player_physics.update()
        self.bee_physics.update()

        # Undersøg om bien rører græsset.
        if self.bee_physics.can_jump():
            # Træk et point fra din score hvis en bi rammer dig.
            for bee in arcade.check_for_collision_with_list(self.player_sprite, self.all_bee_sprites):
                self.score -= 1

            # Få bien til at bevæge sig hen imod din retning.
            if self.bee_sprite.center_x > self.player_sprite.center_x:
                self.bee_sprite.change_x = -BEE_MOVEMENT_SPEED
            else:
                self.bee_sprite.change_x = BEE_MOVEMENT_SPEED

            # Lad bien hoppe op igen.
            self.bee_sprite.change_y = 64 * 0.5

    def on_draw(self):
        # Tegn en tom skærm.
        self.clear()
        # Tegn græsset og kasserne.
        self.wall_list.draw()
        # Tegn spilleren.
        self.player_sprite.draw()
        # Tegn bien.
        self.bee_sprite.draw()
        # Tegn score-teksten.
        self.gui_camera.use()
        arcade.draw_text(f'Score: {self.score}', 10, 10, arcade.csscolor.WHITE, 28)


# Start og kør spillet.
window = BeeGame()
window.setup()
arcade.run()
