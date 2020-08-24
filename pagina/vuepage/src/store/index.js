import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        items: [{
            "mac": 0,
            "online": false,
            "ligado": false,
            "temperaturaAmbiente": 25,
            "temperaturaMotor": 25,
            "timeOn": "00:00:00"
        }]
    },
    getters: {},
    mutations: {
        "SOCKET_event"(state, message) {
            // console.log('mutations ', message)
            state.items = message
        }
    },
    actions: {
        "SOCKET_event"(context, message) {
            //console.log('actions ', message)
            // do something
        }
    },
})
