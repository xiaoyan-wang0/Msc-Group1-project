<template>
 
  <div class="div-main">
    
      
    
    <!-- <div class="div-main-left"> -->
      <!-- <img class="logo-icon" src="./assets/logo.png" /> -->
      <!-- MENU -->
      <!-- <div class="mainpage-menu">
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
      </div> -->
    <!-- </div> -->
    <div class="div-main-content">
 
       <form class="search-model-form">
         <input type="text" id="search-input" placeholder="Search here....."><span class="fa fa-2x fa-search" style="color:#E53637"></span>
        </form> 
      <router-view />
    </div>
  </div>
</template>

<script>
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
  margin: auto;
  margin-top: 10px;
  .div-main-content{
  width: 80%;
  margin: auto;}
}


</style>