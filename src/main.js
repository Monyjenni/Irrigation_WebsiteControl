import Vue from 'vue'
import App from './App.vue'
import router from './router'
import Vuetify from 'vuetify'

Vue.use(Vuetify);

Vue.config.productionTip = false

const vuetify = new Vuetify({
  theme: {
    dark: true, // Set this to true for dark mode, false for light mode
  },
});
new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
