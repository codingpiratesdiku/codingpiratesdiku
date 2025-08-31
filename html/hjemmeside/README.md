# Personlig hjemmeside

Denne guide hjælper dig med at lave din egen personlige hjemmeside!

## Start

Start med at oprette en `index.html` fil. Denne fil indeholder din hjemmeside

```html
<!-- Dette er en kommentar i HTML. Denne kode gør ikke noget -->
<html>
  <head>
    <!-- I denne sektion kan du sætte icon på din hjemmeside og titel -->
  </head>
  <body>
    <!-- Her er indholdet af din hjemmeside (det du kan se) -->
    <h1>Min første hjemmeside!</h1>
  </body>
</html>
```

### Opgaver

- Tilføj et billede af din ynglingsperson
  - Brug `<img src="<sti_til_billede>">`
- Ændr titlen af din hjemmesde
  - Brug `<title>Din titel</title>` i `<head>`
- Giv noget farve til din hjemmeside

```html
<!-- Opret en fil kaldet "style.css" ved siden af "index.html" og læg denne stump kode i <head> af index.html -->
<link
  rel="stylesheet"
  href="style.css" />
```

- Put dette ind i `style.css` (eller find din ynglingsfarve)

```css
:root {
  background-color: powderblue;
}
```
