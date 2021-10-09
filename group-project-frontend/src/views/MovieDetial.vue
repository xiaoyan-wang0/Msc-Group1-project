 <template>
  <div class="detail">
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
        <router-link :to="'/movie/' + movie.imdbID" class="cast-link">
          <a-card hoverable style="width: 150px">
            <template #cover>
              <img
                alt="profile"
                :src="
                  item.profile_path != null
                    ? moviePoster + item.profile_path
                    : emptyprofile
                "
              />
            </template>
            <a-card-meta :title="item.character">
              <template #description>{{ item.name }}</template>
            </a-card-meta>
          </a-card>
        </router-link>
      </div>
    </div>

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
        @ended="onEnded"
        @paused="onPaused"
        @played="onPlayed"
      />
    </a-modal>
    <div class="commonts">
      <a-list
        v-if="comments.length"
        :data-source="comments"
        :header="`${comments.length} ${
          comments.length > 1 ? 'replies' : 'reply'
        }`"
        item-layout="horizontal"
      >
        <template #renderItem="{ item }">
          <a-list-item>
            <a-comment
              :author="item.author"
              :avatar="item.avatar"
              :content="item.content"
              :datetime="item.datetime"
            />
          </a-list-item>
        </template>
      </a-list>
      <a-comment>
        <template #avatar>
          <a-avatar
            src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
            alt="Han Solo"
          />
        </template>
        <template #content>
          <a-form-item>
            <a-textarea  v-model:value="value" :rows="4"/>
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

      // onEnded();
    });

    onMounted(() => {
      console.log("onMounted");
    });

    const handleCancel = () => {
      dialogVisible.value = false;
    };

    // commonts
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
      // commonts
      comments,
      submitting,
      value,
      handleSubmit,
    };
  },
};
</script>

<style lang="scss" >
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
    max-width: 10%;
    flex: 1 1 50%;
    padding: 16px 8px;

    .cast-link {
      display: flex;
      flex-direction: column;
      height: 100%;
    }
  }
}
</style>