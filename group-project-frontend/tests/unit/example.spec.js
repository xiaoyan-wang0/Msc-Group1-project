import { shallowMount } from '@vue/test-utils'
import Home from '@/views/Home.vue'
import AboutUs from '@/views/AboutUs.vue'
import MainPage from '@/views/MainPage.vue'

describe('Home.vue', () => {
  it('Home', async () => {
    const wrapper = shallowMount(Home, {
    })
    const search = wrapper.get('#search-input')
    const form = wrapper.get('.search-model-form')
    await form.trigger('submit');
    expect(search.text()).toContain('')
    await search.setValue('some value')
    await form.trigger('submit');
    expect(search.text()).toContain('')
  })
})

describe('AboutUs.vue', () => {
  it('AboutUs', async () => {
    const wrapper = shallowMount(AboutUs, {
    })
    const form = wrapper.get('.blog__details__item__text')
    expect(form.text()).toContain('sentiment')
  })
})

describe('MainPage.vue', () => {
  it('MainPage', async () => {
    const wrapper = shallowMount(MainPage, {
    })
    const form = wrapper.get('.div-main-content')
    expect(form.text()).toContain('')
  })
})

