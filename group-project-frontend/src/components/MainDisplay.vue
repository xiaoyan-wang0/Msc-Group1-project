<template>
  <!-- Product Section Begin -->
  <section class="product spad">
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
                <router-link :to="'/movie/' + item.Imdb_Id">
                  <div class="product__item">
                    <div
                      class="product__item__pic set-bg"
                      v-bind:style="{
                        'background-image':
                          'url(' + poster + item.posters[0] + ')',
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
                        <!-- <li v-for="genre in findCategary(item.genre_ids)" :key="genre.id" >
                    {genre}
                  </li>> -->
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
            <div class="product__sidebar__view">
              <div class="section-title">
                <h5>Top Views</h5>
              </div>
              <ul class="filter__controls">
                <li class="active" data-filter="*">Day</li>
                <li data-filter=".week">Week</li>
                <li data-filter=".month">Month</li>
                <li data-filter=".years">Years</li>
              </ul>
              <div class="filter__gallery">
                <div
                  class="product__sidebar__view__item set-bg mix day years"
                  style="background-image: url(../assets/trend-1.jpg)"
                >
                  <div class="ep">18 / ?</div>
                  <div class="view"><i class="fa fa-eye"></i> 9141</div>
                  <h5><a href="#">Boruto: Naruto next generations</a></h5>
                </div>
              </div>
            </div>
            <div class="product__sidebar__comment">
              <div class="section-title">
                <h5>New Comment</h5>
              </div>
              <div class="product__sidebar__comment__item">
                <div class="product__sidebar__comment__item__pic">
                  <img
                    src="../assets/trend-3.jpg"
                    style="width: 90px; height: 130px"
                    alt=""
                  />
                </div>
                <div class="product__sidebar__comment__item__text">
                  <ul>
                    <li>Active</li>
                    <li>Movie</li>
                  </ul>
                  <h5>
                    <a href="#">The Seven Deadly Sins: Wrath of the Gods</a>
                  </h5>
                  <span><i class="fa fa-eye"></i> 19.141 Viewes</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { ref, inject, onBeforeMount } from "vue";
import env from "@/env.js";
import Showpart from "./ShowPart.vue";
import router from "@/router";

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
    const poster = ref("");
    poster.value = env.tmdbpic;
    onBeforeMount(() => {
      // Popular movies
      axios
        .get(env.tmdbmovieapi + env.tmdbpopular + env.tmdbkey + env.tmdbtail)
        .then((response) => {
          popularMovieData.value = response.data;
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
        .get(env.AMDBAPI + "movieImdb/movieImdbBottomInfo?numberOfMovies=6", {
          withCredentials: true,
        })
        .then((response) => {
          // popularMovieData.value = JSON.stringify(response.data);
          imdbBotMovies.value = response.data.data;
          console.log("IMDB BOT 10 Movies");
          console.log(imdbBotMovies.value);
          // console.log(hignScoreMovieData.value.results);
        });
    });

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
      router.push({
        name: "ResultDisplay",
        params: {
          //   resultName: "IMDB TOP 10 movies"
          isPopularorHighScore: 5,
        },
      });
    };

    return {
      popularMovieData,
      hignScoreMovieData,
      imdbBotMovies,
      poster,
      showResultPage,
      findCategary,
    };
  },
};
</script>

<style lang="scss" >
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
  padding-bottom: 60px;
  padding-top: 50px;
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
  margin-left: 0px;
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
</style>