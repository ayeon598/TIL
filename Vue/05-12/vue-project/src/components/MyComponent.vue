<template>

  <h1>MyComponent.vue</h1>
  <MyComponentItem/>
  <MyComponentItem/>
  <MyComponentItem/>

</template>

<script setup>
  import MyComponentItem from '@/components/MyComponentItem.vue'
</script>

<style scoped>
  h1 {
    color: blueviolet;
  }
  
</style>