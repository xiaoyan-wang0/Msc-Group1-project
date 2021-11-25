import { createApp } from 'vue'
import App from './App.vue'
import Antd from 'ant-design-vue';
import axios from 'axios'
import router from './router'
import store from './store'
import ElementPlus from 'element-plus'
import VueAxios from 'vue-axios'
import 'element-plus/dist/index.css'
import 'ant-design-vue/dist/antd.css';;

//fontawesome
import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { fas } from '@fortawesome/free-solid-svg-icons'
library.add(fas);
import { fab } from '@fortawesome/free-brands-svg-icons';
library.add(fab);
import { far } from '@fortawesome/free-regular-svg-icons';
library.add(far);
import { dom } from "@fortawesome/fontawesome-svg-core";
dom.watch();
//fontawesome

// Import Bootstrap an BootstrapVue CSS files (order is important)
import "bootstrap/dist/css/bootstrap.min.css";
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.bundle.js'
import "bootstrap"


const app = createApp(App);
app.config.productionTip = false;
// axios.defaults.withCredentials=true;//让ajax携带cookie 
app.use(VueAxios, axios)
app.provide('axios', app.config.globalProperties.axios);  // provide 'axios'
app.component("font-awesome-icon", FontAwesomeIcon);
app.use(store).use(router).use(Antd).use(ElementPlus).mount('#app')
