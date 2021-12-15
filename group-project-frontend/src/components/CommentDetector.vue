<template>
  <div class="detector-div">
    <section class="normal-breadcrumb set-bg detector">
      <div class="container">
        <div class="row">
          <div class="col-lg-12 text-center">
            <div class="normal__breadcrumb__text">
              <h2 style="color: white">Detection Master</h2>
              <p style="color: white">
                Welcome to use our toxic and sentiment comments detector
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
    <div class="detect-upload-div" v-loading="isLoading">
      <a-upload-dragger
        v-model:fileList="fileList"
        name="file"
        :before-upload="beforeUpload"
        :show-upload-list="false"
        :data="{
          language: 'eng',
          apikey: 'cefc90891488957',
          isOverlayRequired: 'true',
        }"
        action="https://api.ocr.space/parse/image"
        @change="handleUploadChange"
      >
        <p class="ant-upload-drag-icon">
          <inbox-outlined></inbox-outlined>
        </p>
        <p class="ant-upload-text">Click or drag image to upload</p>
        <p class="ant-upload-hint">
          Support for a image upload. tranfer to text.
        </p>
      </a-upload-dragger>
    </div>
    <div class="detector-text">
      <h3>Please enter the character!</h3>
      <a-textarea
        v-model:value="commentValue"
        showCount
        :maxlength="500"
        class="detect-input"
      />
      <button
        class="detect-button site-btn"
        type="primary"
        shape="round"
        size="large"
        @click="submitDetect"
      >
        Submit
      </button>
    </div>
    <div class="circle-erea">
      <div class="detector-rate">
        <a-progress
          :width="150"
          type="circle"
          :percent="parseFloat(toxicPercent)"
          :format="(percent) => `${toxicPercent} % Toxic`"
          :stroke-color="{
            '0%': 'white',
            '50%': 'green',
            '100%': 'red',
          }"
        />
        <div class="toxic-rate">
          <span style="color: white">Toxic extent :</span>
          <a :style="{ color: 'red' }">{{ toxicText }}</a>
        </div>
      </div>
      <div class="detector-sentiemnt">
        <div class="sentiemnt-rate">
          <div class="">
            <span style="color: white">Sentiment :</span>
            <a :style="{ color: 'red' }">{{ sentiemntText }}</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import { message } from "ant-design-vue";
import { InboxOutlined } from "@ant-design/icons-vue";
import ToolMethod from "../tools.js";
import UserApi from "../services/user.service";

export default {
  name: "Detector",
  components: { InboxOutlined },
  setup() {
    const commentValue = ref("");
    const commentStatus = ref();
    const toxicPercent = ref(0);
    const isLoading = ref(false);
    const toxicText = ref(" ~ ");
    const sentiemntPercent = ref(0);
    const sentiemntText = ref(" ~ ");

    /**
     * Comment detect event.
     */
    const submitDetect = () => {
      if (commentValue.value !== "") {
        UserApi.detectUserComment(commentValue.value)
          .then((response) => {
            commentStatus.value = response.data.data;
            toxicPercent.value = Number(
              commentStatus.value.toxic[0] * 100
            ).toFixed(2);

            toxicText.value = ToolMethod.showToxicText(
              commentStatus.value.toxic[0]
            );
            sentiemntText.value = ToolMethod.showSentiemntText(
              commentStatus.value.sentiment
            );
          })
          .catch((error) => {
            showErroeMessage();
          });
      }
    };

    const showErroeMessage = () => {
      return message.error("Server is busy, try again later");
    };

    const beforeUpload = (file) => {
      isLoading.value = true;
      const isJpgOrPng =
        file.type === "image/jpeg" || file.type === "image/png";

      if (!isJpgOrPng) {
        message.error("You can only upload JPG file!");
        isLoading.value = false;
      }

      const isLtKB = file.size / 1024 < 1024;

      if (!isLtKB) {
        message.error("Image must smaller than 1MB!");
        isLoading.value = false;
      }

      return isJpgOrPng && isLtKB;
    };

    const handleUploadChange = (info) => {
      const status = info.file.status;

      if (status !== "uploading") {
        // console.log(info.file, info.fileList);
      }
      try {
        if (status === "done") {

          commentValue.value = "";
          if (info.file.response) {
            for (let item of info.file.response.ParsedResults) {
              for (let line of item.TextOverlay.Lines) {
                commentValue.value += " " + line.LineText;
              }
            }
          }

          isLoading.value = false;
          message.success(`${info.file.name} file uploaded successfully.`);
        } else if (status === "error") {
          isLoading.value = false;
          message.error(`${info.file.name} file upload failed.`);
        }
      } catch {
        isLoading.value = false;
        message.error(`${info.file.name} can't reginize text.`);
      }
    };

    return {
      commentValue,
      commentStatus,
      toxicPercent,
      toxicText,
      isLoading,
      sentiemntPercent,
      sentiemntText,
      fileList: ref([]),
      submitDetect,
      handleUploadChange,
      beforeUpload,
    };
  },
};
</script>

<style lang="scss" scoped>
.detector-div {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  padding-top: 10px;
  .detect-upload-div {
    width: 50%;
  }
  .detect-input {
    padding-bottom: 20px;
  }
  .detector {
    align-items: center;
    height: 200px;
    width: 100%;
    .container {
      margin-top: 30px;
    }
  }
  .circle-erea {
    margin-top: 50px;
    width: 50%;
  }
  .detector-text {
    position: relative;
    width: 50%;
    padding-bottom: 30px;
    h3 {
      color: #fff;
    }
    .detect-button {
      position: absolute;
      bottom: 0;
      right: 0;
    }
  }
  .detector-rate {
    min-width: 150px;
    float: left;
    width: 50%;
    span,
    a {
      font-size: 20px;
      font-weight: bold;
    }
    .toxic-rate {
      margin-top: 20px;
      margin-bottom: 40px;
      justify-content: center;
      align-items: center;
    }
  }
  .detector-sentiemnt {
    min-width: 150px;
    float: right;
    width: 50%;
    margin-top: inherit;
    span,
    a {
      font-size: 20px;
      font-weight: bold;
    }
    .sentiemnt-rate {
      margin-top: 20px;
      margin-bottom: 40px;
      justify-content: center;
      align-items: center;
    }
  }
}
</style>