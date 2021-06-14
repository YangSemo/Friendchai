<template>
    <div>
        <!-- Header 크기 - Footer크기 -->
        <b-container fluid>
            <b-row style="height: 80px;"></b-row>
        </b-container>

        <!--오버레이 표시-->
        <b-overlay
            :show="overlayShow"
            rounded="sm"
            z-index="0"
            variant="tranfparent"
            opacity="0"
        >
            <b-container fluid v-if="overlayShow" style="min-height: 100vh; background-color: #EDECEA">
            </b-container>
        </b-overlay>

        <b-container fluid v-if="!overlayShow">
            <b-row>
                <b-col>
                    <a style="font-size: 50px; font-weight: bold;">BrandSearch</a><br>
                    <a style="font-size: 20px;">'{{this.$route.query.searchparam}}'에 대한 검색결과</a>
                </b-col>
            </b-row>
        </b-container>

        <b-container v-if="!overlayShow" fluid style="height: 83vh;">
            <b-row v-for="i in 5" :key="i" align-h="center">
                <b-col cols="auto" @click="detail(item.brand_name)" class="wrapper" v-for="item in sliceitems(items(result), i)" :key="item.brand_name">
                    <b-container class="brandCard">
                        <b-row>
                            <b-col style="font-size: 2vh; font-weight: bold;" cols="auto">
                                {{item.brand_name}}
                            </b-col>
                        </b-row>
                        <b-row>
                            <b-col cols="auto" style="font-size: 1.5vh;">
                                {{item.sector}}
                            </b-col>
                        </b-row>
                        <b-row style="font-size: 1.5vh;">
                            <b-col cols="auto">
                                평균 매출액: {{toPrettyString(item.average_sales)}}
                            </b-col>
                            <b-col cols="auto">
                                창업비용: {{toPrettyString(item.startup_cost)}}
                            </b-col>
                        </b-row>
                    </b-container>
                </b-col>
            </b-row>
            <b-row align-h="end">
                <b-col cols="auto">
                    <b-pagination
                        class="pagination"
                        align="center"
                        v-model="currentPage"
                        :total-rows="rows(result)"
                        :per-page="perPage"
                        first-number
                        last-number>
                    </b-pagination>
                </b-col>
                <b-col cols="4" style="text-align: right; color: #D07D7B; margin-right: 8vw; margin-top: 1vh">
                    * 단위: 천원
                </b-col>
            </b-row>
        </b-container>

        
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Search',    
    data(){
        return {
            overlayShow: true,
            result: null,
            currentPage: 1,
            perPage: 20,
            perRow: 4,
        }
    },
    computed:{
        rows(){
            return (sector) =>{
                return sector.length
            }
        },
        items(){
            return (sector) =>{
                const items = sector
                return items.slice(
                    (this.currentPage -1) * this.perPage,
                    this.currentPage * this.perPage
                )
            }
        },
        sliceitems(){
            return (items, index) =>{
                const list = items
                return list.slice(
                    (index-1) * this.perRow,
                    index * this.perRow
                )
            }
        },     
    },
    created(){
        var url = 'http://34.64.236.155:8000/myapp/brand/?name=';
        axios.get(url + this.$route.query.searchparam).then((res)=>{
             this.result = res.data
             console.log(this.result)
        });
        this.overlayShow = false
    },
    methods:{
        detail(name){
            this.$router.push({
                name: 'BrandDetail',
                query: {name: name},
            })
        },
        toPrettyString(int_param){
            return String(int_param).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
        },
    },
    
}
</script>

<style>
.brandCard{
    width: 20vw;
    height: 13vh;
    display: table-cell;
    vertical-align: middle;
    background-color: #E2DFD8;
    border-radius: 15px;
}
.wrapper{
    display: table; 
    margin-top: 2vh;
}
.pagination{
    margin-top: 2vh;
}
</style>