<template>
  <main>
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
            <el-table-column label="Sentiment Rate" prop="sentiment" sortable  width="155px"/>
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
import { message } from "ant-design-vue";
import { ref, inject, onBeforeMount } from "vue";
import env from "@/env.js";

export default {
  name: "Home",
  components: {},
  setup() {
    const axios = inject("axios"); // inject axios
    const tableData = ref([]);
    onBeforeMount(() => {
      // Fetch comments reported
      axios
        .get(env.AMDBAPI + "admin/getReportComments")
        .then((response) => {
          console.log("getReportComments");
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

    const showErroeMessage = () => {
      return message.error("Sorry, error accured in server");
    };

    const handleEdit = (a, b) => {};

    const handleDelete = (a, b) => {};

    return { tableData, handleEdit, handleDelete };
  },
};
</script>

<style lang="scss">
</style>