<template>
  <p>{{ myMsg }}</p>

  <button @click="updateName">이름 변경</button>

</template>

<script setup>
  defineProps({
    myMsg: String
  })

  const emit = defineEmits(['updateName'])

  // 함수명 updateName은 달라도 상관없다. emit의 updateName은 위랑 같아야 한다.
  const updateName = function () {
    emit('updateName')
  }
</script>

<style scoped>

</style>