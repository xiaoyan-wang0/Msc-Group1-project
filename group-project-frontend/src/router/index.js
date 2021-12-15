import { createRouter, createWebHistory } from 'vue-router'
import AdminHome from '../admin/AdminHome.vue'
import UserTable from '../admin/User.vue'
import CommentTable from '../admin/Comment.vue'
import ReportTable from '../admin/Report.vue'
import AdminLogin from '../admin/AdminLogin.vue'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import MovieDetial from '../views/MovieDetial.vue'
import MainPage from '../views/MainPage.vue'
import AboutUs from '../views/AboutUs.vue'
import Profile from '../components/Profile.vue'
import PersonalSetting from '../components/PersonalSetting.vue'
import CommentDetector from '../components/CommentDetector.vue'
import MainDisplay from '../components/MainDisplay.vue'
import ResultDisplay from '../components/ResultPage.vue'

const routes = [
  {
    path: '/main',
    name: 'Main',
    component: () => import('../views/MainPage.vue'),
    children: [
      {
        path: 'home',
        name: 'Home',
        component: () => import('../views/Home.vue'),
        children: [
          {
            path: 'maindisplay',
            name: 'MainDisplay',
            component: () => import('../components/MainDisplay.vue'),
            props: true
          },
          {
            path: 'result',
            name: 'ResultDisplay',
            component: () => import('../components/ResultPage.vue'),
            props: true
          },

        ],
        redirect: '/main/home/maindisplay',
      },
      {
        path: '/movie/:id',
        name: 'Movie Detail',
        component: () => import('../views/MovieDetial.vue'),
      },
      {
        path: 'profile',
        name: 'Profile',
        component: () => import('../components/Profile.vue'),
      },
      {
        path: 'setting',
        name: 'Setting',
        component: () => import('../components/PersonalSetting.vue'),
      },
      {
        path: 'detector',
        name: 'CommentDetector',
        component: () => import('../components/CommentDetector.vue'),
      },
      {
        path: 'aboutus',
        name: 'AboutUs',
        component: () => import('../views/AboutUs.vue'),
      }
    ],
    redirect: () => import('../views/Home.vue')
  },

  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue'),
  },

  {
    path: '/register',
    name: 'Register',
    component: () => import('../views/Register.vue'),
  },

  {
    path: '/admin',
    name: 'adminHome',
    component: () => import('../admin/AdminHome.vue'),
    children: [
      {
        path: 'user',
        name: 'User',
        component: () => import('../admin/User.vue'),
      }, {
        path: 'comments',
        name: 'Comments',
        component: () => import('../admin/Comment.vue'),
      }, {
        path: 'reports',
        name: 'Reports',
        component: () => import('../admin/Report.vue'),
      },
    ],
    redirect: '/admin/user',
  },

  {
    path: '/adminLogin',
    name: 'adminLogin',
    component: () => import('../admin/AdminLogin.vue'),
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

router.beforeEach((to, from, next) => {
  const publicPages = ['/login', '/register', '/', '/main/home/maindisplay', '/main/home/reslut'];
  const authPages = ['/main/porfile'];
  const authRequired = authPages.includes(to.path);
  console.log("to.path");
  console.log(to.path);
  const loggedIn = localStorage.getItem('user');

  // trying to access a restricted page + not logged in
  // redirect to login page
  if (authRequired && !loggedIn) {
    next('/login');
  } else {
    next();
  }
});

export default router
