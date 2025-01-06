import os

def create_svelte_todo_repo(repo_name):
    # Define the folder structure
    folders = [
        f"{repo_name}/src/components",
        f"{repo_name}/src/stores",
        f"{repo_name}/tasks",
        f"{repo_name}/solutions/task1_solution",
        f"{repo_name}/solutions/task2_solution",
        f"{repo_name}/solutions/task3_solution"
    ]

    # Define the files and their content
    files = {
        f"{repo_name}/README.md": """# Svelte To-Do App

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
""",
        f"{repo_name}/src/App.svelte": """<script>
import TodoList from './components/TodoList.svelte';
</script>

<main>
  <h1>To-Do App</h1>
  <TodoList />
</main>
""",
        f"{repo_name}/src/components/TodoList.svelte": """<script>
let todos = ['Task 1', 'Task 2'];
let newTodo = '';

function addTodo() {
  if (newTodo.trim()) {
    todos = [...todos, newTodo];
    newTodo = '';
  }
}
</script>

<div>
  <input bind:value={newTodo} placeholder=\"Neue Aufgabe\" />
  <button on:click={addTodo}>Hinzufügen</button>

  <ul>
    {#each todos as todo}
      <li>{todo}</li>
    {/each}
  </ul>
</div>
""",
        f"{repo_name}/src/stores/todos.js": """import { writable } from 'svelte/store';

export const todos = writable([]);
""",
        f"{repo_name}/package.json": """{
  "name": "svelte-todo-app",
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "devDependencies": {
    "@sveltejs/vite-plugin-svelte": "^5.0.3",
    "svelte": "^5.15.0",
    "vite": "^6.0.5"
  }
}
""",
        f"{repo_name}/vite.config.js": """import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vite.dev/config/
export default defineConfig({
  plugins: [svelte()],
})
""",
        f"{repo_name}/svelte.config.js": """import { vitePreprocess } from '@sveltejs/vite-plugin-svelte'

export default {
  // Consult https://svelte.dev/docs#compile-time-svelte-preprocess
  // for more information about preprocessors
  preprocess: vitePreprocess(),
}

""",

        f"{repo_name}/.gitignore": """# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*
lerna-debug.log*

node_modules
dist
dist-ssr
*.local

# Editor directories and files
.vscode/*
!.vscode/extensions.json
.idea
.DS_Store
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?

""",
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
create_svelte_todo_repo("03-svelte-todo-app")

