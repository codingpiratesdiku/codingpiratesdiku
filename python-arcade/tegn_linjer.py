#!/usr/bin/env python3

# Importér arcade
import arcade

# Lav et vindue
arcade.open_window(800, 600, "Tegn linjer")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

# Tegn i vinduet
for i in range(100):
    arcade.draw_line(i * 8, i ** 1.1, (i + 1) * 8, (i + 1) ** 1.4, arcade.color.BLACK, 3)
arcade.draw_text("Hej kodepirat!", 123, 405, arcade.color.GREEN, 36)

# Bliv ved med at holde vinduet åbent indtil du lukker det
arcade.finish_render()
arcade.run()
