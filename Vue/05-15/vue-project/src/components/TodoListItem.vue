<template>
  <div>
    <!-- :class - if문 + class 선택자 => true일 때 class가 적용됨 -->
    <span @click="store.updateTodo(todo.id)" :class="{ 'is-done':todo.isDone }">
      {{ todo.text }}
    </span>
    <button @click="store.deleteTodo(todo.id)">Delete</button>
  </div>
</template>

<script setup>

  import { useCounterStore } from '@/stores/counter'

  const store = useCounterStore()

  defineProps({
    todo: Object
  })

</script>

<style scoped>
  .is-done {
    text-decoration: line-through;
  }
</style>