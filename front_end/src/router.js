import Vue from 'vue'
import Router from 'vue-router'

import Login from './components/users/Login'
import Main from './views/Main'

Vue.use(Router)


export default new Router({
    routes : [
        {path: '/', component: Main },
        {path: '/login', component: Login}
    ]
})