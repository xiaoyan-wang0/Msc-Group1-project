 <template>
 <body>
  <section class="anime-details spad">
    <div class="container">
      <div class="anime__details__content">
        <div class="row">
          <div class="col-lg-3">
            <div class="anime__details__pic set-bg">
              <img
                :src="moviePoster + movie.poster_path"
                alt="Movie Poster"
                class="featured-img"
                @click="isShowTrailer = true"
              />
            </div>
          </div>
          <div class="col-lg-9">
            <div class="anime__details__text">
              <div class="anime__details__title">
                <h3>{{ movie.original_title }}</h3>
                <span>{{ movie.release_date }}</span>
              </div>
              <div class="anime__details__rating">
                <a-rate :value="start" disabled allowHalf />
                <p>{{ movie.vote_average }}</p>
              </div>

              <p style="font-size: 20px">{{ movie.overview }}</p>

            <div class="anime__details__widget">
                                <div class="row">
                                    <div class="col-lg-6 col-md-6">
                                        <ul>
                                            <li><span>Type:</span> TV Series</li>
                                            <li><span>Studios:</span> Lerche</li>
                                            <li><span>Date aired:</span> Oct 02, 2019 to ?</li>
                                            <li><span>Status:</span> Airing</li>
                                            <li><span>Genre:</span> Action, Adventure, Fantasy, Magic</li>
                                        </ul>
                                    </div>
                                    <div class="col-lg-6 col-md-6">
                                        <ul>
                                            <li><span>Scores:</span> 7.31 / 1,515</li>
                                            <li><span>Rating:</span> 8.5 / 161 times</li>
                                            <li><span>Duration:</span> 24 min/ep</li>
                                            <li><span>Quality:</span> HD</li>
                                            <li><span>Views:</span> 131,541</li>
                                        </ul>
                                    </div>
                                </div>
                          

              <div class="movie-tag-group">
                  <div class="morebutton">
                <span>Casts </span>
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
                    <el-tag size="small">{{
                      castDetail.known_for_department
                    }}</el-tag>
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
                <span v-for="item in movie.genres" :key="item.id" style="">{{
                  item.name
                }}</span>
              </div>
               </div>

               <div class="anime__details__btn">
                                <a href="#" class="follow-btn"><i class="fa fa-heart"></i> ADD Like list</a>
                                <a href="#" class="watch-btn"><span>Watch trailer</span> </a>
                                </div>
            </div>
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col-lg-8 col-md-8">
          <div class="anime__details__review">
            <div class="section-title">
              <h5>reviews</h5>
            </div>
            <a-tabs type="card">
              <a-tab-pane key="amdb" tab="AMDB reviews" style="">
                <div
                  class="comment-wrap"
                  v-for="item in amdbreview"
                  :key="item.id"
                >
                  <div class="photo-avatar">
                    <div class="avatar">
                      <a-avatar :src="emptyprofile" />
                    </div>
                  </div>
                  <div class="anime__review__item">
                    <div class="anime__review__item__pic"></div>
                    <div class="anime__review__item__text">
                      <h6 class="comment-author">
                        {{ item.userName }}
                      </h6>
                      <p class="comment-text">{{ item.comment }}</p>
                      <div class="bottom-comment">
                        <div class="comment-date">
                          {{ formatDate(item.createTime) }}
                        </div>
                        <ul class="comment-actions">
                          <li class="toxicrate">
                            {{ showToxicText(item.toxic) }} :
                            {{ changeToPercent(item.toxic) }}
                          </li>
                          <li class="sentiemnt-rate">
                            {{ showSentiemntText(item.sentiment) }} :
                            {{ changeToPercent(item.sentiment) }}
                          </li>
                          <li class="report">Report</li>
                        </ul>
                      </div>
                    </div>
                  </div>
                </div>

                <div class="anime__details__form">
                  <div class="section-title">
                    <h5>Your Comment</h5>
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
                </div>
              </a-tab-pane>

              <a-tab-pane key="tmdb" tab="TMDB reviews">
                <div class="section-title">
                  <h5>TMDB reviews</h5>
                </div>
                <div
                  class="comment-wrap"
                  v-for="item in tmdbreview"
                  :key="item.id"
                >
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
                  <div class="anime__review__item">
                    <div class="anime__review__item__pic"></div>
                    <div class="anime__review__item__text">
                      <h6 class="comment-author">{{ item.author }}</h6>
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
                </div>
              </a-tab-pane>
              <a-tab-pane key="imdb" tab="IMDB reviews">
                <div class="section-title">
                  <h5>IMDB reviews</h5>
                </div>
                <div
                  class="comment-wrap"
                  v-for="item in imdbreview"
                  :key="item.id"
                >
                  <div class="photo-avatar">
                    <div class="avatar">
                      <a-avatar :src="emptyprofile" />
                    </div>
                  </div>

                  <div class="anime__review__item">
                    <div class="anime__review__item__pic"></div>
                    <div class="anime__review__item__text">
                      <h6 class="comment-author">{{ item.username }}</h6>
                      <p class="comment-text">{{ item.content }}</p>
                      <div class="bottom-comment">
                        <div class="comment-date">{{ item.date }}</div>
                        <ul class="comment-actions">
                          <li class="toxicrate">
                            {{ showToxicText(item.toxic.tag[0]) }}:{{
                              changeToPercent(item.toxic.tag)
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
                </div>
              </a-tab-pane>
              <a-tab-pane key="youtube" tab="Youtube reviews">
                <div class="section-title">
                  <h5>Youtube reviews</h5>
                </div>
                <div
                  class="comment-wrap"
                  v-for="item in youtubereview"
                  :key="item.id"
                >
                  <div class="photo-avatar">
                    <div class="avatar">
                      <a-avatar :src="item.profile_picture" />
                    </div>
                  </div>

                  <div class="anime__review__item">
                    <div class="anime__review__item__pic"></div>
                    <div class="anime__review__item__text">
                      <h6 class="comment-author">{{ item.username }}</h6>
                      <p class="comment-text">{{ item.review }}</p>
                      <div class="bottom-comment">
                        <div class="comment-date">{{ item.date }}</div>
                      </div>
                    </div>
                  </div>
                </div>
              </a-tab-pane>
            </a-tabs>
          </div>
        </div>
        <div class="col-lg-4 col-md-4">
          <div class="anime__details__sidebar">
            <div class="section-title">
              <h5>you might like...</h5>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  </body>
</template> 

<script>
import { ref, inject, onBeforeMount, computed } from "vue";
import { useRoute } from "vue-router";
import { useStore } from "vuex";
import { YoutubeVue3 } from "youtube-vue3";
import env from "@/env.js";
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
    const store = useStore();
    const currentUser = computed(() => store.state.auth.user);
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
    const youtubereview = ref([]);
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
            .get(
              env.AMDBAPI +
                "movieImdb/movieImdbReviews?movieId=" +
                imdbmovieid.value,
              { withCredentials: true }
            )
            .then((response) => {
              imdbreview.value = response.data.data.reviews.items;
              console.log("imdbreview detail");
              console.log(response.data);
            });

          //Fetch Youtube Comments
          axios
            .get(
              env.AMDBAPI +
                "movieYoutube/movieYoutubeReviews?movieName=" +
                movie.value.original_title,
              { withCredentials: true }
            )
            .then((response) => {
              youtubereview.value = response.data.data;
              console.log("youtubereview detail");
              console.log(youtubereview.value);
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
            castList.value = response.data.cast.slice(0, 3);
            isMore.value = "More";
          }
        });

      //Fetch TMDB Comments
      axios
        .get(
          env.AMDBAPI + "movieTmdb/movieTmdbReviews?movieId=" + movieid.value,
          { withCredentials: true }
        )
        .then((response) => {
          tmdbreview.value = response.data.data.reviews[0];
          console.log("tmdbreview detail");
          console.log(tmdbreview.value);
        });

      getAMDBComments();
    });

    const getAMDBComments = () => {
      //   //Fetch AMDB Comments
      //   axios
      //     .get(
      //       env.AMDBAPI +
      //         "comments/showComments?movieId=" +
      //         movieid.value +
      //         "&userId=" +
      //         currentUser.value.data.userId,
      //       {
      //         withCredentials: true,
      //       }
      //     )
      //     .then((response) => {
      //       amdbreview.value = response.data.data;
      //       console.log("amdbreview detail");
      //       console.log(response.data);
      //       console.log(amdbreview.value);
      //       isCommnetLoading.value = false;
      //     });
    };

    const handleCancel = () => {
      isShowTrailer.value = false;
    };

    const showToxicText = (rate) => {
      return ToolMethod.showToxicText(rate);
    };

    const showSentiemntText = (rate) => {
      return ToolMethod.showSentiemntText(rate);
    };

    const formatDate = (value) => {
      return ToolMethod.formatDate(value);
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
          env.AMDBAPI +
            "comments/addComments?movieId=" +
            movieid.value +
            "&comment=" +
            commentsValue.value +
            "&userId=" +
            currentUser.value.data.userId,
          { withCredentials: true }
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
      youtubereview,
      castDetail,
      isShowCastDetail,
      isCommnetLoading,
      handleCancel,
      handleSubmit,
      showCastDetail,
      showToxicText,
      showSentiemntText,
      changeToPercent,
      changeText,
      formatDate,
    };
  },
};
</script>

<style lang="scss" >
html,
body {
  height: 100%;
  font-family: "Mulish", sans-serif;
  -webkit-font-smoothing: antialiased;
  background: #0b0c2a;
}

h1,
h2,
h3,
h4,
h5,
h6 {
  margin: 0;
  color: #111111;
  font-weight: 400;
  font-family: "Mulish", sans-serif;
}

h1 {
  font-size: 70px;
}

h2 {
  font-size: 36px;
}

h3 {
  font-size: 30px;
}

h4 {
  font-size: 24px;
}

h5 {
  font-size: 18px;
}

h6 {
  font-size: 16px;
}

p {
  font-size: 15px;
  font-family: "Mulish", sans-serif;
  color: #3d3d3d;
  font-weight: 400;
  line-height: 25px;
  margin: 0 0 15px 0;
}

img {
  max-width: 100%;
}

input:focus,
select:focus,
button:focus,
textarea:focus {
  outline: none;
}

a:hover,
a:focus {
  text-decoration: none;
  outline: none;
  color: #ffffff;
}

ul,
ol {
  padding: 0;
  margin: 0;
}

/*---------------------
  Helper CSS
-----------------------*/

.section-title {
  margin-bottom: 30px;
}

.section-title h4,
.section-title h5 {
  color: burlywood;
  font-weight: 600;
  line-height: 21px;
  text-transform: uppercase;
  padding-left: 20px;
  position: relative;
  font-family: "Oswald", sans-serif;
}

.section-title h4:after,
.section-title h5:after {
  position: absolute;
  left: 0;
  top: -6px;
  height: 32px;
  width: 4px;
  background: #e53637;
  content: "";
}

.set-bg {
  background-repeat: no-repeat;
  background-size: cover;
  background-position: top center;
}

.spad {
  padding-top: 100px;
  padding-bottom: 100px;
}

.text-white h1,
.text-white h2,
.text-white h3,
.text-white h4,
.text-white h5,
.text-white h6,
.text-white p,
.text-white span,
.text-white li,
.text-white a {
  color: #fff;
}

/* buttons */

.primary-btn {
  display: inline-block;
  font-size: 13px;
  font-weight: 700;
  text-transform: uppercase;
  color: #ffffff;
  letter-spacing: 2px;
}

.primary-btn span {
  font-size: 18px;
  margin-left: 5px;
  position: relative;
  top: 3px;
}

.site-btn {
  font-size: 13px;
  color: #ffffff;
  background: #e53637;
  font-weight: 700;
  border: none;
  border-radius: 2px;
  letter-spacing: 2px;
  text-transform: uppercase;
  display: inline-block;
  padding: 12px 30px;
}

/* Preloder */

#preloder {
  position: fixed;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  z-index: 999999;
  background: #000;
}

.loader {
  width: 40px;
  height: 40px;
  position: absolute;
  top: 50%;
  left: 50%;
  margin-top: -13px;
  margin-left: -13px;
  border-radius: 60px;
  animation: loader 0.8s linear infinite;
  -webkit-animation: loader 0.8s linear infinite;
}

@keyframes loader {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
    border: 4px solid #f44336;
    border-left-color: transparent;
  }
  50% {
    -webkit-transform: rotate(180deg);
    transform: rotate(180deg);
    border: 4px solid #673ab7;
    border-left-color: transparent;
  }
  100% {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg);
    border: 4px solid #f44336;
    border-left-color: transparent;
  }
}

@-webkit-keyframes loader {
  0% {
    -webkit-transform: rotate(0deg);
    border: 4px solid #f44336;
    border-left-color: transparent;
  }
  50% {
    -webkit-transform: rotate(180deg);
    border: 4px solid #673ab7;
    border-left-color: transparent;
  }
  100% {
    -webkit-transform: rotate(360deg);
    border: 4px solid #f44336;
    border-left-color: transparent;
  }
}

.spacial-controls {
  position: fixed;
  width: 111px;
  height: 91px;
  top: 0;
  right: 0;
  z-index: 999;
}

.spacial-controls .search-switch {
  display: block;
  height: 100%;
  padding-top: 30px;
  background: #323232;
  text-align: center;
  cursor: pointer;
}

.search-model {
  display: none;
  position: fixed;
  width: 100%;
  height: 100%;
  left: 0;
  top: 0;
  background: #000;
  z-index: 99999;
}

.search-model-form {
  padding: 0 15px;
}

.search-model-form input {
  width: 500px;
  font-size: 40px;
  border: none;
  border-bottom: 2px solid #333;
  background: 0 0;
  color: #999;
}

.search-close-switch {
  position: absolute;
  width: 50px;
  height: 50px;
  background: #333;
  color: #fff;
  text-align: center;
  border-radius: 50%;
  font-size: 28px;
  line-height: 28px;
  top: 30px;
  cursor: pointer;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  justify-content: center;
}






/*---------------------
  Anime Details
-----------------------*/

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
  color: #6b5f5f;
  font-weight: 700;
  margin-bottom: 13px;
}

.anime__details__title span {
  font-size: 15px;
  color: #b7b7b7;
  display: block;
}

.anime__details__rating {
  text-align: center;
  position: absolute;
  right: 0;
  top: 0;
}

.anime__details__rating .rating i {
  font-size: 24px;
  color: #e89f12;
  display: inline-block;
}

.anime__details__rating span {
  display: block;
  font-size: 18px;
  color: #b7b7b7;
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

.anime__details__btn .follow-btn {
  font-size: 13px;
  color: #ffffff;
  background: #e53637;
  display: inline-block;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  padding: 14px 20px;
  border-radius: 4px;
  margin-right: 11px;
}

.anime__details__btn .watch-btn span {
  font-size: 13px;
  color: #ffffff;
  background: #e53637;
  display: inline-block;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  padding: 14px 20px;
  border-radius: 4px 0 0 4px;
  margin-right: 1px;
}

.anime__details__btn .watch-btn i {
  font-size: 20px;
  display: inline-block;
  background: #e53637;
  padding: 11px 5px 16px 8px;
  color: #ffffff;
  border-radius: 0 4px 4px 0;
}

.anime__details__review {
  margin-bottom: 55px;
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



/*--------------------------------- Responsive Media Quaries -----------------------------*/

@media only screen and (min-width: 1200px) and (max-width: 1300px) {
  .hero {
    overflow: hidden;
  }
}

@media only screen and (min-width: 1200px) {
  .container {
    max-width: 1170px;
  }
}

/* Medium Device = 1200px */

@media only screen and (min-width: 992px) and (max-width: 1199px) {
  .hero {
    overflow: hidden;
  }
  .login__form {
    position: relative;
    padding-left: 32px;
  }
  .login__social__links ul li a {
    width: 380px;
  }
  .blog__item__text {
    padding: 0 50px;
  }
}

/* Tablet Device = 768px */

@media only screen and (min-width: 768px) and (max-width: 991px) {
  .hero {
    overflow: hidden;
  }
  .header {
    position: relative;
  }
  .header .container {
    position: relative;
  }
  .header__right {
    position: absolute;
    right: 120px;
    top: -42px;
    padding: 0;
  }
  .header__menu {
    display: none;
  }
  .slicknav_menu {
    background: transparent;
    padding: 0;
    display: block;
  }
  .slicknav_nav {
    position: absolute;
    left: 0;
    top: 60px;
    width: 100%;
    background: #ffffff;
    padding: 15px 30px;
    z-index: 9;
  }
  .slicknav_nav ul {
    margin: 0;
  }
  .slicknav_nav .slicknav_row,
  .slicknav_nav a {
    padding: 7px 0;
    margin: 0;
    color: #111111;
    font-weight: 600;
  }
  .slicknav_btn {
    border-radius: 0;
    background-color: #222;
    position: absolute;
    right: 0;
    top: 9px;
  }
  .slicknav_nav .slicknav_arrow {
    color: #111111;
  }
  .slicknav_nav .slicknav_row:hover {
    border-radius: 0;
    background: transparent;
    color: #111111;
  }
  .slicknav_nav a:hover {
    border-radius: 0;
    background: transparent;
    color: #111111;
  }
  .product__sidebar {
    padding-top: 50px;
  }
  .footer__logo {
    text-align: center;
    margin-bottom: 20px;
  }
  .footer__nav {
    margin-bottom: 15px;
  }
  .footer__copyright__text {
    text-align: center;
  }
  .anime__details__widget ul li span {
    width: 90px;
  }
  .anime__details__pic {
    margin-bottom: 40px;
  }
  .anime__details__sidebar {
    padding-top: 50px;
  }
  .login__form {
    padding-left: 0;
    margin-bottom: 40px;
  }
  .login__form:after {
    display: none;
  }
  .login__form form .input__item {
    width: auto;
  }
  .login__register {
    padding-left: 0;
  }
  .signup .login__social__links {
    padding-left: 0;
  }
}

/* Wide Mobile = 480px */

@media only screen and (max-width: 767px) {
  .hero {
    overflow: hidden;
  }
  .header {
    position: relative;
  }
  .header .container {
    position: relative;
  }
  .header__right {
    position: absolute;
    right: 120px;
    top: -42px;
    padding: 0;
  }
  .header__menu {
    display: none;
  }
  .slicknav_menu {
    background: transparent;
    padding: 0;
    display: block;
  }
  .slicknav_nav {
    position: absolute;
    left: 0;
    top: 60px;
    width: 100%;
    background: #ffffff;
    padding: 15px 30px;
    z-index: 9;
  }
  .slicknav_nav ul {
    margin: 0;
  }
  .slicknav_nav .slicknav_row,
  .slicknav_nav a {
    padding: 7px 0;
    margin: 0;
    color: #111111;
    font-weight: 600;
  }
  .slicknav_btn {
    border-radius: 0;
    background-color: #222;
    position: absolute;
    right: 0;
    top: 9px;
  }
  .slicknav_nav .slicknav_arrow {
    color: #111111;
  }
  .slicknav_nav .slicknav_row:hover {
    border-radius: 0;
    background: transparent;
    color: #111111;
  }
  .slicknav_nav a:hover {
    border-radius: 0;
    background: transparent;
    color: #111111;
  }
  .product__sidebar {
    padding-top: 50px;
  }
  .footer__logo {
    text-align: center;
    margin-bottom: 20px;
  }
  .footer__nav {
    margin-bottom: 15px;
  }
  .footer__copyright__text {
    text-align: center;
  }
  .blog__details__title h2 {
    font-size: 34px;
    line-height: normal;
  }
  .anime__details__pic {
    margin-bottom: 40px;
  }
  .anime__details__sidebar {
    padding-top: 50px;
  }
  .btn__all {
    text-align: left;
  }
  .product__page__title .section-title {
    margin-bottom: 30px;
  }
  .product__page__title .product__page__filter {
    text-align: left;
  }
  .anime__details__rating {
    text-align: left;
    position: relative;
    margin-bottom: 20px;
  }
  .blog__details__social {
    overflow: hidden;
  }
  .blog__details__title .blog__details__social a {
    margin-right: 10px;
    margin-bottom: 10px;
    width: calc(50% - 10px);
    float: left;
  }
  .login__form {
    padding-left: 0;
    margin-bottom: 40px;
  }
  .login__form:after {
    display: none;
  }
  .login__form form .input__item {
    width: auto;
  }
  .signup .login__social__links {
    padding-left: 0;
  }
  .login__social__links ul li a {
    width: auto;
  }
  .blog__item__text {
    padding: 0 30px;
  }
  .login__register {
    padding-left: 0;
  }
  .product__sidebar__view .filter__controls li {
    margin-right: 2px;
  }
  .search-model-form input {
    width: 100%;
  }
}

/* Small Device = 320px */

@media only screen and (max-width: 479px) {
  .hero__slider.owl-carousel .owl-nav {
    display: none;
  }
  .hero__items {
    padding: 250px 0 42px 15px;
  }
  .hero__text h2 {
    font-size: 32px;
  }
  .footer__nav ul li {
    margin-right: 10px;
  }
  .anime__details__btn .follow-btn {
    padding: 14px 26px;
    margin-right: 11px;
    margin-bottom: 25px;
  }
  .anime__details__widget ul li span {
    width: 85px;
  }
  .anime__video__player .plyr__volume {
    left: 65px;
  }
  .anime__video__player .plyr__controls .plyr__controls__item.plyr__time {
    left: 95px;
  }
  .anime__video__player .plyr__menu {
    margin-right: 60px;
  }
  .blog__details__title h2 {
    font-size: 30px;
    line-height: normal;
  }
  .blog__details__title .blog__details__social a {
    padding: 16px 25px 14px 20px;
  }
  .blog__details__comment__item.blog__details__comment__item--reply {
    padding-left: 0;
  }
  .blog__details__comment__item__pic {
    margin-right: 25px;
  }
  .blog__details__comment__item__text a {
    margin-right: 6px;
  }
  .login__social__links ul li a i {
    left: 20px;
  }
  .login__form .forget_pass {
    position: relative;
    left: 0;
    bottom: 0;
    margin-top: 25px;
  }
  .header__right a {
    margin-right: 10px;
  }
  .anime__review__item__text h6 span {
    font-size: 12px;
  }
  .anime__review__item__text {
    padding: 18px 20px 20px;
  }
}


  .movie-casts {display: flex; flex-wrap: wrap; margin-left: 100px;}

  .cast {max-width: 25%; flex: 1 1 50%; padding: 16px 8px;}

  .card {
  /* flex布局下元素不按比例缩放 */
  flex-shrink: 0;
  flex-grow: 0;
  position: relative;
  width: 50px;
  height: 100px;
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
  width: 30px;
  height: 30px;
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

.movie-casts {
    display: flex;
    flex-wrap: wrap;
    margin-left: 100px;
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

</style>
