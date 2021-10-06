<template>
  <div class="longin-page">
    <a-button type="primary" @click="showModal"
      >Open Modal with async logic</a-button
    >
    <a-modal
      title="Login"
      :visible="visible"
      :confirm-loading="confirmLoading"
      @ok="handleOk"
    >
      <!-- 
        Login PAGE
      -->
      <div v-if="!isRegister" class="login">
        <a-form
          layout="horizontal"
          :model="formState"
          @finish="handleFinish"
          @finishFailed="handleFinishFailed"
        >
          <a-form-item>
            <a-input :value="formState.user" placeholder="Username">
              <template #prefix
                ><UserOutlined style="color: rgba(0, 0, 0, 0.25)"
              /></template>
            </a-input>
          </a-form-item>
          <a-form-item>
            <a-input-password
              :value="formState.password"
              type="password"
              placeholder="Password"
            >
              <template #prefix
                ><LockOutlined style="color: rgba(0, 0, 0, 0.25)"
              /></template>
            </a-input-password>
          </a-form-item>
          <a-form-item>
            <a-button
              type="primary"
              html-type="submit"
              :disabled="formState.user === '' || formState.password === ''"
            >
              Log in
            </a-button>
            <a class="register-text" @click="showRegister"
              >No account? Click here to register!</a
            >
          </a-form-item>
        </a-form>
      </div>
      <!-- 
        Register PAGE
      -->
      <div v-else class="register-form">
        <a-form
          layout="horizontal"
          :model="registerformState"
          @finish="handleFinish"
          @finishFailed="handleFinishFailed"
        >
          <a-form-item>
            <a-input
              :value="registerformState.user"
              placeholder="Username"
            >
              <template #prefix
                ><UserOutlined style="color: rgba(0, 0, 0, 0.25)"
              /></template>
            </a-input>
          </a-form-item>
          <a-form-item>
            <a-input
              :value="registerformState.email"
              placeholder="Email"
            >
              <template #prefix>
                <MailOutlined style="color: rgba(0, 0, 0, 0.25)" />
              </template>
            </a-input>
          </a-form-item>

          <a-form-item>
            <a-input-password
              :value="registerformState.password"
              type="password"
              placeholder="Password"
            >
              <template #prefix
                ><LockOutlined style="color: rgba(0, 0, 0, 0.25)"
              /></template>
            </a-input-password>
          </a-form-item>

           <a-form-item>
            <a-input-password
              :value="registerformState.password2"
              type="password"
              placeholder="Password again"
            >
              <template #prefix
                ><LockOutlined style="color: rgba(0, 0, 0, 0.25)"
              /></template>
            </a-input-password>
          </a-form-item>

          <a-form-item>
            <a-select
              :value="value1"
              :options="options"
              mode="multiple"
              :size="size"
              placeholder="Please select"
              style="width: 350px"
              @popupScroll="popupScroll"
            >
            </a-select
          ></a-form-item>
        </a-form>
      </div>
    </a-modal>
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
    const modalText = ref("Content of the modal");
    const visible = ref(false);
    const confirmLoading = ref(false);
    const isRegister = ref(false);
    const options = ref([
      {
        value: "china",
        label: "China (中国)",
        icon: "🇨🇳",
      },
      {
        value: "usa",
        label: "USA (美国)",
        icon: "🇺🇸",
      },
      {
        value: "japan",
        label: "Japan (日本)",
        icon: "🇯🇵",
      },
      {
        value: "korea",
        label: "Korea (韩国)",
        icon: "🇨🇰",
      },
    ]);

    const showModal = () => {
      visible.value = true;
    };

    const showRegister = () => {
      isRegister.value = true;
    };

    const handleOk = () => {
      modalText.value = "The modal will be closed after two seconds";
      confirmLoading.value = true;
      setTimeout(() => {
        visible.value = false;
        confirmLoading.value = false;
      }, 2000);
    };
    const formState = reactive({
      user: "",
      password: "",
    });
    const registerformState = reactive({
      user: "",
      email: "",
      password: "",
      password2:''
    });
    const handleFinish = (values) => {
      console.log(values, formState);
    };

    const handleFinishFailed = (errors) => {
      console.log(errors);
    };
    const popupScroll = () => {
      console.log("popupScroll");
    };
    return {
      formState,
      handleFinish,
      handleFinishFailed,
      modalText,
      visible,
      confirmLoading,
      showModal,
      handleOk,
      isRegister,
      showRegister,
      registerformState,
      popupScroll,
      size: ref("default"),
      value1: ref([]),
      options,
    };
  },
});
</script>



<style lang="scss">
.register-text {
  margin-top: 10px;
  font-size: 10px;
  float: right;
}
</style>