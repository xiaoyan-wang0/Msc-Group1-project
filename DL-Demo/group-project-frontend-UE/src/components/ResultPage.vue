<template>
  <div class="show-items">
    <div class="trending__product" v-if="!isIMDBBot">
      <div class="row">
        <div class="col-lg-8 col-md-8 col-sm-8">
          <div class="section-title">
            <h4>{{ resultName }}</h4>
          </div>
        </div>
      </div>
      <div class="row" v-if="itemdata !== undefined">
        <div
          class="col-lg-3 col-md-6 col-sm-6"
          v-for="item in itemdata"
          :key="item.id"
        >
          <router-link :to="'/movie/' + item.id">
            <div class="product__item">
              <div
                class="product__item__pic set-bg test"
                v-bind:style="{
                  'background-image': 'url(' + poster + item.poster_path + ')',
                }"
              >
                <div class="ep">{{ item.vote_average }} / 10</div>
                <div class="comment">
                  <i class="fa fa-comments"></i> {{ item.vote_count }}
                </div>
                <div class="view">
                  <i class="fa fa-eye"></i> {{ item.release_date }}
                </div>
              </div>
              <div class="product__item__text">
                <ul>
                  <li
                    v-for="genre in findCategary(item.genre_ids).slice(0, 2)"
                    :key="genre.id"
                  >
                    {{ genre }}
                  </li>
                </ul>
                <h5>
                  <a href="#">{{ item.title }}</a>
                </h5>
              </div>
            </div>
          </router-link>
        </div>
      </div>
    </div>
    <!-- For imdb bot  -->
    <div class="trending__product" v-else>
      <div class="row">
        <div class="col-lg-8 col-md-8 col-sm-8">
          <div class="section-title">
            <h4>{{ resultName }}</h4>
          </div>
        </div>
      </div>
      <div class="row" v-if="itemdata !== undefined">
        <div
          class="col-lg-3 col-md-6 col-sm-6"
          v-for="item in itemdata"
          :key="item.tmdb_Id"
        >
          <router-link :to="'/movie/' + item.tmdb_Id">
            <div class="product__item">
              <div
                class="product__item__pic set-bg test"
                v-bind:style="{
                  'background-image': 'url(' + item.posters[0] + ')',
                }"
              >
                <div class="ep">{{ Number(item.rating).toFixed(1) }} / 10</div>
                <div class="comment">
                  <!-- <i class="fa fa-comments"></i> {{ item.vote_count }} -->
                </div>
                <div class="view">
                  <i class="fa fa-eye"></i> {{ item.year }}
                </div>
              </div>
              <div class="product__item__text">
                <ul>
                  <li v-for="genre in item.genres.slice(0, 2)" :key="genre.id">
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
import { ref, inject, onMounted, onBeforeMount } from "vue";
import { message } from "ant-design-vue";
import router from "@/router";

export default {
  name: "ResultPage",
  props: {
    name: String,
    isPopularorHighScore: Number,
  },
  setup(props) {
    const poster = ref("");
    const resultName = ref("Result");
    const itemdata = ref();
    const itemtotal = ref(0);
    const isIMDBBot = ref(false);
    const axios = inject("axios"); // inject axios
    poster.value = env.tmdbpic;
    const resource = localStorage.getItem("resultResource");
    const searchValue = localStorage.getItem("searchValue");

    onBeforeMount(() => {
      console.log("onBeforeMount");
      itemdata.value = [];
      resultName.value = "";
      console.log(itemdata.value);
      console.log(resultName.value);
    });

    onMounted(() => {
      console.log("onMounted");
      console.log("RESULT props.isPopularorHighScore");
      // console.log(props.isPopularorHighScore);
      console.log(localStorage.getItem("resultResource"));
      if (resource == 1) {
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
      } else if (resource == 2) {
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
      } else if (resource == 3) {
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
      } else if (resource == 4) {
        resultName.value = "Search result";
        // Search moveis result
        axios
          .get(env.tmdbSearch + env.tmdbkey + env.tmdbquery + searchValue)
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
        isIMDBBot.value = true;
        axios
          .get(
            env.AMDBAPI + "movieImdb/movieImdbBottomInfo?numberOfMovies=20",
            // {
            //   withCredentials: true,
            // }
          )
          .then((response) => {
            // popularMovieData.value = JSON.stringify(response.data);
            itemdata.value = response.data.data;
            console.log("IMDB BOT result");
            console.log(itemdata);
            // console.log(hignScoreMovieData.value.results);
          })
          .catch((error) => {
            console.log("error");
            console.log(error);
            console.log("error");
            showErroeMessage();
          });
      }
    });

    const onChange = (pageNumber) => {
      console.log("Page: ", pageNumber);
      if (resource == 1) {
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
      } else if (resource == 2) {
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
      } else if (resource == 3) {
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
      } else if (resource == 4) {
        resultName.value = "Search result";
        // Search moveis result
        axios
          .get(
            env.tmdbSearch +
              env.tmdbkey +
              env.tmdbquery +
              searchValue +
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
            // {
            //   withCredentials: true,
            // }
          )
          .then((response) => {
            // popularMovieData.value = JSON.stringify(response.data);
            itemdata.value = response.data.data;
            console.log("IMDB BOT result");
            console.log(itemdata);
            // console.log(hignScoreMovieData.value.results);
          })
          .catch((error) => {
            console.log("error");
            console.log(error);
            console.log("error");
            showErroeMessage();
          });
      }
    };

    const showErroeMessage = () => {
      return message.error("Sorry, error accured in server");
    };

    const findCategary = (genres) => {
      let categary = [];
      for (let id of genres) {
        for (const genrn of JSON.parse(localStorage.getItem("genreList"))) {
          // console.log("findCategary([878,28]");
          // console.log(genrn);
          // console.log(id);
          if (genrn.id == id) {
            categary.push(genrn.name);
          }
        }
      }
      // console.log(categary);
      return categary;
    };
    return {
      poster,
      itemdata,
      resultName,
      itemtotal,
      isIMDBBot,
      current: ref(1),
      pageSize: ref(20),
      onChange,
      findCategary,
    };
  },
};
</script>

<style lang="scss" scoped>


.test{
    transition: all 0.4s;
    -moz-transition:all .4s;
    -webkit-transition:all .4s;
    -o-transition:all .4s;
    background-repeat:no-repeat;   /* 不会重复 */
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

.show-items {
  padding-top: 50px;
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
    // width: 120px;
    margin: auto;
    float: right;
  }
}
</style>