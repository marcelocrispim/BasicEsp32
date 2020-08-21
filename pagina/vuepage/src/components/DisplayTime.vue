<template>
    <div class="display">
        <b-icon icon="gear-wide" :animation="animation" font-scale="1" shift-v="0"/>
        {{valor}}
    </div>
</template>

<script>
    export default {
        name: "DisplayTime",
        props: {
            valor: {type: String, default: '00:00:00'},
            ligado: {type: Boolean, default: false}
        },
        computed: {
            animation: function () {
                if (this.ligado) {
                    return 'spin'
                } else {
                    return ''
                }
            }
        }
    }
</script>

<style scoped>
    .display {
        font-family: 'Courier New', 'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: larger;
    }
</style>
