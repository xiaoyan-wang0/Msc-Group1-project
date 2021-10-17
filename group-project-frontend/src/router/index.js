import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import MovieDetial from '../views/MovieDetial.vue'
import MainPage from '../views/MainPage.vue'
import Profile from '../components/Profile.vue'
import CommentDetector from '../components/CommentDetector.vue'

const routes = [
  {
    path: '/main',
    name: 'Main',
    component: MainPage,
    children: [
      {
        path: 'home',
        name: 'Home',
        component: Home
      },
      {
        path: '/movie/:id',
        name: 'Movie Detail',
        component: MovieDetial
      },
      {
        path: 'profile',
        name: 'Profile',
        component: Profile,
      },
      {
        path: 'detector',
        name: 'CommentDetector',
        component: CommentDetector
      }
    ],
    redirect: Home
  },

  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },

  {
    path: '/',
    redirect: MainPage,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

// router.beforeEach((to, from, next) => {
//   const publicPages = ['/login', '/register', '/'];
//   const authRequired = !publicPages.includes(to.path);
//   const loggedIn = localStorage.getItem('user');

//   // trying to access a restricted page + not logged in
//   // redirect to login page
//   if (authRequired && !loggedIn) {
//     next('/login');
//   } else {
//     next();
//   }
// });

export default router
