<template>
  <body class="sb-nav-fixed">
    <nav class="sb-topnav navbar navbar-expand navbar-dark bg-dark">
      <!-- Navbar Brand-->
      <a class="navbar-brand ps-3" href="#">Admin system</a>
      <!-- Sidebar Toggle-->
      <button
        class="btn btn-link btn-sm order-1 order-lg-0 me-4 me-lg-0"
        id="sidebarToggle"
        href="#!"
      >
        <i class="fas fa-bars"></i>
      </button>
      <!-- Navbar Search-->
      <div
        class="
          d-none d-md-inline-block
          form-inline
          ms-auto
          me-0 me-md-3
          my-2 my-md-0
        "
      ></div>

      <div class="navbar-nav ms-auto ms-md-0 me-3 me-lg-4">
        <a
          class="nav-link"
          @click="handleLogout"
          role="button"
          aria-expanded="false"
          ><i class="fas fa-sign-out-alt"></i
        ></a>
      </div>
    </nav>

    <div id="layoutSidenav">
      <div id="layoutSidenav_nav">
        <nav class="sb-sidenav accordion sb-sidenav-dark" id="sidenavAccordion">
          <div class="sb-sidenav-menu">
            <div class="nav">
              <div class="sb-sidenav-menu-heading">Info</div>

              <router-link class="nav-link" :to="'user'">
                <div class="sb-nav-link-icon">
                  <i class="fas fa-user"></i>
                </div>
                Users</router-link
              >
              <div class="sb-sidenav-menu-heading">Comment</div>

              <router-link class="nav-link" :to="'comments'">
                <div class="sb-nav-link-icon">
                  <i class="fas fa-comments"></i>
                </div>
                User Comment
              </router-link>
              <router-link class="nav-link" :to="'reports'">
                <div class="sb-nav-link-icon">
                  <i class="fas fa-book-open"></i>
                </div>
                Report Comment
              </router-link>
            </div>
          </div>
          <div class="sb-sidenav-footer">
            <div class="small">Logged in as:</div>
            AMDB Administrator
          </div>
        </nav>
      </div>
      <div id="layoutSidenav_content">
        <router-view :key="$route.fullPath" />
        <footer class="py-4 bg-light mt-auto">
          <div class="container-fluid px-4">
            <div
              class="d-flex align-items-center justify-content-between small"
            >
              <div class="text-muted">Copyright &copy; TEAM1-AMDB</div>
              <div>
                <a href="#">Privacy Policy</a>
                &middot;
                <a href="#">Terms &amp; Conditions</a>
              </div>
            </div>
          </div>
        </footer>
      </div>
    </div>
  </body>
</template>

<script>
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap/dist/js/bootstrap.bundle.js";
import { ref, defineComponent, onBeforeMount, onMounted } from "vue";
import { message } from "ant-design-vue";
import router from "@/router";
import { useStore } from "vuex";

export default {
  name: "About",

  setup() {
    onMounted(() => {
      const sidebarToggle = document.body.querySelector("#sidebarToggle");

      if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        if (localStorage.getItem("sb|sidebar-toggle") === "true") {
          document.body.classList.toggle("sb-sidenav-toggled");
        }
        sidebarToggle.addEventListener("click", (event) => {
          event.preventDefault();
          document.body.classList.toggle("sb-sidenav-toggled");
          localStorage.setItem(
            "sb|sidebar-toggle",
            document.body.classList.contains("sb-sidenav-toggled")
          );
        });
      }
    });

    const handleLogout = () => {
      console.log("handleLogout");
      localStorage.removeItem("user");
      router.push({
        path: "/",
      });
    };
    return { handleLogout };
  },
};
</script>

<style lang="scss">
</style>