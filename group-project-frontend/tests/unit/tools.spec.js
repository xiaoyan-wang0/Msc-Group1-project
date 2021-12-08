
import tools from '@/tools'
import env from '@/env'
import UserService from '@/services/user.service.js'
import Authheader from '@/services/auth-header.js'
import Authmodule from '@/store/auth.module.js'
import AuthmoduleIndex from '@/store/Index.js'

describe('tools.vue', () => {
  it('tools ', () => {
    tools.RandomNumBoth([1, 2], 2)
    expect(tools.showToxicText(0.5)).toBe("Non toxic");
    expect(tools.showToxicText(0.8)).toBe("Toxic");
    expect(tools.showToxicText(0.99)).toBe("Severe toxic");
    expect(tools.showToxicImg(0.5)).toBe("/img/toxic-green.31dbd2c6.png");
    expect(tools.showToxicImg(0.8)).toBe("/img/toxic-yellow.4f83d804.png");
    expect(tools.showToxicImg(0.99)).toBe("/img/toxic-red.7e1e0c69.png");
    expect(tools.showSentiemntText(0.4)).toBe("Negative");
    expect(tools.showSentiemntText(0.8)).toBe("Positive");
    expect(tools.showSentiemntImg(0.3)).toBe("Negative");
    expect(tools.showSentiemntImg(0.8)).toBe("Positive");
    expect(tools.showSentiemntImg(0.5)).toBe("Neutral");
    expect(tools.changeToPercent(0.55)).toBe("55.00%");
    expect(tools.formatDate('1994-05-13')).toBe("1994-5-13");
    expect(tools.judgeBadWord('shit movie')).toBe("<font color=\"red\"> *** </font> movie");
    expect(tools.judgeBadWordOther('shit movie')).toBe(" ***  movie");
  })
})


describe('env', () => {
  it('env ', () => {
    expect(env.slash_string).toBe("/");
    expect(env.tmdbSearch).toBe("https://api.themoviedb.org/3/search/movie?");
  })
})



describe('UserService', () => {
  it('UserService ', () => {
    UserService.getUpcomingMovies();
    UserService.getPopularMovies();
    UserService.getHighScoreMovies();
    UserService.getImdbBotMovies(6);
    UserService.getMostCommentsMovies(6);
    UserService.getRecommandationByTags(158)
    UserService.getMovieDetail(4535)
    UserService.getRecommandationById(158)
    UserService.setRecommendation(158, 1)
    UserService.getMovieTrailer(158)
    UserService.getMovieCasts(158)
    UserService.getMovieComments(158)
    UserService.getTmdbComments(158)
    UserService.getImdbComments(158)
    UserService.getYoutubeComments('superman', 158)
    UserService.getTwitterComments('superman', 158)
    UserService.detectUserComment(158)
    UserService.postUserComment(158, 'nice', 1)
    UserService.getMovieCastsDetail(158)
    UserService.reportComment(158, 1)
    UserService.addLikeList(158, 1)
    UserService.getSearchMoveis(158, 1)
    UserService.getRecentRecommendation(158)
    UserService.getLikeList(158)
    UserService.getUserCommentList(158)
    UserService.deleteLikeList(158)
    UserService.deleteUserCommentList(158)
    UserService.updateUserInfo({ 1: 'data' })
    UserService.getUserInfo(158)
    // expect(UserService.getUpcomingMovies()).toBe(mockData);
    // expect(UserService.getPopularMovies()).toBe(new Promise())
    // expect(UserService.getHighScoreMovies()).toBe(new Promise())
    // expect(UserService.getImdbBotMovies(6)).toBe(new Promise())
    // expect(UserService.getMostCommentsMovies(6)).toBe(new Promise())
    // expect(UserService.getRecommandationByTags(158)).toBe(new Promise())
  })
})

const fakeLocalStorage = (function () {
  let store = { user: { user: { accessToken: true }, accessToken: true } };

  return {
    getItem: function (key) {
      return JSON.stringify(store[key]);
    },
    setItem: function (key, value) {
      store[key] = value.toString();
    },
    removeItem: function (key) {
      delete store[key];
    },
    clear: function () {
      store = {};
    }
  };
})();

describe('Authheader', () => {
  beforeAll(() => {
  });

  it('Authheader ', () => {
    console.log("localStorage")
    console.log(localStorage.getItem('user'))
    Authheader();

    Object.defineProperty(window, 'localStorage', {
      value: fakeLocalStorage,
    });
    Authheader();
  })
})

describe('Authmodule index', () => {
  it('Authmodule ', () => {
    AuthmoduleIndex;
  })
})


describe('Authmodule', () => {
  it('Authmodule ', () => {
    Authmodule.actions.login;
  })
})


