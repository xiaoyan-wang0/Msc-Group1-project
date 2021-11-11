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
                <!-- 
                <div class="col-md-12">
                  <input data-provide="datepicker">
                  <div class="valid-feedback">You selected a position!</div>
                  <div class="invalid-feedback">Please select a position!</div>
                </div> -->

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

                <div class="col-md-12 mt-3">
                  <label class="mb-3 mr-1" for="gender" style="color: white"
                    >Gender:
                  </label>

                  <input
                    type="radio"
                    class="btn-check"
                    name="gender"
                    id="male"
                    v-model="registerMess.gender"
                    autocomplete="off"
                    required
                  />
                  <label class="btn btn-sm btn-outline-secondary" for="male"
                    >Male</label
                  >

                  <input
                    type="radio"
                    class="btn-check"
                    name="gender"
                    id="female"
                    v-model="registerMess.gender"
                    autocomplete="off"
                    required
                  />
                  <label class="btn btn-sm btn-outline-secondary" for="female"
                    >Female</label
                  >

                  <input
                    type="radio"
                    class="btn-check"
                    name="gender"
                    id="secret"
                    v-model="registerMess.gender"
                    autocomplete="off"
                    required
                  />
                  <label class="btn btn-sm btn-outline-secondary" for="secret"
                    >Secret</label
                  >
                  <div class="valid-feedback mv-up">You selected a gender!</div>
                  <div class="invalid-feedback mv-up">
                    Please select a gender!
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
      console.log("Reggggggggggggg");
      console.log(localStorage.getItem("user"));
      if (localStorage.getItem("user")) {
        router.push({ name: "Setting" });
      }
    });

    const submitRegister = () => {
      console.log("registerMess");
      console.log(registerMess.value);
      const registerFormData = new FormData();
      registerFormData.append("userName", registerMess.value.username);
      registerFormData.append("email", registerMess.value.email);
      registerFormData.append("password", registerMess.value.password);
      registerFormData.append("gender", registerMess.value.gender);
      //Register

      store.dispatch("auth/register", registerFormData).then(
        (response) => {
          console.log("response");
          console.log(response);
          if (response.code === -1) {
            message.error(response.msg, () => {
              console.log("onClose");
            });
          } else if (response.code === 200) {
            message.success(
              response.msg + ", Will return setting page in 3s.",
              () => {
                // router.push({ name: "Setting" });
                location.reload();
                console.log("onClose");
              }
            );
          }
        },
        (error) => {
          console.log("error");
          console.log(error);
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
    Blog
-----------------------*/

.blog {
  padding-top: 70px;
  padding-bottom: 90px;
}

.blog__item {
  height: 580px;
  position: relative;
  margin-left: -10px;
  margin-right: -10px;
  margin-bottom: 10px;
}

.blog__item.small__item {
  height: 285px;
}

.blog__item.small__item .blog__item__text {
  padding: 0 30px;
}

.blog__item.small__item .blog__item__text p {
  margin-bottom: 5px;
}

.blog__item.small__item .blog__item__text h4 a {
  font-size: 20px;
  line-height: 30px;
}

.blog__item__text {
  position: absolute;
  left: 0;
  bottom: 25px;
  text-align: center;
  width: 100%;
  padding: 0 105px;
}

.blog__item__text p {
  color: #ffffff;
  margin-bottom: 12px;
}

.blog__item__text p span {
  color: #e53637;
  margin-right: 5px;
}

.blog__item__text h4 a {
  color: #ffffff;
  line-height: 34px;
}

/*---------------------
  Blog Details
-----------------------*/

.blog-details {
  padding-top: 70px;
}

.blog__details__title {
  text-align: center;
  margin-bottom: 70px;
}

.blog__details__title h6 {
  font-size: 15px;
  color: #ffffff;
  font-weight: 700;
  text-transform: uppercase;
  margin-bottom: 30px;
}

.blog__details__title h6 span {
  color: #b7b7b7;
  font-weight: 400;
  text-transform: none;
}

.blog__details__title h2 {
  color: #ffffff;
  font-size: 48px;
  font-weight: 700;
  line-height: 60px;
  margin-bottom: 38px;
}

.blog__details__title .blog__details__social a {
  display: inline-block;
  font-size: 15px;
  color: #ffffff;
  padding: 16px 35px 14px 20px;
  border-radius: 2px;
  margin-right: 6px;
}

.blog__details__title .blog__details__social a:last-child {
  margin-right: 0;
}

.blog__details__title .blog__details__social a.facebook {
  background: #3b5998;
}

.blog__details__title .blog__details__social a.pinterest {
  background: #ca2027;
}

.blog__details__title .blog__details__social a.linkedin {
  background: #0372b1;
}

.blog__details__title .blog__details__social a.twitter {
  background: #39a1f2;
}

.blog__details__title .blog__details__social a i {
  margin-right: 6px;
}

.blog__details__pic {
  margin-bottom: 30px;
}

.blog__details__pic img {
  min-width: 100%;
}

.blog__details__text {
  margin-bottom: 40px;
}

.blog__details__text p {
  color: #ffffff;
  font-size: 17px;
  line-height: 30px;
}

.blog__details__item__text {
  margin-bottom: 42px;
}

.blog__details__item__text h4 {
  color: #ffffff;
  font-weight: 700;
  margin-bottom: 35px;
}

.blog__details__item__text img {
  min-width: 100%;
  margin-bottom: 26px;
}

.blog__details__item__text p {
  color: #ffffff;
  font-size: 17px;
  line-height: 30px;
  margin-bottom: 0;
}

.blog__details__tags {
  margin-bottom: 60px;
}

.blog__details__tags a {
  display: inline-block;
  color: #b7b7b7;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 2px;
  margin-right: 6px;
  padding: 6px 15px;
  margin-bottom: 10px;
}

.blog__details__tags a:last-child {
  margin-right: 0;
}

.blog__details__btns {
  border-top: 1px solid rgba(255, 255, 255, 0.2);
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
  padding: 20px 0 15px;
  margin-bottom: 65px;
}

.blog__details__btns__item {
  margin-bottom: 20px;
}

.blog__details__btns__item.next__btn {
  text-align: right;
}

.blog__details__btns__item h5 a {
  font-size: 17px;
  letter-spacing: 2px;
  color: #ffffff;
}

.blog__details__btns__item h5 a span {
  font-size: 30px;
  color: #b7b7b7;
  position: relative;
  top: 8px;
}

.blog__details__comment {
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  padding-bottom: 30px;
}

.blog__details__comment h4 {
  color: #ffffff;
  font-weight: 700;
  margin-bottom: 26px;
}

.blog__details__comment__item {
  margin-bottom: 40px;
  overflow: hidden;
}

.blog__details__comment__item.blog__details__comment__item--reply {
  padding-left: 112px;
}

.blog__details__comment__item__pic {
  float: left;
  margin-right: 40px;
}

.blog__details__comment__item__text {
  overflow: hidden;
}

.blog__details__comment__item__text span {
  font-size: 14px;
  color: #b7b7b7;
  display: block;
  margin-bottom: 10px;
}

.blog__details__comment__item__text h5 {
  color: #ffffff;
  font-weight: 700;
  margin-bottom: 10px;
}

.blog__details__comment__item__text p {
  color: #b7b7b7;
  font-size: 14px;
  line-height: 22px;
  margin-bottom: 25px;
}

.blog__details__comment__item__text a {
  display: inline-block;
  color: #ffffff;
  background: rgba(255, 255, 255, 0.1);
  padding: 6px 20px;
  letter-spacing: 2px;
  border-radius: 2px;
  margin-right: 14px;
  -webkit-transition: all, 0.3s;
  -o-transition: all, 0.3s;
  transition: all, 0.3s;
}

.blog__details__comment__item__text a:hover {
  background: #e53637;
}

.blog__details__form {
  padding-top: 50px;
}

.blog__details__form h4 {
  color: #ffffff;
  font-weight: 700;
  margin-bottom: 26px;
}

.blog__details__form form input {
  height: 50px;
  width: 100%;
  background: #ffffff;
  font-size: 15px;
  color: #a6a6a6;
  padding-left: 20px;
  border-radius: 2px;
  border: none;
  margin-bottom: 30px;
}

.blog__details__form form input::-webkit-input-placeholder {
  color: #a6a6a6;
}

.blog__details__form form input::-moz-placeholder {
  color: #a6a6a6;
}

.blog__details__form form input:-ms-input-placeholder {
  color: #a6a6a6;
}

.blog__details__form form input::-ms-input-placeholder {
  color: #a6a6a6;
}

.blog__details__form form input::placeholder {
  color: #a6a6a6;
}

.blog__details__form form textarea {
  height: 115px;
  width: 100%;
  background: #ffffff;
  font-size: 15px;
  color: #a6a6a6;
  padding-left: 20px;
  border-radius: 2px;
  padding-top: 12px;
  resize: none;
  border: none;
  margin-bottom: 34px;
}

.blog__details__form form textarea::-webkit-input-placeholder {
  color: #a6a6a6;
}

.blog__details__form form textarea::-moz-placeholder {
  color: #a6a6a6;
}

.blog__details__form form textarea:-ms-input-placeholder {
  color: #a6a6a6;
}

.blog__details__form form textarea::-ms-input-placeholder {
  color: #a6a6a6;
}

.blog__details__form form textarea::placeholder {
  color: #a6a6a6;
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

/*---------------------
  Sign Up
-----------------------*/

.signup {
  padding-top: 130px;
  padding-bottom: 150px;
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