<template>
  <div class="show-items">
    <div class="item-list">
      <div class="item-title">
        <span>{{ spacename }}</span>
        <a @click="showResultPage()">more</a>
      </div>
      <div class="movies-list" v-if="itemdata.results !== undefined">
        <div
          class="movie"
          v-for="item in itemdata.results.slice(0, 10)"
          :key="item.id"
        >
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
import router from "@/router";

export default {
  name: "Showpart",
  props: {
    spacename: String,
    itemdata: JSON,
    isPopularorHighScore: String
  },
  setup(props) {
    const poster = ref("");
    poster.value = env.tmdbpic;
    //show Result Page
    const showResultPage = () => {
      console.log('isPopularorHighScore');
      console.log( props.isPopularorHighScore);
      router.push({
        name: "ResultDisplay",
        params: {
          isPopularorHighScore: props.isPopularorHighScore,
        },
      });
    };
    return { poster, showResultPage };
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