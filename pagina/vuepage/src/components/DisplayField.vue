<template>
    <div class="corpoDisplayField">

        <b-icon icon="gear-wide" animation="spin" font-scale="1" shift-v="0"/>
        {{principal.toLocaleTimeString()}}


    </div>
</template>

<script>
    export default {
        name: "DisplayField",
        props: {
            principal: {type: Date, default: new Date()},

        }
    }
</script>

<style scoped>


    .corpoDisplayField {
        align-self: center;
        font-size: large;
        margin: 1vh 0.8vw;
        padding: 1.5vh 0;
        background-color: #6393f6;
        border-radius: 3px;
    }


</style>
