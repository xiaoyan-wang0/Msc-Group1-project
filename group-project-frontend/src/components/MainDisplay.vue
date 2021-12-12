<template>
  <section class="product spad maindisplay">
    <div class="affix-div">
      <el-affix :offset="50" target=".maindisplay">
        <!-- <el-button type="primary" @click="isShowDrawer = true"> -->
        <div class="anchor-div" @click="isShowDrawer = true"></div>

        <!-- </el-button> -->
      </el-affix>
      <a-drawer
        v-model:visible="isShowDrawer"
        class="custom-class"
        style="color: red"
        title=""
        placement="right"
        >
        <h5>Go section you like</h5>
        <a-anchor  @change="onChange">
          <a-anchor-link href="#search-div" title="Search" />
          <a-anchor-link href="#carousel" title="Carousel" />
          <a-anchor-link href="#popularMovie" title="Popular Movie" />
          <a-anchor-link href="#hignScoreMovie" title="High score Movie" />
          <a-anchor-link
            href="#mainpage-recommendations"
            title="Recommendations"
          />
        </a-anchor>
      </a-drawer>
    </div>
    <div class="feature-card">
      <div id="carousel" style="">
        <div class="home-carousel-div" style="">
          <div class="home-carousel-left" id="2" style="">
            <div class="main-carousel" v-if="upComingMovieData">
              <el-carousel
                class="carousel-div-defualt"
                :interval="3000"
                direction="vertical"
                height="400px"
              >
                <el-carousel-item v-for="item in fackePic" :key="item.id">
                  <router-link :to="'/movie/' + item.id">
                    <img
                      :src="item.backdrop_path"
                      :alt="item.title"
                      class="featured-img"
                    />
                    <div class="detail">
                      <p>{{ item.title }}</p>
                    </div>
                  </router-link>
                </el-carousel-item>
              </el-carousel>
              <el-carousel
                class="carousel-div-small"
                :interval="3000"
                direction="vertical"
                height="150px"
              >
                <el-carousel-item v-for="item in fackePic" :key="item.id">
                  <router-link :to="'/movie/' + item.id">
                    <img
                      :src="item.backdrop_path"
                      :alt="item.title"
                      class="featured-img"
                    />
                    <div class="detail">
                      <p>{{ item.title }}</p>
                    </div>
                  </router-link>
                </el-carousel-item>
              </el-carousel>
            </div>
          </div>
          <div class="home-carousel-right" id="3" style="">
            <div class="home-carousel-right-title" style="">
              <div class="section-title">
                <h4>
                  <span style="margin-left: 5px">Upcoming</span>
                  <a
                    @click="showResultPage()"
                    class="primary-btn"
                    style="float: right; margin-top: 2px"
                    >View All <span class="arrow_right"></span
                  ></a>
                </h4>
              </div>
            </div>
            <div
              class="home-carousel-right-list"
              style=""
              v-for="item in upComingMovieData.slice(0, 3)"
              :key="item.id"
            >
              <router-link :to="'/movie/' + item.id">
                <div class="home-carousel-right-list-img" style="float: left">
                  <img
                    class="pichover2"
                    style=""
                    :src="moviePoster + item.poster_path"
                    :alt="item.title"
                  />
                </div>
                <div class="home-carousel-right-list-right" style="">
                  <div class="home-carousel-right-list-right-title" style="">
                    {{ item.title }}
                  </div>
                  <div class="home-carousel-right-list-right-content" style="">
                    {{ item.overview }}
                  </div>
                </div>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="container">
      <div class="row">
        <div class="col-lg-8">
          <!-- Upcoming movies -->
          <div id="popularMovie">
            <Showpart
              :itemdata="popularMovieData"
              spacename="Popular Movies"
              isPopularorHighScore="1"
            />
          </div>

          <!-- High score movies -->
          <div id="hignScoreMovie">
            <Showpart
              :itemdata="hignScoreMovieData"
              spacename="High Score Movie"
              isPopularorHighScore="2"
            />
          </div>
        </div>
        <div id="mainpage-recommendations" class="col-lg-4 col-md-6 col-sm-8">
          <div class="product__sidebar">
            <div class="product__sidebar__comment">
              <div class="section-title">
                <h5>The Most Comments movies</h5>
              </div>
              <a-empty v-if="mostRecommendationMovies.length < 1">
                <template #description>
                  <span>
                    <a>Sorry, No recommendations</a>
                  </span>
                </template>
              </a-empty>
              <div
                class="product__sidebar__comment__item"
                v-for="item in mostRecommendationMovies"
                :key="item.id"
              >
                <router-link :to="'/movie/' + item.id">
                  <div class="product__sidebar__comment__item__pic">
                    <img class="pichover" :src="poster + item.poster" alt="" />
                  </div>
                  <div class="product__sidebar__comment__item__text">
                    <h5>
                      <a class="twoline-ellipsis" style="color: white">{{
                        item.title
                      }}</a>
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
                    <span
                      ><i class="fa fa-eye"></i> {{ item.release_date }}</span
                    >
                  </div>
                </router-link>
              </div>
            </div>
            <div
              class="product__sidebar__view"
              v-if="recentRecommendationMovies.length > 0"
            >
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
                    <img class="pichover" :src="poster + item.poster" alt="" />
                  </div>
                  <div class="product__sidebar__comment__item__text">
                    <h5>
                      <a class="twoline-ellipsis" style="color: white">{{
                        item.title
                      }}</a>
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
                    <span
                      ><i class="fa fa-eye"></i> {{ item.release_date }}</span
                    >
                  </div>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { ref, onBeforeMount, computed, nextTick } from "vue";
import { message } from "ant-design-vue";
import env from "@/env.js";
import Showpart from "./ShowPart.vue";
import router from "@/router";
import { useStore } from "vuex";
import ToolMethod from "../tools.js";
import UserApi from "../services/user.service";

export default {
  name: "MainDisplay",
  props: {},
  components: { Showpart },
  setup() {
    const popularMovieData = ref([]);
    const hignScoreMovieData = ref([]);
    const upComingMovieData = ref([]);
    const fackePic = ref([]);
    const store = useStore();
    const mostRecommendationMovies = ref([]);
    const recentRecommendationMovies = ref([]);
    const moviePoster = ref("");
    const isShowDrawer = ref(false);
    moviePoster.value = env.tmdbpic;
    const currentUser = computed(() =>
      JSON.parse(localStorage.getItem("user"))
    );
    const poster = ref("");
    poster.value = env.tmdbpic;
    fackePic.value = [
      {
        id: 425909,
        title: "Ghostbusters: Afterlife",
        backdrop_path: require("@/assets/1.jpg"),
      },
      {
        id: 438695,
        title: "Sing 2",
        backdrop_path: require("@/assets/2.jpg"),
      },
      {
        id: 634649,
        title: "Spider-Man: No Way Home",
        backdrop_path: require("@/assets/3.jpg"),
      },
    ];

    onBeforeMount(() => {
      //Upcoming moveis
      UserApi.getUpcomingMovies().then((response) => {
        upComingMovieData.value = response.data.results;
      });

      // Popular movies
      UserApi.getPopularMovies().then((response) => {
        popularMovieData.value = response.data;
      });

      // High score moveis
      UserApi.getHighScoreMovies().then((response) => {
        hignScoreMovieData.value = response.data;
      });

      // Fetch the most comments recommendation movies
      UserApi.getMostCommentsMovies()
        .then((response) => {
          console.log("getMostComments  recommendation movies");
          console.log(response.data);
          mostRecommendationMovies.value = response.data.data;
        })
        .catch((error) => {
          console.log("error");
          console.log(error);
          console.log("error");
          showErroeMessage();
        });

      // fetch getRecommandationByTags
      if (currentUser.value !== null) {
        UserApi.getRecommandationByTags(currentUser.value.data.userId)
          .then((response) => {
            const randomMovie = response.data.data;
            if (randomMovie.length) {
              recentRecommendationMovies.value = ToolMethod.RandomNumBoth(
                randomMovie,
                randomMovie.length > 4 ? 5 : randomMovie.length
              );
            }
          })
          .catch((error) => {
            console.log("error");
            console.log(error);
            console.log("error");
            showErroeMessage();
          });
      } else {
        recentRecommendationMovies.value = [];
      }
    });

    const showErroeMessage = () => {
      return message.error("Server is busy, try again later");
    };

    //show Result Page
    const showResultPage = () => {
      localStorage.setItem("resultResource", 3);
      router.push({
        name: "ResultDisplay",
        params: {},
      });
    };
    const onChange = (link) => {
      console.log("Anchor:OnChange", link);
      isShowDrawer.value = false;
      // nextTick(() =>
      //   setTimeout(() => {
      //     let company = document.querySelector(link);
      //     document.documentElement.scrollTop = company.offsetTop; //苹果滚动
      //     document.body.scrollTop = company.offsetTop; //安卓滚动
      //   }, 300)
      // );
    };

    return {
      popularMovieData,
      hignScoreMovieData,
      mostRecommendationMovies,
      recentRecommendationMovies,
      upComingMovieData,
      fackePic,
      poster,
      isShowDrawer,
      moviePoster,
      showResultPage,
      onChange,
    };
  },
};
</script>

<style lang="scss" >
.affix-div {
  display: none;
  .anchor-div {
    height: 50px;
    width: 50px;
    background-image: url("../assets/arrow.gif");
    background-size: cover;
  }
}
.testmain {
  transition: all 0.4s;
  -moz-transition: all 0.4s;
  -webkit-transition: all 0.4s;
  -o-transition: all 0.4s;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 100% 100%;
}

.testmain:hover {
  background-size: 110% 110%;
  -webkit-box-shadow: 2px 12px 10px rgba(138, 138, 138, 0.603);
  -moz-box-shadow: 2px 12px 10px rgba(138, 138, 138, 0.603);
  box-shadow: 12px 12px 10px rgba(138, 138, 138, 0.603);
  cursor: pointer;
}

.pichover {
  width: 105px;
  height: 150px;
  transition: all 0.4s;
  -moz-transition: all 0.4s;
  -webkit-transition: all 0.4s;
  -o-transition: all 0.4s;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 100% 100%;
}

.pichover:hover {
  object-fit: cover;
  background-size: 110% 110%;
  -webkit-box-shadow: 2px 12px 10px rgba(138, 138, 138, 0.603);
  -moz-box-shadow: 2px 12px 10px rgba(138, 138, 138, 0.603);
  box-shadow: 12px 12px 10px rgba(138, 138, 138, 0.603);
  cursor: pointer;
}

.pichover2 {
  object-fit: fill;
  width: 74px;
  transition: all 0.4s;
  -moz-transition: all 0.4s;
  -webkit-transition: all 0.4s;
  -o-transition: all 0.4s;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 100% 100%;
}

.pichover2:hover {
  object-fit: cover;
  width: 76px;
  background-size: 110% 110%;
  -webkit-box-shadow: 2px 12px 10px rgba(138, 138, 138, 0.603);
  -moz-box-shadow: 2px 12px 10px rgba(138, 138, 138, 0.603);
  box-shadow: 12px 12px 10px rgba(138, 138, 138, 0.603);
  cursor: pointer;
}
.product {
  padding-bottom: 10px;
  padding-top: 10px;
}

.product-page {
  padding-top: 60px;
}

.btn__all {
  text-align: right;
  margin-bottom: 30px;
}

.trending__product {
  margin-bottom: 50px;
}

.popular__product {
  margin-bottom: 50px;
}

.recent__product {
  margin-bottom: 50px;
}

.product__item {
  margin-bottom: 30px;
}

.product__item__pic {
  height: 325px;
  position: relative;
  border-radius: 5px;
}

.product__item__pic .ep {
  font-size: 13px;
  color: #ffffff;
  background: #e53637;
  display: inline-block;
  padding: 2px 12px;
  border-radius: 4px;
  position: absolute;
  left: 10px;
  top: 10px;
}
.set-bg {
  background-size: cover;
}

.product__item__pic .comment {
  font-size: 13px;
  color: #ffffff;
  background: #3d3d3d;
  display: inline-block;
  padding: 2px 10px;
  border-radius: 4px;
  position: absolute;
  left: 10px;
  bottom: 10px;
}

.product__item__pic .view {
  font-size: 13px;
  color: #ffffff;
  background: #3d3d3d;
  display: inline-block;
  padding: 2px 10px;
  border-radius: 4px;
  position: absolute;
  right: 10px;
  bottom: 10px;
}

.product__item__text {
  padding-top: 20px;
}

.product__item__text ul {
  margin-bottom: 10px;
  padding-left: 0px !important;
}

.product__item__text ul li {
  list-style: none;
  font-size: 10px;
  color: #ffffff;
  font-weight: 700;
  padding: 1px 10px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 50px;
  display: inline-block;
}

.product__item__text h5 a {
  color: #ffffff;
  font-weight: 700;
  line-height: 26px;
}

.product__sidebar .section-title h5 {
  color: #ffffff;
  font-weight: 600;
  font-family: "Oswald", sans-serif;
  line-height: 21px;
  text-transform: uppercase;
  padding-left: 20px;
  position: relative;
}

.product__sidebar .section-title h5:after {
  position: absolute;
  left: 0;
  top: -6px;
  height: 32px;
  width: 4px;
  background: #e53637;
  content: "";
}

.product__sidebar__view {
  position: relative;
  margin-bottom: 80px;
}

.product__sidebar__view .filter__controls {
  position: absolute;
  right: 0;
  top: -5px;
}

.product__sidebar__view .filter__controls li {
  list-style: none;
  font-size: 13px;
  color: #b7b7b7;
  display: inline-block;
  margin-right: 7px;
  cursor: pointer;
}

.product__sidebar__view .filter__controls li.active {
  color: #ffffff;
}

.product__sidebar__view .filter__controls li:last-child {
  margin-right: 0;
}

.product__sidebar__view__item {
  height: 190px;
  position: relative;
  border-radius: 5px;
  margin-bottom: 20px;
}

.product__sidebar__view__item .ep {
  font-size: 13px;
  color: #ffffff;
  background: #e53637;
  display: inline-block;
  padding: 2px 12px;
  border-radius: 4px;
  position: absolute;
  left: 10px;
  top: 10px;
}

.product__sidebar__view__item .view {
  font-size: 13px;
  color: #ffffff;
  background: #3d3d3d;
  display: inline-block;
  padding: 2px 10px;
  border-radius: 4px;
  position: absolute;
  right: 10px;
  top: 10px;
}

.product__sidebar__view__item h5 {
  position: absolute;
  left: 0;
  bottom: 25px;
  width: 100%;
  padding: 0 30px 0 20px;
}

.product__sidebar__view__item h5 a {
  color: #ffffff;
  font-weight: 700;
  line-height: 26px;
}

.product__sidebar__comment {
  margin-bottom: 35px;
}

.product__sidebar__comment__item {
  margin-bottom: 20px;
  overflow: hidden;
  min-width: 300px;
}

.product__sidebar__comment__item__pic {
  float: left;
  margin-right: 15px;
}

.product__sidebar__comment__item__text {
  overflow: hidden;
}

.product__sidebar__comment__item__text ul {
  margin-bottom: 10px;
}

.product__sidebar__comment__item__text ul li {
  list-style: none;
  font-size: 10px;
  color: #ffffff;
  font-weight: 700;
  padding: 1px 10px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 50px;
  display: inline-block;
}

.product__sidebar__comment__item__text h5 {
  margin-bottom: 10px;
}

.product__sidebar__comment__item__text h5 a {
  color: #ffffff;
  font-weight: 700;
  line-height: 26px;
}

.product__sidebar__comment__item__text span {
  display: block;
  font-size: 13px;
  color: #b7b7b7;
}

.product__page__title {
  border-bottom: 2px solid rgba(255, 255, 255, 0.2);
  padding-bottom: 10px;
  margin-bottom: 30px;
}

.product__page__title .section-title {
  margin-bottom: 0;
}

.product__page__title .product__page__filter {
  text-align: right;
}

.product__page__title .product__page__filter p {
  color: #ffffff;
  display: inline-block;
  margin-bottom: 0;
  margin-right: 16px;
}

.product__page__title .product__page__filter .nice-select {
  float: none;
  display: inline-block;
  font-size: 15px;
  color: #3d3d3d;
  font-weight: 700;
  border-radius: 0;
  padding-left: 15px;
  padding-right: 40px;
  height: 32px;
  line-height: 32px;
}

.product__page__title .product__page__filter .nice-select:after {
  border-bottom: 2px solid #111;
  border-right: 2px solid #111;
  height: 8px;
  top: 47%;
  width: 8px;
  right: 15px;
}

.product__page__title .product__page__filter .nice-select .list {
  margin-top: 0;
  border-radius: 0;
}

.product__pagination {
  padding-top: 15px;
}

.product__pagination a {
  display: inline-block;
  font-size: 15px;
  color: #b7b7b7;
  font-weight: 600;
  height: 50px;
  width: 50px;
  border: 1px solid transparent;
  border-radius: 50%;
  line-height: 48px;
  text-align: center;
  -webkit-transition: all, 0.3s;
  -o-transition: all, 0.3s;
  transition: all, 0.3s;
}

.product__pagination a:hover {
  color: #ffffff;
}

.product__pagination a.current-page {
  border: 1px solid #ffffff;
}

.product__pagination a i {
  color: #b7b7b7;
  font-size: 15px;
}

.el-carousel__item h3 {
  color: #475669;
  font-size: 18px;
  opacity: 0.75;
  line-height: 300px;
  margin: 0;
  text-align: center;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
.feature-card {
  // position: relative;
  margin-top: 5px;
  margin-bottom: 35px;
  padding: 0 2px;
  width: 100%;
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
  .main-carousel {
    margin: auto;
    width: 100%;
  }
  .featured-img {
    display: block;
    width: 100%;
    height: 400px;
    object-fit: cover;
    position: relative;
    z-index: 0;
  }
  .detail {
    position: absolute;
    text-align: center;
    font-size: 40px;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.6);
    padding: 5px;
    z-index: 1;
    h3 {
      color: #fff;
      margin-bottom: 5px;
    }
    p {
      color: #fff;
    }
  }
}

.item-list {
  margin: 0 50px;
  min-width: 400px;
}
.item-title {
  color: white;
  span {
    font-size: 50px;
  }
  a {
    margin-top: 25px;
    margin-right: 30px;
    float: right;
    font-size: 25px;
  }
}
.movies-list {
  display: flex;
  flex-wrap: wrap;
  margin: 0px 50px;
  .movie {
    max-width: 20%;
    min-width: 180px;
    flex: 1 1 50%;
    padding: 16px 8px;
    .movie-link {
      display: flex;
      flex-direction: column;
      height: 100%;
      .product-image {
        position: relative;
        display: block;
        img {
          display: block;
          width: 100%;
          height: 300px;
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
        .year {
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
.home-carousel-div {
  position: relative;
  margin: 8px auto;
  display: flex;
  -webkit-box-pack: center;
  justify-content: center;
  // max-width: 1280px;
  .home-carousel-left {
    flex: 846 1 0%;
    margin: 0px 8px;
    position: relative;
    overflow: hidden;
    background: #fff;
  }
  .home-carousel-right {
    flex: 402 1 0%;
    margin: 0px 8px 0px 4px;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    -webkit-box-pack: justify;
    justify-content: space-between;
    .home-carousel-right-title {
      background-color: #111111;
      height: 35px;
      span {
        font-family: Roboto, Helvetica, Arial, sans-serif;
        font-size: 1.25rem;
        font-weight: 600;
        // color: rgb(245, 197, 24);

        color: #fff;
      }
    }
    .home-carousel-right-list {
      background-color: #111111;
      height: 110px;
      .home-carousel-right-list-right {
        width: calc(100% - 76px);
        height: 100%;
        float: right;

        padding: 5px;
        display: table-cell;
        vertical-align: top;
        border-radius: 0.1875rem;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.08);
        .home-carousel-right-list-right-title {
          text-overflow: ellipsis;
          overflow: hidden;
          white-space: nowrap;
          color: white;
          font-size: 18px;
          font-weight: 600;
          font-family: Roboto, Helvetica, Arial, sans-serif;
        }
        .home-carousel-right-list-right-content {
          margin-top: 20px;
          display: -webkit-box;
          -webkit-box-orient: vertical;
          -webkit-line-clamp: 2;
          overflow: hidden;
          color: white;
          font-family: Roboto, Helvetica, Arial, sans-serif;
        }
      }
    }
  }
  .carousel-div-small {
    display: none;
  }
}

@media only screen and (max-width: 798px) {
  .home-carousel-right {
    display: none !important;
  }
  .featured-img {
    height: 150px !important;
  }
  .carousel-div-defualt {
    display: none !important;
  }
  .carousel-div-small {
    display: block !important;
  }
}
@media only screen and (max-width: 480px) {
  .affix-div {
    position: relative;
    top: -50px;
    left: -44px;
    display: block !important;
  }
  .product__item {
    width: 50% !important;
  }
  .product__item__pic {
    height: 160px !important;
  }
  .product__item__text h5 a {
    line-height: 17px !important;
    font-size: 15px !important;
  }
}
</style>