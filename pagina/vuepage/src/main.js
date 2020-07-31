import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VueSocketIO from 'vue-socket.io'
import SocketIO from "socket.io-client"


const options = {path: '/socket.io'}; //Options object to pass into SocketIO
Vue.use(new VueSocketIO({
    debug: false,
    connection: SocketIO('http://192.168.30.43:8000', options),
    vuex: {
        store,
        actionPrefix: 'SOCKET_',
        mutationPrefix: 'SOCKET_'
    },

}))

Vue.config.productionTip = true


new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')
