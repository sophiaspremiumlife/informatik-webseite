# Task 3: Arbeiten mit APIs

Rufen Sie Wetterdaten von einer öffentlichen API ab (z. B. OpenWeatherMap) und zeigen Sie sie auf der Seite an.

### Anforderungen:
- Verwenden Sie `fetch`, um Daten von der API abzurufen.
- Zeigen Sie die Temperatur und den Standort in einem neuen Abschnitt an.
- Behandeln Sie Fehler (z. B. ungültige API-Schlüssel).

### Beispiel:
```javascript
const apiKey = 'Ihr_API_Schluessel';
const url = `https://api.openweathermap.org/data/2.5/weather?q=Zürich&appid=${apiKey}&units=metric`;

document.getElementById('fetchWeather').addEventListener('click', async function() {
    try {
        const response = await fetch(url);
        const data = await response.json();
        document.getElementById('weatherData').innerHTML = `<p>Temperatur in Zürich: ${data.main.temp}°C</p>`;
    } catch (error) {
        console.error('Fehler beim Abrufen der Wetterdaten:', error);
    }
});
```
