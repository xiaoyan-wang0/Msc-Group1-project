<template>
  <div class="show-items">
    <div class="item-list">
      <div class="item-title">
        <span>{{spacename}}</span>
        <a>more</a>
      </div>
      <div class="movies-list" v-if=" itemdata.results!== undefined">
        <div class="movie" v-for="item in itemdata.results.slice(0,10)" :key="item.id">
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
  </div>
</template>

<script>
import env from "@/env.js";
import { ref } from "vue";

export default {
  name: "Showpart",
  props: {
    spacename: String,
    itemdata: JSON
  },
  setup() {
    const poster = ref("");
    poster.value = env.tmdbpic;
    return { poster };
  }
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
  // background: #eee
  //   url(data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAAECAIAAAAmkwkpAAAAHklEQVQImWNkYGBgYGD4//8/A5wF5SBYyAr+//8PAPOCFO0Q2zq7AAAAAElFTkSuQmCC)
  //   repeat;
  // text-shadow: 5px -5px black, 4px -4px white;
  // font-weight: bold;
  // background-clip: text;
  // -webkit-text-fill-color: transparent;
  // -webkit-background-clip: text;

  // text-shadow: 6px 6px 0px rgb(248, 246, 246);

  
  // text-shadow: 0 1px 0 #ccc, 0 2px 0 #c9c9c9, 0 3px 0 #bbb, 0 4px 0 #b9b9b9,
  //   0 5px 0 #aaa, 0 6px 1px rgba(216, 213, 213, 0.911), 0 0 5px rgba(241, 238, 238, 0.979),
  //   0 1px 3px rgb(255, 255, 255), 0 3px 5px rgb(248, 246, 246),
  //   0 5px 10px rgb(238, 236, 236), 0 10px 10px rgb(236, 236, 236),
  //   0 20px 20px rgba(214, 208, 208, 0.904);
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