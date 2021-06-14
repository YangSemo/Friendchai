<template>
    <div>
        <b-nav pills>
            <b-nav-item v-for="item in items" :key="item" @click="type(item)">{{item.title}}</b-nav-item>
            
        </b-nav>
    </div>

</template>
<script>
export default {
    data() {
        return {
            items:[
                {title: '전체', name:'AllResult'},
                {title: '한식', name:'KoreanResult'},
                {title: '중/일식', name:'ChijapResult'},
                {title: '카페', name:'CafeResult'},
                {title: '분식', name:'KimbobResult'},
                {title: '치킨', name:'ChickenResult'},
                {title: '주점', name:'HofResult'},
                {title: '패스트푸드', name:'FastfoodResult'},
                {title: '기타 외식', name:'EtcResult'},
                {title: '기타 외국식', name:'EtcfResult'},
            ]
        }
    },
    methods:{
        type(param){
            this.$router.push({
                name: param.name,
                params: {sector: param.title}
            })
        }
    }
    
    
}
</script>

<style>

</style>