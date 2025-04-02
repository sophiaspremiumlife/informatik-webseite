# Task 3: Navigation mit Flexbox erstellen

## Ziel  
Sie erstellen eine horizontale Navigationsleiste mit HTML und gestalten diese mithilfe von **CSS Flexbox**. Dabei lernen Sie, wie sich Webseitenlayouts flexibel und responsiv gestalten lassen.

---

## Theorieteil: Was bedeutet „Layout“?

Eine Webseite besteht meist aus mehreren **visuell getrennten Bereichen**. Typische Layout-Elemente sind:

- ein **Kopfbereich** (`<header>`)
- ein **Navigationsbereich** (`<nav>`)
- ein **Hauptbereich** mit Inhalt (`<main>`)
- eine **Seitenleiste** (`<aside>`)
- ein **Fussbereich** (`<footer>`)

Früher wurden solche Layouts oft mit Tabellen oder sogenannten „Float“-Techniken umgesetzt – diese Methoden sind jedoch veraltet oder kompliziert. **CSS Flexbox** ist eine moderne Lösung, um Elemente auf einfache Weise **horizontal oder vertikal** anzuordnen – auch auf verschiedenen Bildschirmgrössen.

---

## Vorbereitung: Flexbox kennenlernen

- Spielen Sie das interaktive Lernspiel **[Flexbox Zombies](https://mastery.games/flexboxzombies/)**.
- Bearbeiten Sie mindestens **bis Level 10**, um die wichtigsten Eigenschaften zu verstehen:
  - `display: flex`
  - `justify-content`
  - `align-items`
  - `flex-direction`

> Weitere Informationen finden Sie im [MDN-Artikel zu Flexbox](https://developer.mozilla.org/de/docs/Web/CSS/CSS_Flexible_Box_Layout)

---

## Anforderungen

1. Ergänzen Sie den `<header>` Ihrer HTML-Seite um ein `<nav>`-Element mit einer ungeordneten Liste (`<ul>`) von mindestens drei Links:
   - Start
   - Projekte
   - Kontakt
2. Verwenden Sie **CSS Flexbox**, um die Links horizontal anzuordnen.
3. Zentrieren Sie die Navigation innerhalb des Headers (`justify-content: center`).

---

## Hinweise

- Verwenden Sie eine **externe CSS-Datei** für Ihre Gestaltung.
- Achten Sie auf die semantische Korrektheit Ihrer HTML-Struktur.
- Sollte die Navigation nicht wie gewünscht angezeigt werden, überprüfen Sie:
  - Ob `display: flex` korrekt gesetzt ist
  - Ob Sie `ul` und `li` angepasst haben (z. B. `list-style: none;`, `padding: 0`)

---

## Beispiel HTML

```html
<header>
    <nav>
        <ul>
            <li><a href="#">Start</a></li>
            <li><a href="#">Projekte</a></li>
            <li><a href="#">Kontakt</a></li>
        </ul>
    </nav>
</header>
```

## Beispiel CSS

```css
nav ul {
    display: flex;
    /* noch mehr styles */
    list-style: none;
    padding: 0;
}

nav li {
    margin: 0 1rem;
}
```


