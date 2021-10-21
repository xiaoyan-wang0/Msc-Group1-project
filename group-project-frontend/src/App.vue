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
import {
  LoginOutlined,
  LogoutOutlined,
  UserOutlined,
  RightCircleOutlined,
} from "@ant-design/icons-vue";

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
  }
}
</style>
