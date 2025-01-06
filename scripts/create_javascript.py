import os

def create_javascript_repo(repo_name):
    # Define the folder structure
    folders = [
        f"{repo_name}/scripts",
        f"{repo_name}/tasks",
        f"{repo_name}/solutions/task1_solution",
        f"{repo_name}/solutions/task2_solution",
        f"{repo_name}/solutions/task3_solution"
    ]

    # Define the files and their content
    files = {
        f"{repo_name}/README.md": """# JavaScript Basics

## Aufgabenübersicht

Dieses Repository enthält alle notwendigen Materialien, um grundlegende Konzepte in JavaScript zu erlernen und anzuwenden. Die Aufgaben sind in drei Hauptbereiche gegliedert:

1. **Task 1:** Implementieren Sie einen Button mit einem Event Listener.
2. **Task 2:** Manipulieren Sie den DOM, um Inhalte dynamisch zu verändern.
3. **Task 3:** Arbeiten Sie mit einer API, um Daten abzurufen und anzuzeigen.

## Nutzung des Repositories

1. **Klonen Sie das Repository:**
   ```bash
   git clone <URL_des_Repositories>
   cd javascript-basics
   ```

2. **Arbeiten Sie an den Aufgaben:**
   - Jede Aufgabe ist im Ordner `tasks/` ausführlich beschrieben.
   - Speichern Sie Ihre Lösungen im entsprechenden Ordner im Verzeichnis `solutions/`.

3. **Abgabe:**
   - **Option 1:** Erstellen Sie ein eigenes GitHub-Repository, pushen Sie Ihre Änderungen und teilen Sie den Link.
   - **Option 2:** Nutzen Sie das bereitgestellte Python-Skript `create_zip.py`, um ein ZIP-Archiv Ihrer Arbeit zu erstellen, und laden Sie dieses in Microsoft Teams hoch.

   ```bash
   python create_zip.py
   ```

## Ordnerstruktur

```
javascript-basics/
├── README.md
├── index.html
├── scripts/
│   └── app.js
├── tasks/
│   ├── task1_eventlistener.md
│   ├── task2_dom.md
│   └── task3_api.md
├── solutions/
│   ├── task1_solution
│   ├── task2_solution
│   └── task3_solution
└── create_zip.py
```

## Voraussetzungen

- Installieren Sie einen Texteditor wie VS Code.
- Stellen Sie sicher, dass Python installiert ist, falls Sie die ZIP-Option für die Abgabe nutzen möchten.

## Viel Erfolg beim Lernen von JavaScript!""",
        f"{repo_name}/index.html": """<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Wetter-App</title>
</head>
<body>
    <header>
        <h1>Interaktive Wetter-App</h1>
    </header>
    <main>
        <button id=\"fetchWeather\">Wetterdaten abrufen</button>
        <div id=\"weatherData\"></div>
    </main>
    <script src=\"scripts/app.js\"></script>
</body>
</html>
""",
        f"{repo_name}/scripts/app.js": """// Platz für Ihre JavaScript-Logik
console.log('JavaScript verbunden!');
""",
        f"{repo_name}/tasks/task1_eventlistener.md": """# Task 1: Event Listener implementieren

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
""",
        f"{repo_name}/tasks/task2_dom.md": """# Task 2: DOM-Manipulation

Fügen Sie neue Inhalte in das `div` mit der ID `weatherData` hinzu, wenn der Button geklickt wird.

### Anforderungen:
- Nutzen Sie `innerHTML` oder `createElement`, um Inhalte hinzuzufügen.
- Zeigen Sie eine Beispielnachricht wie \"Wetterdaten werden geladen...\" an.

### Beispiel:
```javascript
document.getElementById('fetchWeather').addEventListener('click', function() {
    document.getElementById('weatherData').innerHTML = '<p>Wetterdaten werden geladen...</p>';
});
```
""",
        f"{repo_name}/tasks/task3_api.md": """# Task 3: Arbeiten mit APIs

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
""",
        f"{repo_name}/create_zip.py": """import os
import zipfile

def create_zip(output_filename, directory):
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, directory)
                zipf.write(file_path, arcname)

if __name__ == '__main__':
    project_dir = 'javascript-basics'  # Der Ordnername des Projekts
    output_file = 'submission.zip'
    create_zip(output_file, project_dir)
    print(f"ZIP-Datei '{output_file}' wurde erfolgreich erstellt.")
"""
    }

    # Create folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    # Create files with content
    for file_path, content in files.items():
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

    print(f"Repository '{repo_name}' wurde erfolgreich erstellt.")

# Usage
create_javascript_repo("02-javascript-basics")

