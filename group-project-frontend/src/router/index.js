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
    component: MainPage,
    children: [
      {
        path: 'home',
        name: 'Home',
        component: Home,
        children: [
          {
            path: 'maindisplay',
            name: 'MainDisplay',
            component: MainDisplay,
            props: true
          },
          {
            path: 'result',
            name: 'ResultDisplay',
            component: ResultDisplay,
            props: true
          },

        ],
        redirect: '/main/home/maindisplay',
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
        path: 'setting',
        name: 'Setting',
        component: PersonalSetting,
      },
      {
        path: 'detector',
        name: 'CommentDetector',
        component: CommentDetector
      },
      {
        path: 'aboutus',
        name: 'AboutUs',
        component: AboutUs
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
    path: '/admin',
    name: 'adminHome',
    component: AdminHome,
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
    redirect: '/admin/user',
  },

  {
    path: '/adminLogin',
    name: 'adminLogin',
    component: AdminLogin
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
