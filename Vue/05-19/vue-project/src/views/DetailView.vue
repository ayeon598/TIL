<template>
  <div>
    <h1>Detail</h1>
    <div v-if="article">
      <p>글번호 : {{ article.id }}</p>
      <p>제목 : {{ article.title }}</p>
      <p>내용 : {{ article.content }}</p>
      <p>작성시간 : {{ article.created_at }}</p>
      <p>수정시간 : {{ article.updated_at }}</p>
    </div>
  </div>
</template>

<script setup>

  import axios from 'axios'
  import { onMounted, ref } from 'vue'
  import { useRoute } from 'vue-router'
  import { useArticleStore } from '@/stores/articles'

  const store = useArticleStore()
  const route = useRoute()
  // 전체게시글 배열 초기화, 단일게시글 null값으로 초기화
  const article = ref(null)

  onMounted(() => {
    axios({
      method: 'get',
      // ArticleListItem의 params
      url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
    })
      .then((res) => {
        article.value = res.data
      })
      .catch(err => console.log(err))
  })

</script>

<style>

</style>
