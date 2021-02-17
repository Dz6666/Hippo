// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Antd from 'ant-design-vue';  // 局部导入组件（仅导入指定的组件） import { Button, message } from 'ant-design-vue';
import 'ant-design-vue/dist/antd.css';
import settings from "./settings";
import axios from "axios";

let echarts = require('echarts')
Vue.prototype.$echarts = echarts  // 方便后续组件中使用到echarts功能将echarts封装到vue对象中（将echarts整个封装给了vue封装方法$echarts这个属性）

Vue.config.productionTip = false
Vue.prototype.$axios = axios    // 原型链形式挂载到vue中，后面通过组件对象可以直接调动ax

Vue.prototype.$settings = settings

Vue.use(Antd);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
