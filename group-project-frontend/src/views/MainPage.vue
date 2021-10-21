<template>
  <div class="div-main">
    <div class="div-main-left">
      <img class="logo-icon" src="../assets/TUD_White.png" />
      <!-- MENU -->
      <div class="mainpage-menu">
        <el-menu
          active-text-color="#ffd04b"
          background-color="#545c64"
          class="el-menu-vertical-demo"
          default-active="/main/home"
          text-color="#fff"
          :router="true"
        >
          <el-menu-item index="/main/home">
            <template #title>
              <i class="el-icon-location"></i>
              <span>M O V I E S</span>
            </template>
          </el-menu-item>
          <el-menu-item index="2" disabled>
            <i class="el-icon-menu"></i>
            <span>Entertaiment</span>
          </el-menu-item>
          <el-menu-item index="/main/profile">
            <i class="el-icon-document"></i>
            <span>Profile</span>
          </el-menu-item>
          <el-menu-item index="/main/detector">
            <i class="el-icon-setting"></i>
            <span>Detector</span>
          </el-menu-item>
        </el-menu>
      </div>
    </div>
    <div class="div-main-right">
      <router-view />
    </div>
  </div>
</template>

<script>
import { ElCarousel } from "element-plus";
import { ref, inject, onBeforeMount } from "vue";
import env from "@/env.js";
import Showpart from "@/components/ShowPart.vue";
export default {
  name: "Home",
  components: {},
  setup() {
    return {};
  },
};
</script>

<style lang="scss">
.div-main {
  float: left;
  width: 100%;
  height: 180px;
  .mainpage-menu {
    margin-top: 100px;
  }
}
.div-main-left {
  float: left;
  // background-color: rgb(136, 136, 161);
  width: 20%;
  height: 180px;
  text-align: center;
  .logo-icon {
    width: 50%;
  }
}
.div-main-right {
  width: 80%;
  float: right;
}
</style>