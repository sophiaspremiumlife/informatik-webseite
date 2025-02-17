# Task 3: Navigation mit Flexbox erstellen

## Ziel
Verstehen Sie das Konzept von **CSS Flexbox** durch ein interaktives Lernspiel.
Erstellen Sie eine Navigationsleiste mit HTML und gestalten Sie diese mit **CSS Flexbox**.

## Anforderungen
- Spielen Sie das kostenlose Lernspiel **[Flexbox Zombies](https://mastery.games/flexboxzombies/)**.
- Arbeiten Sie mindestens **bis Level 10**, um die Grundlagen von Flexbox zu verstehen.
- Notieren Sie sich wichtige Konzepte für später.
- Fügen Sie in den `<header>` eine **Navigation** (`<nav>`) mit einer Liste (`<ul>`) hinzu.
- Erstellen Sie darin mindestens drei Links (`<a>`), z. B. für „Start“, „Projekte“ und „Kontakt“.
- Nutzen Sie **CSS Flexbox**, um die Navigation horizontal auszurichten.
- Verwenden Sie den Artikel zu [CSS Flexbox](https://developer.mozilla.org/de/docs/Web/CSS/CSS_Flexible_Box_Layout) als Referenz.

## Hinweise
- Denken Sie an eine **semantische Struktur**: Warum wird `<nav>` verwendet?
- Testen Sie die Navigation im Browser, um die Darstellung zu überprüfen.
- Falls die Links untereinander erscheinen, prüfen Sie, ob `display: flex;` korrekt gesetzt ist.
- Verwenden Sie `justify-content: center;`, um die Links mittig auszurichten.

# Task 2: Navigation mit Flexbox erstellen

## Beispiel 

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
nav {
    display: flex;
    justify-content: center;
}
```

## Anforderungen

