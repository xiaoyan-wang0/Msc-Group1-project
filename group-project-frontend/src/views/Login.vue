<template>
  <div class="login-page">
    <div id="loginDiv">
      <!-- <a-tabs type="card" v-model:activeKey="activeKey">
        <a-tab-pane key="1" tab="Tab 1">Content of Tab Pane 1</a-tab-pane>
        <a-tab-pane key="2" tab="Tab 2">Content of Tab Pane 2</a-tab-pane>
        <a-tab-pane key="3" tab="Tab 3">Content of Tab Pane 3</a-tab-pane>
      </a-tabs> -->
      <form id="login-form" @submit.prevent="onSubmitLogin()">
        <h1 style="text-align: center; color: aliceblue">Login</h1>
        <!-- <p>
          Username:<input id="username" type="text" required 
            v-model="loginMes.username"/>
        </p> -->

        <div class="login-icon">
          <GoogleOutlined :style="{ fontSize: '50px', color: '#fff' }" />
          <FacebookOutlined :style="{ fontSize: '50px', color: '#fff' }" />
          <TwitterOutlined :style="{ fontSize: '50px', color: '#fff' }" />
        </div>
        <p>
          Email&nbsp;:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input
            id="email"
            type="email"
            required
            v-model="loginMes.email"
          />
        </p>
        <p>
          Password:
          <input
            id="password"
            type="password"
            required
            v-model="loginMes.password"
          />
        </p>

        <div style="text-align: center; margin-top: 30px">
          <input type="submit" class="button" value="Login" />

          <router-link to="/register">
            <input type="register" class="register-button" value="Register"
          /></router-link>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { ref, defineComponent } from "vue";
import { message } from "ant-design-vue";
import {
  GoogleOutlined,
  FacebookOutlined,
  TwitterOutlined,
} from "@ant-design/icons-vue";
import router from "@/router";
import { useStore } from "vuex";
export default defineComponent({
  name: "Login",
  components: { GoogleOutlined, FacebookOutlined, TwitterOutlined },

  setup() {
    const store = useStore();

    const loginMes = ref({
      username: "",
      password: "",
      email: "",
    });

    //Login event
    const onSubmitLogin = () => {
      const loginFormData = new FormData();
      console.log("resploginMes.email");
      console.log(loginMes.value.email);
      console.log("loginMes.password");
      console.log(loginMes.value.password);
      loginFormData.append("email", loginMes.value.email);
      loginFormData.append("password", loginMes.value.password);

      store.dispatch("auth/login", loginFormData).then(
        (response) => {
          console.log("LOGIN");
          console.log(response);

          if (response.code === -1) {
            message.error(response.msg, () => {
              console.log("onClose");
            });
          } else if (response.code === 200) {
            message.success(response.msg + ", Will return in 3s.", () => {
              router.push({ name: "Home" });
            });
          }
        },
        (error) => {
          console.log("login error");
          console.log(error);
        }
      );
      //Login
      // axios({
      //   method: "post",
      //   url: "/api/member/login",
      //   data: loginFormData,
      //   headers: { "Content-Type": "multipart/form-data" },
      // }).then(
      //   (response) => {
      //     console.log("response");
      //     console.log(response);
      //     if (response.data.code === -1) {
      //       message.error(response.data.msg, () => {
      //         console.log("onClose");
      //       });
      //     } else if (response.data.code === 200) {
      //       message.success(response.data.msg + ", Will return in 3s.", () => {
      //         router.push({ name: "Home" });
      //       });
      //     }
      //   },
      //   (error) => {
      //   }
      // );
    };
    return { loginMes, onSubmitLogin, activeKey: ref("1") };
  },
});
</script>

<style lang="scss" scoped>
.ant-modal-body {
  background-color: rgb(235, 235, 235) !important;
}
.login-page {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}
#loginDiv {
  width: 45%;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 400px;
  background-color: rgba(75, 81, 95, 0.3);
  box-shadow: 7px 7px 17px rgba(52, 56, 66, 0.5);
  border-radius: 5px;
  .login-icon {
    display: flex;
    padding-left: 70px;
    padding-right: 50px;
    justify-content: space-between;
  }
}

#name_trip {
  margin-left: 50px;
  color: red;
}

p {
  margin-top: 30px;
  margin-left: 20px;
  color: azure;
}

input {
  margin-left: 15px;
  border-radius: 5px;
  border-style: hidden;
  height: 30px;
  width: 240px;
  background-color: rgba(216, 191, 216, 0.5);
  outline: none;
  color: #f0edf3;
}

.button {
  border-color: cornsilk;
  background-color: rgba(55, 98, 179, 0.7);
  color: aliceblue;
  border-style: hidden;
  border-radius: 5px;
  width: 80px;
  height: 31px;
  font-size: 16px;
}
.register-button {
  padding: 10px;
  margin-left: 15px;
  border-color: cornsilk;
  background-color: rgba(55, 98, 179, 0.7);
  color: aliceblue;
  border-style: hidden;
  border-radius: 5px;
  width: 80px;
  height: 31px;
  font-size: 16px;
}
</style>