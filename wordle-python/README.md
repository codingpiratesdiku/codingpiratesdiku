# Lad os bygge wordle i Python
Kender du spillet wordle? Det blev vildt populært i 2022 da New York Times lancerede det på deres hjemmeside. Du kan prøve spillet [her](https://www.nytimes.com/games/wordle/index.html). Der er også en [dansk version her](https://wørdle.dk).

Det går ud på at gætte et ord på 5 bogstaver. Man har 5 forsøg og får nogle hints undervejs. Det er nok nemmere bare at spille det for at forstå det - prøv det via ovenstående link!

I python filen `wordle.py` er der en simple tekst-baseret udgave. Din opgave er at udvide og gøre spillet sjovere!

## Ideer til udvidelse

### Tilfældige ord
Lige nu vælger man selv et ord og det behøver i princippet ikke være et rigtigt ord. I stedet kunne man lave en funktion som generer et tilfældigt ord fra en liste over rigtige ord. F. eks. også sådan så man ikke kan gætte på et ord, som ikke eksisterer.

[Her er en liste over danske ord på 5 bogstaver](https://github.com/mollerhoj/wordle/blob/main/data/kilder/retskriv.txt).

### Federe design
Man kunne opdatere designet med større skrift, federe farver og emojis! Man kunne også prøve at lave spillet i PyGame hvor man kan lave animationer. 

### Wordle AI
Man kunne lave et program som kan løse en wordle på den smarteste måde. F. eks. ved at gætte på de mest sandsynlige ord først og derefter søge igennem alle ord der passer. [Check evt denne video](https://www.youtube.com/watch?v=v68zYyaEmEA).


## Men hvordan virker det?
Prøv at gå igennem koden og læs kommentarerne. Når du støder på noget kode, som du ikke helt forstår, så spørg en frivillig!

Der er dog noget kode, som forklarer lidt ekstra forklaring:

### Hvordan kan vi farve tekst i terminalen?
Vi bruger dette kode:
```python
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
```
Det ser måske lidt mystisk ud, men det er en måde at kontrollere farver på ved brug af noget der hedder "ASCII escape sequences". Efter vi har defineret det ovenstående, så kan vi for eksempel skriv `print(color.PURPLE + 'Hello, World!' + color.END)`. Hvad sker der når du kører det? Hvordan kan vi printe noget tekst med farven blå eller med fed skrift?


### Hvordan ryder vi skærmen?
Flere steder skriver vi `print("\033[H\033[J", end="")` og det gør at hele terminal konsollen bliver rydet og teksten starter fra øverste venstre hjørne. Jeg er ikke selv helt sikker på hvordan det fungerer, men det er også ved brug af "ASCII escape sequences". Koden er [hapset herfra](https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console) (hvor du også kan læse mere om det hvis du er interreseret).
