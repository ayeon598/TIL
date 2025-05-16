<template>
  <h1>게시판</h1>
  <h2>완료된 할일의 개수 : {{ store.doneTodoCount }}</h2>

  <!-- 게시글 목록 -->
  <TodoList/>
  <!-- 게시글 생성 -->
  <TodoForm/>
</template>

<script setup>
  // 중앙저장소(stores의 counter.js) 가져오기
  import { useCounterStore } from '@/stores/counter'

  import TodoForm from '@/components/TodoForm.vue'
  import TodoList from '@/components/TodoList.vue'

  const store = useCounterStore()

</script>

<style scoped>

</style>