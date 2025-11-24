import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import Userinfo from "../views/Userinfo.vue";
import Textcheck from "../views/Textcheck.vue";
import Apitest from "../views/Apitest.vue";
import Login from "../views/login.vue";
import Lottery from "../views/Lottery.vue";
import Ball from "../views/Ball.vue";
import Star from "../views/Star.vue";

Vue.use(Router)

let router = new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      meta: { requiresAuth: true, breadcrumb: '首页'}
    },
    {
      path: '/about',
      name: 'about',
      component: About,
      meta: { requiresAuth: true, breadcrumb: '关于'}
    },
    {
      path: '/userinfo',
      name: 'userinfo',
      component: Userinfo,
      meta: { requiresAuth: true, breadcrumb: '用户管理'}
    },
    {
      path: '/textcheck',
      name: 'textcheck',
      component: Textcheck,
      meta: { requiresAuth: true, breadcrumb: '错别字检查'}
    },
    {
      path: '/apitest',
      name: 'apitest',
      component: Apitest,
      meta: { requiresAuth: true, breadcrumb: '接口测试'}
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/lottery',
      name: 'lottery',
      component: Lottery,
      meta: { requiresAuth: true, breadcrumb: '转盘' +
          '' +
          ''}
    },
    {
      path: '/ball',
      name: 'ball',
      component: Ball,
      meta: { requiresAuth: true, breadcrumb: '双色球' +
          '' +
          ''}
    },
    {
      path: '/star',
      name: 'star',
      component: Star,
      meta: { requiresAuth: true, breadcrumb: '双色球' +
          '' +
          ''}
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


