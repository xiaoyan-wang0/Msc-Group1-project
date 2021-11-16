import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

import MainPage from '../views/MainPage.vue'

import MainDisplay from '../components/MainDisplay.vue'


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
      

        ],
        redirect: '/main/home/maindisplay',
      },
    
    
     
     
    ],
    redirect: Home
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
