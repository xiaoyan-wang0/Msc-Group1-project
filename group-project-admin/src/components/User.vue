<template>
  <main>
    <el-dialog v-model="blockDialogVisible" title="Warning" width="30%" center>
      <span
        >It should be noted that the content will not be aligned in center by
        default</span
      >
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="blockDialogVisible = false">Cancel</el-button>
          <el-button type="primary" @click="comfirmBlock()">Confirm </el-button>
        </span>
      </template>
    </el-dialog>
    <div class="container-fluid px-4">
      <h1 class="mt-4">User Info</h1>
      <ol class="breadcrumb mb-4">
        <li class="breadcrumb-item active">User information details</li>
      </ol>

      <div class="card mb-4">
        <div class="card-header">
          <i class="fas fa-table me-1"></i>
          Users
        </div>

        <div class="card-body" v-loading="isLoading">
          <el-table :data="tableData" style="width: 100%">
            <el-table-column
              fixed
              prop="userId"
              label="UserId"
              width="150"
              sortable
            />
            <el-table-column prop="userName" label="UserName" />
            <el-table-column prop="email" label="Email" />
            <el-table-column prop="movieTags" label="Genres" />
            <el-table-column prop="ifBlocked" label="Block" />
            <el-table-column prop="overView" label="Overview" />
            <el-table-column fixed="right" label="Operations">
              <template #default="scope">
                <el-button
                  type="danger"
                  size="small"
                  @click="handleClickBlock(scope.$index, tableData)"
                  >Block</el-button
                >
                <el-button
                  type="danger"
                  size="small"
                  @click="handleClickdeleteRow(scope.$index, tableData)"
                  >Unblock</el-button
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
import { ref, inject, onBeforeMount } from "vue";
import { message, notification } from "ant-design-vue";
import router from "@/router";
import env from "@/env.js";

export default {
  name: "CommentTable",
  components: {},
  setup() {
    const axios = inject("axios"); // inject axios
    const tableData = ref([]);
    const blockDialogVisible = ref(false);
    const isLoading = ref(false);
    let blockUserId = "";
    onBeforeMount(() => {
      fetchUserList();
    });

    const handleClickBlock = (index, data) => {
      blockDialogVisible.value = true;
      blockUserId = data[index].userId;
      console.log("handleClickBlock");
      console.log(index);
      console.log(blockUserId);
      console.log(data);
    };

    const fetchUserList = (index, data) => {
      // Fetch  all user list
      axios
        .get(env.AMDBAPI + "admin/userList")
        .then((response) => {
          console.log("get userList");
          console.log(response.data);
          tableData.value = response.data.data;
        })
        .catch((error) => {
          console.log("error");
          console.log(error);
          console.log("error");
          showErroeMessage();
        });
    };

    const comfirmBlock = () => {
      // Fetch comfirm Block
      axios
        .get(env.AMDBAPI + "admin/blockUser?userId=" + blockUserId)
        .then((response) => {
          console.log("blockUser");
          console.log(response.data);
          if (response.data.code == 200) {
            blockDialogVisible.value = false;
            openNotificationWithIcon("success");
            fetchUserList();
          }
        })
        .catch((error) => {
          blockDialogVisible.value = false;
          console.log("error");
          console.log(error);
          console.log("error");
          showErroeMessage();
        });
    };

    const openNotificationWithIcon = (type) => {
      notification[type]({
        message: "Block sucessful!",
        top: "100px",
        // description: "Block sucessful!",
      });
    };

    const showErroeMessage = () => {
      return message.error("Sorry, error accured in server");
    };

    return {
      tableData,
      blockDialogVisible,
      isLoading,
      handleClickBlock,
      comfirmBlock,
    };
  },
};
</script>

<style lang="scss">
</style>