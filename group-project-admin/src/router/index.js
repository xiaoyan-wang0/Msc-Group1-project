import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import UserTable from '../components/User.vue'
import CommentTable from '../components/Comment.vue'
import ReportTable from '../components/Report.vue'

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/home',
    name: 'Home',
    component: Home,
    children: [
      {
        path: 'user',
        name: 'User',
        component: UserTable
      }, {
        path: 'comments',
        name: 'Comments',
        component: CommentTable
      }, {
        path: 'reports',
        name: 'Reports',
        component: ReportTable
      },
    ],
    redirect: '/home/user',
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
