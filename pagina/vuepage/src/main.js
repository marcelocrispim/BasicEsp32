import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VueSocketIO from 'vue-socket.io'
import SocketIO from "socket.io-client"

Vue.use(new VueSocketIO({
    debug: true,
    connection: 'http://127.0.0.1:8000',
    vuex: {
        store,
        actionPrefix: 'SOCKET_',
        mutationPrefix: 'SOCKET_'
    },
    options: {path: "/my-app/"} //Optional options
}))

Vue.config.productionTip = false


new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')
