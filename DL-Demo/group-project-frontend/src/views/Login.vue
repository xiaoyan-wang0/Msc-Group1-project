<template>
  <div>
    <section
      class="normal-breadcrumb set-bg"
      data-setbg="img/normal-breadcrumb.jpg"
    >
      <div class="container">
        <div class="row">
          <div class="col-lg-12 text-center">
            <div class="normal__breadcrumb__text">
              <h2>Login</h2>
              <p>Welcome to AMDB</p>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- Normal Breadcrumb End -->

    <!-- Login Section Begin -->
    <section class="login spad">
      <div class="container">
        <div class="row">
          <div class="col-lg-6">
            <div class="login__form">
              <h3>Login</h3>
              <p></p>
              <form class="login-requires-validation" novalidate>
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
                <p></p>
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
                <p></p>
                <div class="form-check">
                  <input
                    class="form-check-input"
                    type="checkbox"
                    value=""
                    id="invalidCheck"
                    required
                  />
                  <label class="form-check-label" style="color: white"
                    >I confirm that all data are correct</label
                  >
                  <div class="invalid-feedback">
                    Please confirm that the entered data are all correct!
                  </div>
                </div>

                <div class="form-button mt-3">
                  <button id="submit" type="submit" class="site-btn">
                    LogIn
                  </button>
                </div>
              </form>
            </div>
          </div>

          <div class="col-lg-6">
            <div class="login__register">
              <h3>Dont’t Have An Account?</h3>
              <a href="/register" class="primary-btn">Register Now</a>
            </div>
          </div>
        </div>
        <div class="login__social">
          <div class="row d-flex justify-content-center">
            <div class="col-lg-6">
              <div class="login__social__links">
                <span>or</span>
                <ul>
                  <li>
                    <a href="#" class="facebook"
                      ><i class="fab fa-facebook"></i> Sign in With Facebook</a
                    >
                  </li>
                  <li>
                    <a href="#" class="google"
                      ><i class="fab fa-google"></i> Sign in With Google</a
                    >
                  </li>
                  <li>
                    <a href="#" class="twitter"
                      ><i class="fab fa-twitter"></i> Sign in With Twitter</a
                    >
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
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

/*---------------------
  Breadcrumb
-----------------------*/

.breadcrumb-option {
  padding-top: 35px;
}

.breadcrumb__links a {
  font-size: 15px;
  color: #ffffff;
  margin-right: 18px;
  display: inline-block;
  position: relative;
}

.breadcrumb__links a i {
  margin-right: 5px;
  color: #e53637;
}

.breadcrumb__links a:after {
  position: absolute;
  right: -14px;
  top: 0;
  content: "";
  font-family: "FontAwesome";
}

.breadcrumb__links span {
  font-size: 15px;
  color: #b7b7b7;
  display: inline-block;
}

/*---------------------
    Normal Breadcrumb
-----------------------*/

.normal-breadcrumb {
  height: 300px;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  justify-content: center;
}

.normal__breadcrumb__text h2 {
  color: #ffffff;
  font-size: 48px;
  font-family: "Oswald", sans-serif;
  font-weight: 700;
  margin-bottom: 22px;
}

.normal__breadcrumb__text p {
  color: #ffffff;
  font-size: 24px;
  margin-bottom: 0;
}

/*---------------------
  Login
-----------------------*/

.login {
  padding-top: 130px;
  padding-bottom: 120px;
}

.login__form {
  position: relative;
  padding-left: 145px;
}

.login__form:after {
  position: absolute;
  right: -14px;
  top: -40px;
  height: 330px;
  width: 1px;
  background: rgba(255, 255, 255, 0.2);
  content: "";
}

.login__form h3 {
  color: #ffffff;
  font-weight: 700;
  font-family: "Oswald", sans-serif;
  margin-bottom: 30px;
}

.login__form form .input__item {
  position: relative;
  width: 370px;
  margin-bottom: 20px;
}

.login__form form .input__item:before {
  position: absolute;
  left: 50px;
  top: 10px;
  height: 30px;
  width: 1px;
  background: #b7b7b7;
  content: "";
}

.login__form form .input__item input {
  height: 50px;
  width: 100%;
  font-size: 15px;
  color: #b7b7b7;
  background: #ffffff;
  border: none;
  padding-left: 76px;
}

.login__form form .input__item input::-webkit-input-placeholder {
  color: #b7b7b7;
}

.login__form form .input__item input::-moz-placeholder {
  color: #b7b7b7;
}

.login__form form .input__item input:-ms-input-placeholder {
  color: #b7b7b7;
}

.login__form form .input__item input::-ms-input-placeholder {
  color: #b7b7b7;
}

.login__form form .input__item input::placeholder {
  color: #b7b7b7;
}

.login__form form .input__item span {
  color: #b7b7b7;
  font-size: 20px;
  position: absolute;
  left: 15px;
  top: 13px;
}

.login__form form button {
  border-radius: 0;
  margin-top: 10px;
}

.login__form .forget_pass {
  font-size: 15px;
  color: #ffffff;
  display: inline-block;
  position: absolute;
  right: 60px;
  bottom: 12px;
}

.login__register {
  padding-left: 30px;
}

.login__register h3 {
  color: #ffffff;
  font-weight: 700;
  font-family: "Oswald", sans-serif;
  margin-bottom: 30px;
}

.login__register .primary-btn {
  background: #e53637;
  padding: 12px 42px;
}

.login__social {
  padding-top: 52px;
}

.login__social__links {
  text-align: center;
}

.login__social__links span {
  color: #ffffff;
  display: block;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  margin-bottom: 30px;
}

.login__social__links ul li {
  list-style: none;
  margin-bottom: 15px;
}

.login__social__links ul li:last-child {
  margin-bottom: 0;
}

.login__social__links ul li a {
  color: #ffffff;
  display: block;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  width: 460px;
  padding: 14px 0;
  position: relative;
  margin: 0 auto;
}

.login__social__links ul li a.facebook {
  background: #4267b2;
}

.login__social__links ul li a.google {
  background: #ff4343;
}

.login__social__links ul li a.twitter {
  background: #1da1f2;
}

.login__social__links ul li a i {
  font-size: 20px;
  position: absolute;
  left: 32px;
  top: 14px;
}
</style>