import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import Userinfo from "../views/Userinfo.vue";
import Textcheck from "../views/Textcheck.vue";
import Apitest from "../views/Apitest.vue";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/about',
      name: 'about',
      component: About
    },
    {
      path: '/userinfo',
      name: 'userinfo',
      component: Userinfo
    },
    {
      path: '/textcheck',
      name: 'textcheck',
      component: Textcheck
    },
    {
      path: '/apitest',
      name: 'apitest',
      component: Apitest
    }
  ]
})
