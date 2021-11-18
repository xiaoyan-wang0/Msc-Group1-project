<template>
  <div class="home">
    <div class="feature-card">
             
      <div class="search">
        <form class="search-model-form" @submit.prevent="SearchMovies()">
           <input
            type="text"
            id="search-input"
            v-model="search"
            placeholder="Search here....."
          /><a @click="SearchMovies()"
            ><span class="fa fa-2x fa-search" style="color: #e53637"></span
          ></a>
        </form>
      </div>
      <div>
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
                      style="object-fit: fill; width: 74px"
                      :src="moviePoster + item.poster_path"
                      :alt="item.title"
                    />
                  </div>
                  <div class="home-carousel-right-list-right" style="">
                    <div class="home-carousel-right-list-right-title" style="">
                      {{ item.title }}
                    </div>
                    <div
                      class="home-carousel-right-list-right-content"
                      style=""
                    >
                      {{ item.overview }}
                    </div>
                  </div>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- SEACH BAR -->
    <div class="search-bar">
      <!-- <form @submit.prevent="SearchMovies()" class="search-box">
        <input
          type="text"
          placeholder="What are you looking for?"
          v-model="search"
        />
        <input type="submit" value="Search" />
      </form> -->
      <div class="search-content" v-if="showRouterView"></div>
    </div>
    <router-view v-if="showRouterView" />
  </div>
</template>

<script>
import { ElCarousel } from "element-plus";
import { ref, inject, onBeforeMount, nextTick } from "vue";
import env from "@/env.js";
import router from "@/router";
import Showpart from "@/components/ShowPart.vue";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap/dist/js/bootstrap.bundle.js";
export default {
  name: "Home",
  components: { ElCarousel, Showpart },
  setup() {
    const axios = inject("axios"); // inject axios
    const search = ref("");
    const activeIndex = ref("1");
    const itemdata = ref([]);
    const lastestMovieData = ref([]);
    const upComingMovieData = ref([]);
    const moviePoster = ref("");
    const showRouterView = ref(true);
    const fackePic = ref([]);
    moviePoster.value = env.tmdbpic;

    //Search event
    const SearchMovies = () => {
      console.log("SearchMovies");
      console.log(search.value);
      if (search.value != "") {
        showRouterView.value = false;
        nextTick(() => (showRouterView.value = true));
        localStorage.setItem("resultResource", 4);
        localStorage.setItem("searchValue", search.value);
        router.push({
          name: "ResultDisplay",
          params: {
            //   resultName: "IMDB TOP 10 movies"
            // isPopularorHighScore: 4,
            // searchValue: search.value,
          },
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
          upComingMovieData.value = response.data.results;
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
      fackePic.value = [
        {
          id: 580489,
          title: "Venom: Let There Be Carnage",
          backdrop_path: require("@/assets/1.jpg"),
        },
        { id: 438631, title: "Dune", backdrop_path: require("@/assets/2.jpg") },
        {
          id: 574060,
          title: "Gunpowder Milkshake",
          backdrop_path: require("@/assets/3.jpg"),
        },
      ];
    });

    //show Result Page
    const showResultPage = () => {
      showRouterView.value = false;
      nextTick(() => (showRouterView.value = true));
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
      search,
      moviePoster,
      activeIndex,
      itemdata,
      lastestMovieData,
      upComingMovieData,
      fackePic,
      showRouterView,
      handleSelect,
      SearchMovies,
      showResultPage,
    };
  },
};
</script>

<style lang="scss">
.home {
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
    padding: 0 10px;
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
    .search {
      text-align: center;
      margin-bottom: 15px;
    }
    .search-model-form {
      // padding: 0 15px;
    }

    .search-model-form input {
      width: 95%;
      font-size: 40px;
      border: none;
      border-bottom: 2px solid #333;
      background: 0 0;
      color: #999;
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
      border: rgb(241, 238, 238) solid 2px;
      &[type="text"] {
        width: 90%;
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
        font-weight: 600;
        // color: #f5c518;

        color: #42b883;
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
}
</style>