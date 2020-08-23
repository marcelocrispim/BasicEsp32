<template>
    <div id="app">
        <transition-group name="list-complete" tag="container">

            <container
                    v-for="item in filtro"
                    v-bind:key="item.id"
                    class="list-complete-item"
                    :titulo="item.titulo"
                    :cor="item.cor"
                    :ligado="item.ligado"
                    :temperatura="item.temperatura"
            />

        </transition-group>

    </div>
</template>
<script>
    import Container from "./components/Container";


    export default {
        name: 'About',
        components: {
            Container

        },
        data() {
            return {
                items: [
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
            filtro: function () {

                return this.items.filter((item) => item.show == true)
            }
        }
        ,
        created() {
            let n1, n2, n3
            setInterval(() => {
                n1 = Math.floor(Math.random() * 3);
                n2 = Math.floor(Math.random() * 60);
                n3 = Math.floor(Math.random() * 3);
                this.items[n1].show = !this.items[n1].show
                this.items[n3].temperatura = n2
                this.items[n3].ligado = !this.items[n3].ligado
            }, 5000)
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
