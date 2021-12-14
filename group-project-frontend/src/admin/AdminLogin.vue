<template>
  <div class="body">
    <div id="layoutAuthentication">
      <div id="layoutAuthentication_content">
        <main>
          <div class="container">
            <div class="row justify-content-center">
              <div class="col-lg-5">
                <div class="card shadow-lg border-0 rounded-lg mt-5">
                  <div class="card-header">
                    <h3 class="text-center font-weight-light my-4">
                      AMDB Admin System
                    </h3>
                  </div>
                  <div class="card-body">
                    <form>
                      <div class="form-floating mb-3">
                        <input
                          class="form-control"
                          id="inputEmail"
                          type="text"
                          v-model="loginMes.username"
                          placeholder="Please enter Username"
                        />
                        <label for="inputEmail">Username</label>
                      </div>
                      <div class="form-floating mb-3">
                        <input
                          class="form-control"
                          id="inputPassword"
                          type="password"
                          v-model="loginMes.password"
                          placeholder=" Please enter Password"
                        />
                        <label for="inputPassword">Password</label>
                      </div>
                      <div
                        class="
                          d-flex
                          align-items-center
                          justify-content-between
                          mt-4
                          mb-0
                        "
                      >
                        <a class="btn btn-primary" @click="onSubmitLogin"
                          >Login</a
                        >
                      </div>
                    </form>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </main>
      </div>
      <div id="layoutAuthentication_footer">
        <footer class="py-4 bg-light mt-auto">
          <div class="container-fluid px-4">
            <div
              class="d-flex align-items-center justify-content-between small"
            >
              <div class="text-muted">Copyright &copy; AMDB 2021-2022</div>
              <div>
                <a href="#">Privacy Policy</a>
                &middot;
                <a href="#">Terms &amp; Conditions</a>
              </div>
            </div>
          </div>
        </footer>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, inject } from "vue";
import env from "@/env.js";
import { message } from "ant-design-vue";
import router from "@/router";

export default {
  name: "Login",

  setup() {
    const axios = inject("axios"); // inject axios
    const loginMes = ref({
      username: "",
      password: "",
    });
    //Login event
    const onSubmitLogin = () => {
      const loginFormData = new FormData();
      console.log("resploginMes.username");
      console.log(loginMes.value.username);
      console.log("loginMes.password");
      console.log(loginMes.value.password);
      loginFormData.append("name", loginMes.value.username);
      loginFormData.append("password", loginMes.value.password);

      axios({
        method: "post",
        url: env.AMDBAPI + "admin/adminLogin",
        data: loginFormData,
        // withCredentials: true,
        headers: { "Content-Type": "multipart/form-data" },
      })
        .then((response) => {
          console.log("onSubmitLogin");
          console.log(response);
          if (response.data.code != -1) {
            // message.success("Login Sucessfully");
            localStorage.setItem("AMDBAdmin", JSON.stringify(response.data));
            router.push({
              name: "adminHome",
            });
          } else {
            message.error("Sorry, Username or password is wrong");
          }
        })
        .catch((error) => {
          console.log("error");
          console.log(error);
          console.log("error");
          message.error("Sorry, error accured in server");
        });
    };
    return { loginMes, onSubmitLogin };
  },
};
</script>

<style lang="scss">
.body {
  background-color: #fff !important;
  -webkit-text-size-adjust: 100%;

  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
</style>