<template>
  <div class="about-us-div">
    <section class="amdb_aboutus-details spad">
      <div class="container">
        <div class="row d-flex justify-content-center">
          <div class="col-lg-8">
            <div class="amdb_aboutus__details__title">
              <h6>Last update date <span>- Nov 25th, 2021</span></h6>
              <h2>AMDB for Beginners:</h2>
              <h6>CUSTOMISED MULTI-SOURCED MOVIE GUIDE</h6>
            </div>
          </div>
          <div class="col-lg-8">
            <div class="amdb_aboutus__details__content">
              <div class="amdb_aboutus__details__text">
                <p>
                  AMDb (Authentic Movie Database) is a customised multi-sourced
                  movie evaluation system. By using AMDb, people can simply
                  visit our website to have the an understanding about a movie
                  rather than visiting different soucres out there like Imdb,
                  Tmdb, YouTube and Twitter.

                  <br />
                  AMDb is gathering movie reviews and people's opinions about a
                  movie from different sources like IMDb, TMDb, Twitter and
                  YouTube. But AMDb doesn't stop there, a toxicity detector and
                  sentimental detector have been created on AMDb. Thanks to
                  these technologies, users can sort reviews according to how
                  much toxicity they include, and they can customize in a way
                  that they don't see any toxic comments in their understanding.
                  <br />
                  Thanks to the sentimental detector, AMDb gather information
                  about a movie from Twitter and YouTube first, then use the
                  sentimental analyses to detect if comments about a film are
                  positive, negative, or neutral. But that's not all for the
                  AMDb system. It is also offering customized movie
                  recommendations according to the users' favourite genres and
                  liked movies. Another benefit of the AMDb system is AMDb does
                  not need an actual human to check if the comment includes
                  toxicity, so it is more convenient and less convenient costly.
                  Because AMDb has the toxicity detector, it will automatically
                  work when a user comments within our system, unlike other
                  systems.
                </p>
              </div>
              <div class="amdb_aboutus__details__item__text">
                <h4>Comment detector:</h4>
                <p>
                  For AMDb, when users post their comment on AMDb platform, it
                  will be reminded this comment's toxic rate and sentiment
                  result to users. Users can filter comments based on their
                  tolerance for the toxic level or emotional bias. In this way,
                  a relatively non-toxic and fair communication environment can
                  be created for users.
                  <br />
                  For other platforms, AMDb supports browsing of film reviews
                  from TMDb, IMDb, YouTube and Twitter. At the same time, each
                  film review has been tested by the toxic comment detector and
                  its corresponding results are attached in the end of the
                  comment box.
                </p>
              </div>
              <div class="amdb_aboutus__details__item__text">
                <h4>Toxic Level Icons and Explanation</h4>
                <div class="M" style="">
                  <div class="t">
                    <img
                      src="@/assets/toxic-green.png"
                      alt="toxic level 1"
                      style="height: 10%"
                    />
                  </div>
                  <div class="t">
                    <img
                      src="../assets/toxic-red.png"
                      alt="toxic level 3"
                      style="height: 10%"
                    />
                  </div>
                </div>
                <div class="p-conent">
                  <p>
                    When the toxic rate is within the range of 0-54%, the system
                    will use a green skull to indicate that it is most likely
                    non-toxic. When the toxic rate is over the range of 54%, the
                    system will use a red grunt to indicate that it is highly
                    likely toxic.
                  </p>
                </div>
              </div>
              <div class="amdb_aboutus__details__item__text">
                <h4>Sentiment Level Icons and Explanation</h4>
                <div class="M" style="">
                  <div class="t">
                    <img src="../assets/sentiment-green.png" alt="Positive" />
                  </div>
                  <div class="t">
                    <img src="../assets/sentiment-yellow.png" alt="Neuture" />
                  </div>
                  <div class="t">
                    <img src="../assets/sentiment-red.png" alt="Negative" />
                  </div>
                </div>
                <div class="p-conent">
                  <p>
                    The results of sentiment analysis have three labels, green,
                    yellow and red icos correspond to positive, neutral and
                    negative respectively.
                  </p>
                </div>
              </div>
            </div>
          </div>

          <div class="col-lg-8">
            <div class="amdb_aboutus__details__item__text">
              <h4>The worst movies</h4>
              <p>
                On AMDb, there has a section where we are getting the
                worst-rated movies from IMDb; there are two reasons why we are
                doing that. The first reason is people are generally interested
                in best-rated movies, but some of them are also curious about
                worst-rated movies, and most people find that interesting.
                Another reason to have worst-rated movies in our system is, it
                is a great way to represent the capabilities of our toxicity
                analyses and sentimental analyses since worst-rated movies
                generally include harsh and negative reviews.
              </p>
            </div>
            <!-- IMDB bot 10 movies  -->
            <div class="trending__amdb_movies" id="imdbbot">
              <div class="row">
                <div class="col-lg-8 col-md-8 col-sm-8"></div>
                <div class="col-lg-4 col-md-4 col-sm-4">
                  <div class="btn__all">
                    <a
                      id="ImdbBotMore"
                      @click="showResultPage()"
                      class="primary-btn"
                      >View All <span class="arrow_right"></span
                    ></a>
                  </div>
                </div>
              </div>
              <div class="row" v-if="imdbBotMovies.length > 0">
                <div
                  class="col-lg-4 col-md-6 col-sm-6 movie-content"
                  v-for="item in imdbBotMovies"
                  :key="item.id"
                >
                  <router-link :to="'/movie/' + item.tmdb_Id">
                    <div class="amdb_movies__item">
                      <div
                        v-bind:style="{
                          'background-image': 'url(' + item.posters[0] + ')',
                        }"
                        class="amdb_movies__item__pic set-bg testmain"
                      >
                        <div class="ep">
                          {{ Number(item.rating).toFixed(1) }} / 10
                        </div>
                        <div class="view">
                          <i class="fa fa-eye"></i> {{ item.year }}
                        </div>
                      </div>
                      <div class="amdb_movies__item__text">
                        <ul>
                          <li
                            v-for="genre in item.genres.slice(0, 2)"
                            :key="genre.id"
                          >
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
          </div>
          <div id="teaminfo" class="col-lg-8 teaminfo">
            <div class="amdb_aboutus__details__content">
              <div class="amdb_aboutus__details__text">
                <div class="section-title">
                  <h4>Our Team</h4>
                </div>
                <p>
                  XIAOYAN WANG (ASD) -
                  <a href="mailto:xiaoyanwang0513@gmail.com">
                    xiaoyanwang0513@gmail.com
                  </a>
                  <br />
                  PINGAN ZHANG (ASD) -
                  <a href="mailto:pinganzhang518@gmail.com">
                    pinganzhang518@gmail.com
                  </a>
                  <br />
                  EGE BILIR (ASD) -
                  <a href="mailto:egebilir@gmail.com"> egebilir@gmail.com </a>
                  <br />
                  TENGKAI GAO (DS) -
                  <a href="mailto:tengkaigao@gmail.com">
                    tengkaigao@gmail.com
                  </a>
                  <br />
                  YIZHANG HUA (DS) -
                  <a href="mailto:lzshmm@gmail.com"> lzshmm@gmail.com </a>
                  <br />
                  YILING LIAO (DS) -
                  <a href="mailto:elim.yilinliao@gmailcom">
                    elim.yilinliao@gmailcom
                  </a>
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { ref, onBeforeMount } from "vue";
import router from "@/router";
import UserApi from "../services/user.service";
export default {
  name: "AboutUs",
  components: {},
  setup() {
    const imdbBotMovies = ref([]);
    onBeforeMount(() => {
      // IMDB BOT 10 movies
      UserApi.getImdbBotMovies(6)
        .then((response) => {
          imdbBotMovies.value = response.data.data;
        })
        .catch((error) => {
          showErroeMessage();
        });
    });

    const showErroeMessage = () => {
      return message.error("Server is busy, try again later");
    };

    //show Result Page
    const showResultPage = () => {
      localStorage.setItem("resultResource", 5);
      router.push({
        name: "ResultDisplay",
        params: {
          isPopularorHighScore: 5,
        },
      });
    };
    return { imdbBotMovies, showResultPage };
  },
};
</script>

<style lang="scss" scoped>
.p-conent {
  display: inline-block;
}
div .t {
  float: left;
  margin: 10px;
  width: 150px;
}

.amdb_aboutus-details {
  padding-top: 70px;
}

.spad {
  padding-top: 100px;
  padding-bottom: 100px;
}

.amdb_aboutus__details__title {
  text-align: center;
  margin-bottom: 70px;
}

.amdb_aboutus__details__title h6 {
  font-size: 15px;
  color: #ffffff;
  font-weight: 700;
  text-transform: uppercase;
  margin-bottom: 30px;
}

.amdb_aboutus__details__title h6 span {
  color: #b7b7b7;
  font-weight: 400;
  text-transform: none;
}

.amdb_aboutus__details__title h2 {
  color: #ffffff;
  font-size: 48px;
  font-weight: 700;
  line-height: 60px;
  margin-bottom: 38px;
}

.amdb_aboutus__details__title .amdb_aboutus__details__social a {
  display: inline-block;
  font-size: 15px;
  color: #ffffff;
  padding: 16px 35px 14px 20px;
  border-radius: 2px;
  margin-right: 6px;
}
.amdb_aboutus__details__pic {
  margin-bottom: 30px;
}

.amdb_aboutus__details__pic img {
  min-width: 100%;
}

.amdb_aboutus__details__text {
  margin-bottom: 40px;
}

.amdb_aboutus__details__text p {
  color: #ffffff;
  font-size: 17px;
  line-height: 30px;
}

.amdb_aboutus__details__item__text {
  margin-bottom: 42px;
}

.amdb_aboutus__details__item__text h4 {
  color: #ffffff;
  font-weight: 700;
  margin-bottom: 35px;
}

.amdb_aboutus__details__item__text img {
  min-width: 100%;
  margin-bottom: 26px;
}

.amdb_aboutus__details__item__text p {
  color: #ffffff;
  font-size: 17px;
  line-height: 30px;
  margin-bottom: 0;
}
.teaminfo a {
  color: aquamarine;
}

@media only screen and (max-width: 480px) {
  .spad {
    padding-bottom: 20px;
  }
  .amdb_aboutus-details {
    padding-top: 10px;
  }
  .about-us-div {
    .amdb_aboutus__details__title h2 {
      line-height: 30px !important;
    }
    .amdb_aboutus__details__text p {
      font-size: 13px;
      line-height: 17px;
    }
    .amdb_aboutus__details__item__text h4 {
      margin-bottom: 0px;
    }
    .amdb_aboutus__details__item__text p {
      font-size: 13px;
      line-height: 17px;
    }
    .amdb_aboutus__details__item__text img {
      margin-bottom: 0px;
    }
  }
}
</style>