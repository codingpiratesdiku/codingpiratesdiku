# Python med arcade-biblioteket

## Installation

Vi skal installere Python, som er et *programmeringssprog*, og arcade, som er et *bibliotek* til Python som gør at man kan tegne grafik.

For at kode Python med arcade skal vi også installere Visual Studio Code, som vi bruger til at skrive Python-kode.

### 1. Installér Visual Studio Code

Download <https://code.visualstudio.com/>.

(Hvis du allerede er vant til at skrive kode i noget andet end Visual Studio Code, behøver du ikke at hente det.)


### 2. Installér Python **version 3.11**

Dette er ikke den helt nyeste version, men det er vigtigt for at arcade kan virke.

- Windows: https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe
- macOS: https://www.python.org/ftp/python/3.11.9/python-3.11.9-macos11.pkg
- Ubuntu: Her kan det godt være at den nyeste udgave (Python 3.12) er okay, så prøv den: `sudo apt install python3-full`

**Vigtigt (muligvis Windows-specifikt):** Når du installerer Python, skal du klikke i checkboxen "Add python.exe to PATH" nederst i vinduet.  Hvis du har glemt dette, kan du køre installeren igen, klikke "Modify", klikke "Next" og så klikke i checkboxen "Add Python to environment variables", og så færdiggøre installationen. 
Det kan også være nødvendigt at sørge for at Windows tillader dig at køre denne version af python. Åben startmenuen og skriv "Administrer appens kørselsaliasser" og klik. Sørg for at "python.exe" og "python3.exe" er slået fra.  


### 3. Installér arcade

Åbn Visual Studio Code, åbn en ny terminal deri, og kør `pip install arcade`.

Hvis dette fejler, kan du prøve at køre `pip --version`. Hvis denne siger noget med Python 3.12, er det fordi at du (også) har Python 3.12 liggende.  Prøv så i stedet at kører `pip3.11 install arcade`, hvilket eksplicit vil bruge Python 3.11, som vi ved virker til arcade.


## Få vist noget på skærmen

Nu skal du se om Python virker ved at prøve at skrive noget Python-kode for at tegne lidt på din skærm.

Lav en ny fil i Visual Studio Code og indsæt al denne kode:

```python
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
```

Det skal gerne se sådan her ud hvis det virker:

![](tegn_linjer.png)

Prøv at ændre nogle af tallene og se hvad der sker.  Det er ikke så vigtigt hvad de gør, bare prøv at ændre det billede du får.


## Flere guides

- Tegn træer: https://api.arcade.academy/en/latest/examples/drawing_with_loops.html#drawing-with-loops
- Følg Platformer-tutorial (engelsk): https://api.arcade.academy/en/latest/examples/platform_tutorial/index.html
- Se indbyggede resourcer: https://api.arcade.academy/en/latest/resources.html
