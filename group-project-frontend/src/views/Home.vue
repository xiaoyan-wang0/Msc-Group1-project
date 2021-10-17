<template>
  <div class="home">
    <div class="feature-card">
      <!-- carousel -->
      <div class="main-carousel" v-if="upComingMovieData.results">
        <el-carousel :interval="3000" type="card" height="350px">
          <el-carousel-item
            v-for="item in upComingMovieData.results.slice(0, 6)"
            :key="item.id"
          >
            <router-link :to="'/movie/' + item.id">
              <img
                :src="moviePoster + item.poster_path"
                :alt="item.title"
                class="featured-img"
              />
              <div class="detail">
                <p>{{ item.overview }}</p>
              </div>
            </router-link>
          </el-carousel-item>
        </el-carousel>
      </div>
    </div>

    <!-- SEACH BAR -->
    <div class="search-bar">
      <form @submit.prevent="SearchMovies()" class="search-box">
        <input
          type="text"
          placeholder="What are you looking for?"
          v-model="search"
        />
        <input type="submit" value="Search" />
      </form>
    </div>
    <!-- the lastest movies -->
    <!-- <Showpart :itemdata="lastestMovieData" spacename="The lastest movies" /> -->

    <!-- Upcoming movies -->
    <Showpart :itemdata="popularMovieData" spacename="Popular Movies" />

    <!-- High score movies -->
    <Showpart :itemdata="hignScoreMovieData" spacename="High Score Movie" />

    <!--  movies searched -->
    <div class="movies-list">
      <div class="movie" v-for="movie in movies" :key="movie.imdbID">
        <router-link :to="'/movie/' + movie.imdbID" class="movie-link">
          <div class="product-image">
            <img :src="movie.Poster" alt="Movie Poster" />
            <div class="type">{{ movie.Type }}</div>
          </div>
          <div class="detail">
            <p class="year">{{ movie.Year }}</p>
            <h3>{{ movie.Title }}</h3>
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { ElCarousel } from "element-plus";
import { ref, inject, onBeforeMount } from "vue";
import env from "@/env.js";
import Showpart from "@/components/ShowPart.vue";
export default {
  name: "Home",
  components: { ElCarousel, Showpart },
  setup() {
    const axios = inject("axios"); // inject axios
    const search = ref("");
    const movies = ref([]);
    const activeIndex = ref("1");
    const itemdata = ref([]);
    const popularMovieData = ref([]);
    const lastestMovieData = ref([]);
    const hignScoreMovieData = ref([]);
    const upComingMovieData = ref([]);
    const moviePoster = ref("");
    moviePoster.value = env.tmdbpic;

    //Search event
    const SearchMovies = () => {
      if (search.value != "") {
        console.log(
          env.omdbapi + env.omdbkey + env.omdbapisearch + search.value
        );
        axios
          .get(
            env.omdbapi +
              env.omdbkey +
              env.omdbapisearch +
              search.value +
              "&plot=full"
          )
          .then((response) => {
            movies.value = response.data.Search;
            search.value = "";
            itemdata.value = response.data.Search;
            console.log(itemdata);
          });
      }
    };

    //Select menu event
    const handleSelect = (key, keyPath) => {
      console.log(key, keyPath);
    };

    onBeforeMount(() => {
      //Upcoming moveis
      axios
        .get(env.tmdbmovieapi + env.tmdbupcoming + env.tmdbkey + env.tmdbtail)
        .then((response) => {
          upComingMovieData.value = response.data;
          console.log(upComingMovieData.value.results);
        });
      //THe lastest moveis
      // axios
      //   .get(env.tmdbmovieapi + env.tmdblatest + env.tmdbkey + env.tmdbtail)
      //   .then(response => {
      //     lastestMovieData.value = response.data;
      //     console.log(response.data);
      //     console.log(lastestMovieData.value);
      // });
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
    });

    return {
      search,
      movies,
      moviePoster,
      activeIndex,
      SearchMovies,
      handleSelect,
      itemdata,
      popularMovieData,
      lastestMovieData,
      hignScoreMovieData,
      upComingMovieData,
    };
  },
};
</script>

<style lang="scss">

.home {
  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
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
    position: relative;
    padding: 0 30px;
    .featured-img {
      display: block;
      width: 100%;
      height: 500px;
      // object-fit: cover;
      position: relative;
      z-index: 0;
    }
    .detail {
      position: absolute;
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

  // .main-menu li ul {
  // font-size: 500px;
  // }
  .search-box {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 16px;
    input {
      display: block;
      appearance: none;
      border: none;
      outline: none;
      background: none;

      border: rgb(241, 238, 238) solid 0.5px;
      &[type="text"] {
        width: 100%;
        color: #fff;
        background-color: #161616 0.5;
        font-size: 20px;
        padding: 10px 16px;
        border-radius: 8px;
        margin-bottom: 15px;
        transition: 0.4s;
        &::placeholder {
          color: #f3f3f3;
        }
        &:focus {
          box-shadow: 3px 3px 16px rgba(250, 249, 249, 0.5);
        }
      }
      &[type="submit"] {
        width: 100%;
        max-width: 300px;
        background-color: #3d3d3d;
        padding: 16px;
        border-radius: 8px;
        color: #fff;
        font-size: 20px;
        text-transform: uppercase;
        transition: 0.4s;
        &:active {
          background-color: #f3f3f3;
        }
      }
    }
  }
  .item-list {
    margin: 0 50px;
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
}
</style>