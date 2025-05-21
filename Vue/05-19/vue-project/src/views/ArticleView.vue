<template>
  <div>
    <h1>Articles</h1>
    <RouterLink :to="{ name:'CreateView'}">
      [CREATE]
    </RouterLink>
    <!-- 전체 게시글 목록 -->
    <ArticleList />
  </div>
</template>

<script setup>
  import ArticleList from '@/components/ArticleList.vue'
  import { onMounted } from 'vue'
  import { useArticleStore } from '@/stores/articles'
  import { RouterLink } from 'vue-router'

  const store = useArticleStore()

  onMounted(() => {
    store.getArticles()
  })


</script>

<style>

</style>
