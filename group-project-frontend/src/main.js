import { createApp } from 'vue'
import App from './App.vue'
import Antd from 'ant-design-vue';
import axios from 'axios'
import router from './router'
import store from './store'
import ElementPlus from 'element-plus'
import VueAxios from 'vue-axios'
import 'element-plus/dist/index.css'
import 'ant-design-vue/dist/antd.css';


const app = createApp(App);
app.config.productionTip = false;
app.use(VueAxios, axios)
app.provide('axios', app.config.globalProperties.axios)  // provide 'axios'
app.use(store).use(router).use(Antd).use(ElementPlus).mount('#app')
