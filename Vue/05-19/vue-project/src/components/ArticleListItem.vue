<template>
  <div>
    <h5>{{ article.id }}</h5>
    <p>{{ article.title }}</p>
    <p>{{ article.content }}</p>
    <RouterLink :to="{ name: 'DetailView', params: {id: article.id}}">
      [DETAIL]
    </RouterLink>
  </div>
</template>

<script setup>

  defineProps({
    article: Object
  })

  import { RouterLink } from 'vue-router'
</script>
