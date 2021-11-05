<template>
  <div class="show-items">
    <div class="item-list">
      <div class="item-title">
        <span>{{ resultName }}</span>
      </div>
      <div class="movies-list" v-if="itemdata !== undefined">
        <div class="movie" v-for="item in itemdata" :key="item.id">
          <router-link :to="'/movie/' + item.id" class="movie-link">
            <div class="product-image">
              <img :src="poster + item.poster_path" alt="Movie Poster" />
              <div class="type">{{ item.vote_average }}</div>
            </div>
            <div class="detail">
              <p class="year">{{ item.release_date }}</p>
              <h3>{{ item.title }}</h3>
            </div>
          </router-link>
        </div>
      </div>
    </div>
    <div class="result-pagiantion">
      <a-pagination
        class="result-pagiantion-content"
        size="large"
        v-model:current="current"
        :total="itemtotal"
        :pageSize="pageSize"
        @change="onChange"
      />
    </div>
  </div>
</template>

<script>
import env from "@/env.js";
import { ref, inject, onMounted } from "vue";
import router from "@/router";

export default {
  name: "ResultPage",
  props: {
    name: String,
    isPopularorHighScore: Number,
    searchValue: String,
  },
  setup(props) {
    const poster = ref("");
    const resultName = ref("Result");
    const itemdata = ref();
    const itemtotal = ref(0);
    const axios = inject("axios"); // inject axios
    poster.value = env.tmdbpic;

    onMounted(() => {
      console.log("RESULT props.isPopularorHighScore");
      console.log(props.isPopularorHighScore);
      if (props.isPopularorHighScore == 1) {
        // Popular movies
        resultName.value = "Popular movies Result";
        axios
          .get(env.tmdbmovieapi + env.tmdbpopular + env.tmdbkey + env.tmdbtail)
          .then((response) => {
            itemdata.value = response.data.results;
            console.log("REsult page Popula");
            console.log(itemdata.value);
            itemtotal.value = response.data.total_results;
          });
      } else if (props.isPopularorHighScore == 2) {
        resultName.value = "High score moveis Result";
        // High score moveis
        axios
          .get(
            env.tmdbmovieapi + env.tmdbhighscore + env.tmdbkey + env.tmdbtail
          )
          .then((response) => {
            // popularMovieData.value = JSON.stringify(response.data);
            itemdata.value = response.data.results;
            console.log("REsult page score moveis Result");
            console.log(itemdata.value);
            // console.log(hignScoreMovieData.value.results);
            itemtotal.value = response.data.total_results;
          });
      } else if (props.isPopularorHighScore == 3) {
        resultName.value = "Upcoming Movies Result";
        // High score moveis
        axios
          .get(env.tmdbmovieapi + env.tmdbupcoming + env.tmdbkey + env.tmdbtail)

          .then((response) => {
            // popularMovieData.value = JSON.stringify(response.data);
            itemdata.value = response.data.results;
            console.log("Result page score moveis");
            console.log(itemdata.value);
            console.log(itemdata.value);
            // console.log(hignScoreMovieData.value.results);
            itemtotal.value = response.data.total_results;
            console.log(itemtotal.value);
          });
      } else if (props.isPopularorHighScore == 4) {
        resultName.value = "Search result";
        // Search moveis result
        axios
          .get(
            env.tmdbSearch +
              env.tmdbkey +
              env.tmdbquery +
              props.searchValue +
              "&page= "
          )

          .then((response) => {
            itemdata.value = response.data.results;
            console.log("Search moveis result");
            console.log(itemdata.value);
            console.log(itemdata.value);
            itemtotal.value = response.data.total_results;
            console.log(itemtotal.value);
          });
      } else {
        resultName.value = "IMDB BOTTOM result";
        axios
          .get(
            env.AMDBAPI + "movieImdb/movieImdbBottomInfo?numberOfMovies=20",
            {
              withCredentials: true,
            }
          )
          .then((response) => {
            // popularMovieData.value = JSON.stringify(response.data);
            itemdata.value = response.data.data;
            console.log("IMDB BOT result");
            console.log(itemdata);
            // console.log(hignScoreMovieData.value.results);
          });
      }
    });

    const onChange = (pageNumber) => {
      console.log("Page: ", pageNumber);
      if (props.isPopularorHighScore == 1) {
        // Popular movies
        resultName.value = "Popular movies Result";
        axios
          .get(
            env.tmdbmovieapi +
              env.tmdbpopular +
              env.tmdbkey +
              env.tmdbtail +
              "&page= " +
              pageNumber
          )
          .then((response) => {
            itemdata.value = response.data.results;
            console.log("REsult page Popula");
            console.log(itemdata.value);
          });
      } else if (props.isPopularorHighScore == 2) {
        resultName.value = "High score moveis Result";
        // High score moveis
        axios
          .get(
            env.tmdbmovieapi +
              env.tmdbhighscore +
              env.tmdbkey +
              env.tmdbtail +
              "&page= " +
              pageNumber
          )
          .then((response) => {
            // popularMovieData.value = JSON.stringify(response.data);
            itemdata.value = response.data.results;
            console.log("REsult page score moveis Result");
            console.log(itemdata.value);
            // console.log(hignScoreMovieData.value.results);
          });
      } else if (props.isPopularorHighScore == 3) {
        resultName.value = "Upcoming Movies Result";
        // High score moveis
        axios
          .get(
            env.tmdbmovieapi +
              env.tmdbupcoming +
              env.tmdbkey +
              env.tmdbtail +
              "&page= " +
              pageNumber
          )

          .then((response) => {
            // popularMovieData.value = JSON.stringify(response.data);
            itemdata.value = response.data.results;
            console.log("Result page score moveis");
            console.log(itemdata.value);
            // console.log(hignScoreMovieData.value.results);
          });
      } else if (props.isPopularorHighScore == 4) {
        resultName.value = "Search result";
        // Search moveis result
        axios
          .get(
            env.tmdbSearch +
              env.tmdbkey +
              env.tmdbquery +
              props.searchValue +
              "&page= " +
              pageNumber
          )

          .then((response) => {
            itemdata.value = response.data.results;
            console.log("Search moveis result");
            console.log(itemdata.value);
            console.log(itemdata.value);
            itemtotal.value = response.data.total_results;
            console.log(itemtotal.value);
          });
      } else {
        resultName.value = "IMDB BOTTOM result";
        axios
          .get(
            env.AMDBAPI + "movieImdb/movieImdbBottomInfo?numberOfMovies=20",
            {
              withCredentials: true,
            }
          )
          .then((response) => {
            // popularMovieData.value = JSON.stringify(response.data);
            itemdata.value = response.data.data;
            console.log("IMDB BOT result");
            console.log(itemdata);
            // console.log(hignScoreMovieData.value.results);
          });
      }
    };
    return {
      poster,
      itemdata,
      resultName,
      itemtotal,
      current: ref(1),
      pageSize: ref(20),
      onChange,
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
          height: 250px;
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
.result-pagiantion {
  .result-pagiantion-content {
    justify-content: center;
    width: 520px;
    margin: auto;
    float: right;
  }
}
</style>