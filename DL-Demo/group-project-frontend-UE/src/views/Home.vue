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
    const showRouterView = ref(true);
    const fackePic = ref([]);

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

    onBeforeMount(() => {});

  

    return {
      search,
      activeIndex,
      itemdata,
      lastestMovieData,
      showRouterView,
      handleSelect,
      SearchMovies,
    };
  },
};
</script>

<style lang="scss">



.home {
  // .main-menu li ul {
  // font-size: 500px;
  // }
  .feature-card {
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
  }
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
}
</style>