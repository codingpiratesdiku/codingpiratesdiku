# Lad os skjule tekst i billeder

I det her projekt vil vi prøve at skjule tekst i billeder, men man kan ikke se
det med det blotte øje. Emnet hedder steganografi ([læs mere her på
Wikipedia](https://da.wikipedia.org/wiki/Steganografi)) og det drejer sig om at
skjule beskeder.

F. eks. er der en hemmelig besked inkluderet i det her billede, men det kan ikke
ses med det blotte øje. Det er din opgave at dekryptere beskeden!

![secret](img/nothing_to_see_here.png)

## Hvordan kan man skjule tekst i billede uden man kan se det?

### Først skal vi forstå hvordan computeren håndterer billeder.

Computere håndterer billeder ved hjælp af en samling af små farvede punkter, som
kaldes pixels. Hver pixel har en bestemt farve, som er angivet ved hjælp af en
kombination af tre farver, som kaldes rød, grøn og blå (RGB).

Hver pixel i et RGB-billede har en numerisk værdi for rød, grøn og blå
farvekanaler, hvor hvert tal repræsenterer intensiteten af den pågældende farve
i pixelen. For eksempel kan en pixel have værdierne (255, 0, 0), som betyder, at
pixelen er helt rød, eller (0, 255, 0), som betyder, at pixelen er helt grøn.

Det vil sige, at et billede på fire pixels kan beskrives sådan her

```
[
    (255, 0, 0), (0, 0, 255),
    (0, 0, 255), (255, 0, 0)
]
```

Det vil resultere i et billede der ser sådan her ud:

![redblue](img/redblue.png)

### Vi kan bruge pixel RGB værdier til at kryptere en besked
