<template>
    <div class="corpoDisplayField">
        <div class="linhaUp linha">
            <div class="fieldMaster">600V</div>
        </div>
        <div class="linhaDown linha">
            <div class="fieldSon">596Vmin</div>
            <div class="fieldSon">602Vmax</div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "DisplayField"
    }
</script>

<style scoped>
    .corpoDisplayField {
        margin: 1vh 0.8vw;

    }

    .linha {
        height: 2.5vh;
    }

    .linhaDown {
        display: flex;
    }

    .fieldMaster {
        margin: 0vh 4vw;
    }

    .fieldSon {
        margin: 0vh 0vw;
        width: 8.5vw;
        height: 5vh;
    }
</style>