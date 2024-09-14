#!/usr/bin/env python3

# Importér arcade:
import arcade

FIRKANT_STØRRELSE = 50

# Lav en Python-klasse
class Animation(arcade.Window):
    def __init__(self):
        # Lav et vindue.
        super().__init__(1600, 800, "Bevæg og animér en firkant")
        # Sæt baggrundsfarven.
        arcade.set_background_color(arcade.csscolor.BLACK)

    def setup(self):
        # Sæt starttid til 0.
        self.t = 0
        # Sæt firkantents startposition.
        self.x = 400
        self.y = 300
        # Sæt firkantens startretning (ingen).
        self.x_bevægelse = 0
        self.y_bevægelse = 0
        # Sæt firkantens startrotation (ingen).
        self.rotation = 0

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.y_bevægelse = 1
        if key == arcade.key.DOWN:
            self.y_bevægelse = -1
        if key == arcade.key.LEFT:
            self.x_bevægelse = -1
        if key == arcade.key.RIGHT:
            self.x_bevægelse = 1

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.y_bevægelse = 0
        if key == arcade.key.DOWN:
            self.y_bevægelse = 0
        if key == arcade.key.LEFT:
            self.x_bevægelse = 0
        if key == arcade.key.RIGHT:
            self.x_bevægelse = 0

    def on_update(self, delta_time):
        # Opdater tiden med den tid der er gået siden sidste billede.
        self.t += delta_time
        # Opdater position baseret på bevægelse.
        bevægelse_per_delta = delta_time * 100
        self.x += self.x_bevægelse * bevægelse_per_delta
        self.y += self.y_bevægelse * bevægelse_per_delta
        # Opdater rotation.
        self.rotation += self.x_bevægelse + self.y_bevægelse

        # FORSLAG TIL UDVIDELSE:
        #
        #   1. Gør firkanten hurtigere jo længere den bliver bevæget rundt (acceleration).
        #   2. Gør firkanten større jo længere den bliver bevæget rundt.

    def on_draw(self):
        # Tegn en tom skærm.
        self.clear()
        # Tegn en firkant.
        arcade.draw_rectangle_filled(
            self.x, self.y,
            FIRKANT_STØRRELSE, FIRKANT_STØRRELSE,
            arcade.color.WHITE, self.rotation)

# Start og kør.
window = Animation()
window.setup()
arcade.run()
