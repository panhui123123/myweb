import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import Userinfo from "../views/Userinfo.vue";
import Textcheck from "../views/Textcheck.vue";
import Apitest from "../views/Apitest.vue";
import Login from "../views/login.vue";
import Lottery from "../views/Lottery.vue";

Vue.use(Router)

let router = new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      meta: { requiresAuth: true }
    },
    {
      path: '/about',
      name: 'about',
      component: About,
      meta: { requiresAuth: true }
    },
    {
      path: '/userinfo',
      name: 'userinfo',
      component: Userinfo,
      meta: { requiresAuth: true }
    },
    {
      path: '/textcheck',
      name: 'textcheck',
      component: Textcheck,
      meta: { requiresAuth: true }
    },
    {
      path: '/apitest',
      name: 'apitest',
      component: Apitest,
      meta: { requiresAuth: true }
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/lottery',
      name: 'lottery',
      component: Lottery
    }
  ]
})

router.beforeEach((to, from, next) => {
  // 检查路由是否需要认证
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // 检查用户是否已经登录
    if (!localStorage.getItem('user')) {
      // 如果用户未登录，重定向到登录页面
      next({
        path: '/login',
        query: { redirect: to.fullPath }
      })
    } else {
      next() // 确保一定要调用 next()
    }
  } else {
    next() // 确保一定要调用 next()
  }
})

export default router


