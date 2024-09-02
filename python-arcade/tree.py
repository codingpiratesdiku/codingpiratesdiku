#!/usr/bin/env python3

# Se https://api.arcade.academy/en/latest/install/index.html for hjælp til installation.
import arcade
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Tree"

class Tree(arcade.Window):
    def __init__(self):
        # Lav et vindue.
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        # Sæt baggrundsfarven.
        arcade.set_background_color(arcade.csscolor.WHITE)

    def setup(self):
        self.n = 3

    def on_key_press(self, key, modifiers):
        pass

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.n += 1
        if key == arcade.key.DOWN:
            self.n -= 1

    def on_update(self, delta_time):
        pass

    def draw_tree(self, n, d, height, x, y):
        if n == 0:
            return
        n1 = n - 1
        height1 = height - 10
        x0 = x
        y0 = y + height
        for degree in [d - 25, d + 25]:
            (x1, y1) = arcade.rotate_point(x0, y0, x, y, degree)
            arcade.draw_line(x, y, x1, y1, arcade.color.BROWN, 3)
            self.draw_tree(n1, degree, height1, x1, y1)

    def on_draw(self):
        # Tegn en tom skærm.
        self.clear()
        # Tegn roden.
        arcade.draw_line(500, 0, 500, 100, arcade.color.BROWN, 3)
        # Tegn træet.
        self.draw_tree(self.n, 0, 100, 500, 100)

# Start og kør.
window = Tree()
window.setup()
arcade.run()
