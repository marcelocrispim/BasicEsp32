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
        "SOCKET_event"(state, message) {
            console.log('mutations ', message)
            state.l3 = message.l3
            state.l4 = message.l3
            // do something
        }
    },
    actions: {
        "SOCKET_event"(context, message) {
            console.log('actions ', message)
            // do something
        }
    },
})
