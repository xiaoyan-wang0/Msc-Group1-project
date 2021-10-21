<template>
  <div>
    <header>
      <router-link to="/" class="AMDB-link">
        <h1><span>AM</span>DB</h1>
      </router-link>
      <div class="logicon" v-if="!currentUser">
        <router-link to="/login" class="header-login">
          <span> Sign In</span>
        </router-link>

        <router-link to="/register">
          <span> Sign Up</span>
        </router-link>
      </div>
      <div v-if="currentUser" class="logouticon">
        <router-link to="/main/profile" class="header-profile">
          <a-tooltip placement="topLeft" color="white">
            <template #title>
              <span>{{ currentUser.data.userName }}</span>
            </template>
            <span> {{ currentUser.data.userName }}</span></a-tooltip
          >
        </router-link>
        <a-tooltip placement="topLeft" color="white">
          <template #title>
            <span>LOGOUT</span>
          </template>
          <a @click.prevent="logOut">
            <RightCircleOutlined style="margin-right: 5px" />
            <span> LogOut</span>
          </a></a-tooltip
        >
      </div>
      <!-- <div class="navbar-div">
        <nav class="navbar navbar-expand-custom navbar-mainbg">
          <a class="navbar-brand navbar-logo" href="#">Navbar</a>
          <button
            class="navbar-toggler"
            type="button"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <i class="fas fa-bars text-white"></i>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav ml-auto">
              <div class="hori-selector">
                <div class="left"></div>
                <div class="right"></div>
              </div>
              <li class="nav-item">
                <a class="nav-link" href="javascript:void(0);"
                  ><i class="fas fa-tachometer-alt"></i>Dashboard</a
                >
              </li>
              <li class="nav-item active">
                <a class="nav-link" href="javascript:void(0);"
                  ><i class="far fa-address-book"></i>Address Book</a
                >
              </li>
              <li class="nav-item">
                <a class="nav-link" href="javascript:void(0);"
                  ><i class="far fa-clone"></i>Components</a
                >
              </li>
              <li class="nav-item">
                <a class="nav-link" href="javascript:void(0);"
                  ><i class="far fa-calendar-alt"></i>Calendar</a
                >
              </li>
              <li class="nav-item">
                <a class="nav-link" href="javascript:void(0);"
                  ><i class="far fa-chart-bar"></i>Charts</a
                >
              </li>
              <li class="nav-item">
                <a class="nav-link" href="javascript:void(0);"
                  ><i class="far fa-copy"></i>Documents</a
                >
              </li>
            </ul>
          </div>
        </nav>
      </div> -->
    </header>
    <main>
      <router-view />
    </main>

    <footer>
      <div class="footer"></div>
    </footer>
  </div>
</template>

<script>
import { computed, onMounted } from "vue";
import { useStore } from "vuex";
import router from "@/router";
import {
  LoginOutlined,
  LogoutOutlined,
  UserOutlined,
  RightCircleOutlined,
} from "@ant-design/icons-vue";
import {navfunction} from "./views/navbar.js";

export default {
  components: {
    LoginOutlined,
    LogoutOutlined,
    UserOutlined,
    RightCircleOutlined,
  },
  setup() {
    const store = useStore();
    const currentUser = computed(() => store.state.auth.user);
    const logOut = () => {
      store.dispatch("auth/logout");
      router.push("/");
    };
    onMounted(() => {
      // navfunction();
    });
    return { currentUser, logOut };
  },
};
</script>

<style lang="scss">
body {
  background-color: #080808 !important;

  min-width: 600px;
  .ant-modal-body {
    padding: 0 !important;
    background-color: black;
  }
  textarea.ant-input {
    height: 150px !important;
  }
}
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Times New Roman", Times, serif;

  &::selection {
    background: transparentize(#42b883, 0.5);
  }

  a {
    text-decoration: none;
  }

  header {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 10px 16px;
    // background-color: #2c3d4e;
    box-shadow: 0px 0px 6 px rgba(0, 0, 0, 0.1);
    .AMDB-link {
      h1 {
        color: #fff;
        font-size: 50px;
        margin-top: 20px;

        span {
          font-size: 50px;
          color: #42b883;
        }
      }
    }
    .logicon {
      color: #fff;
      font-size: 20px;
      position: absolute;
      right: 20px;
      .header-login {
        margin-right: 20px;
      }
    }
    .logouticon {
      color: #fff;
      font-size: 20px;
      position: absolute;
      right: 20px;
      .header-profile {
        margin-right: 20px;
      }
    }
    .navbar-div {
      .navbar-logo {
        padding: 15px;
        color: #fff;
      }
      .navbar-mainbg {
        background-color: #5161ce;
        padding: 0px;
      }
      #navbarSupportedContent {
        overflow: hidden;
        position: relative;
      }
      #navbarSupportedContent ul {
        padding: 0px;
        margin: 0px;
      }
      #navbarSupportedContent ul li a i {
        margin-right: 10px;
      }
      #navbarSupportedContent li {
        list-style-type: none;
        float: left;
      }
      #navbarSupportedContent ul li a {
        color: rgba(255, 255, 255, 0.5);
        text-decoration: none;
        font-size: 15px;
        display: block;
        padding: 20px 20px;
        transition-duration: 0.6s;
        transition-timing-function: cubic-bezier(0.68, -0.55, 0.265, 1.55);
        position: relative;
      }
      #navbarSupportedContent > ul > li.active > a {
        color: #5161ce;
        background-color: transparent;
        transition: all 0.7s;
      }
      #navbarSupportedContent a:not(:only-child):after {
        content: "\f105";
        position: absolute;
        right: 20px;
        top: 10px;
        font-size: 14px;
        font-family: "Font Awesome 5 Free";
        display: inline-block;
        padding-right: 3px;
        vertical-align: middle;
        font-weight: 900;
        transition: 0.5s;
      }
      #navbarSupportedContent .active > a:not(:only-child):after {
        transform: rotate(90deg);
      }
      .hori-selector {
        display: inline-block;
        position: absolute;
        height: 100%;
        top: 0px;
        left: 0px;
        transition-duration: 0.6s;
        transition-timing-function: cubic-bezier(0.68, -0.55, 0.265, 1.55);
        background-color: #fff;
        border-top-left-radius: 15px;
        border-top-right-radius: 15px;
        margin-top: 10px;
      }
      .hori-selector .right,
      .hori-selector .left {
        position: absolute;
        width: 25px;
        height: 25px;
        background-color: #fff;
        bottom: 10px;
      }
      .hori-selector .right {
        right: -25px;
      }
      .hori-selector .left {
        left: -25px;
      }
      .hori-selector .right:before,
      .hori-selector .left:before {
        content: "";
        position: absolute;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background-color: #5161ce;
      }
      .hori-selector .right:before {
        bottom: 0;
        right: -25px;
      }
      .hori-selector .left:before {
        bottom: 0;
        left: -25px;
      }

      @media (min-width: 992px) {
        .navbar-expand-custom {
          -ms-flex-flow: row nowrap;
          flex-flow: row nowrap;
          -ms-flex-pack: start;
          justify-content: flex-start;
        }
        .navbar-expand-custom .navbar-nav {
          -ms-flex-direction: row;
          flex-direction: row;
        }
        .navbar-expand-custom .navbar-toggler {
          display: none;
        }
        .navbar-expand-custom .navbar-collapse {
          display: -ms-flexbox !important;
          display: flex !important;
          -ms-flex-preferred-size: auto;
          flex-basis: auto;
        }
      }

      @media (max-width: 991px) {
        #navbarSupportedContent ul li a {
          padding: 12px 30px;
        }
        .hori-selector {
          margin-top: 0px;
          margin-left: 10px;
          border-radius: 0;
          border-top-left-radius: 25px;
          border-bottom-left-radius: 25px;
        }
        .hori-selector .left,
        .hori-selector .right {
          right: 10px;
        }
        .hori-selector .left {
          top: -25px;
          left: auto;
        }
        .hori-selector .right {
          bottom: -25px;
        }
        .hori-selector .left:before {
          left: -25px;
          top: -25px;
        }
        .hori-selector .right:before {
          bottom: -25px;
          left: -25px;
        }
      }
    }
  }
}
</style>
