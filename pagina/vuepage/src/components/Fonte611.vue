<template>
    <div id="pai">
        <table>
            <tr>
                <td colspan="2">
                    P600
                </td>

                <td colspan="2">
                    {{p600}}
                </td>

            </tr>
            <tr>
                <td colspan="2">
                    15V
                </td>

                <td colspan="2">
                    {{v15}}
                </td>

            </tr>
            <tr>
                <td colspan="2">
                    5V
                </td>

                <td colspan="2">
                    {{v5}}
                </td>

            </tr>
            <tr>
                <td colspan="4">

                </td>

            </tr>
            <tr>
                <td colspan="4">

                </td>

            </tr>
            <tr>
                <td>
                    Spp
                </td>
                <td>
                    <div class="ledLinha">
                        <div class="leds" id="l1" v-bind:class="{ ligado: led1 }"></div>
                        <div class="leds" id="l2" v-bind:class="{ ligado: led2 }"></div>
                    </div>
                </td>
                <td>
                    5V
                </td>
                <td>
                    FAULT
                </td>
            </tr>
            <tr>
                <td>
                    Ext
                </td>
                <td>
                    <div class="ledLinha">
                        <div class="leds" id="l3" v-bind:class="{ ligado: led3 }"></div>
                        <div class="leds" id="l4" v-bind:class="{ ligado: led4 }"></div>
                    </div>
                </td>
                <td>
                    Unit
                </td>
                <td>
                    ENABLE
                </td>
            </tr>
            <tr>
                <td>
                    FF
                </td>
                <td>
                    <div class="ledLinha">
                        <div class="leds" id="l5" v-bind:class="{ ligado: led5 }"></div>
                        <div class="leds" id="l6" v-bind:class="{ ligado: led6 }"></div>
                    </div>
                </td>
                <td>
                    Uzk
                </td>
                <td>
                    FAULT
                </td>
            </tr>
        </table>
    </div>
</template>

<script>
    export default {
        name: "Fonte2",
        props: {
            led1: {type: Boolean, default: false},
            led2: {type: Boolean, default: false},
            led3: {type: Boolean, default: false},
            led4: {type: Boolean, default: false},
            led5: {type: Boolean, default: false},
            led6: {type: Boolean, default: false},
            p600: {type: String, default: '600V'},
            v15: {type: String, default: '15V'},
            v5: {type: String, default: '5V'},
        },

    }
</script>

<style scoped>
    #pai {
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        font-size: large;
        font-weight: lighter;
        background-color: azure;
        width: fit-content;
    }

    .ledLinha {
        display: flex;

    }

    .leds {
        width: 30px;
        height: 30px;
        border-radius: 15px;
        opacity: .1;
        transition: 200ms opacity;
        margin: 3px;
    }

    td {
        border: 1px solid antiquewhite;
        padding: 3px;
    }

    #l1 {
        background-color: red;
    }

    #l2 {
        background-color: red;
    }

    #l3 {
        background-color: yellow;
    }

    #l4 {
        background-color: green;
    }

    #l5 {
        background-color: red;
    }

    #l6 {
        background-color: red;
    }

    .ligado {
        opacity: 1;
        transition: 200ms opacity;
    }
</style>
