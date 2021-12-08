

import Routerindex from '@/router/index.js'
import AuthService from '@/services/auth.service.js'
import axios from "axios";

jest.mock("axios");

const fakeLocalStorage2 = (function () {
  let store = { user: false };

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

describe('Routerindex', () => {
  beforeAll(() => {
  });

  it('Routerindex ', () => {

    Routerindex.push({ path: "/login" });
    Routerindex.push({ path: "/main/porfile" });
    Object.defineProperty(window, 'localStorage', {
      value: fakeLocalStorage2,
    });

    Routerindex.push({ path: "/main/porfile" });
  })
})



describe('AuthService', () => {
  beforeAll(() => {
  });

  it('AuthService ', () => {
    // given
    const data = {
      data: {
        code: 200,
        hits: [
          {
            objectID: '1',
            title: 'a',
          },
          {
            objectID: '2',
            title: 'b',
          },
        ],
      },
    };
    jest.spyOn(axios, 'default').mockResolvedValue({
      name: 'abc',
    })
    AuthService.login({ user: 'user' });
    AuthService.logout();
    AuthService.register({ user: 'user' });
    jest.spyOn(axios, 'default').mockResolvedValue({
      name: 'abc',
      data: data
    })
    AuthService.login({ user: 'user' });
    AuthService.logout();
    AuthService.register({ user: 'user' });

  })

  it('AuthService 2', async () => {


  })
})
