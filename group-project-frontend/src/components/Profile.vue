<template>
  <section class="anime-details spad">
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-md-8">
          <div class="anime__details__review">
            <div class="section-title">
              <h5>Person Detial</h5>
              <div class="container2">
                <div class="profile">
                  <div class="profile-image">
                    <img
                      :src="
                        AMDBAPI + 'member/getUserImage?userId=' + user.userId
                      "
                      alt=""
                    />
                  </div>
                  <div class="profile-user-settings">
                    <h1 class="profile-user-name">{{ user.userName }}</h1>
                    <button
                      class="btn profile-settings-btn"
                      @click="showSettingPage()"
                      aria-label="profile settings"
                    >
                      <i class="fas fa-user-cog" aria-hidden="true"></i>
                    </button>
                    <div class="email">
                      <span class="profile-stat-count"></span> {{ user.email }}
                    </div>
                  </div>
                  <div class="profile-stats">
                    <ul>
                      <!-- <li>
                        <span class="profile-stat-count"></span>
                        {{ user.email }}
                      </li> -->
                      <li>
                        <span class="profile-stat-count">{{
                          likeListData.length
                        }}</span>
                        Movie Likes
                      </li>
                      <li>
                        <span class="profile-stat-count">{{
                          commentsData.length
                        }}</span>
                        Comments
                      </li>
                    </ul>
                  </div>
                  <div class="profile-bio">
                    <p>
                      <span class="profile-real-name"
                        >Overview: {{ user.overView }}</span
                      >
                    </p>
                  </div>
                </div>
                <!-- End of profile section -->
              </div>
              <!-- End of container -->
            </div>
            <div class="anime__details__form">
              <div class="section-title">
                <h5>My Movie List</h5>
                <p></p>
                <div class="movie-like-list" v-loading="isLoading">
                  <el-scrollbar>
                    <a-table :columns="likeColumns" :data-source="likeListData">
                      <template #name="{ text }">
                        <a>{{ text }}</a>
                      </template>
                      <template #customTitle>
                        <span>
                          <smile-outlined />
                          Name
                        </span>
                      </template>
                      <template #tags="{ text: tags }">
                        <span>
                          <a-tag
                            v-for="tag in tags"
                            :key="tag"
                            :color="'volcano'"
                          >
                            {{ tag.toUpperCase() }}
                          </a-tag>
                        </span>
                      </template>
                      <template #action="{ record }">
                        <span>
                          <a @click="deleteLike(record)">Delete</a>
                        </span>
                      </template>
                    </a-table>
                  </el-scrollbar>
                </div>
              </div>
            </div>
            <div class="anime__details__form">
              <div class="section-title">
                <h5>My Comments</h5>
                <p></p>
                <div class="movie-like-list" v-loading="isLoading">
                  <el-scrollbar>
                    <a-table
                      :columns="commentsColumns"
                      :data-source="commentsData"
                    >
                      <template #name="{ text }">
                        <a>{{ text }}</a>
                      </template>
                      <template #customTitle>
                        <span>
                          <smile-outlined />
                          Name
                        </span>
                      </template>
                      <template #tags="{ text: tags }">
                        <span>
                          <a-tag
                            v-for="tag in tags"
                            :key="tag"
                            :color="'volcano'"
                          >
                            {{ tag.toUpperCase() }}
                          </a-tag>
                        </span>
                      </template>
                      <template #action="{ record }">
                        <span>
                          <a @click="deleteComment(record)">Delete</a>
                        </span>
                      </template>
                    </a-table>
                  </el-scrollbar>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="col-lg-4 col-md-4">
          <div class="anime__details__sidebar">
            <div class="section-title">
              <h5>Recommend to you</h5>
            </div>
            <div
              class="product__sidebar__comment__item"
              v-for="item in recentRecommendationMovies"
              :key="item.id"
            >
              <router-link :to="'/movie/' + item.id">
                <div class="product__sidebar__comment__item__pic">
                  <img
                    class="pichover"
                    :src="poster + item.poster"
                    style="width: 90px; height: 130px"
                    alt=""
                  />
                </div>
                <div class="product__sidebar__comment__item__text">
                  <h5>
                    <a style="color: white">{{ item.title }}</a>
                  </h5>
                  <ul>
                    <li
                      v-for="genre in item.genres[0].slice(0, 2)"
                      :key="genre.id"
                    >
                      {{ genre.name }}
                    </li>
                  </ul>
                  <div class="ep">{{ item.vote_average + "/ 10" }}</div>
                  <span><i class="fa fa-eye"></i> {{ item.release_date }}</span>
                </div>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { ref, inject, onBeforeMount, h } from "vue";
import { notification, message } from "ant-design-vue";
import { SmileOutlined } from "@ant-design/icons-vue";
import { ElMessageBox } from "element-plus";
import router from "@/router";
import env from "@/env.js";

export default {
  name: "Profile",
  components: { SmileOutlined },

  setup() {
    const user = ref("");
    const commentsData = ref([]);
    const isLoading = ref(false);
    const likeListData = ref([]);
    const recentRecommendationMovies = ref([]);
    const poster = ref("");
    poster.value = env.tmdbpic;
    env.AMDBAPI;

    const AMDBAPI = ref(env.AMDBAPI);
    const axios = inject("axios"); // inject axios
    const likeColumns = ref([
      {
        title: "Movie name",
        dataIndex: "title",
        key: "title",
      },
      //   {
      //     title: "Poster",
      //     dataIndex: "poster_path",
      //     key: "poster_path",
      //     customRender: (record) => {
      //       return <img src={record.poster_path} />;
      //     },
      //   },
      {
        title: "Tags",
        key: "vote_average",
        dataIndex: "vote_average",
        slots: {
          customRender: "vote_average",
        },
      },
      {
        title: "Action",
        key: "action",
        slots: {
          customRender: "action",
        },
      },
    ]);

    const commentsColumns = ref([
      {
        title: "Movie name",
        dataIndex: "title",
        key: "title",
      },
      {
        title: "Comment",
        dataIndex: "comment",
        key: "comment",
      },
      {
        title: "Toxic rate",
        dataIndex: "toxic",
        key: "toxic",
      },
      {
        title: "Sentiment rate",
        dataIndex: "sentiment",
        key: "sentiment",
      },
      {
        title: "Date",
        dataIndex: "createTime",
        key: "createTime",
      },
      {
        title: "Action",
        key: "action",
        slots: {
          customRender: "action",
        },
      },
    ]);
    onBeforeMount(() => {
      if (!localStorage.getItem("user")) {
        router.push({
          name: "Login",
        });
        return;
      }
      user.value = JSON.parse(localStorage.getItem("user")).data;
      console.log("profile user.value");
      console.log(user.value);

      // fetch like List
      fetchMovieLike();
      // fetch comment List
      fetchCommentList();

      // fetch getRecommandationByTags
      axios
        .get(
          env.AMDBAPI +
            "rec/getRecommandationByTags?userId=" +
            user.value.userId
        )
        .then((response) => {
          console.log("getRecommandationByTags");
          console.log(response.data.data);
          recentRecommendationMovies.value = response.data.data;
        })
        .catch((error) => {
          console.log("error");
          console.log(error);
          console.log("error");
          showErroeMessage();
          isLoading.value = false;
        });
    });

    const fetchMovieLike = () => {
      isLoading.value = true;
      // fetch like List
      axios
        .get(env.AMDBAPI + "member/showMovieList?userId=" + user.value.userId)
        .then((response) => {
          console.log("showMovieList");
          console.log(response.data.data);
          likeListData.value = response.data.data;
          isLoading.value = false;
        })
        .catch((error) => {
          console.log("error");
          console.log(error);
          console.log("error");
          showErroeMessage();
          isLoading.value = false;
        });
    };

    const fetchCommentList = () => {
      isLoading.value = true;
      // fetch comment List
      axios
        .get(
          env.AMDBAPI + "/member/showCommentList?userId=" + user.value.userId
        )
        .then((response) => {
          console.log("showCommentList");
          console.log(response.data.data);
          commentsData.value = response.data.data;
          isLoading.value = false;
        })
        .catch((error) => {
          console.log("error");
          console.log(error);
          console.log("error");
          showErroeMessage();
          isLoading.value = false;
        });
    };

    const deleteLike = (record) => {
      console.log("record");
      console.log(record);
      ElMessageBox.confirm("Do you confirm to delete this item?", "Warning", {
        confirmButtonText: "OK",
        cancelButtonText: "Cancel",
        type: "warning",
      })
        .then(() => {
          axios
            .get(env.AMDBAPI + "member/deleteMovieLikes?Id=" + record.Id)
            .then((response) => {
              console.log("deleteMovieLikes");
              console.log(response.data);
              if (response.data.code == 200) {
                deleteSuccessful();
                fetchMovieLike();
              }
            })
            .catch((error) => {
              console.log("error");
              console.log(error);
              console.log("error");
              showErroeMessage();
            });
        })
        .catch(() => {});
    };

    const deleteComment = (record) => {
      console.log("record");
      console.log(record);

      ElMessageBox.confirm(
        "Do you confirm to delete this comment?",
        "Warning",
        {
          confirmButtonText: "OK",
          cancelButtonText: "Cancel",
          type: "warning",
        }
      )
        .then(() => {
          axios
            .get(env.AMDBAPI + "member/deleteComment?id=" + record.id)
            .then((response) => {
              console.log("deleteMovieLikes");
              console.log(response.data);
              if (response.data.code == 200) {
                deleteSuccessful();
                fetchCommentList();
              }
            })
            .catch((error) => {
              console.log("error");
              console.log(error);
              console.log("error");
              showErroeMessage();
            });
        })
        .catch(() => {});
    };

    const deleteSuccessful = () => {
      notification.open({
        duration: 2,
        message: "Delete successfully!",
        icon: h(SmileOutlined, {
          style: "color: #108ee9",
        }),
      });
    };

    const showErroeMessage = () => {
      return message.error("Sorry, error accured in server");
    };

    const showSettingPage = () => {
      router.push({
        name: "Setting",
      });
    };

    return {
      user,
      isLoading,
      likeColumns,
      commentsColumns,
      commentsData,
      likeListData,
      AMDBAPI,
      poster,
      recentRecommendationMovies,
      deleteLike,
      deleteComment,
      showSettingPage,
    };
  },
};
</script>

<style lang="scss" scoped>
.movie-like-list {
  min-width: 300px;
}
.anime-details {
  padding-top: 60px;
}

.anime__details__content {
  margin-bottom: 65px;
}

.anime__details__text {
  position: relative;
}

.anime__details__text p {
  color: #b7b7b7;
  font-size: 18px;
  line-height: 30px;
}

.anime__details__pic {
  height: 440px;
  border-radius: 5px;
  position: relative;
}

.anime__details__pic .comment {
  font-size: 13px;
  color: #ffffff;
  background: #3d3d3d;
  display: inline-block;
  padding: 2px 10px;
  border-radius: 4px;
  position: absolute;
  left: 10px;
  bottom: 25px;
}

.anime__details__pic .view {
  font-size: 13px;
  color: #ffffff;
  background: #3d3d3d;
  display: inline-block;
  padding: 2px 10px;
  border-radius: 4px;
  position: absolute;
  right: 10px;
  bottom: 25px;
}

.anime__details__title {
  margin-bottom: 20px;
}

.anime__details__title h3 {
  color: #ffffff;
  font-weight: 700;
  margin-bottom: 13px;
}

.anime__details__title span {
  font-size: 15px;
  color: #b7b7b7;
  display: block;
}

.anime__details__widget {
  margin-bottom: 15px;
}

.anime__details__widget ul {
  margin-bottom: 20px;
}

.anime__details__widget ul li {
  list-style: none;
  font-size: 15px;
  color: #ffffff;
  line-height: 30px;
  position: relative;
  padding-left: 18px;
}

.anime__details__widget ul li:before {
  position: absolute;
  left: 0;
  top: 12px;
  height: 6px;
  width: 6px;
  background: #b7b7b7;
  content: "";
}

.anime__details__widget ul li span {
  color: #b7b7b7;
  width: 115px;
  display: inline-block;
}

.anime__review__item {
  overflow: hidden;
  margin-bottom: 15px;
}

.anime__review__item__pic {
  float: left;
  margin-right: 20px;
  position: relative;
}

.anime__review__item__pic:before {
  position: absolute;
  right: -30px;
  top: 15px;
  border-top: 15px solid transparent;
  border-left: 15px solid #1d1e39;
  content: "";
  -webkit-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  transform: rotate(45deg);
}

.anime__review__item__pic img {
  height: 50px;
  width: 50px;
  border-radius: 50%;
}

.anime__review__item__text {
  overflow: hidden;
  background: #1d1e39;
  padding: 18px 30px 16px 20px;
  border-radius: 10px;
}

.anime__review__item__text h6 {
  color: #ffffff;
  font-weight: 700;
  margin-bottom: 10px;
}

.anime__review__item__text h6 span {
  color: #b7b7b7;
  font-weight: 400;
}

.anime__review__item__text p {
  color: #b7b7b7;
  line-height: 23px;
  margin-bottom: 0;
}

.anime__details__form form textarea {
  width: 100%;
  font-size: 15px;
  color: #b7b7b7;
  padding-left: 20px;
  padding-top: 12px;
  height: 110px;
  border: none;
  border-radius: 5px;
  resize: none;
  margin-bottom: 24px;
}

.anime__details__form form button {
  font-size: 11px;
  color: #ffffff;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  background: #e53637;
  border: none;
  padding: 10px 15px;
  border-radius: 2px;
}

.container2 {
  max-width: 93.5rem;
  margin: 0 auto;
  padding: 0 1rem;

  img {
    display: block;
  }
  .btn {
    display: inline-block;
    font: inherit;
    background: none;
    border: none;
    color: #e53637;
    padding: 0;
    cursor: pointer;
  }

  .btn:focus {
    outline: 0.5rem auto #4d90fe;
  }
}

/* Profile Section */

.profile {
  padding: 40px 0;
}

.profile::after {
  content: "";
  display: block;
  clear: both;
}

.profile-image {
  float: left;
  width: calc(33.333% - 1rem);
  min-width: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-right: 3rem;
}

.profile-image img {
  border-radius: 50%;
}

.profile-user-settings,
.profile-stats,
.profile-bio {
  float: left;
  width: calc(66.666% - 2rem);
}

.profile-user-settings {
  margin-top: 1.1rem;
}

.profile-user-name {
  display: inline-block;
  font-size: 2.2rem;
  font-weight: 300;
  overflow: hidden;
  color: #fff;
}

.profile-edit-btn {
  font-size: 1.4rem;
  line-height: 1.8;
  border: 0.1rem solid #dbdbdb;
  border-radius: 0.3rem;
  padding: 0 2.4rem;
  margin-left: 2rem;
}

.profile-settings-btn {
  font-size: 2rem;
  margin-left: 1rem;
}

.profile-stats {
  margin-top: 2.3rem;
}

.profile-stats li {
  display: inline-block;
  font-size: 1.6rem;
  line-height: 1.5;
  color: #fff;
  margin-right: 4rem;
  cursor: pointer;
}

.profile-stats li:last-of-type {
  margin-right: 0;
}

.profile-bio {
  font-size: 1.6rem;
  font-weight: 400;
  line-height: 1.5;
  margin-top: 2.3rem;
}

.email,
.profile-stat-count {
  font-weight: 600;
  font-size: 25px;
  color: #fff;
}

.profile-real-name {
  word-break: normal;
  max-width: 500px;
  display: block;
  white-space: pre-wrap;
  word-wrap: break-word;
  overflow: hidden;
}

.profile-real-name,
.profile-stat-count,
.profile-edit-btn {
  font-weight: 600;
  color: #fff;
}

/* Media Query */

@media screen and (max-width: 40rem) {
  .email {
    font-size: 12px;
  }
  .profile {
    display: flex;
    flex-wrap: wrap;
    padding: 4rem 0;
  }

  .profile::after {
    display: none;
  }

  .profile-image,
  .profile-user-settings,
  .profile-bio,
  .profile-stats {
    float: none;
    width: auto;
  }

  .profile-image img {
    width: 7.7rem;
  }

  .profile-user-settings {
    flex-basis: calc(100% - 10.7rem);
    display: flex;
    flex-wrap: wrap;
    margin-top: 1rem;
  }

  .profile-user-name {
    font-size: 0.2rem !important;
  }

  .profile-edit-btn {
    order: 1;
    padding: 0;
    text-align: center;
    margin-top: 1rem;
  }

  .profile-edit-btn {
    margin-left: 0;
  }

  .profile-bio {
    font-size: 1.4rem;
    margin-top: 1.5rem;
  }

  .profile-edit-btn,
  .profile-bio,
  .profile-stats {
    flex-basis: 100%;
  }

  .profile-stats {
    order: 1;
    margin-top: 1.5rem;
  }

  .profile-stats ul {
    display: flex;
    text-align: center;
    padding: 1.2rem 0;
    border-top: 0.1rem solid #dadada;
    border-bottom: 0.1rem solid #dadada;
  }

  .profile-stats li {
    font-size: 1.4rem;
    flex: 1;
    margin: 0;
  }

  .profile-stat-count {
    display: block;
  }
}

/*

The following code will only run if your browser supports CSS grid.

Remove or comment-out the code block below to see how the browser will fall-back to flexbox & floated styling. 

*/

@supports (display: grid) {
  .profile {
    display: grid;
    grid-template-columns: 1fr 2fr;
    grid-template-rows: repeat(3, auto);
    grid-column-gap: 3rem;
    align-items: center;
  }

  .profile-image {
    grid-row: 1 / -1;
  }

  .profile-image,
  .profile-user-settings,
  .profile-stats,
  .profile-bio,
  .gallery-item,
  .gallery {
    width: auto;
    margin: 0;
  }

  @media (max-width: 40rem) {
    .profile {
      grid-template-columns: auto 1fr;
      grid-row-gap: 1.5rem;
    }

    .profile-image {
      grid-row: 1 / 2;
    }

    .profile-user-settings {
      display: grid;
      grid-template-columns: auto 1fr;
      grid-gap: 1rem;
    }

    .profile-edit-btn,
    .profile-stats,
    .profile-bio {
      grid-column: 1 / -1;
    }

    .profile-user-settings,
    .profile-edit-btn,
    .profile-settings-btn,
    .profile-bio,
    .profile-stats {
      margin: 0;
    }
  }
}
</style>