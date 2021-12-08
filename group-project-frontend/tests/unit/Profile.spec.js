import { shallowMount, mount } from '@vue/test-utils'
import Profile from '@/components/Profile.vue'
import UserService from '@/services/user.service.js'

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

describe('Profile.vue', () => {
  it('Profile',  async () => {
    // given
    const data = {
      data: {
        code: 200,
        userId: 1
      },
    };
    //  jest.spyOn(UserService, 'getUserCommentList').mockResolvedValue({
    //   name: 'abc',
    //   data: data
    // })
    //  jest.spyOn(UserService, 'getLikeList').mockResolvedValue({
    //   name: 'abc',
    //   data: data
    // })
    //  jest.spyOn(UserService, 'getRecentRecommendation').mockResolvedValue({
    //   name: 'abc',
    //   data: data
    // })

     Object.defineProperty(window, 'localStorage', {
      value: fakeLocalStorage,
    });

    const profile = shallowMount(Profile, {
    })
    await mainDisplay2.find(".primary-btn").trigger('click')
     Object.defineProperty(window, 'localStorage', {
      value: fakeLocalStorage2,
    });
    await profile.find(".profile-settings-btn").trigger('click')

  })
})
