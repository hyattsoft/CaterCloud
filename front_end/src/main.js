import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import router from './router'
import store from './store/index'

Vue.config.productionTip = false


Vue.use(ElementUI)
router.beforeEach((to, from, next) =>{
  let isLogin = store.getters.isLogin
  console.log(isLogin)
  if(!isLogin){
    if(to.path !== '/login'){
      return next({path: '/login'});
    }else{
      next();
    }
  }
  else{
    if(to.path === '/login'){
      return next({path: '/main'})
    }
  }
})

new Vue({
  el: "#app",
  router,
  store,
  render: h => h(App),
})
// .$mount('#app')
