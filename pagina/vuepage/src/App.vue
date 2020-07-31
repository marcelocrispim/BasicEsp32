<template>
    <div id="app">
        <container titulo="Estação 1"/>
        <container titulo="Estação 2"/>
        <container titulo="Estação 3"/>
        <container titulo="Estação 4"/>
        <container titulo="Estação 5"/>
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
        background-color: aliceblue;
        display: flex;
    }
</style>
