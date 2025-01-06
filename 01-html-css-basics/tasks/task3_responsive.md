# Task 3: Responsive Design

Optimieren Sie Ihre Webseite für mobile Geräte, um ein responsives Design zu gewährleisten.

### Anforderungen
1. Nutzen Sie Media Queries in der Datei `styles/style.css`, um das Layout für kleinere Bildschirme anzupassen.
2. Stellen Sie sicher, dass die Navigation auf mobilen Geräten als vertikale Liste angezeigt wird.
3. Passen Sie Schriftgrössen und Abstände an, um die Lesbarkeit auf Smartphones zu verbessern.

### Beispiel für Media Queries
```css
@media (max-width: 600px) {
    header {
        flex-direction: column;
    }
    nav a {
        display: block;
        margin: 0.5em 0;
    }
}
```
