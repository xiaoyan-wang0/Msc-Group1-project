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
                  <button
                    id="submit"
                    type="submit"
                    class="site-btn"
                    :disabled="isLoading"
                  >
                    {{ isLoading ? "Loading..." : "LogIn" }}
                  </button>
                </div>
              </form>
            </div>
          </div>

          <div class="col-lg-6">
            <div class="login__register">
              <h3>Don't Have An Account?</h3>
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
                    <v-facebook-login
                      style="display: none"
                      @login="faceboogLogin"
                      @logout="faceboogLogin"
                      app-id="903265547247503"
                    ></v-facebook-login>
                    <a @click="logInWithFacebook" class="facebook"
                      ><i
                        class="fab fa-facebook"
                        @click="logInWithFacebook"
                      ></i>
                      Sign in With Facebook</a
                    >
                  </li>
                  <li>
                    <a href="#" class="google" style="display: none"
                      ><i class="fab fa-google"></i> Sign in With Google</a
                    >
                  </li>
                  <li>
                    <a href="#" class="twitter" style="display: none"
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
import { ref, defineComponent, onMounted, inject, onBeforeMount } from "vue";
import { message } from "ant-design-vue";
import {
  GoogleOutlined,
  FacebookOutlined,
  TwitterOutlined,
} from "@ant-design/icons-vue";
import router from "@/router";
import { useStore } from "vuex";
import VFacebookLogin from "vue-facebook-login-component-next";
import { VFBLoginScope as VFacebookLoginScope } from "vue-facebook-login-component-next";
import env from "@/env.js";

export default defineComponent({
  name: "Login",
  components: {
    GoogleOutlined,
    FacebookOutlined,
    TwitterOutlined,
    VFacebookLoginScope,
    VFacebookLogin,
  },
  setup() {
    const axios = inject("axios"); // inject axios
    const store = useStore();
    const isLoading = ref(false);
    const fbSignInParams = ref({
      scope: "email,user_likes",
      return_scopes: true,
    });

    const loginMes = ref({
      username: "",
      password: "",
      email: "",
    });

    onBeforeMount(() => {
      if (localStorage.getItem("user")) {
        router.push({ name: "Setting" });
      }
    });

    /**
     * Login submit event.
     */
    const onSubmitLogin = () => {
      isLoading.value = true;
      const loginFormData = new FormData();
      loginFormData.append("email", loginMes.value.email);
      loginFormData.append("password", loginMes.value.password);

      store.dispatch("auth/login", loginFormData).then(
        (response) => {

          if (response.code === -1) {
            isLoading.value = false;
            message.error(response.msg, () => {
            });
          } else if (response.code === 200) {
            message.success(response.msg + ", Will return in 3s.", () => {
              router.push({ name: "Home" });
              isLoading.value = false;
            });
          }
        },
        (error) => {
          showErroeMessage();
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

    /**
     * Format img url.
     * @item  data
     */
    const faceboogLogin = (value) => {
    };

    /**
     * Check email exist.
     * @data  Email
     */
    const checkEmail = (data) => {
      // Fetch checkEmail
      axios
        .get(env.AMDBAPI + "admin/getUser?email=" + data.email)
        .then((response) => {
          if (response.data.code === -1) {
            const registerFormData = new FormData();
            registerFormData.append("userName", data.name);
            registerFormData.append("email", data.email);
            registerFormData.append("password", "12345678");
            store.dispatch("auth/register", registerFormData).then(
              (response) => {
                if (response.code === -1) {
                  message.error(response.msg, () => {
                  });
                } else if (response.code === 200) {
                  message.success(
                    response.msg + ", Will return setting page in 3s.",
                    () => {
                      location.reload();
                    }
                  );
                }
              },
              (error) => {
                showErroeMessage();
              }
            );
          } else if (response.data.code === 200) {
            const loginFormData = new FormData();
            loginFormData.append("email", data.email);
            loginFormData.append("password", 12345678);

            store.dispatch("auth/login", loginFormData).then(
              (response) => {

                if (response.code === -1) {
                  message.error(response.msg, () => {
                  });
                } else if (response.code === 200) {
                  message.success(response.msg + ", Will return in 3s.", () => {
                    router.push({ name: "Home" });
                  });
                }
              },
              (error) => {
                showErroeMessage();
              }
            );
          }
        })
        .catch((error) => {
          showErroeMessage();
        });
    };

    const logInWithFacebook = async () => {
      await loadFacebookSDK(document, "script", "facebook-jssdk");
      await initFacebook();
      window.FB.login(
        function (response) {
          if (response.authResponse) {
            // alert("You are logged in &amp; cookie set!");
            FB.api("/me?fields=id,name,email", function (response) {
              checkEmail(response);
            });
            window.close();
            // Now you can redirect the user or do an AJAX request to
            // a PHP script that grabs the signed request from the cookie.
          } else {
            alert("User cancelled login or did not fully authorize.");
          }
        },
        {
          scope: "email",
        }
      );
      return false;
    };

    const initFacebook = async () => {
      window.fbAsyncInit = function () {
        window.FB.init({
          appId: "903265547247503", //You will need to change this
          cookie: true, // This is important, it's not enabled by default
          xfbml: true,
          version: "v13.0",
        });
      };
    };

    const loadFacebookSDK = async (d, s, id) => {
      var js,
        fjs = d.getElementsByTagName(s)[0];
      if (d.getElementById(id)) {
        return;
      }
      js = d.createElement(s);
      js.id = id;
      js.src = "https://connect.facebook.net/en_US/sdk.js";
      fjs.parentNode.insertBefore(js, fjs);
    };
    const showErroeMessage = () => {
      isLoading.value = false;
      return message.error("Server is busy, try again later");
    };

    return {
      loginMes,
      isLoading,
      activeKey: ref("1"),
      fbSignInParams,
      onSubmitLogin,
      faceboogLogin,
      logInWithFacebook,
    };
  },
});
</script>

<style lang="scss" scoped>
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
  padding-top: 50px;
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
  width: 330px;
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