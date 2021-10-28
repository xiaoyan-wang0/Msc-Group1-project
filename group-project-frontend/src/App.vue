<template>
  <div>
    <header>
      <div class="navbar-div">
        <section class="navigation">
          <div class="nav-container">
            <div class="brand">
              <router-link to="/" class="AMDB-link">
                <img class="logo-icon" src="./assets/logo.png" />
                <span class="span1">AM</span> <span class="span2">DB</span>
              </router-link>
            </div>
            <nav>
              <div class="nav-mobile">
                <a id="nav-toggle" href="#!"><span></span></a>
              </div>
              <ul class="nav-list">
                <li>
                  <a href="/">Home</a>
                </li>

                <li>
                  <a href="#"></a>
                </li>
                <li>
                  <a href="#"></a>
                </li>
                <li>
                  <a href="/main/porfile">Profile</a>
                </li>

                <li>
                  <a href="/main/detector">Detector</a>
                </li>
                <li></li>
                <li class="header-login-li">
                  <router-link to="/login" class="header-login">
                    <span> Sign In</span>
                  </router-link>
                </li>
                <li class="header-login-li">
                  <router-link to="/register" class="header-register">
                    <span> Sign Up</span>
                  </router-link>
                </li>
              </ul>
            </nav>
          </div>
        </section>
      </div>
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
import { computed, onMounted, ref } from "vue";
import { useStore } from "vuex";
import router from "@/router";
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
    const store = useStore();
    const currentUser = computed(() => store.state.auth.user);

    const active = ref("home");

    const logOut = () => {
      store.dispatch("auth/logout");
      router.push("/");
    };
    onMounted(() => {
      navfunction();
    });
    return { currentUser, active, logOut };
  },
};
</script>

<style lang="scss">
body {
  background-color: #000 !important;

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
  font-family: Roboto, Helvetica, Arial, sans-serif;

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
    // padding: 10px 16px;
    // background-color: #2c3d4e;
    box-shadow: 0px 0px 6 px rgba(0, 0, 0, 0.1);
    .AMDB-link {
      float: left;
      .span1 {
        padding-top: 5555px;
        margin: 0 0 0 50px;
        color: #fff;
        vertical-align: middle;
        font-size: 27px;
      }
      .span2 {
        font-size: 27px;
        vertical-align: middle;
        color: #42b883;
      }
    }

    .logo-icon {
      width: 50px;
      margin-bottom: 2px;
    }
    .logicon {
      font-size: 25px !important;
      float: right;
      color: white;
    }
    .header-login {
      span {
        margin-left: 50px;
        vertical-align: middle;
      }
    }
    .header-register {
      span {
        vertical-align: middle;
      }
    }
    .logouticon {
      float: right;
      color: #fff;
      font-size: 20px;
      .header-profile {
        margin-right: 20px;
      }
    }
    .navbar-div {
      background-color: #252525;
      width: 100%;

      nav {
        display: inline-block;
        margin: 0 auto;
        background-color: #252525;
        // box-shadow: 0 1px 1px #ccc;
        // border-radius: 2px;
      }

      nav span {
        display: inline-block;
        padding: 0px 0px;
        color: #fff !important;
        font-weight: bold;
        font-size: 20px;
        text-decoration: none !important;
        line-height: 1;
        text-transform: uppercase;
        background-color: transparent;

        transition: background-color 0.25s;
      }

      nav span:first-child {
        border-radius: 2px 0 0 2px;
      }

      nav span:last-child {
        border-radius: 0 2px 2px 0;
      }

      nav.home .home,
      nav.projects .projects,
      nav.profile .profile,
      nav.detector .detector {
        background-color: #e35885;
      }

      div.content {
        font-size: 22px;
        font-weight: bold;
        color: #7d9098;
      }

      div.content b {
        color: #ffffff;
        display: inline-block;
        padding: 5px 10px;
        background-color: #c4d7e0;
        border-radius: 2px;
        text-transform: uppercase;
        font-size: 18px;
      }
    }

    // Navigation Variables
    $content-width: 70%;
    $breakpoint: 799px;
    $nav-height: 70px;
    $nav-background: #111010;
    $nav-font-color: #ffffff;
    $link-hover-color: #2581dc;

    // Outer navigation wrapper
    .navigation {
      height: $nav-height;
      background: $nav-background;
    }

    // Logo and branding
    .brand {
      position: absolute;
      padding-left: 5px;
      float: left;
      line-height: $nav-height;
      text-transform: uppercase;
      font-size: 1.4em;
      a,
      a:visited {
        color: $nav-font-color;
        text-decoration: none;
      }
    }

    // Container with no padding for navbar
    .nav-container {
      max-width: $content-width;
      margin: 0 auto;
    }
    // Navigation
    nav {
      float: right;
      font-size: 20px;

      ul {
        list-style: none;
        margin: 0;
        padding: 0;
        li {
          float: left;
          position: relative;
          a,
          a:visited {
            display: block;
            padding: 0 20px;
            line-height: $nav-height;
            background: $nav-background;
            color: $nav-font-color;
            text-decoration: none;
            &:hover {
              background: $link-hover-color;
              color: $nav-font-color;
            }
            &:not(:only-child):after {
              padding-left: 4px;
              content: " ▾";
            }
          } // Dropdown list
          ul li {
            min-width: 190px;
            a {
              vertical-align: middle;
              padding: 15px;
              line-height: 20px;
            }
          }
        }
        .header-login-li a:hover {
          background: none !important;
        }
      }
    }

    // Dropdown list binds to JS toggle event
    .nav-dropdown {
      position: absolute;
      display: none;
      z-index: 1;
      box-shadow: 0 3px 12px rgba(0, 0, 0, 0.15);
    }

    /* Mobile navigation */

    // Binds to JS Toggle
    .nav-mobile {
      display: none;
      position: absolute;
      top: 0;
      right: 0;
      background: $nav-background;
      height: $nav-height;
      width: $nav-height;
    }
    @media only screen and (max-width: 798px) {
      // Hamburger nav visible on mobile only
      .header-login {
        span {
          margin-left: 0px;
        }
      }
      .nav-mobile {
        display: block;
      }
      nav {
        width: 100%;
        padding: $nav-height 0 15px;
        ul {
          display: none;
          li {
            float: none;
            a {
              padding: 15px;
              line-height: 20px;
            }
            ul li a {
              padding-left: 30px;
            }
          }
        }
      }
      .nav-dropdown {
        position: static;
      }
    }
    @media screen and (min-width: $breakpoint) {
      .header-login {
        span {
          // margin-left: 0px;
        }
      }
      .nav-list {
        display: block !important;
      }
    }
    #nav-toggle {
      position: absolute;
      left: 18px;
      top: 22px;
      cursor: pointer;
      padding: 10px 35px 16px 0px;
      span,
      span:before,
      span:after {
        cursor: pointer;
        border-radius: 1px;
        height: 5px;
        width: 35px;
        background: $nav-font-color;
        position: absolute;
        display: block;
        content: "";
        transition: all 300ms ease-in-out;
      }
      span:before {
        top: -10px;
      }
      span:after {
        bottom: -10px;
      }
      &.active span {
        background-color: transparent;
        &:before,
        &:after {
          top: 0;
        }
        &:before {
          transform: rotate(45deg);
        }
        &:after {
          transform: rotate(-45deg);
        }
      }
    }
  }
}
</style>
