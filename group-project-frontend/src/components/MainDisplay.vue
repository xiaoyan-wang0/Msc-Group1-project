<template>
  <div class="mainShow">
    <!-- the lastest movies -->
    <!-- <Showpart :itemdata="lastestMovieData" spacename="The lastest movies" /> -->

    <!-- Upcoming movies -->
    <Showpart :itemdata="popularMovieData" spacename="Popular Movies" isPopularorHighScore="1"/>

    <!-- High score movies -->
    <Showpart :itemdata="hignScoreMovieData" spacename="High Score Movie" isPopularorHighScore="2"/>

    <!-- IMDB TOP 10 movies  -->
    <div class="show-items">
      <div class="item-list">
        <div class="item-title">
          <span>IMDB TOP 10 movies</span>
          <a @click="showResultPage()">more</a>
        </div>
        <div class="movies-list">
          <div class="movie" v-for="item in imdbBotMovies" :key="item.Imdb_Id">
            <router-link :to="'/movie/' + item.Imdb_Id" class="movie-link">
              <div class="product-image">
                <img :src="item.posters[0].link" alt="Movie Poster" />
                <div class="type">{{ item.Imdb_Rating[0] }}</div>
              </div>
              <div class="detail">
                <p class="year">{{ item.year }}</p>
                <h3>{{ item.movie_title }}</h3>
              </div>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
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
        .get("/api/movieImdb/movieImdbBottomInfo?numberOfMovies=10")
        .then((response) => {
          // popularMovieData.value = JSON.stringify(response.data);
          imdbBotMovies.value = response.data.data;
          console.log("IMDB BOT 10 movies");
          console.log(imdbBotMovies.value);
          // console.log(hignScoreMovieData.value.results);
        });
    });

    //show Result Page
    const showResultPage = () => {
      router.push({
        name: "ResultDisplay",
        params: {
        //   resultName: "IMDB TOP 10 movies"
        },
      });
    };

    return {
      popularMovieData,
      hignScoreMovieData,
      imdbBotMovies,
      showResultPage,
    };
  },
};
</script>

<style lang="scss" scoped>
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
    max-width: 25%;
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
          background-color: #000152;
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
</style>