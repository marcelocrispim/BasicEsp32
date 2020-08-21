<template>
    <div class="display">
        <b-icon v-show="icone2" icon="thermometer-half" :class="cor"/>
        <b-icon v-show="icone1" icon="thermometer" :class="cor"/>

        {{valor}}
    </div>
</template>

<script>
    export default {
        name: "DisplayTemp",
        props: {
            valor: {type: String, default: '00:00:00'}
        },
        data() {
            return {
                icone1: true,
                icone2: false
            }
        },
        computed: {
            cor: function () {
                if (this.valor < 31) {
                    this.icone1 = true
                    this.icone2 = false
                    return 'verde'
                } else if (this.valor > 30 & this.valor < 45) {
                    this.icone1 = false
                    this.icone2 = true
                    return 'amarelo'
                } else {
                    this.icone1 = false
                    this.icone2 = true
                    return 'vermelho'
                }
            },

        }
    }
</script>

<style scoped>
    .display {
        font-size: larger;
    }

    .verde {
        color: green;
    }

    .amarelo {
        color: yellow;
    }

    .vermelho {
        color: red;
    }

</style>
