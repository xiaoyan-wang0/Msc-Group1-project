<template>
  <main>
    <el-dialog v-model="deleteDialogVisible" title="Warning" width="30%" center>
      <span
        >It should be noted that the content will not be aligned in center by
        default</span
      >
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="blockDialogVisible = false">Cancel</el-button>
          <el-button type="primary" @click="comfirmDelete()"
            >Confirm
          </el-button>
        </span>
      </template>
    </el-dialog>
    <div class="container-fluid px-4" v-loading="isLoading">
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
            <el-table-column prop="comment" label="Content" width="300px" />
            <el-table-column prop="userId" label="User Id" />
            <el-table-column prop="movieId" label="Movie Id" />
            <el-table-column prop="toxic" label="Toxic Rate" sortable />
            <el-table-column prop="sentiment" label="Sentiment Rate" sortable />
            <el-table-column prop="createTime" label="Date" sortable />
            <el-table-column fixed="right" label="Operations">
              <template #default="scope">
                <el-button
                  type="danger"
                  size="small"
                  @click.prevent="handleDelete(scope.$index, tableData)"
                >
                  Delete
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
                [' Non toxic', toxic.toxic],
                ['Toxic', toxic.midToxic + toxic.noneToxic],
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
                ['Positive', sentiment.positive],
                ['Neutral', sentiment.neutral],
                ['Negative', sentiment.negative],
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
import { message, notification } from "ant-design-vue";
import env from "@/env.js";

export default {
  name: "CommentTable",
  components: {},
  setup() {
    const axios = inject("axios"); // inject axios
    const tableData = ref([]);
    const toxic = ref({});
    const sentiment = ref({});
    const deleteDialogVisible = ref(false);
    const isLoading = ref(false);
    let deleteId = "";

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
      fetchAllCommentsList();
    });

    const fetchAllCommentsList = () => {
      isLoading.value = true;
      // Fetch  all comments list
      axios
        .get(env.AMDBAPI + "admin/commentsList")
        .then((response) => {
          console.log("all comments list");
          console.log(response.data);
          tableData.value = response.data.data;
          deleteDialogVisible.value = false;
          isLoading.value = false;
        })
        .catch((error) => {
          console.log("error");
          console.log(error);
          console.log("error");
          deleteDialogVisible.value = false;
          showErroeMessage();
        });
    };

    const handleDelete = (index, data) => {
      deleteDialogVisible.value = true;
      deleteId = data[index].id;
      console.log("deleteId");
      console.log(deleteId);
    };

    const comfirmDelete = () => {
      // Fetch comfirm Block
      // delete comments
      axios
        .get(env.AMDBAPI + "admin/deleteComments?id=" + deleteId)
        .then((response) => {
          console.log("deleteComments");
          console.log(response.data);
          if (response.data.code == 200) {
            fetchAllCommentsList();
            openNotificationWithIcon("success");
          }
        })
        .catch((error) => {
          console.log("error");
          console.log(error);
          console.log("error");
          showErroeMessage();
        });
    };

    const openNotificationWithIcon = (type) => {
      notification[type]({
        message: "Delete sucessful!",
        top: "100px",
        // description: "Block sucessful!",
      });
    };

    const showErroeMessage = () => {
      isLoading.value = false;
      return message.error("Sorry, error accured in server");
    };
    return {
      tableData,
      toxic,
      sentiment,
      deleteDialogVisible,
      handleDelete,
      comfirmDelete,
    };
  },
};
</script>

<style lang="scss">
</style>