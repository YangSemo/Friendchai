<template>
    <div>
        <!-- Header 크기 - Footer크기 -->
        <b-container fluid>
            <b-row style="height: 150px;"></b-row>
        </b-container>

        <b-container>
            <b-row>
                <b-col>
                    <a style="font-size: 50px; font-weight: bold;">Result</a>
                </b-col>
            </b-row>
        </b-container>

        <b-container fluid style="margin-top: 8vh">
            <b-row align-h="center">
                <b-col md="auto" style="cursor: pointer;" @click="type(item)" v-for="item in items" :key="item">
                    <img class="category" :src="require(`@/assets/${item.src}`)">
                    <a> {{item.title}}</a>
                </b-col>
            </b-row>
        </b-container>

        <router-view></router-view>
    </div>

</template>
<script>
export default {
    data() {
        return {
            label: '',
            items:[
                {title: '전체', name:'AllResult', src:'all.png'},
                {title: '한식', name:'KoreanResult', src:'korean.png'},
                {title: '중/일식', name:'ChijapResult',src:'chijap.png'},
                {title: '카페', name:'CafeResult',src:'cafe.png'},
                {title: '제과제빵', name:'BreadResult',src:'bread.png'},
                {title: '분식', name:'KimbobResult',src:'kimbob.png'},
                {title: '치킨', name:'ChickenResult',src:'chicken.png'},
                {title: '주점', name:'HofResult',src:'hof.png'},
                {title: '패스트푸드', name:'FastfoodResult',src:'fastfood.png'},
                {title: '기타 외식', name:'EtcResult',src:'etc.png'},
                {title: '기타 외국식', name:'EtcfResult',src:'etcf.png'},
            ]
        }
    },
    methods:{
        type(param){
            this.$router.push({
                name: param.name,
                query: {
                    sector: param.title,
                    label: this.label,
                }
            })
        },
    },
    created() {
        this.label = this.$route.query.label
    },
}
</script>

<style>

</style>