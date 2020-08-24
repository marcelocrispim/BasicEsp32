<template>
    <div id="app">
        <transition-group name="list-complete" tag="container">

            <container
                    v-for="item in items"
                    v-bind:key="item.id"
                    class="list-complete-item"
                    :titulo="item.nome"
                    :ligado="item.ligado"
                    :tempo="item.timeOn"
                    v-show="item.online"
            />

        </transition-group>

    </div>
</template>
<script>
    import Container from "./components/Container";
    import {mapState} from 'vuex'

    export default {
        name: 'app',
        components: {
            Container: Container
        },
        data() {
            return {
                itemsx: [
                    {
                        'id': 0,
                        'titulo': 'estação 1',
                        'cor': 'bordaVerde',
                        'show': true,
                        'tempo': '00:02',
                        'ligado': true,
                        'temperatura': 25
                    },
                    {
                        'id': 1,
                        'titulo': 'estação 2',
                        'cor': 'bordaVerde',
                        'show': true,
                        'tempo': '00:02',
                        'ligado': true,
                        'temperatura': 25
                    },
                    {
                        'id': 2,
                        'titulo': 'estação 3',
                        'cor': 'bordaVerde',
                        'show': true,
                        'tempo': '00:02',
                        'ligado': true,
                        'temperatura': 25
                    }]

            }
        },
        computed: {

            ...mapState(['items'])
        }
        ,
        created() {

        }
    }
</script>
<style scoped>
    .list-complete-item {
        transition: all 2s;
        display: inline-block;

    }

    .list-complete-leave-active {
        position: absolute;
    }


    .list-complete-enter, .list-complete-leave-to {
        opacity: 0;
        transform: scale(.01);
        box-shadow: 0 0 0 black;
    }

    #app {
        transition: 1200ms linear all;
        background-color: rgba(212, 212, 212, 0.64);

        display: flex;
        flex-wrap: wrap;
        margin: 0;
        width: 100vw;
        height: 100vh;
    }
</style>
