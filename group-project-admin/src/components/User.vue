<template>
  <main>
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

        <div class="card-body">
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
            <el-table-column prop="overView" label="Overview" />
            <el-table-column fixed="right" label="Operations">
              <template #default="scope">
                <el-button
                  type="text"
                  size="small"
                  @click="handleClickdeleteRow(scope.$index, tableData)"
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
    onBeforeMount(() => {
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
    });

    const handleClickdeleteRow = (a, b) => {
      console.log("handleClickdeleteRow");
      console.log(a);
      console.log(b);
    };

    const showErroeMessage = () => {
      return message.error("Sorry, error accured in server");
    };
    return { tableData, handleClickdeleteRow };
  },
};
</script>

<style lang="scss">
</style>