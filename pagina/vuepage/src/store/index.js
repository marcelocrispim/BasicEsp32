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
    getters: {
        l1: state => state.l1,
        l2: state => state.l2,
        l3: state => state.l3,
        l4: state => state.l4,
        l5: state => state.l5,
        l6: state => state.l6,

    },
    mutations: {
        "SOCKET_event"(state, message) {
            console.log('mutations ', message)
            state.l3 = message.bt1
            state.l4 = message.bt1
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
