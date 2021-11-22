<template>
  <div class="div-main">
    <div class="div-main-content">
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