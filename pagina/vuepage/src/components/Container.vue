<template>
    <div class="bodyContainer">
        <div>
            <h4 class="tituloContainer">{{titulo}}</h4>
        </div>
        <div class="corpoContainer" v-bind:class="cor">
            <display-field></display-field>

        </div>
    </div>
</template>

<script>
    import Fonte611 from "./Fonte611";
    import DisplayField from "./DisplayField";

    export default {
        name: "Container",
        components: {
            Fonte611,
            DisplayField
        },
        props: {
            titulo: {type: String, default: 'Estação X'},
            cor: {type: String, default: 'bordaPreta'}
        }
    }
</script>

<style scoped>
    .bodyContainer {
        box-shadow: 5px 5px 5px #888888;
        margin: 2vh 1vw;
        border-radius: 15px;
        height: 95vh;
        width: 18vw;
        border: solid 1px black;
        background-color: grey;
        align-items: center;

    }

    .tituloContainer {
        padding: 3px;
        text-align: center;
        height: 3vh;
        width: 18vw;
        font-weight: lighter;
        font-size: large;
        font-family: 'Mulish', 'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }

    .corpoContainer {
        background-color: darkgrey;
        z-index: 10;
        height: 88vh;
        margin: .5vw;
        width: 17vw;
        text-align: center;
        border-radius: 5px;

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
