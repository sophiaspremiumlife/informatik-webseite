<script>
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
  <input bind:value={newTodo} placeholder="Neue Aufgabe" />
  <button on:click={addTodo}>Hinzufügen</button>

  <ul>
    {#each todos as todo}
      <li>{todo}</li>
    {/each}
  </ul>
</div>
