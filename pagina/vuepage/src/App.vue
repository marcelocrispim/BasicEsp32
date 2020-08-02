<template>
    <div id="app">
        <container titulo="Estação 1" cor="bordaVerde"/>
        <container titulo="Estação 2"/>
        <container titulo="Estação 3" cor="bordaVerde"/>
        <container titulo="Estação 4"/>
        <container titulo="Estação 5" cor="bordaVermelha"/>
    </div>
</template>
<script>
    import Container from "./components/Container";


    export default {
        name: 'About',
        components: {
            Container

        },
    }
</script>
<style lang="scss">
    #app {
        background-color: gainsboro;
        display: flex;
        margin: 0;
    }
</style>
