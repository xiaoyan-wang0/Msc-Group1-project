<template>
  <div class="register-page">
    <div class="registerDiv">
      <form @submit.prevent="submitRegister(this.params)">
        <h1>Register</h1>
        <p>
          Username:<input
            id="username"
            type="text"
            autofocus
            required
            v-model="registerMess.username"
            placeholder="Please enter username"
          />
        </p>

        <p>
          Password:<input
            id="password"
            type="password"
            v-model="registerMess.password"
            required
            placeholder="Must have at least 6 characters "
          />
        </p>

        <p>
          Password:<input
            id="surePassword"
            type="password"
            v-model="registerMess.surePassword"
            placeholder="Enter password again"
            required
          />
        </p>

        <p>
          Birthday:
          <input
            id="birthday"
            type="date"
            placeholder="Enter password again"
            v-model="registerMess.birthday"
          />
        </p>

        <p class="interests">
          Interests:
          <a-checkable-tag
            v-model:checked="registerMess.isAction"
            effect="light"
            >Action</a-checkable-tag
          >
          <a-checkable-tag v-model:checked="registerMess.isComedy"
            >Comedy</a-checkable-tag
          >
          <a-checkable-tag v-model:checked="registerMess.isFantasy"
            >Fantasy</a-checkable-tag
          >
          <a-checkable-tag v-model:checked="registerMess.isThriller"
            >Thriller</a-checkable-tag
          >
        </p>
        <p class="interests2">
          <a-checkable-tag v-model:checked="registerMess.isHorror"
            >Horror</a-checkable-tag
          >
          <a-checkable-tag v-model:checked="registerMess.isMystery"
            >Mystery</a-checkable-tag
          >
          <a-checkable-tag v-model:checked="registerMess.isDrama"
            >Drama</a-checkable-tag
          >
          <a-checkable-tag v-model:checked="registerMess.isRomance"
            >Romance</a-checkable-tag
          >
        </p>
        <p>
          Email:
          <input
            id="email"
            class="email"
            type="email"
            required
            v-model="registerMess.email"
            placeholder="Please enter email address"
          />
        </p>

        <p style="text-align: center">
          <input type="submit" class="button" value="submit" />
          <router-link to="/login">
            <input type="reset" class="button" value="return"
          /></router-link>
        </p>
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
import { ref, defineComponent, inject } from "vue";
import { message } from "ant-design-vue";
import router from "@/router";
export default defineComponent({
  name: "Login",
  components: { UserOutlined, LockOutlined, MailOutlined },

  setup() {
    const axios = inject("axios"); // inject axios
    const registerMess = ref({
      username: "",
      password: "",
      birthday: "",
      interests: "",
      email: "",
      surePassword: "",
      isAction: false,
      isComedy: false,
      isDrama: false,
      isFantasy: false,
      isHorror: false,
      isMystery: false,
      isRomance: false,
      isThriller: false,
    });
    const submitRegister = () => {
      console.log("registerMess");
      console.log(registerMess.value);
      const registerFormData = new FormData();
      registerFormData.append("userName", registerMess.value.username);
      registerFormData.append("email", registerMess.value.email);
      registerFormData.append("password", registerMess.value.password);
      //Login
      axios({
        method: "post",
        url: "/api/member/reg",
        data: registerFormData,
        headers: { "Content-Type": "multipart/form-data" },
      }).then(
        (response) => {
          console.log("response");
          console.log(response);
          if (response.data.code === -1) {
            message.error(response.data.msg, () => {
              console.log("onClose");
            });
          } else if (response.data.code === 200) {
            message.success(response.data.msg + ", Will return in 3s.", () => {
              router.push({ name: "Login" });
              console.log("onClose");
            });
          }
        },
        (error) => {
          console.log("error");
          console.log(error);
        }
      );
    };
    return { registerMess, submitRegister };
  },
});
</script>



<style lang="scss" scoped>
.register-page {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}
.registerDiv {
  width: 37%;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 650px;
  background-color: rgba(75, 81, 95, 0.3);
  box-shadow: 7px 7px 17px rgba(52, 56, 66, 0.5);
  border-radius: 5px;
}

p {
  margin-top: 10px;
  margin-left: 20px;
  color: azure;
}
.interests2 {
  margin-left: 76px;
}
.interests2 > input {
  width: 30px;
  height: 17px;
}
.interests > input {
  width: 30px;
  height: 17px;
}

input,
select {
  margin-left: 15px;
  border-radius: 5px;
  border-style: hidden;
  height: 30px;
  width: 200px;
  outline: none;
  color: #000000;
  padding-left: 10px;
}

.button {
  border-color: cornsilk;
  background-color: rgba(100, 149, 237, 0.7);
  color: aliceblue;
  border-style: hidden;
  border-radius: 5px;
  width: 100px;
  height: 31px;
  font-size: 16px;
}

.introduce {
  margin-left: 110px;
}

.introduce > textarea {
  background-color: rgba(216, 191, 216, 0.5);
  border-style: hidden;
  outline: none;
  border-radius: 5px;
}

h1 {
  text-align: center;
  margin-bottom: 20px;
  margin-top: 20px;
  color: #f0edf3;
}

b {
  margin-left: 50px;
  color: #ffeb3b;
  font-size: 10px;
  font-weight: initial;
}
.email {
  margin-left: 30px;
}
</style>