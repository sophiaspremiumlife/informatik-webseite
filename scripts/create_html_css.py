import os

def create_repo_with_readme(repo_name):
    # Define the folder structure
    folders = [
        f"{repo_name}/styles",
        f"{repo_name}/tasks",
        f"{repo_name}/solutions/task1_solution",
        f"{repo_name}/solutions/task2_solution",
        f"{repo_name}/solutions/task3_solution"
    ]

    # Define the files and their content
    files = {
        f"{repo_name}/README.md": """# HTML & CSS Basics

## Aufgabenübersicht

Dieses Repository enthält alle notwendigen Materialien, um grundlegende Konzepte in HTML und CSS zu erlernen und anzuwenden. Die Aufgaben sind in drei Hauptbereiche gegliedert:

1. **Task 1:** Erstellen Sie die Grundstruktur einer Portfolio-Seite.
2. **Task 2:** Arbeiten Sie mit Flexbox, um ein modernes Layout zu gestalten.
3. **Task 3:** Optimieren Sie Ihre Webseite für mobile Geräte (Responsive Design).

## Nutzung des Repositories

1. **Klonen Sie das Repository:**
   ```bash
   git clone <URL_des_Repositories>
   cd html-css-basics
   ```

2. **Arbeiten Sie an den Aufgaben:**
   - Jede Aufgabe ist im Ordner `tasks/` ausführlich beschrieben.
   - Speichern Sie Ihre Lösungen im entsprechenden Ordner im Verzeichnis `solutions/`.

3. **Abgabe:**
   - **Option 1:** Erstellen Sie ein eigenes GitHub-Repository, pushen Sie Ihre Änderungen und teilen Sie den Link mit der Lehrperson.
   - **Option 2:** Nutzen Sie das bereitgestellte Python-Skript `create_zip.py`, um ein ZIP-Archiv Ihrer Arbeit zu erstellen, und laden Sie dieses in Microsoft Teams hoch.

   ```bash
   python create_zip.py
   ```

## Ordnerstruktur

```
html-css-basics/
├── README.md
├── index.html
├── styles/
│   └── style.css
├── tasks/
│   ├── task1_structure.md
│   ├── task2_flexbox.md
│   └── task3_responsive.md
├── solutions/
│   ├── task1_solution
│   ├── task2_solution
│   └── task3_solution
└── create_zip.py
```

## Voraussetzungen

- Installieren Sie einen Texteditor wie VS Code.
- Stellen Sie sicher, dass Python installiert ist, falls Sie die ZIP-Option für die Abgabe nutzen möchten.

## Aufgaben im Detail

### Task 1: HTML-Grundstruktur erstellen
- Ziel: Erstellen Sie die Grundstruktur einer Portfolio-Seite mit den Elementen `<header>`, `<main>` und `<footer>`.
- Datei: `index.html`
- Beispiel: Im Ordner `tasks/task1_structure.md` finden Sie weitere Hinweise.

### Task 2: Flexbox für Layout
- Ziel: Verwenden Sie CSS-Flexbox, um ein modernes Layout zu erstellen.
- Datei: `styles/style.css`
- Beispiel: Im Ordner `tasks/task2_flexbox.md` finden Sie Details.

### Task 3: Responsive Design
- Ziel: Optimieren Sie Ihre Webseite für mobile Geräte.
- Datei: `styles/style.css`
- Beispiel: Details und Beispielcode sind in `tasks/task3_responsive.md` verfügbar.

## Viel Erfolg beim Lernen von HTML & CSS!""",
        f"{repo_name}/index.html": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>Portfolio-Seite</title>\n</head>\n<body>\n    <header>\n        <h1>Meine Portfolio-Seite</h1>\n    </header>\n    <main>\n        <p>Willkommen auf meiner Portfolio-Seite!</p>\n    </main>\n    <footer>\n        <p>&copy; 2025</p>\n    </footer>\n</body>\n</html>",
        f"{repo_name}/styles/style.css": "/* Basis-Styling */\nbody {\n    font-family: Arial, sans-serif;\n    margin: 0;\n    padding: 0;\n}\n\nheader {\n    background-color: #333;\n    color: white;\n    padding: 1em;\n    text-align: center;\n}\n\nfooter {\n    background-color: #333;\n    color: white;\n    padding: 0.5em;\n    text-align: center;\n    position: fixed;\n    bottom: 0;\n    width: 100%;\n}",
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
    project_dir = 'html-css-basics'  # Der Ordnername des Projekts
    output_file = 'submission.zip'
    create_zip(output_file, project_dir)
    print(f"ZIP-Datei '{output_file}' wurde erfolgreich erstellt.")"""
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
create_repo_with_readme("01-html-css-basics")

