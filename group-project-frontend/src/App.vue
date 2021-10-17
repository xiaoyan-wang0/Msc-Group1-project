<template>
  <div>
    <header>
      <router-link to="/">
        <h1><span>AM</span>DB</h1>
      </router-link>
      <div class="logicon" v-if="!currentUser">
        <router-link to="/login">
          <a-tooltip placement="topLeft" color="blue">
            <template #title>
              <span>LOGIN</span>
            </template>
            <LoginOutlined :spin="true" style="margin-right: 20px" />
          </a-tooltip>
        </router-link>

        <router-link to="/">
          <a-tooltip placement="topLeft" color="blue">
            <template #title>
              <span>LOGOUT</span>
            </template>
            <LogoutOutlined :spin="true" /> </a-tooltip
        ></router-link>
      </div>
      <div v-if="currentUser" class="logicon">
        <li class="nav-item">
          <router-link to="/profile" class="nav-link">
            <font-awesome-icon icon="user" />
            {{ currentUser.username }}
          </router-link>
        </li>
        <li class="nav-item">
          <a class="nav-link" @click.prevent="logOut">
            <font-awesome-icon icon="sign-out-alt" /> LogOut
          </a>
        </li>
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
import { computed } from "vue";
import { useStore } from "vuex";
import router from "@/router";
import { LoginOutlined, LogoutOutlined } from "@ant-design/icons-vue";

export default {
  components: { LoginOutlined, LogoutOutlined },
  setup() {
    const store = useStore();
    const currentUser = computed(() => store.state.auth.user);
    const logOut = () => {
      store.dispatch("auth/logout");
      router.push("/");
    };
    return { currentUser, logOut };
  },
};
</script>

<style lang="scss">
body {
  background-color: #080808 !important;
  .ant-modal-body {
    padding: 0 !important;
    background-color: black;
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
      margin-top: 20px;

      span {
        color: #42b883;
      }
    }

    .logicon {
      color: #fff;
      font-size: 40px;
      position: absolute;
      right: 30px;
    }
  }
}
</style>
