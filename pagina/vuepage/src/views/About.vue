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

    import Fonte611 from "../components/Fonte611";
    import io from 'socket.io-client';

    export default {
        name: 'About',
        components: {
            Fonte611

        },
        data() {
            return {
                l1: false,
                l2: false,
                l3: true,
                l4: false,
                l5: false,
                l6: false,
            }

        },
        methods: {
            update: () => {
                const socket = io('http://127.0.0.1:8000');
                socket.on('connect', () => {
                    console.log('socket io conectado')

                })
                socket.on('disconnect', () => {
                    console.log('socket io desconectado')
                })
                socket.on('event', (res) => {
                    console.log('dado = ', res.data, ' ', typeof res.data)

                    $.data.l3 = res.data
                });

            }
        },
        mounted() {
            this.update()
        }

    }

</script>
<style>

</style>
