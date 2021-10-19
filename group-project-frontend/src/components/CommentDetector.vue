<template>
  <div class="detector-div">
    <div class="detector-text">
      <h1>Please enter the character to be detected！</h1>
      <a-textarea
        v-model:value="commentValue"
        showCount
        :maxlength="200"
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
        <span>Toxic rate :</span>
        <a :style="{ color: 'red' }">{{toxicPercent + "%"}}</a>
      </div>
    </div>
    <div class="detector-sentiemnt">
      <a-progress
        width="250px"
        type="circle"
        :percent="50"
        :format="(percent) => `${percent} % Sentiemnt`"
        :stroke-color="{
          '0%': 'white',
          '0%': 'green',
          '100%': 'red',
        }"
      />
      <div class="sentiemnt-rate">
        <div class="">
          <span>Positive :</span>
          <a :style="{ color: 'red' }">-</a>
        </div>
        <div class="">
          <span>Neutral :</span>
          <a :style="{ color: 'red' }">-</a>
        </div>
        <div class="">
          <span>Negative :</span>
          <a :style="{ color: 'red' }">-</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, inject } from "vue";
export default {
  name: "Detector",
  components: {},
  setup() {
    const axios = inject("axios"); // inject axios
    const commentValue = ref("");
    const commentStatus = ref();
    const toxicPercent = ref(0);
    const submitDetect = () => {
      //  Comment detect
      axios
        .get("/api/comments/toxic?title=" + commentValue.value)
        .then((response) => {
          commentStatus.value = response.data.data;
          toxicPercent.value = Number(commentStatus.value.tag[0]*100).toFixed(2)
          console.log("Comment detect");
          console.log(response.data);
        });
    };
    return { commentValue,commentStatus,toxicPercent, submitDetect };
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
      font-size: 25px;
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
      font-size: 25px;
      font-weight: bold;
    }
    .sentiemnt-rate {
      float: right;
      display: flex;
      justify-content: center;
      flex-direction: column;
      align-items: center;
      margin-top: 60px;
    }
  }
}
</style>