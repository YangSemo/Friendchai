<template>
    <div>
        <b-container fluid>
            <b-container id='alert_empty'>
            </b-container>
            
            <b-row align-h="center" align-v="start" style="height: 80vh;">
                <b-col cols="4" style="padding-top: 4vh">
                    <a style="overflow: auto;">
                        <b-container class="Top10" v-for="item in brands" :key="item.brand_name" @click="detail(item.brand_name)">
                            <span class="resultCardTitle">{{item.brand_name}}&nbsp;</span><span class="resultCardText">{{item.sector}}</span><br>
                            <span class="resultCardText">평균매출액 </span>{{toPrettyString(item.average_sales)}}&nbsp;<span class="resultCardText">창업비용 </span>{{toPrettyString(item.startup_cost)}}
                        </b-container>
                    </a>
                </b-col>
                <b-col cols="8" style="padding-top: 5vh;">
                    <!-- 기본 표 -->
                    <b-container v-if="!openWindow" fluid>
                        <b-table :items='this.brand_list'></b-table>
                    </b-container>

                    <!-- 상세보기창 -->
                    <b-container v-if="openWindow" fluid>
                        <div style="overflow: auto; max-height: 70vh;">
                            <router-view style="background-color: #E2DFD8"/>
                        </div>
                    </b-container>
                </b-col>
            </b-row>
        </b-container>

        <!-- 여백 -->
        <b-container fluid>
            <b-row style="height: 10vh;"></b-row>
        </b-container>
    </div>
    
</template>

<script>
import axios from 'axios'

export default {
    data(){
        return{
            openWindow: '',
            overlayShow: true,
            brand_list: null,
            brands: null,           
        }
    },
    created() {
        let p1 = this.$route.query.p1
        let p2 = this.$route.query.p2
        let p3 = this.$route.query.p3
        let p4 = this.$route.query.p4
        let p5 = this.$route.query.p5
        let p6 = this.$route.query.p6
        let sector = this.$route.query.sector
        axios.get('http://34.64.236.155:8000/myapp/customtheme/?p1='+ p1 + '&p2=' + p2 + '&p3=' + p3 + '&p4=' + p4 + '&p5=' + p5 + '&p6=' + p6 + '&sector=' + sector).then((res) =>{
            var weight = [0.9, 0.7, 0.5, 0.3, 0.2, 0.1]
            console.log(res.data);

            if(res.data.length < 1){
                console.log(res.data);
                var subject = document.getElementById('alert_empty');
                subject.innerHTML = '<br><br><strong>데이터가 없습니다.</strong>';
                return ;
            }

            for(var i = 0; i<res.data.length; i++){
                res.data[i].total_ratio = res.data[i].franchise_months_ratio * weight[p1] + res.data[i].num_of_franchise_ratio * weight[p2] + res.data[i].average_sales_ratio * weight[p3] +
                res.data[i].startup_cost_ratio * weight[p4] + res.data[i].rate_of_opening_ratio * weight[p5] + res.data[i].rate_of_closing_ratio * weight[p6]

                console.log(res.data[i].total_ratio)
            }
            this.brands = res.data;

            this.brands.sort(function(a, b){
                return b.total_ratio - a.total_ratio
            })

            this.brand_list = []
            for(i = 0; i<res.data.length; i++){
                this.brand_list.push(
                    {
                        '순위': i+1,
                        '브랜드 이름': this.brands[i].brand_name, '가맹점수': this.brands[i].num_of_franchise, '가맹 개월수': this.brands[i].franchise_months, '연평균매출액(단위: 천원)': this.toPrettyString(this.brands[i].average_sales),
                        '창업비용(단위: 천원)': this.toPrettyString(this.brands[i].startup_cost), '개점률(%)': this.brands[i].rate_of_opening, '폐점률(%)': this.brands[i].rate_of_closing
                    }
                );
            }

            console.log(this.brands)
            for( i = 0; i < this.brands.length; i ++){
                console.log(this.brands[i].total_ratio)
            }
        })
    },
    methods:{
        detail(brandName){
            if(this.openWindow == brandName){
                this.openWindow = ''
                console.log(this.openWindow)
            }else if(this.openWindow == null){
                this.openWindow = brandName
                console.log(this.openWindow)
            }else{
                this.openWindow = brandName
                console.log(this.openWindow)
                this.$router.push({
                    name: '5',
                    query: {name: brandName}
                })
            }
        },
        toPrettyString(int_param){
            return String(int_param).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
        },
    }
}
</script>

<style>
.Top10{
    background-color: #E9DDC8;
    width: 90%;
    height: 7vh;
    margin-top: 0.5vh;
    border-radius: 20px;
    padding-top: 10px;
    text-align: left;
    cursor: pointer;
}
.resultCardTitle{
    font-size: 2vh;
    font-weight: bold;
    text-align: left;
}
.resultCardText{
    font-size: 1.5vh;
    font-weight: bold;
}
</style>