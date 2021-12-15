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
              <h2>Sign Up</h2>
              <p>Welcome to AMDB</p>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section class="signup spad">
      <div class="container">
        <div class="row">
          <div class="col-lg-6">
            <div class="login__form">
              <h3>Register</h3>
              <p></p>
              <form class="requires-validation" novalidate>
                <div class="col-md-12">
                  <input
                    class="form-control"
                    type="text"
                    name="name"
                    v-model="registerMess.username"
                    placeholder="Username"
                    required
                  />
                  <div class="valid-feedback">Username field is valid!</div>
                  <div class="invalid-feedback">
                    Username field cannot be blank!
                  </div>
                </div>

                <p></p>
                <div class="col-md-12">
                  <input
                    class="form-control"
                    type="email"
                    name="email"
                    v-model="registerMess.email"
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
                    v-model="registerMess.password"
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
                  <label class="form-check-label" style="color: white"
                    >I confirm that all data are correct</label
                  >
                  <div class="invalid-feedback">
                    Please confirm that the entered data are all correct!
                  </div>
                </div>

                <div class="form-button mt-3">
                  <button id="submit" type="submit" class="site-btn">
                    Register
                  </button>
                </div>
              </form>

              <h5>Already have an account? <a href="/login">Log In!</a></h5>
            </div>
          </div>
          <div class="col-lg-6">
            <div class="login__social__links">
              <h3>Login With:</h3>
              <ul>
                <li>
                  <a href="/login" class="facebook"
                    ><i class="fab fa-facebook"></i> Sign in With Facebook</a
                  >
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import {
  UserOutlined,
  LockOutlined,
  MailOutlined,
} from "@ant-design/icons-vue";
import { ref, defineComponent, onBeforeMount, onMounted } from "vue";
import { message } from "ant-design-vue";
import router from "@/router";
import { useStore } from "vuex";
export default defineComponent({
  name: "Login",
  components: { UserOutlined, LockOutlined, MailOutlined },

  setup() {
    const store = useStore();
    const registerMess = ref({
      username: "",
      password: "",
      gender: "",
      email: "",
    });

    onBeforeMount(() => {
      if (localStorage.getItem("user")) {
        router.push({ name: "Setting" });
      }
    });

    /**
     * Submit data for register.
     */
    const submitRegister = () => {
      const registerFormData = new FormData();
      registerFormData.append("userName", registerMess.value.username);
      registerFormData.append("email", registerMess.value.email);
      registerFormData.append("password", registerMess.value.password);
      registerFormData.append("gender", registerMess.value.gender);
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
        }
      );
    };

    onMounted(() => {
      const forms = document.querySelectorAll(".requires-validation");
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
              submitRegister();
            }

            form.classList.add("was-validated");
          },
          false
        );
      });
    });

    return { registerMess, submitRegister };
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

/*---------------------
  Sign Up
-----------------------*/

.signup {
  padding-top: 20px;
  padding-bottom: 100px;
}

.signup .login__form:after {
  height: 450px;
}

.signup .login__form h5 {
  font-size: 15px;
  color: #ffffff;
  margin-top: 36px;
}

.signup .login__form h5 a {
  color: #e53637;
  font-weight: 700;
}

.signup .login__social__links {
  text-align: left;
  padding-left: 40px;
}

.signup .login__social__links h3 {
  color: #ffffff;
  font-weight: 700;
  font-family: "Oswald", sans-serif;
  margin-bottom: 30px;
}

.signup .login__social__links ul li a {
  margin: 0;
  text-align: center;
}
</style>