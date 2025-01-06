# Svelte To-Do App

## Überblick

Diese To-Do-App hilft Ihnen, die Grundlagen von Svelte zu lernen. Dabei geht es um:

1. **Komponenten erstellen**: Sie erstellen Bausteine wie Listen oder Buttons.
2. **Datenbindungen nutzen**: Daten in der Benutzeroberfläche direkt aktualisieren.
3. **Daten speichern**: Aufgaben im Browser abspeichern, sodass sie beim Neustart noch da sind.

## Voraussetzungen

- Installieren Sie [Node.js](https://nodejs.org/) und `npm`.
- Laden Sie die Abhängigkeiten mit:

```bash
npm install
```

- Starten Sie die App mit:

```bash
npm run dev
```

## Aufgabenübersicht

### **Task 1: Erstellen einer Svelte-Komponente**
- Erstellen Sie eine To-Do-Liste als Komponente.
- Fügen Sie ein Eingabefeld hinzu, um neue Aufgaben einzutragen.

### **Task 2: Reaktive Datenbindungen**
- Verknüpfen Sie Eingabefelder mit Variablen.
- Machen Sie Aufgaben dynamisch, sodass sie hinzugefügt oder gelöscht werden können.

### **Task 3: Speicherung mit Local Storage**
- Speichern Sie die Aufgaben im Browser.
- Stellen Sie sicher, dass die Daten nach einem Neustart verfügbar sind.

## Grundlagen

### **1. Komponenten**
- Eine Komponente ist ein Baustein wie ein Button oder eine Liste.
- **Doku:** [Svelte-Komponenten](https://svelte.dev/docs#component-format-script)
- **Beispiel:**
  ```svelte
  <script>
    let name = "Welt";
  </script>

  <h1>Hallo {name}!</h1>
  ```

### **2. Reaktive Datenbindungen**
- Mit Datenbindungen werden Änderungen automatisch sichtbar.
- **Doku:** [Reaktivität in Svelte](https://svelte.dev/docs#reactivity)
- **Beispiel:**
  ```svelte
  <script>
    let count = 0;
  </script>

  <button on:click={() => count++}>Klick mich</button>
  <p>Der Zähler steht bei {count}</p>
  ```

### **3. Local Storage**
- Local Storage speichert Daten direkt im Browser.
- **Doku:** [MDN: Local Storage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)
- **Beispiel:**
  ```javascript
  localStorage.setItem('key', 'value');
  const value = localStorage.getItem('key');
  console.log(value); // 'value'
  ```

## Verzeichnisstruktur

```
svelte-todo-app/
├── README.md
├── src/
│   ├── App.svelte
│   ├── components/
│   │   ├── TodoList.svelte
│   └── stores/
│       └── todos.js
├── tasks/
│   ├── task1_component.md
│   ├── task2_binding.md
│   └── task3_storage.md
├── solutions/
│   ├── task1_solution/
│   │   ├── App.svelte
│   │   └── TodoList.svelte
│   ├── task2_solution/
│   │   ├── App.svelte
│   │   └── AddTodo.svelte
│   └── task3_solution/
│       ├── App.svelte
│       └── stores/todos.js
├── package.json
├── vite.config.js
└── svelte.config.js
```

---
