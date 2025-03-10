#!/usr/bin/env python3

# Importér arcade
import arcade

# Hvor hurtig tekst skal bevæge sig
tekst_hastighed = 200

# Lav et vindue
class AnimationWindow(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Animation")
        # Lav en variabel til hvor på x-aksen teksten skal skrives
        self.text_x = 100
        # Lav en variabel til om x skal blive større eller mindre
        self.text_x_factor = +1

    def on_update(self, delta_time: float):
        # Gør x større eller mindre afhængig af om self.text_x_factor er -1 eller +1.
        self.text_x += self.text_x_factor * delta_time * tekst_hastighed

        # Ændr retning hvis self.text_x er lig med eller over 400
        if self.text_x >= 400:
            self.text_x_factor = -1
        # eller hvis self.text_x er lig med eller mindre end 100
        if self.text_x <= 100:
            self.text_x_factor = +1
        # Disse to if'er vil få teksten til at bevæge sig frem og tilbage.

    def on_draw(self):
        # Fjern alt hvad der blev tegnet sidste gang on_draw blev kaldt
        self.clear()
        # Sæt baggrundsfarven
        arcade.set_background_color(arcade.color.WHITE)
        # Skriv noget tekst til skærmen hvor vi bruger variablen self.text_x
        arcade.draw_text("Hej kodepirat!", self.text_x, 405, arcade.color.GREEN, 36)

if __name__ == '__main__':
    AnimationWindow().run()
