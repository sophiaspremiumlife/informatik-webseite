# Task 4: Responsive Design mit Media Queries

## Ziel
Passen Sie die Webseite an verschiedene Bildschirmgrößen an, indem Sie **CSS Media Queries** nutzen.

## Anforderungen
- Optimieren Sie die Navigationsleiste für mobile Geräte:
  - Ändern Sie die Darstellung so, dass die Links **untereinander** erscheinen, wenn der Bildschirm schmaler als 600px ist.
- Verbessern Sie die **Lesbarkeit**:
  - Passen Sie die Schriftgröße für kleine Bildschirme an.
  - Vermeiden Sie zu lange Zeilen.
- Nutzen Sie den Artikel zu [CSS Media Queries](https://developer.mozilla.org/de/docs/Web/CSS/Media_Queries) als Hilfe.

## Hinweise
- Verwenden Sie `@media (max-width: 600px)`, um die Regeln für kleinere Bildschirme zu setzen.
- Testen Sie die Webseite, indem Sie das Browserfenster verkleinern oder die Entwickler-Tools (`F12 > Geräteansicht`) nutzen.
- Achten Sie darauf, dass die Navigation auf **mobilen Geräten** weiterhin nutzbar bleibt.

## Beispiel CSS
```css
@media (max-width: 600px) {
    nav ul {
        flex-direction: column;
        align-items: center;
    }
    
    nav ul li {
        margin: 10px 0;
    }
}

