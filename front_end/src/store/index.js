import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
    logined: false,
    Loginedname: null,
    UserId: null,
}

var mutations = {
    LOGIN(state, user){
        sessionStorage.setItem("Loginedname",user.Loginedname)
        sessionStorage.setItem("UserId", user.UserId)
        sessionStorage.setItem("logined", true)
    },
    LOGOUT(state){
        sessionStorage.removeItem("Loginedname")
        sessionStorage.removeItem("UserId")
        sessionStorage.removeItem("logined")
        state.Loginedname = ""
        state.UserId = ""
        state.logined = false
    }
}

var getters = {
    isLogin (state) {
        if(!state.logined){
            state.logined = sessionStorage.getItem("logined")
            state.Loginedname = sessionStorage.getItem("Loginedname")
            state.UserId = sessionStorage.getItem("UserId")
        }
        return state.logined
    }
}

export default new Vuex.Store({
    getters,
    state,
    mutations
})