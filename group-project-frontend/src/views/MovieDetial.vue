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

      <p>{{ movie.overview }}</p>
      <a-rate :value="start" disabled allowHalf />
      <p>{{ movie.vote_average }}</p>
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

      <!-- </el-dialog> -->
    </a-modal>
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

  methods: {
    stopCurrentVideo() {
      this.$refs.youtube.player.stopVideo();
    },
    onEnded() {
      console.log("## OnEnded");
    },
    onPaused() {
      console.log("## OnPaused");
    },
    onPlayed() {
      console.log("## OnPlayed");
      // this.$refs.youtube.player.stopVideo();
    },
    onReady() {
      this.$refs.youtube.player.stopVideo();
    },
  },
  setup() {
    const axios = inject("axios"); // inject axios
    const movie = ref({});
    const start = ref();
    const route = useRoute();
    const moviePoster = ref("");
    const video_id = ref("");
    const dialogVisible = ref(false);
    let youtube = ref(null);
    moviePoster.value = env.tmdbpic;

    // Comments
    const comments = ref([]);
    const submitting = ref(false);
    const value = ref("");

    const action = ref();
    onBeforeMount(() => {
      // fetch(
      //   `http://www.omdbapi.com/?apikey=${env.omdbkey}&i=${route.params.id}&plot=full`
      // )
      //   .then((response) => response.json())
      //   .then((data) => {
      //     console.log(data);
      //     movie.value = data;
      //     start.value = movie.value.imdbRating / 2;
      //   });

      // fetch movie detail
      axios
        .get(env.tmdbmovieapi + route.params.id + "?" + env.tmdbkey)
        .then((response) => {
          movie.value = response.data;
          console.log("movie detail");
          console.log(movie.value);
          start.value = movie.value.vote_average / 2;
        });

      axios
        .get(
          env.tmdbmovieapi +
            route.params.id +
            env.tmdbvideo +
            env.tmdbkey +
            env.tmdbtail
        )
        .then((response) => {
          const video = response.data.results;
          console.log("video_id");
          console.log(video);
          video_id.value = video[0].key;
          // video_id.value = "Vd2sm63Xwfw"
          console.log(video_id.value);
        });

      // onEnded();
    });

    onMounted(() => {
      console.log("onMounted");
      // console.log(youtube.value.autoplay);
      // youtube.value = ;
    });

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

    const handleCancel = () => {
      dialogVisible.value = false;
    };
    return {
      movie,
      start,
      comments,
      submitting,
      value,
      handleSubmit,
      handleCancel,
      action,
      moviePoster,
      video_id,
      youtube,
      dialogVisible,
    };
  },
};
</script>

<style lang="scss" >
.movie-detail {
  padding: 16px;
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
</style>