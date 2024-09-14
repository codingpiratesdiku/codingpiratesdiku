#!/usr/bin/env python3

# Importér arcade:
import arcade

# Lav en Python-klasse
class Animation(arcade.Window):
    def __init__(self):
        # Lav et vindue.
        super().__init__(800, 600, "Lav en animation")
        # Sæt baggrundsfarven.
        arcade.set_background_color(arcade.csscolor.WHITE)

    def setup(self):
        # Sæt starttid til 0.
        self.t = 0

    def on_update(self, delta_time):
        # Opdater tiden med den tid der er gået siden sidste billede.
        self.t += delta_time

    def on_draw(self):
        # Tegn en tom skærm.
        self.clear()
        # Tegn en linje der bliver længere.
        arcade.draw_line(0, 300, self.t * 20, 300, arcade.color.BLUE, 5)
        # Tegn en cirkel der bliver større.
        arcade.draw_circle_outline(400, 300, self.t * 10, arcade.color.RED, 5)

# Start og kør.
window = Animation()
window.setup()
arcade.run()
