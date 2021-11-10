<template>
  <section class="setting anime-details spad">
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-md-8">
          <div class="anime__details__review">
            <div class="section-title">
              <h5>Person Setting</h5>

              <!-- Basic Vertical form layout section start -->
              <section id="basic-vertical-layouts">
                <div class="col-md-12 col-12">
                  <div class="card-body">
                    <form class="form form-horizontal">
                      <div class="form-body">
                        <div class="row">
                          <div class="col-md-4">
                            <label>Avatar</label>
                          </div>
                          <div class="col-md-8">
                            <div class="form-group has-icon-left">
                              <div class="position-relative">
                                <a-upload
                                  v-model:file-list="fileList"
                                  name="avatar"
                                  list-type="picture-card"
                                  class="avatar-uploader"
                                  :show-upload-list="false"
                                  :before-upload="beforeUpload"
                                  @change="handleUploadChange"
                                >
                                  <img
                                    v-if="imageUrl"
                                    :src="imageUrl"
                                    alt="avatar"
                                  />
                                  <div v-else>
                                    <loading-outlined
                                      v-if="loading"
                                    ></loading-outlined>
                                    <plus-outlined v-else></plus-outlined>
                                    <div class="ant-upload-text">Upload</div>
                                  </div>
                                </a-upload>
                              </div>
                            </div>
                          </div>

                          <div class="col-md-4">
                            <label>UserName</label>
                          </div>
                          <div class="col-md-8">
                            <div class="form-group has-icon-left">
                              <div class="position-relative">
                                <input
                                  type="text"
                                  :value="userName"
                                  class="form-control"
                                  placeholder="Please enter UserName"
                                  id="first-name-icon"
                                  required
                                />
                                <div class="form-control-icon">
                                  <i class="bi bi-person"></i>
                                </div>
                              </div>
                            </div>
                          </div>
                          <p></p>
                          <div class="col-md-4">
                            <label>Email</label>
                          </div>
                          <div class="col-md-8">
                            <div class="form-group has-icon-left">
                              <div class="position-relative">
                                <input
                                  type="email"
                                  :value="email"
                                  class="form-control"
                                  placeholder="Email"
                                  disabled
                                  id="first-name-icon"
                                  required
                                />
                                <div class="form-control-icon">
                                  <i class="bi bi-envelope"></i>
                                </div>
                              </div>
                            </div>
                          </div>

                          <p></p>
                          <div class="col-md-4">
                            <label>Password</label>
                          </div>
                          <div class="col-md-8">
                            <div class="form-group has-icon-left">
                              <div class="position-relative">
                                <el-input
                                  v-model="password"
                                  placeholder="Please input password"
                                  show-password
                                  required
                                />
                                <div class="form-control-icon">
                                  <i class="bi bi-lock"></i>
                                </div>
                              </div>
                            </div>
                          </div>

                          <p></p>
                          <div class="col-md-4">
                            <label>Birthday</label>
                          </div>
                          <div class="col-md-8">
                            <div class="form-group has-icon-left">
                              <div class="position-relative">
                                <div class="form-group with-title mb-3">
                                  <el-date-picker
                                    v-model="value2"
                                    type="date"
                                    placeholder="Pick a day"
                                    :disabled-date="disabledDate"
                                    :shortcuts="shortcuts"
                                    format="DD/MM/YYYY"
                                  >
                                  </el-date-picker>
                                </div>
                              </div>
                            </div>
                          </div>

                          <div class="col-md-4">
                            <label>Interests</label>
                          </div>
                          <div class="col-md-8">
                            <div class="form-group has-icon-left">
                              <div class="position-relative">
                                <div class="form-group with-title mb-3">
                                  <a-select
                                    v-model:value="selectValue"
                                    mode="multiple"
                                    style="width: 100%"
                                    placeholder="Please select"
                                    :options="options"
                                    @popupScroll="popupScroll"
                                    @change="handleChange"
                                  >
                                  </a-select>
                                </div>
                              </div>
                            </div>
                          </div>

                          <div class="col-md-4">
                            <label>Overview</label>
                          </div>
                          <div class="col-md-8">
                            <div class="form-group has-icon-left">
                              <div class="position-relative">
                                <div class="form-group with-title mb-3">
                                  <a-textarea
                                    v-model:value="overViewValue"
                                    showCount
                                    :maxlength="200"
                                    class="detect-input"
                                  />
                                </div>
                              </div>
                            </div>
                          </div>

                          <div class="col-12 d-flex justify-content-end">
                            <div class="anime__details__btn">
                              <a @click="submitChange()" class="follow-btn">
                                Submit
                              </a>

                              <a @click="returnFun()" class="follow-btn">
                                Return
                              </a>
                            </div>
                          </div>
                        </div>
                      </div>
                    </form>
                  </div>
                </div>
              </section>
              <!-- // Basic Vertical form layout section end -->
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { ref, inject, onBeforeMount, h, reactive, toRefs } from "vue";
import { PlusOutlined, LoadingOutlined } from "@ant-design/icons-vue";
import { message } from "ant-design-vue";
import router from "@/router";
import env from "@/env.js";

function getBase64(img, callback) {
  const reader = new FileReader();
  reader.addEventListener("load", () => callback(reader.result));
  reader.readAsDataURL(img);
}

export default {
  name: "Setting",
  components: {
    LoadingOutlined,
    PlusOutlined,
  },

  setup() {
    const axios = inject("axios"); // inject axios
    const selectValue = ref([]);
    const fileList = ref([]);
    const loading = ref(false);
    const imageUrl = ref("");

    const options = ref([
      {
        value: "28",
        label: "Action",
      },
      {
        value: "12",
        label: "Adventure",
      },
      {
        value: "16",
        label: "Animation",
      },
      {
        value: "35",
        label: "Comedy",
      },
      {
        value: "80",
        label: "Crime",
      },

      {
        value: "99",
        label: "Documentary",
      },

      {
        value: "18",
        label: "Drama",
      },

      {
        value: "10751",
        label: "Family",
      },

      {
        value: "14",
        label: "Fantasy",
      },

      {
        value: "36",
        label: "History",
      },
      {
        value: "27",
        label: "Horror",
      },
      {
        value: "10402",
        label: "Music",
      },
      {
        value: "9648",
        label: "Mystery",
      },
      {
        value: "10749",
        label: "Romance",
      },
      {
        value: "878",
        label: "Science Fiction",
      },
      {
        value: "10770",
        label: "TV Movie",
      },
      {
        value: "53",
        label: "Thriller",
      },
      {
        value: "10752",
        label: "War",
      },
      {
        value: "37",
        label: "Western",
      },
    ]);
    const email = ref("");
    const password = ref("");
    const userName = ref("");
    const overViewValue = ref("");

    const state = reactive({
      disabledDate(time) {
        return time.getTime() > Date.now();
      },
      shortcuts: [
        {
          text: "Today",
          value: new Date(),
        },
        {
          text: "Yesterday",
          value: () => {
            const date = new Date();
            date.setTime(date.getTime() - 3600 * 1000 * 24);
            return date;
          },
        },
        {
          text: "A week ago",
          value: () => {
            const date = new Date();
            date.setTime(date.getTime() - 3600 * 1000 * 24 * 7);
            return date;
          },
        },
      ],
      value2: new Date(),
    });

    onBeforeMount(() => {
      const user = JSON.parse(localStorage.getItem("user"));
      console.log("user.data");
      userName.value = user.data.userName;
      email.value = user.data.email;
      password.value = user.data.password;
    });

    const popupScroll = () => {
      console.log("popupScroll");
      console.log(selectValue.value);
    };

    const handleChange = () => {
      console.log("handleChange");
      console.log(selectValue.value);
    };

    const handleUploadChange = (info) => {
      if (info.file.status === "uploading") {
        loading.value = true;
        return;
      }

      if (info.file.status === "done") {
        // Get this url from response in real world.
        getBase64(info.file.originFileObj, (base64Url) => {
          imageUrl.value = base64Url;
          loading.value = false;
        });
      }

      if (info.file.status === "error") {
        loading.value = false;
        message.error("upload error");
      }
    };

    const beforeUpload = (file) => {
      const isJpgOrPng =
        file.type === "image/jpeg" || file.type === "image/png";

      if (!isJpgOrPng) {
        message.error("You can only upload JPG file!");
      }

      const isLtKB = file.size / 1024 < 100;

      if (!isLtKB) {
        message.error("Image must smaller than 100kb!");
      }

      return isJpgOrPng && isLt2M;
    };

    return {
      userName,
      selectValue,
      options,
      fileList,
      loading,
      imageUrl,
      email,
      password,
      overViewValue,
      handleChange,
      beforeUpload,
      popupScroll,
      handleUploadChange,
      ...toRefs(state),
    };
  },
};
</script>

<style lang="scss" scoped>
.setting label {
  color: #ffffff;
  font-weight: 600;
  line-height: 21px;
  text-transform: uppercase;
  padding-left: 20px;
  position: relative;
  font-family: "Oswald", sans-serif;
}

.anime__details__btn .follow-btn {
  font-size: 13px;
  color: #ffffff;
  background: #e53637;
  display: inline-block;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  padding: 14px 20px;
  border-radius: 4px;
  margin-right: 11px;
}

.anime__details__btn .watch-btn span {
  font-size: 13px;
  color: #ffffff;
  background: #e53637;
  display: inline-block;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  padding: 14px 20px;
  border-radius: 4px 0 0 4px;
  margin-right: 1px;
}

.anime__details__btn .watch-btn i {
  font-size: 20px;
  display: inline-block;
  background: #e53637;
  padding: 11px 5px 16px 8px;
  color: #ffffff;
  border-radius: 0 4px 4px 0;
}
.form-group[class*="has-icon-"].has-icon-left .form-control {
  padding-left: 2.5rem;
}

.form-group[class*="has-icon-"].has-icon-left .form-control-icon {
  left: 0;
}

.form-group[class*="has-icon-"].has-icon-right .form-control {
  padding-right: 2.5rem;
}

.form-group[class*="has-icon-"].has-icon-right .form-control-icon {
  right: 0;
}

.form-group[class*="has-icon-"] .form-control:focus ~ .form-control-icon i,
.form-group[class*="has-icon-"] .form-control:focus ~ .form-control-icon svg {
  color: #5a8dee;
}

.form-group[class*="has-icon-"] .form-control.form-control-xl {
  padding-left: 3rem;
}

.form-group[class*="has-icon-"]
  .form-control.form-control-xl
  ~ .form-control-icon
  i {
  font-size: 1.6rem;
}

.form-group[class*="has-icon-"]
  .form-control.form-control-xl
  ~ .form-control-icon
  i:before {
  color: #a6a8aa;
}

.form-group[class*="has-icon-"] .form-control-icon {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  padding: 0 0.6rem;
}

.form-group[class*="has-icon-"] .form-control-icon i,
.form-group[class*="has-icon-"] .form-control-icon svg {
  width: 1.2rem;
  color: #6c757d;
  font-size: 1.2rem;
}

.form-group[class*="has-icon-"] .form-control-icon i:before,
.form-group[class*="has-icon-"] .form-control-icon svg:before {
  vertical-align: sub;
}
</style>