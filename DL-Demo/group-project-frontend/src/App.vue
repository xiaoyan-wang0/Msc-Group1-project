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
                  <a href="/main/Person_2">Profile</a>
                </li>

                <li>
                  <a href="/main/detector">Detector</a>
                </li>
                <li class="header-login-li" v-if="currentUser">
                  <router-link to="/login" class="header-login">
                    <span> {{ currentUser.data.userName }}</span>
                  </router-link>
                </li>
                <li v-if="currentUser">
                  <a href="/" @click="logOut()">Log Out</a>
                </li>
                <li class="header-login-li" v-if="!currentUser">
                   <router-link to="/login" class="header-login"><span> <i class="fa fa-user-circle"></i></span> </router-link>
                </li>
            

         
                  
                

           
                </ul>


           </nav>
           
             
          </div>
        </section>
      </div>
    </header>
    <main>
      <router-view />
      <div>wxy</div>
    </main>

    <!-- Footer Section Begin -->
    <footer class="footer">
      <div class="page-up">
        <a href="#" id="scrollToTopButton"
          ><span class="arrow_carrot-up fa fa-angle-up"></span
        ></a>
      </div>
      <div class="container">
        <div class="row">
          <div class="col-lg-3">
            <div class="footer__logo">
              <a href="./index.html"
                ><img
                  class="logo-icon"
                  src="./assets/logo.png"
                  style="height: 80px"
                  alt=""
              /></a>
            </div>
          </div>
          <div class="col-lg-6">
            <div class="footer__nav">
              <ul>
                <li class="active"><a href="./index.html">Homepage</a></li>
                <li><a href="./categories.html">Categories</a></li>
                <li><a href="./blog.html">Our Blog</a></li>
                <li><a href="#">Contacts</a></li>
              </ul>
            </div>
          </div>
          <div class="col-lg-3">
            <p>
              <!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
              Copyright All rights reserved | This template is made with
              <i class="fa fa-heart" aria-hidden="true"></i> by
              <a href="https://colorlib.com" target="_blank">Colorlib</a>
              <!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
            </p>
          </div>
        </div>
      </div>
    </footer>
    <!-- Footer Section End -->
 
  </div>
  
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

    return { currentUser, active, logOut };
  },
};
</script>

<style lang="scss">
body {
  background-color: #101018 !important;

  min-width: 400px;
  .ant-modal-body {
    padding: 0 !important;
    background-color: black;
  }
  textarea.ant-input {
    height: 150px !important;
  }
  .ant-progress-circle .ant-progress-text{
    color: white !important;
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
        font-size: 30px;
        font-weight: 900;
      }
      .span2 {
        font-size: 30px;
        vertical-align: middle;
        color: #e53637;
        font-weight: 900;
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
      // background-color: #252525;
      width: 100%;

      nav {
        display: inline-block;
        margin: 0 auto;
        // background-color: #252525;
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
    $nav-background: #0a0a13;
    $nav-font-color: #ffffff;
    $link-hover-color: #e53637;

    // Outer navigation wrapper
    .navigation {
      height: $nav-height;
      background: $nav-background;
      box-shadow: 0px 0px 15px 0px #e53637;
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

  /*---------------------
  Helper CSS
-----------------------*/

  h1,
  h2,
  h3,
  h4,
  h5,
  h6 {
    margin: 0;
    color: #111111;
    font-weight: 400;
    font-family: "Mulish", sans-serif;
  }

  h1 {
    font-size: 70px;
  }

  h2 {
    font-size: 36px;
  }

  h3 {
    font-size: 30px;
  }

  h4 {
    font-size: 24px;
  }

  h5 {
    font-size: 18px;
  }

  h6 {
    font-size: 16px;
  }

  p {
    font-size: 15px;
    font-family: "Mulish", sans-serif;
    color: #3d3d3d;
    font-weight: 400;
    line-height: 25px;
    margin: 0 0 15px 0;
  }

  img {
    max-width: 100%;
  }

  input:focus,
  select:focus,
  button:focus,
  textarea:focus {
    outline: none;
  }

  a:hover,
  a:focus {
    text-decoration: none;
    outline: none;
    color: #ffffff;
  }

  ul,
  ol {
    padding: 0;
    margin: 0;
  }

  .section-title {
    margin-bottom: 30px;
  }

  .section-title h4,
  .section-title h5 {
    color: #ffffff;
    font-weight: 600;
    line-height: 21px;
    text-transform: uppercase;
    padding-left: 20px;
    position: relative;
    font-family: "Oswald", sans-serif;
  }

  .section-title h4:after,
  .section-title h5:after {
    position: absolute;
    left: 0;
    top: -6px;
    height: 32px;
    width: 4px;
    background: #e53637;
    content: "";
  }

  .set-bg {
    background-repeat: no-repeat;
    background-size: cover;
    background-position: top center;
  }

  .spad {
    padding-bottom: 100px;
  }

  .text-white h1,
  .text-white h2,
  .text-white h3,
  .text-white h4,
  .text-white h5,
  .text-white h6,
  .text-white p,
  .text-white span,
  .text-white li,
  .text-white a {
    color: #fff;
  }

  /* buttons */

  .primary-btn {
    display: inline-block;
    font-size: 13px;
    font-weight: 700;
    text-transform: uppercase;
    color: #ffffff;
    letter-spacing: 2px;
  }

  .primary-btn span {
    font-size: 18px;
    margin-left: 5px;
    position: relative;
    top: 3px;
  }

  .site-btn {
    font-size: 13px;
    color: #ffffff;
    background: #e53637;
    font-weight: 700;
    border: none;
    border-radius: 2px;
    letter-spacing: 2px;
    text-transform: uppercase;
    display: inline-block;
    padding: 12px 30px;
  }
}

/*---------------------
  Footer
-----------------------*/

.footer {
      box-shadow: 0px 0px 15px 0px #e53637;
  background: #0a0a13;
  padding-top: 60px;
  padding-bottom: 40px;
  position: relative;
}

.page-up {
  position: absolute;
  left: 50%;
  top: -25px;
  margin-left: -25px;
}

.page-up a {
  display: inline-block;
  font-size: 36px;
  color: #ffffff;
  height: 50px;
  width: 50px;
  background: #e53637;
  line-height: 50px;
  text-align: center;
  border-radius: 50%;
}

.page-up a span {
  position: relative;
  top: 2px;
  left: -1px;
}

.footer__nav {
  text-align: center;
}

.footer__nav ul li {
  list-style: none;
  display: inline-block;
  position: relative;
  margin-right: 40px;
}

.footer__nav ul li:last-child {
  margin-right: 0;
}

.footer__nav ul li a {
  font-size: 15px;
  color: #b7b7b7;
  display: block;
  font-weight: 700;
}

.footer__copyright__text {
  color: #b7b7b7;
  margin-bottom: 0;
  text-align: right;
}

.footer__copyright__text a {
  color: #e53637;
}

/*--------------------------------- Responsive Media Quaries -----------------------------*/

@media only screen and (min-width: 1200px) and (max-width: 1300px) {
  .hero {
    overflow: hidden;
  }
}

@media only screen and (min-width: 1200px) {
  .container {
    max-width: 1170px;
  }
}

/* Medium Device = 1200px */

@media only screen and (min-width: 992px) and (max-width: 1199px) {
  .hero {
    overflow: hidden;
  }
  .login__form {
    position: relative;
    padding-left: 32px;
  }
  .login__social__links ul li a {
    width: 380px;
  }
  .blog__item__text {
    padding: 0 50px;
  }
}

/* Tablet Device = 768px */

@media only screen and (min-width: 768px) and (max-width: 991px) {
  .hero {
    overflow: hidden;
  }
  .header {
    position: relative;
  }
  .header .container {
    position: relative;
  }
  .header__right {
    position: absolute;
    right: 120px;
    top: -42px;
    padding: 0;
  }
  .header__menu {
    display: none;
  }
  .slicknav_menu {
    background: transparent;
    padding: 0;
    display: block;
  }
  .slicknav_nav {
    position: absolute;
    left: 0;
    top: 60px;
    width: 100%;
    background: #ffffff;
    padding: 15px 30px;
    z-index: 9;
  }
  .slicknav_nav ul {
    margin: 0;
  }
  .slicknav_nav .slicknav_row,
  .slicknav_nav a {
    padding: 7px 0;
    margin: 0;
    color: #111111;
    font-weight: 600;
  }
  .slicknav_btn {
    border-radius: 0;
    background-color: #222;
    position: absolute;
    right: 0;
    top: 9px;
  }
  .slicknav_nav .slicknav_arrow {
    color: #111111;
  }
  .slicknav_nav .slicknav_row:hover {
    border-radius: 0;
    background: transparent;
    color: #111111;
  }
  .slicknav_nav a:hover {
    border-radius: 0;
    background: transparent;
    color: #111111;
  }
  .product__sidebar {
    padding-top: 50px;
  }
  .footer__logo {
    text-align: center;
    margin-bottom: 20px;
  }
  .footer__nav {
    margin-bottom: 15px;
  }
  .footer__copyright__text {
    text-align: center;
  }
  .anime__details__widget ul li span {
    width: 90px;
  }
  .anime__details__pic {
    margin-bottom: 40px;
  }
  .anime__details__sidebar {
    padding-top: 50px;
  }
  .login__form {
    padding-left: 0;
    margin-bottom: 40px;
  }
  .login__form:after {
    display: none;
  }
  .login__form form .input__item {
    width: auto;
  }
  .login__register {
    padding-left: 0;
  }
  .signup .login__social__links {
    padding-left: 0;
  }
}

/* Wide Mobile = 480px */

@media only screen and (max-width: 767px) {
  .hero {
    overflow: hidden;
  }
  .header {
    position: relative;
  }
  .header .container {
    position: relative;
  }
  .header__right {
    position: absolute;
    right: 120px;
    top: -42px;
    padding: 0;
  }
  .header__menu {
    display: none;
  }
  .slicknav_menu {
    background: transparent;
    padding: 0;
    display: block;
  }
  .slicknav_nav {
    position: absolute;
    left: 0;
    top: 60px;
    width: 100%;
    background: #ffffff;
    padding: 15px 30px;
    z-index: 9;
  }
  .slicknav_nav ul {
    margin: 0;
  }
  .slicknav_nav .slicknav_row,
  .slicknav_nav a {
    padding: 7px 0;
    margin: 0;
    color: #111111;
    font-weight: 600;
  }
  .slicknav_btn {
    border-radius: 0;
    background-color: #222;
    position: absolute;
    right: 0;
    top: 9px;
  }
  .slicknav_nav .slicknav_arrow {
    color: #111111;
  }
  .slicknav_nav .slicknav_row:hover {
    border-radius: 0;
    background: transparent;
    color: #111111;
  }
  .slicknav_nav a:hover {
    border-radius: 0;
    background: transparent;
    color: #111111;
  }
  .product__sidebar {
    padding-top: 50px;
  }
  .footer__logo {
    text-align: center;
    margin-bottom: 20px;
  }
  .footer__nav {
    margin-bottom: 15px;
  }
  .footer__copyright__text {
    text-align: center;
  }
  .blog__details__title h2 {
    font-size: 34px;
    line-height: normal;
  }
  .anime__details__pic {
    margin-bottom: 40px;
  }
  .anime__details__sidebar {
    padding-top: 50px;
  }
  .btn__all {
    text-align: left;
  }
  .product__page__title .section-title {
    margin-bottom: 30px;
  }
  .product__page__title .product__page__filter {
    text-align: left;
  }
  .anime__details__rating {
    text-align: left;
    position: relative;
    margin-bottom: 20px;
  }
  .blog__details__social {
    overflow: hidden;
  }
  .blog__details__title .blog__details__social a {
    margin-right: 10px;
    margin-bottom: 10px;
    width: calc(50% - 10px);
    float: left;
  }
  .login__form {
    padding-left: 0;
    margin-bottom: 40px;
  }
  .login__form:after {
    display: none;
  }
  .login__form form .input__item {
    width: auto;
  }
  .signup .login__social__links {
    padding-left: 0;
  }
  .login__social__links ul li a {
    width: auto;
  }
  .blog__item__text {
    padding: 0 30px;
  }
  .login__register {
    padding-left: 0;
  }
  .product__sidebar__view .filter__controls li {
    margin-right: 2px;
  }
  .search-model-form input {
    width: 100%;
  }
}

/* Small Device = 320px */

@media only screen and (max-width: 479px) {
  .hero__slider.owl-carousel .owl-nav {
    display: none;
  }
  .hero__items {
    padding: 250px 0 42px 15px;
  }
  .hero__text h2 {
    font-size: 32px;
  }
  .footer__nav ul li {
    margin-right: 10px;
  }
  .anime__details__btn .follow-btn {
    padding: 14px 26px;
    margin-right: 11px;
    margin-bottom: 25px;
  }
  .anime__details__widget ul li span {
    width: 85px;
  }
  .anime__video__player .plyr__volume {
    left: 65px;
  }
  .anime__video__player .plyr__controls .plyr__controls__item.plyr__time {
    left: 95px;
  }
  .anime__video__player .plyr__menu {
    margin-right: 60px;
  }
  .blog__details__title h2 {
    font-size: 30px;
    line-height: normal;
  }
  .blog__details__title .blog__details__social a {
    padding: 16px 25px 14px 20px;
  }
  .blog__details__comment__item.blog__details__comment__item--reply {
    padding-left: 0;
  }
  .blog__details__comment__item__pic {
    margin-right: 25px;
  }
  .blog__details__comment__item__text a {
    margin-right: 6px;
  }
  .login__social__links ul li a i {
    left: 20px;
  }
  .login__form .forget_pass {
    position: relative;
    left: 0;
    bottom: 0;
    margin-top: 25px;
  }
  .header__right a {
    margin-right: 10px;
  }
  .anime__review__item__text h6 span {
    font-size: 12px;
  }
  .anime__review__item__text {
    padding: 18px 20px 20px;
  }
}
.form-control {
  display: block;
  width: 100%;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  color: #402B2B;
  background-color: #F5F5F5;
  background-clip: padding-box;
  border: 1px solid #E0E0E0;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  border-radius: 0.5rem;
  -webkit-transition: border-color 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out;
  transition: border-color 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out;
  -o-transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
  transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
  transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out;
}
</style>
