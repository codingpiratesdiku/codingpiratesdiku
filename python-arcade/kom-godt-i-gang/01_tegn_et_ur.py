#!/usr/bin/env python3

# Importér arcade:
import arcade

# Lav et vindue:
arcade.open_window(800, 600, "Tegn en enkelt linje")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

# Tegn cirklen
x_midte = 400
y_midte = 300
radius = 200
farve = arcade.color.BLACK
tykkelse = 5
arcade.draw_circle_outline(x_midte, y_midte, radius, farve, tykkelse)

# Tegn den store minutviser
vinkel = 180
længde = 0.9
## Tegn linjen:
(x2, y2) = arcade.rotate_point(x_midte, y_midte - radius * længde, x_midte, y_midte, vinkel)
arcade.draw_line(x_midte, y_midte, x2, y2, farve, tykkelse)

# Tegn den lille timeviser
vinkel = 60
længde = 0.6
## Tegn linjen:
(x2, y2) = arcade.rotate_point(x_midte, y_midte - radius * længde, x_midte, y_midte, vinkel)
arcade.draw_line(x_midte, y_midte, x2, y2, farve, tykkelse - 1)

# Bliv ved med at holde vinduet åbent indtil du lukker det:
arcade.finish_render()
arcade.run()
