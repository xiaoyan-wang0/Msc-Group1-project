<template>
  <div class="trending__amdb_movies">
    <div class="row">
      <div class="col-lg-8 col-md-8 col-sm-8">
        <div class="section-title">
          <h4>{{ spacename }}</h4>
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
    <div class="row" v-if="itemdata.results !== undefined">
      <div
        class="col-lg-4 col-md-6 col-sm-6 movie-content"
        v-for="item in itemdata.results.slice(0, 6)"
        :key="item.id"
      >
        <router-link :to="'/movie/' + item.id">
          <div class="amdb_movies__item">
            <div
              class="amdb_movies__item__pic set-bg test"
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
            <div class="amdb_movies__item__text">
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
    isPopularorHighScore: String,
  },
  setup(props) {
    const poster = ref("");
    poster.value = env.tmdbpic;

    /**
     * Jump to result page.
     */
    const showResultPage = () => {
      localStorage.setItem("resultResource", props.isPopularorHighScore);
      router.push({
        name: "ResultDisplay",
        params: {},
      });
    };

    /**
     * Change genres to label.
     * @genres  genres id from imdb
     */
    const findCategary = (genres) => {
      let categary = [];
      for (let id of genres) {
        for (const genrn of JSON.parse(localStorage.getItem("genreList"))) {
          if (genrn.id == id) {
            categary.push(genrn.name);
          }
        }
      }
      return categary;
    };
    return { poster, showResultPage, findCategary };
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
      .amdb_movies-image {
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

.test {
  transition: all 0.4s;
  -moz-transition: all 0.4s;
  -webkit-transition: all 0.4s;
  -o-transition: all 0.4s;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 100% 100%;
}

.test:hover {
  background-size: 110% 110%;
  -webkit-box-shadow: 2px 12px 10px rgba(138, 138, 138, 0.603);
  -moz-box-shadow: 2px 12px 10px rgba(138, 138, 138, 0.603);
  box-shadow: 12px 12px 10px rgba(138, 138, 138, 0.603);
  cursor: pointer;
}
</style>