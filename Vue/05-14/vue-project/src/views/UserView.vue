<template>
  <div>
    <RouterLink :to="{ name : 'user-profile'}">Profile</RouterLink>
    <RouterLink :to="{ name : 'user-posts'}">Posts</RouterLink>

    <h1>UserView</h1>
    <h2>{{ userId }}번의 User 페이지</h2>

    <button @click="goHome">Home</button>
    
    <button @click="routeUpdate">100번 유저 페이지</button>
  </div>
  <RouterView/>
</template>

<script setup>
  import { ref } from 'vue'
  import { RouterLink, RouterView } from 'vue-router'
  // useRoute : read-only, useRouter : write-only
  import { useRoute, useRouter } from 'vue-router'
  // 가드 Leave : 페이지 나갈 때, Update : 페이지 url 변경될 때
  import { onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'

  const route = useRoute()
  const router = useRouter()
  const userId = ref(route.params.id)

  const goHome = function () {
    // push : 이전 페이지로 돌아갈 수 있음(히스토리에 추가됨)
    // replace : 이전 페이지로 돌아갈 수 없음(히스토리에 추가되지 않음)
    router.replace({name: 'home'})
  }

  const routeUpdate = function () {
    router.push({name: 'user', params: {id:100} })
  }

  onBeforeRouteLeave((to, from) => {
    const answer = window.confirm('정말 떠나실 건가요?')
    if (answer == false) {
      return false // 페이지 이동 X
    }
  })

  // to: 100번 유저, from: 1번 유저
  onBeforeRouteUpdate((to, from) => {
    userId.value = to.params.id
  })
</script>

<style scoped>
    
</style>