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
          width="150px"
          type="circle"
          :percent="toxicPercent"
          :format="(percent) => `${toxicPercent} % Toxic`"
          :stroke-color="{
            '0%': 'white',
            '0%': 'green',
            '100%': 'red',
          }"
        />
        <div class="toxic-rate">
          <span style="color: white">Toxic extent :</span>
          <a :style="{ color: 'red' }">{{ toxicText }}</a>
        </div>
      </div>
      <div class="detector-sentiemnt">
        <a-progress
          width="150px"
          type="circle"
          :percent="sentiemntPercent"
          :format="(percent) => `${sentiemntPercent} % Sentiment`"
          :stroke-color="{
            '0%': 'white',
            '0%': 'green',
            '100%': 'red',
          }"
        />
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
import { ref, inject } from "vue";
import { message } from "ant-design-vue";
import ToolMethod from "../tools.js";
import env from "@/env.js";
export default {
  name: "Detector",
  components: {},
  setup() {
    const axios = inject("axios"); // inject axios
    const commentValue = ref("");
    const commentStatus = ref();
    const toxicPercent = ref(0);
    const toxicText = ref("~");
    const sentiemntPercent = ref(0);
    const sentiemntText = ref("~");
    const submitDetect = () => {
      //  Comment detect
      axios
        .post(env.AMDBAPI + "/comments/toxic?title=" + commentValue.value, {
          withCredentials: true,
        })
        .then((response) => {
          commentStatus.value = response.data.data;
          toxicPercent.value = Number(
            commentStatus.value.toxic[0] * 100
          ).toFixed(2);

          toxicText.value = ToolMethod.showToxicText(
            commentStatus.value.toxic[0]
          );
          sentiemntPercent.value = Number(
            commentStatus.value.sentiment[0] * 100
          ).toFixed(2);
          sentiemntText.value = ToolMethod.showSentiemntText(
            commentStatus.value.sentiment[0]
          );
          console.log("Comment detect");
          console.log(response.data);
        })
        .catch((error) => {
          console.log("error");
          console.log(error);
          console.log("error");
          showErroeMessage();
        });
    };
    const showErroeMessage = () => {
      return message.error("Sorry, error accured in server");
    };
    return {
      commentValue,
      commentStatus,
      toxicPercent,
      toxicText,
      sentiemntPercent,
      sentiemntText,
      submitDetect,
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
  .detect-input {
    padding-bottom: 20px;
  }
  .detector {
    align-items: center;
    height: 200px;
    width: 100%;
    // background-image: url("../assets/detector_backgroud.jpg");
    // opacity: 0.1;
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
      // float: right;
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