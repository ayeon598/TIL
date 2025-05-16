<template>

  <h1>App.vue</h1>
  <!-- 자식 컴포넌트 -->
  <!-- self-closing 태그 -->
  <MyComponent/>

</template>

<!-- createApp의 setup함수와 차이점 : return문이 필요없다. -->
<script setup>

  // 컴포넌트 불러오는 방법 2가지
  // 1. 상대 경로
  // import MyComponent from './components/MyComponent.vue'
  // 2. src 별칭 : @
  import MyComponent from '@/components/MyComponent.vue'
</script>

<!-- scoped : 이 파일(App.vue) 안에서만 스타일이 적용됨. 자식 컴포넌트에는 적용 안 됨.-->
<style scoped>
  h1 {
    color: burlywood;
  }
</style>