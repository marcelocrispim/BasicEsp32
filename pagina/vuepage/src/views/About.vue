<template>
    <div class="about">
        <Fonte611 :led1="l1"
                  :led2="l2"
                  :led3="l3"
                  :led4="l4"
                  :led5="l5"
                  :led6="l6"/>

    </div>
</template>
<script>

    import Fonte611 from "../components/Fonte611"
    import {mapState} from 'vuex'

    export default {
        name: 'About',
        components: {
            Fonte611

        },
        data() {
            return {}

        },
        computed: {
            ...mapState({
                l1: state => state.l1,
                l2: state => state.l2,
                l3: state => state.l3,
                l4: state => state.l4,
                l5: state => state.l5,
                l6: state => state.l6
            })
        },
        methods: {},
        mounted() {

        }

    }

</script>
<style>

</style>
