<template>
  <div class="login-page">
    <div id="loginDiv">
      <form action="" id="login-form" method="post">
        <h1 style="text-align: center; color: aliceblue">Login</h1>
        <p>
          Username:<input id="userNname" type="text" /><label
            id="name_trip"
          ></label>
        </p>

        <p>
          Password: <input id="password" type="password" /><label
            id="password_trip"
          ></label>
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
import {
  UserOutlined,
  LockOutlined,
  MailOutlined,
} from "@ant-design/icons-vue";
import { ref, defineComponent, reactive } from "vue";
export default defineComponent({
  name: "Login",
  components: { UserOutlined, LockOutlined, MailOutlined },

  setup() {
    return {};
  },
});
</script>

<style lang="scss" scoped>
.login-page {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}
#loginDiv {
  width: 37%;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 300px;
  background-color: rgba(75, 81, 95, 0.3);
  box-shadow: 7px 7px 17px rgba(52, 56, 66, 0.5);
  border-radius: 5px;
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
  width: 140px;
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