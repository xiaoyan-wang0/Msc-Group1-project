<template>
  <div class="login-page">
    <div class="form-body">
      <div class="row">
        <div class="form-holder">
          <div class="form-content">
            <div class="form-items">
              <h3>Sign In</h3>
              <p></p>
              <form class="login-requires-validation" novalidate>
                <!-- <div class="col-md-12">
                  <input
                    class="form-control"
                    type="text"
                    name="name"
                    placeholder="Username"
                    required
                    v-model="loginMes.username"
                  />
                  <div class="valid-feedback">Username field is valid!</div>
                  <div class="invalid-feedback">
                    Username field cannot be blank!
                  </div>
                </div> -->

                <div class="col-md-12">
                  <input
                    class="form-control"
                    type="email"
                    name="email"
                    v-model="loginMes.email"
                    placeholder="E-mail Address"
                    required
                  />
                  <div class="valid-feedback">Email field is valid!</div>
                  <div class="invalid-feedback">
                    Email field cannot be blank!
                  </div>
                </div>

                <div class="col-md-12">
                  <input
                    class="form-control"
                    type="password"
                    name="password"
                    placeholder="Password"
                    v-model="loginMes.password"
                    required
                  />
                  <div class="valid-feedback">Password field is valid!</div>
                  <div class="invalid-feedback">
                    Password field cannot be blank!
                  </div>
                </div>

                <div class="form-check">
                  <input
                    class="form-check-input"
                    type="checkbox"
                    value=""
                    id="invalidCheck"
                    required
                  />
                  <label class="form-check-label"
                    >I confirm that all data are correct</label
                  >
                  <div class="invalid-feedback">
                    Please confirm that the entered data are all correct!
                  </div>
                </div>

                <div class="form-button mt-3">
                  <button id="submit" type="submit" class="btn btn-primary">
                    LogIn
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, defineComponent, onMounted } from "vue";
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
    };

    onMounted(() => {
      const forms = document.querySelectorAll(".login-requires-validation");
      Array.from(forms).forEach(function (form) {
        form.addEventListener(
          "submit",
          function (event) {
            if (!form.checkValidity()) {
              event.preventDefault();
              event.stopPropagation();
            } else {
              event.preventDefault();
              event.stopPropagation();
              onSubmitLogin();
            }

            form.classList.add("was-validated");
          },
          false
        );
      });
    });
    return { loginMes, onSubmitLogin, activeKey: ref("1") };
  },
});
</script>

<style lang="scss" scoped>
.login-page {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;

  overflow: hidden;

  font-family: "Poppins", sans-serif;
  font-weight: 400;
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
  -moz-osx-font-smoothing: grayscale;
  .form-holder {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    min-height: 100vh;
  }

  .form-holder .form-content {
    position: relative;
    text-align: center;
    display: -webkit-box;
    display: -moz-box;
    display: -ms-flexbox;
    display: -webkit-flex;
    display: flex;
    -webkit-justify-content: center;
    justify-content: center;
    -webkit-align-items: center;
    align-items: center;
    padding: 60px;
  }

  .form-content .form-items {
    border: 3px solid #fff;
    padding: 40px;
    display: inline-block;
    width: 100%;
    min-width: 540px;
    -webkit-border-radius: 10px;
    -moz-border-radius: 10px;
    border-radius: 10px;
    text-align: left;
    -webkit-transition: all 0.4s ease;
    transition: all 0.4s ease;
  }

  .form-content h3 {
    color: #fff;
    text-align: left;
    font-size: 28px;
    font-weight: 600;
    margin-bottom: 5px;
  }

  .form-content h3.form-title {
    margin-bottom: 30px;
  }

  .form-content p {
    color: #fff;
    text-align: left;
    font-size: 17px;
    font-weight: 300;
    line-height: 20px;
    margin-bottom: 30px;
  }

  .form-content label,
  .was-validated .form-check-input:invalid ~ .form-check-label,
  .was-validated .form-check-input:valid ~ .form-check-label {
    color: #fff;
  }
  .form-check {
    margin-top: 15px;
  }

  .form-content input[type="text"],
  .form-content input[type="password"],
  .form-content input[type="email"],
  .form-content select {
    width: 100%;
    padding: 9px 20px;
    text-align: left;
    border: 0;
    outline: 0;
    border-radius: 6px;
    background-color: #fff;
    font-size: 15px;
    font-weight: 300;
    color: #8d8d8d;
    -webkit-transition: all 0.3s ease;
    transition: all 0.3s ease;
    margin-top: 16px;
  }

  .btn-primary {
    background-color: #6c757d;
    outline: none;
    border: 0px;
    box-shadow: none;
  }

  .btn-primary:hover,
  .btn-primary:focus,
  .btn-primary:active {
    background-color: #495056;
    outline: none !important;
    border: none !important;
    box-shadow: none;
  }

  .form-content textarea {
    position: static !important;
    width: 100%;
    padding: 8px 20px;
    border-radius: 6px;
    text-align: left;
    background-color: #fff;
    border: 0;
    font-size: 15px;
    font-weight: 300;
    color: #8d8d8d;
    outline: none;
    resize: none;
    height: 120px;
    -webkit-transition: none;
    transition: none;
    margin-bottom: 14px;
  }

  .form-content textarea:hover,
  .form-content textarea:focus {
    border: 0;
    background-color: #ebeff8;
    color: #8d8d8d;
  }

  .mv-up {
    margin-top: -9px !important;
    margin-bottom: 8px !important;
  }

  .invalid-feedback {
    color: #ff606e;
  }

  .valid-feedback {
    color: #2acc80;
  }
}
</style>