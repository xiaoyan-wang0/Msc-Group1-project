<template>
  <!-- Product Section Begin -->
  <section class="product spad">
    <div class="feature-card">
      <div id="1" style="">
        <div class="home-carousel-div" style="">
          <div class="home-carousel-left" id="2" style="">
            <div class="main-carousel" v-if="upComingMovieData">
              <el-carousel
                class="carousel-div"
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
                <!-- <el-carousel-item
                    v-for="item in upComingMovieData.slice(0, 3)"
                    :key="item.id"
                  > 
                  <el-carousel-item v-for="item in fackePic" :key="item.id">
                    <router-link :to="'/movie/' + item.id">
                      <img
                        :src="moviePoster + item.backdrop_path"
                        :alt="item.title"
                        class="featured-img"
                      />
                      <div class="detail">
                        <p>{{ item.title }}</p>
                      </div>
                    </router-link>
                  </el-carousel-item> -->
              </el-carousel>
            </div>
          </div>
          <div class="home-carousel-right" id="3" style="">
            <div class="home-carousel-right-title" style="">
              <div class="section-title">
                <h4>
                  <span style="margin-left: 5px">Upcoming</span>
                  <a
                    @click="showResultPage2()"
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
                    style="object-fit: fill; width: 74px"
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
          <!-- the lastest movies -->
          <!-- <Showpart :itemdata="lastestMovieData" spacename="The lastest movies" /> -->

          <!-- Upcoming movies -->
          <Showpart
            :itemdata="popularMovieData"
            spacename="Popular Movies"
            isPopularorHighScore="1"
          />

          <!-- High score movies -->
          <Showpart
            :itemdata="hignScoreMovieData"
            spacename="High Score Movie"
            isPopularorHighScore="2"
          />

          <!-- IMDB bot 10 movies  -->
          <!-- <div class="show-items">
      <div class="item-list">
        <div class="item-title">
          <span>IMDB Bottom Movies</span>
          <a @click="showResultPage()">more</a>
        </div>
        <div class="movies-list">
          <div class="movie" v-for="item in imdbBotMovies" :key="item.Imdb_Id">
            <router-link :to="'/movie/' + item.Imdb_Id" class="movie-link">
              <div class="product-image">
                <img :src="poster+ item.posters[0]" alt="Movie Poster" />
                <div class="type">{{ Number(item.rating).toFixed(1) }}</div>
              </div>
              <div class="detail">
                <p class="year">{{ item.year }}</p>
                <h3>{{ item.movie_title }}</h3>
              </div>
            </router-link>
          </div>
        </div>
      </div>
    </div> -->
          <div class="trending__product">
            <div class="row">
              <div class="col-lg-8 col-md-8 col-sm-8">
                <div class="section-title">
                  <h4>IMDB Bottom Movies</h4>
                </div>
              </div>
              <div class="col-lg-4 col-md-4 col-sm-4">
                <div class="btn__all">
                  <a @click="showResultPage()" class="primary-btn"
                    >View All <span class="arrow_right"></span
                  ></a>
                </div>
              </div>
            </div>
            <div class="row" v-if="imdbBotMovies !== undefined">
              <div
                class="col-lg-4 col-md-6 col-sm-6"
                v-for="item in imdbBotMovies"
                :key="item.id"
              >
                <router-link :to="'/movie/' + item.tmdb_Id">
                  <div class="product__item">
                    <div
                      class="product__item__pic set-bg test"
                      v-bind:style="{
                        'background-image': 'url(' + item.posters[0] + ')',
                      }"
                    >
                      <div class="ep">
                        {{ Number(item.rating).toFixed(1) }} / 10
                      </div>
                      <!-- <div class="comment"><i class="fa fa-comments"></i> 11</div> -->
                      <div class="view">
                        <i class="fa fa-eye"></i> {{ item.year }}
                      </div>
                    </div>
                    <div class="product__item__text">
                      <ul>
                        <li
                          v-for="genre in item.genres.slice(0, 2)"
                          :key="genre.id"
                        >
                          {{ genre }}
                        </li>
                      </ul>
                      <h5>
                        <a href="#">{{ item.movie_title }}</a>
                      </h5>
                    </div>
                  </div>
                </router-link>
              </div>
            </div>
          </div>
        </div>
        <div class="col-lg-4 col-md-6 col-sm-8">
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
                    <img
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
                    <span
                      ><i class="fa fa-eye"></i> {{ item.release_date }}</span
                    >
                  </div>
                </router-link>
              </div>
            </div>
            <div
              class="product__sidebar__view"
              v-if="recentRecommendationMovies !== []"
            >
              <div class="section-title">
                <h5>Recent Views recommendations</h5>
              </div>
              <!-- <div class="filter__gallery">
                <div
                  class="product__sidebar__view__item set-bg mix day years"
                  :style="{
                    backgroundImage: 'url(' + '../assets/trend-1.jpg' + ')',
                  }"
                >
                  <div class="ep">18 / ?</div>
                  <div class="view"><i class="fa fa-eye"></i> 9141</div>
                  <h5><a href="#">Boruto: Naruto next generations</a></h5>
                </div>
              </div> -->
              <div
                class="product__sidebar__comment__item"
                v-for="item in recentRecommendationMovies"
                :key="item.id"
              >
                <router-link :to="'/movie/' + item.id">
                  <div class="product__sidebar__comment__item__pic">
                    <img
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
import { ref, inject, onBeforeMount, computed } from "vue";
import { message } from "ant-design-vue";
import env from "@/env.js";
import Showpart from "./ShowPart.vue";
import router from "@/router";
import { useStore } from "vuex";

export default {
  name: "MainDisplay",
  props: {},
  components: { Showpart },
  setup() {
    const axios = inject("axios"); // inject axios
    const popularMovieData = ref([]);
    const hignScoreMovieData = ref([]);
    const imdbBotMovies = ref([]);
    const genreList = ref([]);
    const upComingMovieData = ref([]);
    const fackePic = ref([]);
    const store = useStore();
    const mostRecommendationMovies = ref([]);
    const recentRecommendationMovies = ref([]);
    const moviePoster = ref("");
    moviePoster.value = env.tmdbpic;
    const currentUser = computed(() => store.state.auth.user);
    const poster = ref("");
    poster.value = env.tmdbpic;
    onBeforeMount(() => {
      //Upcoming moveis
      axios
        .get(env.tmdbmovieapi + env.tmdbupcoming + env.tmdbkey + env.tmdbtail)
        .then((response) => {
          upComingMovieData.value = response.data.results;
          console.log(upComingMovieData.value.results);
        });

      fackePic.value = [
        {
          id: 566525,
          title: "Shang-Chi and the Legend of the Ten Rings",
          backdrop_path: require("@/assets/2.jpg"),
        },
        {
          id: 370172,
          title: "No Time to Die",
          backdrop_path: require("@/assets/3.jpg"),
        },
        {
          id: 580489,
          title: "Venom: Let There Be Carnage",
          backdrop_path: require("@/assets/1.jpg"),
        },
      ];

      // Popular movies
      axios
        .get(env.tmdbmovieapi + env.tmdbpopular + env.tmdbkey + env.tmdbtail)
        .then((response) => {
          popularMovieData.value = response.data;
          console.log("popularMovieData.results");
          console.log(popularMovieData.value.results);
        });
      // High score moveis
      axios
        .get(env.tmdbmovieapi + env.tmdbhighscore + env.tmdbkey + env.tmdbtail)
        .then((response) => {
          // popularMovieData.value = JSON.stringify(response.data);
          hignScoreMovieData.value = response.data;
          // console.log(hignScoreMovieData.value.results);
        });

      // IMDB BOT 10 movies
      axios
        .get(
          env.AMDBAPI + "movieImdb/movieImdbBottomInfo?numberOfMovies=6"
          // { withCredentials: true,}
        )
        .then((response) => {
          // popularMovieData.value = JSON.stringify(response.data);
          imdbBotMovies.value = response.data.data;
          console.log("IMDB BOT 10 Movies");
          console.log(imdbBotMovies.value);
          // console.log(hignScoreMovieData.value.results);
        })
        .catch((error) => {
          console.log("error");
          console.log(error);
          console.log("error");
          showErroeMessage();
        });

      // Fetch the most comments recommendation movies
      axios
        .get(env.AMDBAPI + "rec/getMostComments")
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

      // Fetch recently recommendation movies
      if (currentUser.value !== null) {
        axios
          .get(
            env.AMDBAPI +
              "rec/getRecommandation?userId=" +
              currentUser.value.data.userId
          )
          .then((response) => {
            console.log(
              "recently recommendation movies recentRecommendationMovies"
            );
            console.log(response.data);
            recentRecommendationMovies.value = response.data.data;
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
      return message.error("Sorry, error accured in server");
    };

    const findCategary = (genres) => {
      let categary = [];
      for (let id of genres) {
        for (const genrn of JSON.parse(localStorage.getItem("genreList"))) {
          console.log("findCategary([878,28]");
          console.log(genrn);
          console.log(id);
          if (genrn.id == id) {
            categary.push(genrn.name);
          }
        }
      }
      console.log(categary);
      return categary;
    };
    //show Result Page
    const showResultPage = () => {
      localStorage.setItem("resultResource", 5);
      router.push({
        name: "ResultDisplay",
        params: {
          //   resultName: "IMDB TOP 10 movies"
          isPopularorHighScore: 5,
        },
      });
    };
    //show Result Page
    const showResultPage2 = () => {
      localStorage.setItem("resultResource", 3);
      router.push({
        name: "ResultDisplay",
        params: {
          //   resultName: "IMDB TOP 10 movies"
          // isPopularorHighScore: 3,
        },
      });
    };

    return {
      popularMovieData,
      hignScoreMovieData,
      imdbBotMovies,
      mostRecommendationMovies,
      recentRecommendationMovies,
      upComingMovieData,
      fackePic,
      poster,
      moviePoster,
      showResultPage,
      showResultPage2,
      findCategary,
    };
  },
};
</script>

<style lang="scss" >


.test{
    transition: all 0.4s;
    -moz-transition:all .4s;
    -webkit-transition:all .4s;
    -o-transition:all .4s;
    background-repeat:no-repeat;   
    background-position: center;   
    background-size: 100% 100%;
    
  }
  .test:hover{
    background-size: 110% 110%;
    -webkit-box-shadow: 2px 12px 10px rgba(138, 138, 138, 0.603);
    -moz-box-shadow: 2px 12px 10px  rgba(138, 138, 138, 0.603);
    box-shadow: 12px 12px 10px rgba(138, 138, 138, 0.603);
    cursor: pointer;
  }


.item-list {
  margin: 0 50px;
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
        background-color: #363636;
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
  background-image: url("../assets/trend-1.jpg");
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
    height: 500px;
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
        width: calc(100% - 74px);
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
}

@media only screen and (max-width: 798px) {
  .home-carousel-right {
    display: none !important;
  }
}
</style>