 <template>
  <div class="detail-page">
    <a-modal
      :visible="isShowTrailer"
      :maskClosable="true"
      :closable="false"
      :footer="null"
      :destroyOnClose="true"
      :width="700"
      @cancel="handleCancel"
    >
      <YoutubeVue3
        ref="youtube"
        :videoid="video_id"
        :width="700"
        :autoplay="0"
        :height="400"
      />
    </a-modal>
    <div class="movie-detail">
      <h2>{{ movie.original_title }}</h2>
      <p>{{ movie.release_date }}</p>
      <img
        :src="moviePoster + movie.poster_path"
        alt="Movie Poster"
        class="featured-img"
        @click="isShowTrailer = true"
      />
      <el-tag
        class="tag-group"
        style="magin-right: 8px"
        v-for="item in movie.genres"
        :key="item.id"
      >
        {{ item.name }}
      </el-tag>
      <p style="font-size:20px">{{ movie.overview }}</p>
      <a-rate :value="start" disabled allowHalf />
      <p>{{ movie.vote_average }}</p>
    </div>

    <div class="comments">
      <a-tabs type="card" v-model:activeKey="activeKey">
        <a-tab-pane key="amdb" tab="AMDB reviews" v-loading="isCommnetLoading"
           style="height:600px">
          <h1>AMDB reviews</h1>
          <div class="comment-wrap" v-for="item in amdbreview" :key="item.id">
            <div class="photo-avatar">
              <div class="avatar">
                <a-avatar :src="emptyprofile" />
              </div>
            </div>
            <div class="comment-block">
              <p class="comment-author">{{ item.userName }}</p>
              <p class="comment-text">{{ item.comment }}</p>
              <div class="bottom-comment">
                <div class="comment-date">{{ item.createTime }}</div>
                <ul class="comment-actions">
                  <li class="toxicrate">
                    {{ showToxicText(item.toxic) }} :
                    {{ changeToPercent(item.toxic) }}
                  </li>
                  <li class="report">Report</li>
                </ul>
              </div>
            </div>
          </div>

          <a-comment>
            <template #avatar>
              <a-avatar
                src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
                alt="Han Solo"
              />
            </template>
            <template #content>
              <a-form-item>
                <a-textarea v-model:value="commentsValue" :rows="4" />
              </a-form-item>
              <a-form-item>
                <a-button
                  html-type="submit"
                  :loading="submitting"
                  type="primary"
                  @click="handleSubmit"
                >
                  Add Comment
                </a-button>
              </a-form-item>
            </template>
          </a-comment>
        </a-tab-pane>
        <a-tab-pane key="tmdb" tab="TMDB reviews">
          <h1>TMDB reviews</h1>
          <div class="comment-wrap" v-for="item in tmdbreview" :key="item.id">
            <div class="photo-avatar">
              <div class="avatar">
                <a-avatar
                  :src="
                    item.author_details.avatar_path !== null
                      ? moviePoster + item.profile_path
                      : emptyprofile
                  "
                />
              </div>
            </div>
            <div class="comment-block">
              <p class="comment-author">{{ item.author }}</p>
              <p class="comment-text">{{ item.content }}</p>
              <div class="bottom-comment">
                <div class="comment-date">{{ item.updated_at }}</div>
                <ul class="comment-actions">
                  <li class="toxicrate">
                    {{ showToxicText(item.toxic.tag[0]) }}:{{
                      changeToPercent(item.toxic.tag)
                    }}
                  </li>
                  <li class="report">Report</li>
                </ul>
              </div>
            </div>
          </div>
        </a-tab-pane>
        <a-tab-pane key="imdb" tab="IMDB reviews"
          ><h1>IMDB reviews</h1>
          <div class="comment-wrap" v-for="item in imdbreview" :key="item.id">
            <div class="photo-avatar">
              <div class="avatar">
                <a-avatar :src="emptyprofile" />
              </div>
            </div>
            <div class="comment-block">
              <p class="comment-author">{{ item.username }}</p>
              <p class="comment-text">{{ item.content }}</p>
              <div class="bottom-comment">
                <div class="comment-date">{{ item.date }}</div>
                <ul class="comment-actions">
                  <li class="toxicrate">
                    {{ showToxicText(item.toxic.tag[0]) }} :{{
                      changeToPercent(item.toxic.tag[0])
                    }}
                  </li>
                  <li class="report">Report</li>
                  <li class="report">
                    {{ item.warningSpoilers ? "warningSpoilers" : "" }}
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </a-tab-pane>
      </a-tabs>
    </div>

    <div class="morebutton">
      <a @click="changeText()">{{ isMore }}</a>
    </div>
    <div class="movie-casts">
      <div
        class="card"
        v-for="item in castList"
        :key="item.id"
        @click="showCastDetail(item.id)"
      >
        <div class="photo">
          <img
            :src="
              item.profile_path != null
                ? moviePoster + item.profile_path
                : emptyprofile
            "
            alt="Cast profile"
          />
        </div>
        <h2>{{ item.name }}</h2>
        <h3>{{ item.character }}</h3>
        <p></p>
      </div>
    </div>
    <el-dialog v-model="isShowCastDetail" title="Detail">
      <el-descriptions class="margin-top" :column="1">
        <el-descriptions-item label="Name:">{{
          castDetail.name
        }}</el-descriptions-item>
        <el-descriptions-item label="Birthday:">{{
          castDetail.birthday
        }}</el-descriptions-item>
        <el-descriptions-item label="Department:">
          <el-tag size="small">{{ castDetail.known_for_department }}</el-tag>
        </el-descriptions-item>
        <el-descriptions-item label="Popularity:">{{
          castDetail.popularity
        }}</el-descriptions-item>
        <el-descriptions-item label="Also known as:">{{
          castDetail.also_known_as
        }}</el-descriptions-item>
        <el-descriptions-item label="Biography:">{{
          castDetail.biography
        }}</el-descriptions-item>
      </el-descriptions>

      <template #footer>
        <span class="dialog-footer">
          <el-button type="primary" @click="isShowCastDetail = false"
            >Confirm</el-button
          >
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<script>
import { ref, inject, onBeforeMount } from "vue";
import { useRoute } from "vue-router";
import env from "@/env.js";
import { YoutubeVue3 } from "youtube-vue3";
import ToolMethod from "../tools.js";

import {
  LikeFilled,
  LikeOutlined,
  DislikeFilled,
  DislikeOutlined,
} from "@ant-design/icons-vue";

export default {
  components: {
    LikeFilled,
    LikeOutlined,
    DislikeFilled,
    DislikeOutlined,
    YoutubeVue3,
  },

  setup() {
    const axios = inject("axios"); // inject axios
    const movie = ref({});
    const casts = ref({});
    const castList = ref([]);
    const isMore = ref("");
    const castDetail = ref({});
    const start = ref();
    const route = useRoute();
    const movieid = ref("");
    const imdbmovieid = ref("");
    const tmdbreview = ref([]);
    const amdbreview = ref([]);
    const imdbreview = ref([]);
    const moviePoster = ref("");
    const video_id = ref("");
    const emptyprofile = ref("");
    const isShowTrailer = ref(false);
    const isCommnetLoading = ref(false);
    const isShowCastDetail = ref(false);
    let youtube = ref(null);
    moviePoster.value = env.tmdbpic;
    movieid.value = route.params.id;
    emptyprofile.value =
      "https://img1.sc115.com/uploads/sc/jpg/HD/49/21850.jpg";
    //comments
    const comments = ref([]);
    const submitting = ref(false);
    const commentsValue = ref("");
    onBeforeMount(() => {
      // fetch movie detail
      axios
        .get(env.tmdbmovieapi + movieid.value + "?" + env.tmdbkey)
        .then((response) => {
          movie.value = response.data;
          console.log("movie detail");
          console.log(movie.value);
          start.value = movie.value.vote_average / 2;
          console.log("imdbmovieid");
          console.log(imdbmovieid.value);
          imdbmovieid.value = response.data.imdb_id;
          //Fetch IMDB Comments
          axios
            .get("/api/movieImdb/movieImdbReviews?movieId=" + imdbmovieid.value)
            .then((response) => {
              imdbreview.value = response.data.data.reviews.items;
              console.log("imdbreview detail");
              console.log(response.data);
            });
        });

      //Fetch trailer
      axios
        .get(
          env.tmdbmovieapi +
            movieid.value +
            env.tmdbvideo +
            env.tmdbkey +
            env.tmdbtail
        )
        .then((response) => {
          const video = response.data.results;
          console.log("video_id");
          console.log(video);
          // TODO no videos
          video_id.value = video[0].key;
          console.log(video_id.value);
        });

      //Fetch casts
      axios
        .get(
          env.tmdbmovieapi +
            movieid.value +
            env.tmdbcredits +
            env.tmdbkey +
            env.tmdbtail
        )
        .then((response) => {
          casts.value = response.data;
          console.log("casts detail");
          console.log(casts.value);
          if (response.data.cast.length <= 10) {
            castList.value = casts.value.cast;
            isMore.value = "";
          } else {
            castList.value = response.data.cast.slice(0, 10);
            isMore.value = "More";
          }
        });

      //Fetch TMDB Comments
      axios
        .get("/api/movieTmdb/movieTmdbReviews?movieId=" + movieid.value)
        .then((response) => {
          tmdbreview.value = response.data.data.reviews[0];
          console.log("tmdbreview detail");
          console.log(tmdbreview.value);
        });
      getAMDBComments();
    });

    const getAMDBComments = () => {
      //Fetch AMDB Comments
      axios
        .get("/api/comments/showComments?movieId=" + movieid.value)
        .then((response) => {
          amdbreview.value = response.data.data;
          console.log("amdbreview detail");
          console.log(response.data);
          console.log(amdbreview.value);

          isCommnetLoading.value = false;
        });
    };

    const handleCancel = () => {
      isShowTrailer.value = false;
    };

    const showToxicText = (rate) => {
      return ToolMethod.showToxicText(rate);
    };

    const changeToPercent = (value) => {
      return ToolMethod.changeToPercent(value);
    };

    const changeText = () => {
      console.log("castList.value.length");
      console.log(castList.value.length);
      console.log(casts.value.cast);
      if (castList.value.length <= 10) {
        castList.value = casts.value.cast;
        isMore.value = "Less";
      } else {
        castList.value = casts.value.cast.slice(0, 10);
        isMore.value = "More";
      }
    };

    // comments
    const handleSubmit = () => {
      if (!commentsValue.value) {
        return;
      }
      isCommnetLoading.value = true;
      submitting.value = true;
      // Add comments
      axios
        .get(
          "/api/comments/addComments?movieId=" +
            movieid.value +
            "&comment=" +
            commentsValue.value
        )
        .then((response) => {
          // tmdbreview.value = response.data;
          console.log("Add comments ");
          console.log(response.data);
          submitting.value = false;
          getAMDBComments();
        });

      // submitting.value = true;
      // setTimeout(() => {
      //   submitting.value = false;
      //   comments.value = [
      //     {
      //       author: "Han Solo",
      //       avatar:
      //         "https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png",
      //       content: commentsValue.value,
      //       datetime: moment().fromNow(),
      //     },
      //     ...comments.commentsValue,
      //   ];
      //   commentsValue.value = "";
      // }, 1000);
    };

    const showCastDetail = (id) => {
      isShowCastDetail.value = true;
      console.log("showCastDetail");
      console.log(id);
      //Fetch Cast Detials
      axios
        .get(env.tmdbperson + id + "?" + env.tmdbkey + env.tmdbtail)
        .then((response) => {
          castDetail.value = response.data;
          console.log("castDetail detail");
          console.log(castDetail.value);
        });
    };
    return {
      movie,
      start,
      casts,
      moviePoster,
      video_id,
      imdbmovieid,
      movieid,
      youtube,
      isShowTrailer,
      emptyprofile,
      isMore,
      castList,
      // comments
      comments,
      submitting,
      commentsValue,
      tmdbreview,
      imdbreview,
      amdbreview,
      castDetail,
      isShowCastDetail,
      isCommnetLoading,
      handleCancel,
      handleSubmit,
      showCastDetail,
      showToxicText,
      changeToPercent,
      changeText,
    };
  },
};
</script>

<style lang="scss" >
.detail-page {
  .movie-detail {
    padding: 50px;

    .tag-group {
      margin-right: 20px;
      margin-bottom: 10px;
    }
    h2 {
      color: #fff;
      font-size: 28px;
      font-weight: 600;
      margin-bottom: 16px;
    }
    .featured-img {
      display: block;
      max-width: 300px;
      margin-bottom: 16px;
    }
    p {
      color: #fff;
      font-size: 18px;
      line-height: 1.4;
    }
  }
  .morebutton {
    font-size: 40px;
    color: #fff;
    text-align: right;
    margin-right: 150px;
  }
  .movie-casts {
    display: flex;
    flex-wrap: wrap;
    margin-left: 30px;
    .cast {
      max-width: 25%;
      flex: 1 1 50%;
      padding: 16px 8px;

      .cast-link {
        display: flex;
        flex-direction: column;
        height: 100%;
        .product-image {
          position: relative;
          display: block;
          img {
            display: block;
            width: 100%;
            height: 350px;
            object-fit: cover;
          }
          .type {
            position: absolute;
            padding: 8px 16px;
            background-color: rgba(86, 98, 168, 0.8);
            color: #fff;
            bottom: 16px;
            left: 0px;
            text-transform: capitalize;
          }
        }
        .detail {
          background-color: #111111;
          padding: 16px 8px;
          flex: 1 1 100%;
          border-radius: 0px 0px 8px 8px;
          .character {
            color: #aaa;
            font-size: 14px;
          }
          h3 {
            color: #fff;
            font-weight: 600;
            font-size: 18px;
          }
        }
      }
    }
  }

  .comments {
    margin: 2.5rem auto 0;
    max-width: 90%;
    padding: 0 1.25rem;
    h1 {
      color: #fff;
    }
  }
  .comment-wrap {
    margin-bottom: 1.25rem;
    display: table;
    width: 100%;
    min-height: 5.3125rem;
  }
  .photo-avatar {
    padding-top: 0.625rem;
    display: table-cell;
    width: 3.5rem;
  }
  .photo-avatar .avatar {
    height: 2.25rem;
    width: 2.25rem;
    border-radius: 50%;
    background-size: contain;
  }
  .comment-block {
    padding: 5px;
    background-color: #fff;
    display: table-cell;
    vertical-align: top;
    border-radius: 0.1875rem;
    box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.08);
  }
  .comment-text {
    margin-bottom: 1.25rem;
  }
  .bottom-comment {
    color: #acb4c2;
    font-size: 0.875rem;
  }
  .comment-date {
    float: left;
  }
  .comment-actions {
    float: right;
  }
  .comment-actions li {
    display: inline;
  }
  .comment-actions li.toxicrate {
    padding-right: 0.625rem;
    border-right: 1px solid #e1e5eb;
  }
  .comment-actions li.report {
    padding-left: 0.625rem;
  }
}

.card {
  /* flex布局下元素不按比例缩放 */
  flex-shrink: 0;
  flex-grow: 0;
  position: relative;
  width: 150px;
  height: 200px;
  overflow: hidden;
  margin: 20px;
  background-color: var(--border-color);
  border-radius: 20px;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  /* flex 子元素 纵向排列 */
  // flex-direction: column;
  /* 增加个阴影 */
  box-shadow: 0 0 30px #5c5b5b;
  /* 同意给字体价格颜色 */
  color: var(--font_color);

  .photo {
    position: absolute;
    /* 默认为放大 */
    width: 100%;
    height: 100%;
    top: 0px;
    // border-radius: 0%;
    overflow: hidden;
    transition: 0.5s;
    border-radius: 18px;
  }

  h2 {
    position: absolute;
    top: 280px;
    color: #fff;
    transition: 0.5s;
  }
  h3 {
    margin-top: 170px;
    font-size: 16px;
    width: 100%;
    color: #fff;
    font-weight: normal;
    text-align: center;
    margin-bottom: 20px;
    padding-bottom: 20px;
    border-bottom: 1px solid var(--h2_border_color);
  }
  p {
    width: 90%;
    /* 段落缩进2个字符大小 */
    text-indent: 2em;
    font-size: 8px;
    color: #ffffff;
    margin-bottom: 10px;
    line-height: 30px;
  }

  a {
    color: var(--font_color);
    text-decoration: none;
    // padding: 12px 36px;
    border: 1px solid var(--a_border_color);
    border-radius: 8px;
  }
}
.photo::before {
  /* 通过before增加渐变背景实现遮罩，让文字默认看起来清晰一些 */
  position: absolute;
  content: "";
  width: 100%;
  height: 100%;
  background-image: linear-gradient(
    to top,
    rgb(51, 50, 50),
    transparent,
    transparent
  );
}
.card:hover .photo::before {
  /* 缩小时隐藏 */
  display: none;
}

.photo img {
  /* 图片高宽均为100% */
  /* 然后按照cover缩放，裁切长边 */
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.card:hover .photo {
  /* 鼠标移上变小 */
  width: 120px;
  height: 120px;
  top: 10px;
  left: 10px;
  border-radius: 50%;
  box-shadow: 0 0 20px #111;
}

.card:hover h2 {
  font-size: 15px;
  position: absolute;
  top: 140px;
}

a:hover {
  color: #fff;
  background-color: var(--a_hover_background_color);
}
</style>