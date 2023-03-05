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


word = "badeland"
guessed_letters = []
masked_secret = "_" * len(word)
errors = 0

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
