# Task 2: DOM-Manipulation

Fügen Sie neue Inhalte in das `div` mit der ID `weatherData` hinzu, wenn der Button geklickt wird.

### Anforderungen:
- Nutzen Sie `innerHTML` oder `createElement`, um Inhalte hinzuzufügen.
- Zeigen Sie eine Beispielnachricht wie "Wetterdaten werden geladen..." an.

### Beispiel:
```javascript
document.getElementById('fetchWeather').addEventListener('click', function() {
    document.getElementById('weatherData').innerHTML = '<p>Wetterdaten werden geladen...</p>';
});
```
