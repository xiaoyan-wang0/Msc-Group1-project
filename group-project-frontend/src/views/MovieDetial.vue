 <template>
  <div class="detail-page">
    <a-modal
      :visible="dialogVisible"
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
        @click="dialogVisible = true"
      />
      <el-tag
        class="tag-group"
        style="magin-right: 8px"
        v-for="item in movie.genres"
        :key="item.id"
      >
        {{ item.name }}
      </el-tag>
      <p>{{ movie.overview }}</p>
      <a-rate :value="start" disabled allowHalf />
      <p>{{ movie.vote_average }}</p>
    </div>

    <div class="movie-casts">
      <div class="cast" v-for="item in casts.cast" :key="item.id">
        <router-link :to="'/movie/' + item.imdbID" class="cast-link">
          <div class="product-image">
            <img
              :src="
                item.profile_path != null
                  ? moviePoster + item.profile_path
                  : emptyprofile
              "
              alt="Cast profile"
            />
            <!-- <div class="type">{{ movie.Type }}</div> -->
          </div>
          <div class="detail">
            <p class="character">{{ item.character }}</p>
            <h3>{{ item.name }}</h3>
          </div>
        </router-link>
      </div>
    </div>

    <div class="comments">
      <div
        class="comment-wrap"
        v-for="item in tmdbreview.results"
        :key="item.id"
      >
        <div class="photo">
          <div class="avatar">
            <a-avatar :src="item.author_details.avatar_path" />
          </div>
        </div>
        <div class="comment-block">
          <p class="comment-author">{{ item.author }}</p>
          <p class="comment-text">{{ item.content }}</p>
          <div class="bottom-comment">
            <div class="comment-date">{{ item.updated_at }}</div>
            <ul class="comment-actions">
              <li class="complain">Complain</li>
              <li class="reply">Reply</li>
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
            <a-textarea v-model:value="value" :rows="4" />
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
    </div>
  </div>
</template>

<script>
import { ref, inject, onBeforeMount, onMounted } from "vue";
import { useRoute } from "vue-router";
import env from "@/env.js";
import moment from "moment";
import { YoutubeVue3 } from "youtube-vue3";

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
    const start = ref();
    const route = useRoute();
    const movieid = ref();
    const tmdbreview = ref();
    const moviePoster = ref("");
    const video_id = ref("");
    const emptyprofile = ref("");
    const dialogVisible = ref(false);
    let youtube = ref(null);
    moviePoster.value = env.tmdbpic;
    movieid.value = route.params.id;
    emptyprofile.value =
      "https://img1.sc115.com/uploads/sc/jpg/HD/49/21850.jpg";
    //comments
    const comments = ref([]);
    const submitting = ref(false);
    const value = ref("");
    onBeforeMount(() => {
      // fetch movie detail
      axios
        .get(env.tmdbmovieapi + movieid.value + "?" + env.tmdbkey)
        .then((response) => {
          movie.value = response.data;
          console.log("movie detail");
          console.log(movie.value);
          start.value = movie.value.vote_average / 2;
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
        });

      //Fetch TMDB Comments
      axios
        .get(
          env.tmdbmovieapi +
            movieid.value +
            env.tmdbreviews +
            env.tmdbkey +
            env.tmdbtail
        )
        .then((response) => {
          tmdbreview.value = response.data;
          console.log("tmdbreview detail");
          console.log(tmdbreview.value);
        });
    });

    // onMounted(() => {
    //   console.log("onMounted");
    // });

    const handleCancel = () => {
      dialogVisible.value = false;
    };

    // comments
    const handleSubmit = () => {
      if (!value.value) {
        return;
      }

      submitting.value = true;
      setTimeout(() => {
        submitting.value = false;
        comments.value = [
          {
            author: "Han Solo",
            avatar:
              "https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png",
            content: value.value,
            datetime: moment().fromNow(),
          },
          ...comments.value,
        ];
        value.value = "";
      }, 1000);
    };

    return {
      movie,
      start,
      casts,

      handleCancel,

      moviePoster,
      video_id,
      youtube,
      dialogVisible,
      emptyprofile,
      // comments
      comments,
      submitting,
      value,
      tmdbreview,
      handleSubmit,
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
      max-width: 200px;
      margin-bottom: 16px;
    }
    p {
      color: #fff;
      font-size: 18px;
      line-height: 1.4;
    }
  }
  .movie-casts {
    display: flex;
    flex-wrap: wrap;
    margin-left: 30px;
    .cast {
      max-width: 20%;
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
  }
  .comment-wrap {
    margin-bottom: 1.25rem;
    display: table;
    width: 100%;
    min-height: 5.3125rem;
  }
  .photo {
    padding-top: 0.625rem;
    display: table-cell;
    width: 3.5rem;
  }
  .photo .avatar {
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
  .comment-actions li.complain {
    padding-right: 0.625rem;
    border-right: 1px solid #e1e5eb;
  }
  .comment-actions li.reply {
    padding-left: 0.625rem;
  }
}
</style>