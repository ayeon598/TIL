<template>
  <div>
    <!-- prevent : 새로고침 막기 -->
    <form @submit.prevent="createTodo(todoText)" ref="formElem">
      <input type="text" v-model="todoText">
      <input type="submit">
    </form>
  </div>
</template>

<script setup>

  import {ref} from 'vue'
  import { useCounterStore } from '@/stores/counter'

  const store = useCounterStore()

  const todoText = ref('')
  const formElem = ref(null)

  // create 함수
  const createTodo = function (todoText) {
    // stores의 addTodo 함수 가져오기
    store.addTodo(todoText)
    // 할 일 추가될 때마다 폼 초기화
    formElem.value.reset()
  }
</script>

<style scoped>

</style>