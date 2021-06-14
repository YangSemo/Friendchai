<template>
    <div>
        <!-- Header 크기 - Footer크기 -->
        <b-container v-if="!overlayShow" fluid>
            <b-row style="height: 90px;"></b-row>
        </b-container>

        <!-- 검색창 -->
        <b-container v-if="!overlayShow" style="margin-bottom: 2vh;">
            <b-row>
                <b-col>
                    <a style="font-size: 50px; font-weight: bold;">BrandList</a><br>
                </b-col>
            </b-row>
            <b-input-group>
                <b-input type="text" v-model="search" style="border-radius: 20px 0 0 20px;"></b-input>
                <b-button style=" border-radius: 0 20px 20px 0;" @click="searchbrand"><img src="@/assets/search.png" style="height: 14px;"></b-button>
            </b-input-group>
        </b-container>

        <!-- 카테고리 -->
        <b-container fluid>
            <b-row align-h="center" v-if="!overlayShow">
                <b-col md="auto" style="cursor: pointer;" @click="changeSelected(item.value)" v-for="item in titles" :key="item.sector">
                    <img class="category" :src="require(`@/assets/${item.src}`)">
                    <a> {{item.title}}</a>
                </b-col>
            </b-row>
        </b-container>

        <b-container v-if="selected == 'all'" fluid style="height: 83vh;">
            <b-row v-for="i in 5" :key="i" align-h="center">
                <b-col cols="auto" @click="detail(item.brand_name)" class="wrapper" v-for="item in sliceitems(items(brands), i)" :key="item.brand_name">
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
                        :total-rows="rows(brands)"
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

        <b-container v-if="selected == 'korean'" fluid style="height: 83vh;">
            <b-row v-for="i in 5" :key="i" align-h="center">
                <b-col cols="auto" @click="detail(item.brand_name)" class="wrapper" v-for="item in sliceitems(items(korean), i)" :key="item.brand_name">
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
                        :total-rows="rows(korean)"
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

        <b-container v-if="selected == 'cafe'" fluid style="height: 83vh;">
            <b-row v-for="i in 5" :key="i" align-h="center">
                <b-col cols="auto" @click="detail(item.brand_name)" class="wrapper" v-for="item in sliceitems(items(cafe), i)" :key="item.brand_name">
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
                        :total-rows="rows(cafe)"
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

        <b-container v-if="selected == 'chicken'" fluid style="height: 83vh;">
            <b-row v-for="i in 5" :key="i" align-h="center">
                <b-col cols="auto" @click="detail(item.brand_name)" class="wrapper" v-for="item in sliceitems(items(chicken), i)" :key="item.brand_name">
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
                        :total-rows="rows(chicken)"
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

        <b-container v-if="selected == 'fastfood'" fluid style="height: 83vh;">
            <b-row v-for="i in 5" :key="i" align-h="center">
                <b-col cols="auto" @click="detail(item.brand_name)" class="wrapper" v-for="item in sliceitems(items(fastfood), i)" :key="item.brand_name">
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
                        :total-rows="rows(fastfood)"
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

        <b-container v-if="selected == 'bread'" fluid style="height: 83vh;">
            <b-row v-for="i in 5" :key="i" align-h="center">
                <b-col cols="auto" @click="detail(item.brand_name)" class="wrapper" v-for="item in sliceitems(items(bread), i)" :key="item.brand_name">
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
                        :total-rows="rows(bread)"
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

        <b-container v-if="selected == 'chijap'" fluid style="height: 83vh;">
            <b-row v-for="i in 5" :key="i" align-h="center">
                <b-col cols="auto" @click="detail(item.brand_name)" class="wrapper" v-for="item in sliceitems(items(chijap), i)" :key="item.brand_name">
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
                        :total-rows="rows(chijap)"
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

        <b-container v-if="selected == 'kimbob'" fluid style="height: 83vh;">
            <b-row v-for="i in 5" :key="i" align-h="center">
                <b-col cols="auto" @click="detail(item.brand_name)" class="wrapper" v-for="item in sliceitems(items(kimbob), i)" :key="item.brand_name">
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
                        :total-rows="rows(kimbob)"
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

        <b-container v-if="selected == 'hof'" fluid style="height: 83vh;">
            <b-row v-for="i in 5" :key="i" align-h="center">
                <b-col cols="auto" @click="detail(item.brand_name)" class="wrapper" v-for="item in sliceitems(items(hof), i)" :key="item.brand_name">
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
                        :total-rows="rows(hof)"
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

        <b-container v-if="selected == 'etc'" fluid style="height: 83vh;">
            <b-row v-for="i in 5" :key="i" align-h="center">
                <b-col cols="auto" @click="detail(item.brand_name)" class="wrapper" v-for="item in sliceitems(items(etc), i)" :key="item.brand_name">
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
                        :total-rows="rows(etc)"
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

        <b-container v-if="selected == 'etc_f'" fluid style="height: 83vh;">
            <b-row v-for="i in 5" :key="i" align-h="center">
                <b-col cols="auto" @click="detail(item.brand_name)" class="wrapper" v-for="item in sliceitems(items(etc_f), i)" :key="item.brand_name">
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
                        :total-rows="rows(etc_f)"
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
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data(){
        return {
            search: '',
            perRow: 4,
            selected: null,
            brands: null,
            korean: null,
            cafe: null,
            chicken: null,
            fastfood: null,
            chijap: null,
            kimbob: null,
            hof: null,
            etc: null,
            etc_f: null,
            bread: null,
            perPage: 20,
            currentPage: 1,
            overlayShow: true,
            titles: [
                { title: '전체', value: 'all', src: 'all.png'},
                { title: '한식', value: 'korean', src: 'korean.png'},
                { title: '카페', value: 'cafe', src: 'cafe.png'},
                { title: '치킨', value: 'chicken', src: 'chicken.png'},
                { title: '패스트푸드', value: 'fastfood', src: 'fastfood.png'},
                { title: '제과제빵', value: 'bread', src: 'bread.png'},
                { title: '중/일식', value: 'chijap', src: 'chijap.png'},
                { title: '분식', value: 'kimbob', src: 'kimbob.png'},
                { title: '주점', value: 'hof', src: 'hof.png'},
                { title: '기타외식', value: 'etc', src: 'etc.png'},
                { title: '기타외국식', value: 'etc_f', src: 'etcf.png'},                
            ]
            
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
        }
    },
    methods: {
        detail(name){
            this.$router.push({
                name: 'BrandDetail',
                query: {name: name},
            })
        },
        changeSelected(sector){
            this.currentPage = 1
            this.selected = sector
        },
        searchbrand(){
            this.$router.push({
                name: 'BrandSearch',
                query: {searchparam: this.search},
            })
        },
        toPrettyString(int_param){
            return String(int_param).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
        },
    },
    created() {
        axios.get('http://34.64.236.155:8000/myapp/brand').then((res)=>{
            this.brands = res.data;
            this.korean = this.brands.filter(item => item.sector ==="한식");
            this.bread = this.brands.filter(item => item.sector === "제과제빵");
            this.cafe = this.brands.filter(item => item.sector === "카페");
            this.chicken = this.brands.filter(item => item.sector === "치킨");
            this.fastfood = this.brands.filter(item => item.sector === "패스트푸드");
            this.chijap = this.brands.filter(item => item.sector === "중/일식");
            this.kimbob = this.brands.filter(item => item.sector === "분식");
            this.hof = this.brands.filter(item => item.sector === "주점");
            this.etc = this.brands.filter(item => item.sector === "기타 외식");
            this.etc_f = this.brands.filter(item => item.sector === "기타 외국식");
            console.log(this.brands)
            this.overlayShow = false
            this.brands.pop()
            if(this.$route.query.sector != null){
                this.changeSelected(this.$route.query.sector)
            }else{
                this.selected = 'all'
            }
                       
        });    
    },
}
</script>

<style>
.category{
    height: 2vh;
}
.brandCard{
    width: 20vw;
    height: 13vh;
    display: table-cell;
    vertical-align: middle;
    background-color: #E2DFD8;
    border-radius: 15px;
    cursor: pointer;
}
.wrapper{
    display: table; 
    margin-top: 2vh;
}


</style>