<template>
  <div class="detector-div">
    <div class="detector-text">
      <h3>Please enter the character to be detected！</h3>
      <a-textarea
        v-model:value="commentValue"
        showCount
        :maxlength="500"
        class="detect-input"
      />
      <a-button
        class="detect-button"
        type="primary"
        shape="round"
        :size="large"
        @click="submitDetect"
      >
        Submit
      </a-button>
    </div>
    <div class="detector-rate">
      <a-progress
        width="250px"
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
        <span>Toxic extent :</span>
        <a :style="{ color: 'red' }">{{ toxicText }}</a>
      </div>
    </div>
    <div class="detector-sentiemnt">
      <a-progress
        width="250px"
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
          <span>Sentiment :</span>
          <a :style="{ color: 'red' }">{{ sentiemntText }}</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, inject } from "vue";
import ToolMethod from "../tools.js";
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
        .get("/api/comments/toxic?title=" + commentValue.value)
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
        });
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
  background-color: #fff;
  padding-top: 50px;
  .detector-text {
    position: relative;
    width: 50%;
    padding-bottom: 30px;
    .detect-button {
      position: absolute;
      bottom: 0;
      right: 0;
    }
  }
  .detector-rate {
    width: 50%;
    span,
    a {
      margin-left: 30px;
      font-size: 20px;
      font-weight: bold;
    }
    .toxic-rate {
      float: right;
      display: flex;
      justify-content: center;
      align-items: center;
      margin-top: 110px;
    }
  }
  .detector-sentiemnt {
    margin-top: 50px;
    width: 50%;
    span,
    a {
      margin-left: 30px;
      font-size: 20px;
      font-weight: bold;
    }
    .sentiemnt-rate {
      float: right;
      display: flex;
      justify-content: center;
      align-items: center;
      margin-top: 110px;
    }
  }
}
</style>