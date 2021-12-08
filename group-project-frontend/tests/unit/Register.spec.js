import { shallowMount, mount } from '@vue/test-utils'
import Register from '@/views/Register.vue'

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

describe('Register.vue', () => {
  it('Register', async () => {
    const register = shallowMount(Register, {
    })
    const form = register.get('.requires-validation')
    await form.trigger('submit');
    expect(register.text()).toContain('')

  })
  it('Register', async () => {
    const register = shallowMount(Register, { attachTo: document.body })
    Object.defineProperty(window, 'localStorage', {
      value: fakeLocalStorage,
    });
    const mHeaderPos = [{ checkValidity: jest.fn().mockReturnValueOnce(true) }, { checkValidity: jest.fn().mockReturnValueOnce(false) }];
    const mHeader = { offsetTop: 100, submit: jest.fn().mockReturnValueOnce(mHeaderPos) };
    jest.spyOn(document, 'querySelectorAll').mockReturnValueOnce(mHeaderPos);
    const form = register.get('.requires-validation')
    await form.trigger('submit');
    await register.find('input[type="text"]').setValue('some value')
    await register.find('input[type="password"]').setValue('somevalue@gmail.com')
    await register.find('input[type="email"]').setValue('some value')
    await register.find('input[type="checkbox"]').setChecked()
    await form.trigger('submit');
    expect(register.text()).toContain('')
  })
})
