<template>

    <div class="bodyContainer" v-bind:class="{ bodyContainerRed: pisca }">
        <div>
            <h4 class="tituloContainer">{{titulo}}</h4>
        </div>
        <div class="corpoContainer" v-bind:class="cor">
            <display-time :valor="tempo" :ligado="ligado"/>
            <display-temp :valor="temperatura"/>

        </div>
    </div>

</template>

<script>
    import Fonte611 from "./Fonte611";
    import DisplayField from "./DisplayField";
    import DisplayTime from "./DisplayTime";
    import DisplayTemp from "./DisplayTemp";

    export default {
        name: "Container",
        components: {
            Fonte611,
            DisplayField,
            DisplayTime,
            DisplayTemp
        },
        props: {
            titulo: {type: String, default: 'Estação X'},
            cor: {type: String, default: 'bordaPreta'},
            temperatura: {type: Number, default: 25},
            tempo: {type: String, default: '00:00'},
            ligado: {type: Boolean, default: false}
        },
        data() {
            return {
                pisca: false
            }
        }
        ,
        created() {
            setInterval(() => {
                if (this.cor == 'bordaVermelha') {
                    this.pisca = !this.pisca
                }
            }, 1000)
        }

    }
</script>

<style scoped>


    .bodyContainer {
        box-shadow: 5px 5px 5px #888888;
        margin: 2vh 1vw;
        border-radius: 15px;
        height: 45vh;
        width: 17.5vw;
        border: solid 1px black;
        background-color: grey;
        align-items: center;
        transition: 1000ms;
        font-family: 'Courier New', 'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }

    .tituloContainer {
        padding: 3px;
        text-align: center;
        height: 3vh;
        width: 18vw;
        font-weight: lighter;
        font-size: large;
        transition: 1000ms;
        text-transform: uppercase;
    }

    .corpoContainer {
        background-color: #6392f5;
        z-index: 10;
        height: 40vh;
        margin: .5vw;
        width: 16.5vw;
        text-align: center;
        border-radius: 5px;
        transition: 1000ms;
        padding: 5px;
    }

    .bodyContainerRed {
        background-color: red;
    }

    .bordaVerde {
        border: solid darkgreen 4px;
    }

    .bordaVermelha {
        border: solid red 6px;
    }

    .bordaPreta {
        border: solid black 2px;
    }
</style>
