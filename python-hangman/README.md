# Lad os bygge et hangman spil i Python!
I kender garanteret hangman spillet. Det går ud på, at man skal gætte et hemmeligt ord. Man må kun gætte ét bogstav af gangen.

Lad os lave et hangman spil i Python som fungerer via kommandolinjen/terminalen! Det eneste, det kræver er Python installeret.

Hvis du blot vil se det endelige spil, så tjek filen `hangman.py` ud.

## Første skridt: hvordan viser vi en hangman?
Fra Python kender vi `print` funktionen. F.eks kan vi skrive `print("Hello world!")` og så vises `Hello world!` i terminalen. 

Ved brug af `print` kan vi printe/vise en enkelt linje. Nu skal vi blot finde en måde at vise en hel hangman struktur linje for linje. Det kan vi gøre sådan her:
```python
hangman = [
    "  _______",
    " |/      |",
    " |",  
    " |",
    " |",
    " |",  
    " |",
    "_|___"
]
for line in hangman:
    print(line)
```
Prøv at køre det kode og se hvad der sker! Vi har defineret variablen `hangman` som en liste af strings og så looper vi igennem den liste og printer hver string. Men hvorfor ikke bare bruge `print(hangman)`? Prøv det og se hvad der sker!

## Andet skridt: hvordan viser vi en hangman med fejl?
Vi skal også kunne vise en hangman med fejl. F. eks. kunne de 3 første fejl se sådan her ud:
```
Første fejl         Anden fejl         Tredje fejl
  _______           _______            _______
 |/      |          |/      |          |/      |
 |      (_)         |      (_)         |      (_)
 |                  |      \|          |      \|/
 |                  |                  |
 |                  |                  |
 |                  |                  |
_|___              _|___              _|___
```
Vi kan tilføje en fejl ved at ændre i linjerne som vi definerede ovenover i variablen `hangman`. F. eks. kan vi tilføje første fejl ved at ændre linje 2 i `hangman` listen. Vi kan tilføje fejl nummer 2 og 3 ved at ændre i linje 3 i `hangman` listen. Det vil altså sige at for at opdatere vores hangman med en fejl, så skal vi vide hvilken linje (et tal) som skal overskrives og hvad vi skal overskrive linjen med (en string/tekst).

Det kan vi definere i Python således
```python
hangman_errors = [
    (2, " |      (_)"),  # Første fejl: tilføj hoved på linje 2
    (3, " |      \|"),   # Anden fejl: tilføj en arm på linje 3
    (3, " |      \|/"),  # Tredje fejl: tilføj begge arme på linje 3
    (4, " |       |"),   # Fjerde fejl: tilføj krop på linje 4
    (5, " |      / "),   # Femte fejl: tilføj et ben på linje 5
    (5, " |      / \\"), # Sjette fejl: tilføj begge ben på linje 5
]
```
Her har vi defineret en variabel, som vi kalder `hangman_errors`, til at være en liste af tuples. Men hov, hvad er en tuple? Prøv at søg på Google! En tuple bruges til at opbevare flere forskellige ting i én variabel. I det her tilfælde er det første element den linje som vi skal overskrive og det andet element er den string/tekst som vi vil overskrive med.

Lad os lave en funktion, som kan printe en hangman alt efter hvor mange fejl man har lavet
```python
def display_hangman(hangman, hangman_errors, num_errors):
    """Dette er en funktion som printer en hangman struktur"""

    for i in range(num_errors):     # Loop igennem antallet af fejl
        idx = hangman_errors[i][0]  # For hver fejl find hvilken linje der skal ændres
        line = hangman_errors[i][1] # For hver fejl find hvad linje skal ændres til
        hangman[idx] = line         # Ændr linjen

    # Print hver linje i hangman strukturen
    for line in hangman:
        print(line)

hangman = [
    "  _______",
    " |/      |",
    " |",  
    " |",
    " |",
    " |",  
    " |",
    "_|___"
]

hangman_errors = [
    (2, " |      (_)"),  # Første fejl: tilføj hoved på linje 2
    (3, " |      \|"),   # Anden fejl: tilføj en arm på linje 3
    (3, " |      \|/"),  # Tredje fejl: tilføj begge arme på linje 3
    (4, " |       |"),   # Fjerde fejl: tilføj krop
    (5, " |      / "),   # Femte fejl: tilføj et ben
    (5, " |      / \\"), # Sjette fejl: tilføj begge ben
]
```
Hvad sker der når du kører `display_hangman(hangman, hangman_errors, 0)`? Hvad sker der når du kører `display_hangman(hangman, hangman_errors, 6)`? Prøv dig frem.


## Tredje skridt: lad os lave spil logikken
Lad os definere 4 variable
```python
word = "badeland"                   # Det hemmelige ord der skal gættes
guessed_letters = []                # En liste af gættede bogstaver (starter tom)
masked_secret = "_" * len(word)     # Den maskerede hemmelighed fx "_ _ _ _ _ _ _ _"
errors = 0                          # Antallet af fejl lavet (starter som nul)
```
Giver det mening, at vi skal bruge de 4 variable? Hvad tror du `masked_secret` er? Prøv at udforsk ved at ændre `word` og køre `print(masked_secret)`.

Nu kan vi lave hoved-loopet i spillet. Altså der hvor selve spil-logikken foregår.
```python
while not set(word).issubset(guessed_letters):

    display_hangman(hangman, hangman_errors, errors) # Vis hangman

    print(masked_secret) # Vis det maskerede ord

    print("Du har gættet på: ", guessed_letters)

    # Tjek om spilleren har tabt
    if errors >= len(hangman_errors):
        print("Du har tabt!")
        exit()
    
    # Få et gæt fra spilleren
    guess = input("Gæt et bogstav: ")
    guessed_letters.append(guess)

    # Opdater det maskerede ord
    masked_secret = ""
    for letter in word:
        if letter in guessed_letters:
            masked_secret = masked_secret + letter
        else:
            masked_secret = masked_secret + "_"

    # Tjek om der blev lavet en fejl
    if not guess in word:
        errors = errors + 1

# Hvis vi når hertil, så har spilleren vundet!
display_hangman(hangman, hangman_errors, errors)
print(word)
print("Tillykke du har vundet!")
```

Wow, det var meget kode! Hvad sker der dog her. Prøv at kør koden (husk at kopiere alt det ovenstående kode inklusiv de andre afsnit). Virker det? Kan du forklare hvad koden gør?

Lad os prøve at bryde det ned i mindre bidder. 

Den her linje
```python
while not set(word).issubset(guessed_letters):
```
beskriver et `while` loop. Et `while` loop fortsætter så længe at dens `condition` er sand. I det her tilfælde er dens condition `not set(word).issubset(guessed_letters)`. Det betyder: fortsæt så længe at alle bogstaverne i det hemmelig or (variablen `word`) ikke eksisterer i de gættede ord (variablen `guessed_letters`). Hvad sker der f. eks. hvis du kører `set("hej").issubset(['h', 'x', 'y', 'z', 'e', 'r', 'j'])`?

De her linjer
```python
# Få et gæt fra spilleren
guess = input("Gæt et bogstav: ")
guessed_letters.append(guess)
```
modtager et bogstav fra brugeren til variablen `guess` og tilføjer det til listen over alle de gættede bogstaver, `guessed_letters`.

De her linjer
```python
# Opdater det maskerede ord
masked_secret = ""
for letter in word:
    if letter in guessed_letters:
        masked_secret = masked_secret + letter
    else:
        masked_secret = masked_secret + "_"
```
går igennem alle bogstaverne i det hemmelige ord, `word`, og tjekker om bogstavet eksisterer i `guessed_letters`. Hvis det gør, så tilføjer vi bogstavet til det maskerede ord. Hvis ikke, så tilføjer vi bare underscore, `_`. På den måde viser vi kun de bogstaver, som er blevet gættet.

Giver det mening? Spørg en frivillig om resten af koden!

## Videre udvikling
- Prøv at udvid hangman med et andet design eller flere fejl
- Tilføj så man kan gætte et helt ord
- Lav en bedre vinder-besked til sidst
- Gør så man ikke mister liv ved at gætte på et bogstav man allerede har gættet på
- Måske kan man tilføje farver til spillet?

## Tips
- Prøv at tilføj `print("\033[H\033[J", end="")` i starten af loopet. Det "clearer" hele skærmen.
- Hvis du skriver `python` i din terminal/kommandolinje, så kan du teste enkelt python kommandoer.
- Spørg en frivillig!
