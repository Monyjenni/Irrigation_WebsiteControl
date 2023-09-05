import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AuthLayout from '../views/Layout/AuthLayout.vue'
import AppLayout from '../views/Layout/AppLayout.vue'
import Home from '../views/Home/HomeView.vue'
import History from '../views/Home/HistoryVue.vue'
import Menu from '../views/Home/MenuVue.vue'
import Setting from '../views/Home/SettingVue.vue'



Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: AuthLayout,
    children: [{
      path: '',
      component: HomeView 
    }]
  },
  {
    path: '/',
    name: 'user',
    component: AppLayout,
    children: [
      {
      path: '/home',
      component: Home
      }, 
      {
        path: '/history',
        component: History
      },
      {
        path: '/menu',
        component: Menu
      },
      {
        path: '/setting',
        component: Setting
      }

  ]
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
