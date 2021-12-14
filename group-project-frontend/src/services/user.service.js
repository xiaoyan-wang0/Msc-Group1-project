import myAxios from './AmdbAxios.js';
import env from "@/env.js";

const API_URL = '/api/';

class UserService {
  /**
  **
  **   MainDIPlay.vue
  **
  **/

  // Upcoming moveis
  getUpcomingMovies(pageNumber) {
    console.log("getUpcomingMovies");
    return myAxios.othersAxios({
      url: env.tmdbupcoming + env.tmdbkey + env.tmdbtail + "&page= " + pageNumber,
      method: 'get',
    });
  }

  // Get Popular movies
  getPopularMovies(pageNumber) {
    console.log("getPopularMovies");
    return myAxios.othersAxios({
      url: env.tmdbpopular + env.tmdbkey + env.tmdbtail + "&page= " + pageNumber,
      method: 'get',
    });
  }

  // Get High score moveis
  getHighScoreMovies(pageNumber) {
    console.log("getHighScoreMovies");
    return myAxios.othersAxios({
      url: env.tmdbhighscore + env.tmdbkey + env.tmdbtail + "&page= " + pageNumber,
      method: 'get',
    });
  }

  // Get IMDB BOT  movies
  getImdbBotMovies(num) {
    console.log("getImdbBotMovies");
    return myAxios.amdbAxios({
      url: "movieImdb/movieImdbBottomInfo?numberOfMovies=" + num,
      method: 'get',
    });
  }

  // Fetch the most comments recommendation movies
  getMostCommentsMovies() {
    console.log("getMostCommentsMovies");
    return myAxios.amdbAxios({
      url: "rec/getMostComments",
      method: 'get',
    });
  }

  // Get RecommandationByTags
  getRecommandationByTags(id) {
    console.log("getRecommandationByTags");
    return myAxios.amdbAxios({
      url: "rec/getRecommandationByTags?userId=" + id,
      method: 'get',
    });
  }


  /**
  **
  **   MovieDetial.vue
  **
  **/

  // Get movie detail
  getMovieDetail(movieid) {
    console.log("getMovieDetail");
    return myAxios.othersAxios({
      url: movieid + "?" + env.tmdbkey,
      method: 'get',
    });
  }

  // Get RecommandationByTags
  getRecommandationById(movieid) {
    console.log("getRecommandationById");
    return myAxios.amdbAxios({
      url: "rec/getRecommendationById?movieId=" + movieid,
      method: 'get',
    });
  }

  // set Recommendation
  setRecommendation(movieid, userId, tag) {
    console.log("setRecommendation");
    return myAxios.amdbAxios({
      url: "rec/setRecommandation?movieId=" + movieid
        + "&userId=" + userId + "&tagId=" + tag,
      method: 'get',
    });
  }

  // Get trailer
  getMovieTrailer(movieid) {
    console.log("getMovieTrailer");
    return myAxios.othersAxios({
      url: movieid +
        env.tmdbvideo +
        env.tmdbkey +
        env.tmdbtail,
      method: 'get',
    });
  }

  // Get casts
  getMovieCasts(movieid) {
    console.log("getMovieCasts");
    return myAxios.othersAxios({
      url: movieid +
        env.tmdbcredits +
        env.tmdbkey +
        env.tmdbtail,
      method: 'get',
    });
  }

  // Get movie comments
  getMovieComments(movieid) {
    console.log("getMovieComments");
    return myAxios.amdbAxios({
      url: "comments/showComments?movieId=" + movieid,
      method: 'get',
    });
  }

  // Get TMDB Comments
  getTmdbComments(movieid) {
    console.log("getTmdbComments");
    return myAxios.amdbAxios({
      url: "movieTmdb/movieTmdbReviews?movieId=" + movieid,
      method: 'get',
    });
  }

  // Get IMDB Comments
  getImdbComments(movieid) {
    console.log("getTmdbComments");
    return myAxios.amdbAxios({
      url: "movieImdb/movieImdbReviews?movieId=" + movieid,
      method: 'get',
    });
  }

  // Get Youtube Comments
  getYoutubeComments(name, movieid) {
    console.log("getYoutubeComments");
    return myAxios.amdbAxios({
      url: "movieYoutube/movieYoutubeReviews?movieName=" + name + "&movieId=" + movieid,
      method: 'get',
    });
  }

  // Get twitter Comments
  getTwitterComments(name, movieid) {
    console.log("getTwitterComments");
    return myAxios.amdbAxios({
      url: "movieTwitter/movieTwitterReviews?movieName='" + name + "'&movieId=" + movieid,
      method: 'get',
    });
  }

  // Detect user Comment
  detectUserComment(commentsValue) {
    console.log("detectUserComment");
    const detectFormData = new FormData();
    detectFormData.append("title", commentsValue);
    return myAxios.amdbAxios({
      url: "/comments/toxic",
      data: detectFormData,
      method: 'post',
      headers: {
        "Content-Type": "multipart/form-data"
      }
    });
  }

  // Post user Comment
  postUserComment(data) {
    console.log("postUserComment");
    return myAxios.amdbAxios({
      url: "comments/addComments",
      data: data,
      method: 'post',
      headers: {
        "Content-Type": "multipart/form-data"
      }
    });
  }

  // Get cast detail
  getMovieCastsDetail(id) {
    console.log("getMovieCastsDetail");
    return myAxios.othersAxios({
      url: env.tmdbperson + id + "?" + env.tmdbkey + env.tmdbtail,
      method: 'get',
    });
  }

  // Add to like list
  addLikeList(movieid, userId) {
    console.log("addLikeList");
    return myAxios.amdbAxios({
      url: "member/movieLikes?userId=" +
        userId + "&movieId=" + movieid,
      method: 'get',
    });
  }

  // Report comment
  reportComment(reportCommentId, userId) {
    console.log("addLikeList");
    return myAxios.amdbAxios({
      url: "admin/doReport?id=" +
        reportCommentId + "&userId=" + userId,
      method: 'get',
    });
  }

  /**
  **
  **   ResultPage.vue
  **
  **/

  // get Search moveis result
  getSearchMoveis(searchValue, pageNumber) {
    console.log("getSearchMoveis");
    return myAxios.othersAxios({
      url: env.tmdbSearch + env.tmdbkey + env.tmdbquery + searchValue + "&page= " + pageNumber,
      method: 'get',
    });
  }



  /**
  **
  **   Profile.vue
  **
  **/

  // recently recommendation movies
  getRecentRecommendation(userId) {
    console.log("getRecentRecommendation");
    return myAxios.amdbAxios({
      url: "rec/getRecommandation?userId=" + userId,
      method: 'get',
    });
  }

  // Get history list
  getHistoryList(userId) {
    console.log("getHistoryList");
    return myAxios.amdbAxios({
      url: "rec/showHistory?userId=" + userId,
      method: 'get',
    });
  }

  // Get like list
  getLikeList(userId) {
    console.log("getLikeList");
    return myAxios.amdbAxios({
      url: "member/showMovieList?userId=" + userId,
      method: 'get',
    });
  }

  // Get like list
  getUserCommentList(userId) {
    console.log("getUserCommentList");
    return myAxios.amdbAxios({
      url: "/member/showCommentList?userId=" + userId,
      method: 'get',
    });
  }

  // Delete like list
  deleteLikeList(userId) {
    console.log("deleteLikeList");
    return myAxios.amdbAxios({
      url: "member/deleteMovieLikes?Id=" + userId,
      method: 'get',
    });
  }

  // Delete user comment list
  deleteUserCommentList(userId) {
    console.log("deleteUserCommentList");
    return myAxios.amdbAxios({
      url: "member/deleteComment?id=" + userId,
      method: 'get',
    });
  }


  /**
  **
  **   CommentDetector.vue
  **
  **/

  //  Detect user Comment


  /**
  **
  **   PersonalSetting.vue
  **
  **/
  // Update user info
  updateUserInfo(data) {
    console.log("updateUserInfo");
    return myAxios.amdbAxios({
      url: "member/setUserInfo",
      data: data,
      method: 'post',
      headers: {
        "Content-Type": "multipart/form-data"
      }
    });
  }

  // get user info
  getUserInfo(userId) {
    console.log("getUserInfo");
    return myAxios.amdbAxios({
      url: "member/getUserInfo?userId=" + userId,
      method: 'get'
    });
  }

}

export default new UserService();