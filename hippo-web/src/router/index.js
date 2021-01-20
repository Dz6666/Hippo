import Vue from 'vue'
// import 起包别名 from 功能包中抛出的功能
import Router from 'vue-router'   // ./router是一个包名称。都在node_modules中安装着了，此包有一个功能通过前端访问路径找到对应的组件 export default {被抛出的功能才能被引入}

// 通过路径找到对应的vue组件对象  @表示src/components/HelloWord.vue文件
import ShowCenter from '@/components/ShowCenter'

import Login from '@/components/Login'

// 想要使用功能必须use一下。才可以使用路由的功能
Vue.use(Router);
export default new Router({
  mode:'history',
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/hippo',
      name: 'ShowCenter',
      component: ShowCenter
    },
  ],
})

