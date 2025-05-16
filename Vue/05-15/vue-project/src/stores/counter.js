import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  // ==== state 영역 ====

  // 할 일의 id
  let id = 0
  // 할 일의 목록 todo
  const todos = ref([])

  // ==== action 영역 ====

  // create
  const addTodo = function (todoText) {
    todos.value.push({
      id: id++,
      text: todoText, // 작성한 일
      isDone: false // 완료 여부
    })
  }

  // delete
  const deleteTodo = function (todoId) {
    const index = todos.value.findIndex((todo) => todo.id === todoId)
    todos.value.splice(index, 1)  // index번째의 1개 항목 제거
  }

  // update(취소선)
  const updateTodo = function (todoId) {
    // map() : 배열의 각 요소를 순회하면서 새로운 배열을 반환
    todos.value = todos.value.map((todo) => {
      if (todo.id === todoId) {
        todo.isDone = !todo.isDone // false -> true, true -> false
      }
      return todo
    })
  }

  // ==== getter 영역 ====

  // computed : 완료된 할 일의 개수를 계산
  const doneTodoCount = computed(() => {
    // isDone true인 것만 모아서 새 배열 만든다.
    const doneTodos = todos.value.filter((todo) => todo.isDone)
    // 배열의 길이를 반환(완료된 할 일의 개수)
    return doneTodos.length
  })

  return { todos, addTodo, doneTodoCount, deleteTodo, updateTodo }
}, { persist: true })
// persist: true : 새로고침해도 데이터 유지
