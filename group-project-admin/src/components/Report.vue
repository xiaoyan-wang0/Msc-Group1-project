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
    <div class="container-fluid px-4">
      <h1 class="mt-4">Report Comment</h1>
      <ol class="breadcrumb mb-4">
        <li class="breadcrumb-item active">User Reported Comment details</li>
      </ol>

      <div class="card mb-4">
        <div class="card-header">
          <i class="fas fa-table me-1"></i>
          Comments
        </div>

        <div class="card-body">
          <el-table
            :data="tableData"
            style="width: 100%"
            :default-sort="{ prop: 'createTime', order: 'descending' }"
          >
            <el-table-column label="ID" prop="id" />
            <el-table-column label="User ID" prop="userId" />
            <el-table-column label="Date" prop="createTime" sortable />
            <el-table-column label="Content" prop="comment" />
            <el-table-column label="MovieId" prop="movieId" />
            <el-table-column label="Toxic Rate" prop="toxic" sortable />
            <el-table-column
              label="Sentiment Rate"
              prop="sentiment"
              sortable
              width="155px"
            />
            <el-table-column align="right" label="Operations">
              <template #default="scope">
                <el-button
                  size="mini"
                  @click="handleEdit(scope.$index, scope.row)"
                  >Edit</el-button
                >
                <el-button
                  size="mini"
                  type="danger"
                  @click="handleDelete(scope.$index, scope.row)"
                  >Delete</el-button
                >
              </template>
            </el-table-column>
          </el-table>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import { message,notification  } from "ant-design-vue";
import { ref, inject, onBeforeMount } from "vue";
import env from "@/env.js";

export default {
  name: "Home",
  components: {},
  setup() {
    const axios = inject("axios"); // inject axios
    const tableData = ref([]);
    const deleteDialogVisible = ref(false);
    let deleteId = "";
    onBeforeMount(() => {
      fetchAllCommentsList();
    });

    const showErroeMessage = () => {
      return message.error("Sorry, error accured in server");
    };

    const fetchAllCommentsList = () => {
      // Fetch comments reported
      axios
        .get(env.AMDBAPI + "admin/getReportComments")
        .then((response) => {
          console.log("getReportComments");
          console.log(response.data);
          tableData.value = response.data.data;
          deleteDialogVisible.value = false;
        })
        .catch((error) => {
          console.log("error");
          console.log(error);
          console.log("error");
          deleteDialogVisible.value = false;
          showErroeMessage();
        });
    };

    const handleEdit = (a, b) => {};

    const handleDelete = (index, data) => {
      console.log("data[index]");
      console.log(data.id);
      console.log(index);
      deleteDialogVisible.value = true;
      deleteId = data.id;
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

    return {
      tableData,
      deleteDialogVisible,
      handleEdit,
      handleDelete,
      comfirmDelete,
    };
  },
};
</script>

<style lang="scss">
</style>