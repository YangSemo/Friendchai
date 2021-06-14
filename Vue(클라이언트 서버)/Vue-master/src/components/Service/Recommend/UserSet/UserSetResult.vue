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
            p1: '',
            p2: '',
            p3: '',
            p4: '',
            p5: '',
            p6: '',
            items:[
                {title: '전체', name:'allResult', src:'all.png'},
                {title: '한식', name:'koreanResult', src:'korean.png'},
                {title: '중/일식', name:'chijapResult',src:'chijap.png'},
                {title: '카페', name:'cafeResult',src:'cafe.png'},
                {title: '제과제빵', name:'breadResult',src:'bread.png'},
                {title: '분식', name:'kimbobResult',src:'kimbob.png'},
                {title: '치킨', name:'chickenResult',src:'chicken.png'},
                {title: '주점', name:'hofResult',src:'hof.png'},
                {title: '패스트푸드', name:'fastfoodResult',src:'fastfood.png'},
                {title: '기타 외식', name:'etcResult',src:'etc.png'},
                {title: '기타 외국식', name:'etcfResult',src:'etcf.png'},
            ]
        }
    },
    methods:{
        type(param){
            this.$router.push({
                name: param.name,
                query: {
                    sector: param.title,
                    p1: this.p1,
                    p2: this.p2,
                    p3: this.p3,
                    p4: this.p4,
                    p5: this.p5,
                    p6: this.p6,
                }
            })
        }
    },
    created() {
        this.p1= this.$route.query.p1
        this.p2= this.$route.query.p2
        this.p3= this.$route.query.p3
        this.p4= this.$route.query.p4
        this.p5= this.$route.query.p5
        this.p6= this.$route.query.p6
        
    },
    
    
}
</script>

<style>
#a{
    height: 100%;
    width: 100%;
}
.result{
    margin-top: 0px;
    height: 100%;
}
</style>