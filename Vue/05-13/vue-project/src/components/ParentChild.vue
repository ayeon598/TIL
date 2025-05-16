<template>

  <p>{{ myMsg }}</p>
  <p>{{ dynamicProps }}</p>

  <button @click="emitArgs">추가 인자 전달</button>
  <br>
  <button @click="buttonClick">버튼 클릭</button>

  <ParentGrandChild
    :my-msg="myMsg"
    @update-name="updateName"
  />
</template>

<script setup>

  import ParentGrandChild from '@/components/ParentGrandChild.vue'
  // 내려받은 props : defineProps
  // my-msg : 케밥케이스, myMsg : 카멜케이스
  defineProps({
    myMsg: String,
    dynamicProps: String,
  })

  const emit = defineEmits(['emitArgs', 'someEvent', 'updateName'])

  const emitArgs = function () {
    emit('emitArgs', 1, 2, 3)
  }

  const buttonClick = function () {
    emit('someEvent')
  }

  const updateName = function () {
    emit('updateName')
  }
</script>

<style scoped>

</style>