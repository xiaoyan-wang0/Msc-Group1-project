<template>
  <main>
    <div class="container-fluid px-4">
      <h1 class="mt-4">User Comment</h1>
      <ol class="breadcrumb mb-4">
        <li class="breadcrumb-item active">User Comment details</li>
      </ol>

      <div class="card mb-4">
        <div class="card-header">
          <i class="fas fa-table me-1"></i>
          Comments
        </div>

        <div class="card-body">
          <el-table :data="tableData" style="width: 100%" max-height="550">
            <el-table-column fixed prop="id" label="ID" />
            <el-table-column prop="comment" label="Content" />
            <el-table-column prop="userId" label="User Id" />
            <el-table-column prop="movieId" label="Movie Id" />
            <el-table-column prop="toxic" label="Toxic Rate" sortable/>
            <el-table-column prop="sentiment" label="Sentiment Rate" sortable/>
            <el-table-column prop="createTime" label="Date" sortable/>
            <el-table-column fixed="right" label="Operations">
              <template #default="scope">
                <el-button
                  type="text"
                  size="small"
                  @click.prevent="handleDelete(scope.$index, tableData)"
                >
                  Remove
                </el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>
      </div>

      <div class="row">
        <div class="col-lg-6">
          <div class="card mb-4">
            <div class="card-header">
              <i class="fas fa-chart-bar me-1"></i>
              Bar Chart
            </div>
            <bar-chart
              :data="[
                ['Positive', sentiment.positive],
                ['Negative', sentiment.negative],
              ]"
              :colors="['#3949AB', '#E53935']"
            ></bar-chart>
            <div class="card-footer small text-muted">
              Updated yesterday at {{ new Date() }}
            </div>
          </div>
        </div>
        <div class="col-lg-6">
          <div class="card mb-4">
            <div class="card-header">
              <i class="fas fa-chart-pie me-1"></i>
              Pie Chart
            </div>
            <pie-chart
              :data="[
                [' Non toxic', toxic.toxic],
                ['Toxic', toxic.midToxic],
                [' Severe toxic', toxic.noneToxic],
              ]"
              :colors="['#43A047', '#FFB300', '#E53935']"
            ></pie-chart>
            <div class="card-footer small text-muted">
              Updated yesterday at {{ new Date() }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import { ref, inject, onBeforeMount } from "vue";
import { message } from "ant-design-vue";
import router from "@/router";
import env from "@/env.js";

export default {
  name: "CommentTable",
  components: {},
  setup() {
    const axios = inject("axios"); // inject axios
    const tableData = ref([]);
    const toxic = ref({});
    const sentiment = ref({});

    onBeforeMount(() => {
      // Fetch  toxic num
      axios
        .get(env.AMDBAPI + "admin/getToxicRate")
        .then((response) => {
          console.log("getToxicRate list");
          console.log(response.data);
          toxic.value = response.data.data;
        })
        .catch((error) => {
          console.log("error");
          console.log(error);
          console.log("error");
          showErroeMessage();
        });
      // Fetch Sentiment num
      axios
        .get(env.AMDBAPI + "admin/getSentimentRate")
        .then((response) => {
          console.log("sentiment list");
          console.log(response.data);
          sentiment.value = response.data.data;
        })
        .catch((error) => {
          console.log("error");
          console.log(error);
          console.log("error");
          showErroeMessage();
        });

      // Fetch  all comments list
      axios
        .get(env.AMDBAPI + "admin/commentsList")
        .then((response) => {
          console.log("all comments list");
          console.log(response.data);
          tableData.value = response.data.data;
        })
        .catch((error) => {
          console.log("error");
          console.log(error);
          console.log("error");
          showErroeMessage();
        });
    });

    const handleDelete = (a, b) => {};

    const showErroeMessage = () => {
      return message.error("Sorry, error accured in server");
    };
    return { tableData, toxic, sentiment, handleDelete };
  },
};
</script>

<style lang="scss">
</style>