<template>
  <header>
    <router-link to="/">
      <h1><span>Vue</span>Movie</h1>
    </router-link>
  </header>
  <main>
    <router-view />
  </main>

  <footer>
    <div class="footer"></div>
  </footer>
</template>

<style lang="scss">
body {
  // background-color: #35495e !important;
  background-color: #222b32 !important;
  // background-image: radial-gradient(
  //     white,
  //     rgba(255, 255, 255, 0.2) 2px,
  //     transparent 40px
  //   ),
  //   radial-gradient(white, rgba(255, 255, 255, 0.15) 1px, transparent 30px),
  //   radial-gradient(white, rgba(255, 255, 255, 0.1) 2px, transparent 40px),
  //   radial-gradient(
  //     rgba(255, 255, 255, 0.4),
  //     rgba(255, 255, 255, 0.1) 2px,
  //     transparent 30px
  //   );
  // background-size: 550px 550px, 350px 350px, 250px 250px, 150px 150px;
  // background-position: 0 0, 40px 60px, 130px 270px, 70px 100px;
  .ant-modal-body {
    padding:  0 !important;
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

    h1 {
      color: #fff;
      font-size: 28px;

      span {
        color: #42b883;
      }
    }
  }
}
</style>
