<template>
  <main>
    <el-dialog v-model="blockDialogVisible" title="Warning" width="30%" center>
      <span>{{ dialogContent }}</span>
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
              width="100px"
              sortable
            />
            <el-table-column prop="userName" label="UserName" />
            <el-table-column prop="email" label="Email" width="150px" />
            <el-table-column prop="movieTags" label="Genres" />
            <el-table-column prop="ifBlocked" label="Block" />
            <el-table-column prop="overView" label="Overview" width="300px" />
            <el-table-column fixed="right" label="Operations" width="175px">
              <template #default="scope">
                <el-button
                  type="danger"
                  size="small"
                  @click="handleClickBlock(scope.$index, tableData, 0)"
                  >Block</el-button
                >
                <el-button
                  type="danger"
                  size="small"
                  @click="handleClickBlock(scope.$index, tableData, 1)"
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
import env from "@/env.js";

export default {
  name: "CommentTable",
  components: {},
  setup() {
    const axios = inject("axios"); // inject axios
    const tableData = ref([]);
    const blockDialogVisible = ref(false);
    const isLoading = ref(false);
    const dialogContent = ref("");
    let blockUserId = "";
    let isblockorUn = 0;

    onBeforeMount(() => {
      fetchUserList();
    });

    /**
     * Block user event.
     * @index  row index
     * @data  row data
     * @isblock  check block
     */
    const handleClickBlock = (index, data, isblock) => {
      blockDialogVisible.value = true;
      blockUserId = data[index].userId;
      if (isblock === 0) {
        isblockorUn = 0;
        dialogContent.value = "Are you sure to block this user?";
      } else {
        isblockorUn = 1;
        dialogContent.value = "Are you sure to unblock this user?";
      }
    };

    /**
     * get user info event.
     */
    const fetchUserList = () => {
      isLoading.value = true;
      // Fetch  all user list
      axios
        .get(env.AMDBAPI + "admin/userList")
        .then((response) => {
          tableData.value = response.data.data;
          isLoading.value = false;
        })
        .catch((error) => {
          showErroeMessage();
        });
    };

    /**
     * Comform block user event.
     */
    const comfirmBlock = () => {
      if (isblockorUn === 0) {
        // Fetch comfirm Block
        axios
          .get(env.AMDBAPI + "admin/blockUser?userId=" + blockUserId)
          .then((response) => {
            if (response.data.code == 200) {
              blockDialogVisible.value = false;
              openNotificationWithIcon("success", "block");
              fetchUserList();
            }
          })
          .catch((error) => {
            blockDialogVisible.value = false;
            showErroeMessage();
          });
      } else {
        handleClicUnblock();
      }
    };

    /**
     * Unblock user event.
     */
    const handleClicUnblock = () => {
      // Fetch comfirm Block
      axios
        .get(env.AMDBAPI + "admin/unBlockUser?userId=" + blockUserId)
        .then((response) => {
          if (response.data.code == 200) {
            blockDialogVisible.value = false;
            openNotificationWithIcon("success", "unblock");
            fetchUserList();
          }
        })
        .catch((error) => {
          blockDialogVisible.value = false;
          showErroeMessage();
        });
    };

    const openNotificationWithIcon = (type, isblock) => {
      notification[type]({
        message: isblock + " sucessful!",
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
      dialogContent,
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