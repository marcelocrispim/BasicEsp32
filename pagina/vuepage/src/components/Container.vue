<template>
    <div class="bodyContainer">
        <div>
            <h4 class="tituloContainer">{{titulo}}</h4>
        </div>
        <div class="corpoContainer">
            <Fonte611 :led1="true"
            />
        </div>
    </div>
</template>

<script>
    import Fonte611 from "./Fonte611";

    export default {
        name: "Container",
        components: {
            Fonte611
        },
        props: {
            titulo: {type: String, default: 'Estação X'},

        }
    }
</script>

<style scoped>
    .bodyContainer {
        box-shadow: 5px 5px 5px #888888;
        margin: 10px;
        border-radius: 15px;
        height: 95vh;
        width: 18vw;
        border: solid 1px black;
        background-color: grey;

    }

    .tituloContainer {
        text-align: center;
        height: 3vh;
        width: 18vw;
        font-weight: lighter;
        font-size: large;
        font-family: 'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }

    .corpoContainer {
        background-color: darkgrey;
        z-index: 10;
        height: 78vh;
        width: 18vw;
    }
</style>
