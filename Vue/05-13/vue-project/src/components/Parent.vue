<template>

  <!-- name과 message를 props -->
  <!-- message는 정적 props -->
  <!-- name은 동적 props -->
  <ParentChild
    @emit-args="getNumbers"
    @some-event="someCallback"
    @update-name="updateName"
    my-msg = "message"
    :dynamic-props="name"
  />
  <!-- item을 props -->
  <ParentItem
    v-for="item in items"
    :key="item.id"
    :my-prop="item"
  />

</template>

<script setup>
  import {ref} from 'vue'
  import ParentChild from '@/components/ParentChild.vue'
  import ParentItem from '@/components/ParentItem.vue'

  const name = ref('Bob')

  const items = ref([
    {id: 1, name: '사과'},
    {id: 2, name: '바나나'},
    {id: 3, name: '딸기'},
  ])

  const getNumbers = function(...args) {
    alert(`ParentChild가 발신한 추가인자 ${args} 수신했다`)
  }

  const someCallback = function() {
    alert('ParentChild가 발신한 이벤트를 수신했다.')
  }

  const updateName = function() {
    name.value = 'Bella'
  }
  
</script>

<style scoped>

</style>