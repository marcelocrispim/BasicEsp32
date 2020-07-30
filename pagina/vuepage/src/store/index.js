import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        l1: false,
        l2: false,
        l3: false,
        l4: false,
        l5: false,
        l6: false
    },
    mutations: {
        "SOCKET_event"() {
            // do something
        }
    },
    actions: {
        "SOCKET_event"() {
            // do something
        }
    },
})
