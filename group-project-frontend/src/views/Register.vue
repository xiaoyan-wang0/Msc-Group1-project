<template>
  <div class="register-page">
    <div class="form-body">
      <div class="row">
        <div class="form-holder">
          <div class="form-content">
            <div class="form-items">
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
                  <label class="mb-3 mr-1" for="gender">Gender: </label>

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
                  <label class="form-check-label"
                    >I confirm that all data are correct</label
                  >
                  <div class="invalid-feedback">
                    Please confirm that the entered data are all correct!
                  </div>
                </div>

                <div class="form-button mt-3">
                  <button id="submit" type="submit" class="btn btn-primary">
                    Register
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
import {
  UserOutlined,
  LockOutlined,
  MailOutlined,
} from "@ant-design/icons-vue";
import { ref, defineComponent, inject, onMounted } from "vue";
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
            message.success(response.msg + ", Will return in 3s.", () => {
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
.register-page {
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