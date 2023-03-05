# Dette er en måde hvorpå man kan bruge farver i terminalen (se README)
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


def display_words(words):
    """Dette er en funktion til at printe alle ord i en liste på nye linjer."""

    for word in words: # Loop igennem alle ord i listen `words``
        print(word)    # Print ordet på en ny linje

    print() # Tilføj en tom linje
    print() # Tilføj en tom linje


# Definer det hemmelige ord
word = "zebra"

# Man har 6 gæt
num_guesses = 6

# Lav en liste af maskererede ord på samme længde som det hemmelige ord
masked_words = ["_" * len(word) for i in range(num_guesses)]

# Variabel som er True/False for at indikere om man har vundet - starter som False
won = False

# Ryd skærmen til at starte med og print de maskerede ord
print("\033[H\033[J", end="")
display_words(masked_words)

# Loop igennem antallet af gæt (som er 6 i den originale wordle)
for num in range(num_guesses):

    guess = input("Enter word: ")
    while len(guess) != len(word):
        guess = input("Forkert længde. Enter word: ")

    # Ryd skærmen
    print("\033[H\033[J", end="")

    # Hvis gættet er korrekt, så sæt variablen, `won`, til True
    if guess == word:
        won = True

    # Loop igennem gættet og farv bogstaverne
    colored_guess = ""
    for i, letter in enumerate(guess):
        if word[i] == letter: # Farv grønt hvis bogstavet er på samme plads/index i det hemmelige ord
            colored_guess += color.GREEN + letter + color.END
        elif letter in word: # Ellers farv gult hvis bogstavet er i det hemmelige ord
            colored_guess += color.YELLOW + letter + color.END
        else: # Ellers lad være med at farve
            colored_guess += letter

    # Opdater de maskerede ord
    masked_words[num] = colored_guess

    # Hvis de maskerede ord
    display_words(masked_words)

    # Hvis man har ramt korrekt, så hop ud af loopet
    if won:
        break

# Check om spilleren har vundet eller tabt
if won:
    print("Congratulations!")
else:
    print("ØV, you lost! The word was", word)
