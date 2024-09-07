#!/usr/bin/env python3

# Importér arcade:
import arcade

# Lav et vindue:
arcade.open_window(800, 600, "Tegn en enkelt linje")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

# Vælg en farve fra farverne her: https://api.arcade.academy/en/latest/arcade.color.html
farve = arcade.color.BLACK
# Vælg en tykkelse:
tykkelse = 5
# Vælg hvor linjen skal starte:
x1 = 100
y1 = 100
# Vælg hvor linjen skal slutte:
x2 = 500
y2 = 300

# Tegn linjen:
arcade.draw_line(x1, y1, x2, y2, farve, tykkelse)

# Bliv ved med at holde vinduet åbent indtil du lukker det:
arcade.finish_render()
arcade.run()
