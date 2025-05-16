import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserView from '../views/UserView.vue'
import LoginView from '../views/LoginView.vue'

import UserProfile from '@/components/UserProfile.vue'
import UserHome from '@/components/UserHome.vue'
import UserPosts from '@/components/UserPosts.vue'

// 로그인 상태 true
const isAuthenticated = true

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/user/:id', // URL
      component: UserView,  // views 디렉토리

      // beforeEnter : 라우트 가드
      beforeEnter: (to, from) => {
        console.log(from)
        console.log(to)
      },
      // components 디렉토리
      children : [
        {path: '', name: 'user', component: UserHome},  // localhost/user/:id
        {path: 'posts', name: 'user-posts', component: UserPosts},  // localhost/user/:id/posts
        {path: 'profile', name: 'user-profile', component: UserProfile},  // localhost/user/:id/profile
      ]
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      beforeEnter: (to, from) => {
        if (isAuthenticated === true) {
          console.log('이미 로그인 상태입니다.')
          // 내가 로그인 버튼을 눌렀는데 이미 로그인 되어있는 상태라면 홈으로 가기
          return { name: 'home'}
        }
      }
    }
  ],
})

export default router
