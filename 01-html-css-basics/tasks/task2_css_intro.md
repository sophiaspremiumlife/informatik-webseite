# Task 2: Einführung in CSS

## Ziel  
Verstehen, was CSS ist, wie es eingebunden wird und wie man erste einfache Styles auf HTML-Elemente anwendet.

---

## Theorie

CSS (Cascading Style Sheets) wird verwendet, um das **Aussehen** von HTML-Inhalten zu gestalten. Es gibt drei Möglichkeiten, CSS einzubinden:

### 1. Inline-Styles (nicht empfohlen)

```html
<p style="color: red;">Das ist ein roter Text.</p>
```

> Diese Variante wird **nicht empfohlen**, da sie unübersichtlich ist und sich schlecht warten lässt.

### 2. Interner Stilblock mit `<style>` (für Experimente geeignet)

```html
<head>
    <style>
        p {
            color: red;
        }
    </style>
</head>
```

### 3. Externe CSS-Datei (empfohlen)

```html
<!-- index.html -->
<head>
    <link rel="stylesheet" href="styles.css">
</head>
```

```css
/* styles.css */
p {
    color: red;
}
```

---

## Wichtige Grundbegriffe

Ein CSS-Stil besteht aus:

- einem **Selektor**, der angibt, **welches HTML-Element** angesprochen wird
- einer oder mehreren **Eigenschaft-Wert-Zuweisungen**

Beispiel:
```css
h1 {
    color: blue;
    font-size: 2em;
}
```

---

## Aufgaben

### Aufgabe 1: CSS mit `<style>`-Tag anwenden
- Fügen Sie Ihrer bestehenden HTML-Seite im `<head>` einen `<style>`-Block hinzu.
- Gestalten Sie Überschriften (`<h1>`) mit einer anderen Farbe und grösserer Schriftgrösse.
- Geben Sie Absätzen (`<p>`) eine graue Schriftfarbe und einen grösseren Zeilenabstand mit `line-height`.

### Aufgabe 2: Externes Stylesheet einbinden
- Erstellen Sie eine neue Datei mit dem Namen `styles.css`.
- Verlinken Sie diese im `<head>` Ihrer HTML-Datei mit `<link>`.
- Übertragen Sie die CSS-Regeln aus Ihrem `<style>`-Block in die neue Datei.

### Aufgabe 3: Hintergrund und Schriftgestaltung
- Verändern Sie den Hintergrund der Seite mit der Eigenschaft `background-color`.
- Wählen Sie eine andere Schriftart (z. B. `Arial, sans-serif`) mit der Eigenschaft `font-family`.

---

## Freiwillige Zusatzaufgabe

- Binden Sie eine Schriftart von [Google Fonts](https://fonts.google.com/) ein.
- Gestalten Sie den `<header>` Ihrer Seite mit einer Hintergrundfarbe, einem Innenabstand (`padding`) und weisser Schriftfarbe.

---

## Hinweise

- Verwenden Sie einfache Farben (z. B. `lightgray`, `black`, `white`, `navy`) oder hexadezimale Farbcodes (z. B. `#333333`).
- Öffnen Sie die Datei in einem Browser und beobachten Sie die Veränderungen.
- Achten Sie auf eine übersichtliche Struktur in Ihrer `styles.css`.

---

## Weitere Ressourcen

- [MDN Web Docs: CSS-Grundlagen](https://developer.mozilla.org/de/docs/Learn/CSS/First_steps/What_is_CSS)
- [W3Schools: CSS Introduction](https://www.w3schools.com/css/css_intro.asp)
- [Google Fonts](https://fonts.google.com/)

---

Möchten Sie dieses Markdown direkt als Datei speichern oder in ein bestimmtes Repo einfügen lassen?
