<template>
    <div class="home">
        <img :src=img[n] width="400">
    </div>
</template>

<script>

    export default {
        name: 'Home',
        data() {
            return {
                img: ['/static/img/ledy1_m.jpg', '/static/img/ledy2_m.jpg', '/static/img/ledy_m.jpg'],
                n: 1
            }
        },
        methods: {},
        created() {
            setInterval(() => {
                this.n = this.n + 1
                if (this.n > 2) {
                    this.n = 0
                }
            }, 1500)
        }
    }
</script>
