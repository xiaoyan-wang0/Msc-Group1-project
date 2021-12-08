import { shallowMount, mount } from '@vue/test-utils'
import MainDisplay from '@/components/MainDisplay.vue'
import UserService from '@/services/user.service.js'
import axios from "axios";


jest.mock("axios");

const fakeLocalStorage = (function () {
  let store = { user: { user: { accessToken: true }, accessToken: true, data: { userId: 1 } }, data: { userId: 1 } };

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

const fakeLocalStorage2 = (function () {
  let store = { user: null };

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

describe('MainDisplay.vue', () => {

  it('MainDisplay', async () => {
    // given
    const data = {
      data: {
        code: 200,
        userId: 1
      },
    };
    jest.spyOn(UserService, 'getUpcomingMovies').mockResolvedValue({
      name: 'abc',
      data: data
    })
    jest.spyOn(UserService, 'getPopularMovies').mockResolvedValue({
      name: 'abc',
      data: data
    })
    jest.spyOn(UserService, 'getHighScoreMovies').mockResolvedValue({
      name: 'abc',
      data: data
    })
    jest.spyOn(UserService, 'getImdbBotMovies').mockResolvedValue({
      name: 'abc',
      data: data
    })
    jest.spyOn(UserService, 'getRecommandationByTags').mockResolvedValue({
      name: 'abc',
      data: { data: [1, 2, 3] }
    })
    jest.spyOn(UserService, 'getMostCommentsMovies').mockResolvedValue({
      name: 'abc',
      data: data
    })

    await Object.defineProperty(window, 'localStorage', {
      value: fakeLocalStorage,
    });
    const mainDisplay = shallowMount(MainDisplay, {
    })
    await Object.defineProperty(window, 'localStorage', {
      value: fakeLocalStorage,
    });
  })

  it('MainDisplay2', async () => {
    // given
    const data = {
      data: {
        code: 200,
        userId: 1
      },
    };
    jest.spyOn(UserService, 'getUpcomingMovies').mockResolvedValue({
      name: 'abc',
      data: data
    })
    jest.spyOn(UserService, 'getPopularMovies').mockResolvedValue({
      name: 'abc',
      data: data
    })
    jest.spyOn(UserService, 'getHighScoreMovies').mockResolvedValue({
      name: 'abc',
      data: data
    })
    jest.spyOn(UserService, 'getImdbBotMovies').mockResolvedValue({
      name: 'abc',
      data: data
    })
    jest.spyOn(UserService, 'getRecommandationByTags').mockResolvedValue({
      name: 'abc',
      data: data
    })
    jest.spyOn(UserService, 'getMostCommentsMovies').mockResolvedValue({
      name: 'abc',
      data: data
    })

    await Object.defineProperty(window, 'localStorage', {
      value: fakeLocalStorage2,
    });

    const mainDisplay2 = shallowMount(MainDisplay, {
    })
    await Object.defineProperty(window, 'localStorage', {
      value: fakeLocalStorage2,
    });


    await mainDisplay2.find(".primary-btn").trigger('click')
    await mainDisplay2.find("#ImdbBotMore").trigger('click')


  })
})
