# Task 1: Event Listener implementieren

Erstellen Sie einen Button, der beim Klick eine Nachricht in der Konsole ausgibt.

### Anforderungen:
- Verwenden Sie `document.getElementById()` oder `querySelector`, um den Button auszuwählen.
- Fügen Sie einen Event Listener hinzu, der das Klickereignis behandelt.

### Beispiel:
```javascript
document.getElementById('fetchWeather').addEventListener('click', function() {
    console.log('Der Button wurde geklickt!');
});
```
