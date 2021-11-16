<template>
  
     <main>
      <router-view :key="$route.fullPath" />
    
    </main>

   
  
</template>

<script>
import { computed, onMounted, ref, inject, onBeforeMount } from "vue";
import { useStore } from "vuex";
import router from "@/router";
import env from "@/env.js";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap/dist/js/bootstrap.bundle.js";


import {
  LoginOutlined,
  LogoutOutlined,
  UserOutlined,
  RightCircleOutlined,
} from "@ant-design/icons-vue";
import { navfunction } from "./views/navbar.js";

export default {
  components: {
    LoginOutlined,
    LogoutOutlined,
    UserOutlined,
    RightCircleOutlined,
  },
  setup() {
      
    const sidebarToggle = document.body.querySelector('#sidebarToggle');

       if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }
    const store = useStore();
    const axios = inject("axios"); // inject axios
    const currentUser = computed(() => store.state.auth.user);

    const active = ref("home");

    const logOut = () => {
      store.dispatch("auth/logout");
      router.push("/");
    };
    onMounted(() => {
      console.log("currentUser.data");
      console.log(currentUser);
      navfunction();
    });
    onBeforeMount(() => {
      // Get the list of official genres for movies.
      axios
        .get(env.tmdbgenrelist + env.tmdbkey + env.tmdbtail)
        .then((response) => {
          console.log("genreList");
          console.log(response.data.genres);
          localStorage.setItem(
            "genreList",
            JSON.stringify(response.data.genres)
          );
        });
    });

    return { currentUser, active, logOut ,sidebarToggle};
  },
};
</script>

<style lang="scss">


</style>
