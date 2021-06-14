<template>
    <div>
        <b-container v-if="!overlayShow" fluid>
            <!-- 여백 -->
            <b-container fluid>
                <b-row style="height: 100px;"></b-row>
            </b-container>
            <b-row align-h="center" class="detailTitle">
                <b-col cols="auto">
                    <a>{{this.br_detail[0].brand_name}}</a>
                </b-col>
            </b-row>

            <b-row class="detailSelect" align-h="around">
                <b-col cols="auto" @click="changeSelect('hq')" :class="[isSelected == 'hq' ? 'select2' : '']" style="border-radius: 20px">
                    본사 정보
                </b-col>
                <b-col cols="auto" @click="changeSelect('br')" :class="[isSelected == 'br' ? 'select2' : '']" style="border-radius: 20px">
                    브랜드 정보
                </b-col>
            </b-row>
            <hr>
                
            <b-container fluid class="detailBody" v-if="isSelected == 'hq'">
                <div>
                    <span class="tableTitle"><strong>본사 기본 정보</strong></span>
                    <b-table :items="this.hq_basic_items"></b-table>
                    <b-table :items="this.hq_basic2_items"></b-table>
                    <br><hr><br>

                    <span class="tableTitle"><strong>본사 매출 정보</strong></span>
                    <b-table :items="this.hq_economic_items"></b-table>
                    <br><hr><br>

                    <span class="tableTitle"><strong>본사 가맹 정보</strong></span>
                    <b-table :items="this.hq_franchise_items"></b-table>
                    <br><hr><br>

                    <span class="tableTitle"><strong>최근 3년간 법 위반 사실</strong></span>
                    <b-table :items="this.hq_law_items"></b-table>
                    <br><hr><br>
                    </div>
                    <div>
                        <p>위 정보는 공정거래위원회에 등록된 가맹사업거래 정보공개서를 분석한 정보입니다. 참고용으로만 활용하시기 바랍니다.</p>
                </div>
            </b-container>
            <b-container fluid v-if="isSelected == 'br'">
                <div>
                    <span class="tableTitle"><strong>브랜드 가맹 정보</strong></span>
                    <b-table :items="br_items_1"></b-table>
                    <b-table :items="br_items_2" ></b-table>
                    <br><hr><br>

                    <span class="tableTitle"><strong>브랜드 매출 정보</strong></span>
                    <b-table :items="br_items_3" ></b-table>
                    <br><hr><br>

                    <span class="tableTitle"><strong>브랜드 기본 비용</strong></span>
                    <b-table :items="br_items_4" ></b-table>
                    <br><hr><br>

                    <span class="tableTitle"><strong>인테리어 비용</strong></span>
                    <b-table :items="br_items_5" ></b-table>
                        
                </div>
            </b-container>
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
            isSelected: 'br',
            overlayShow: true,
            br_detail: null,
            hq: null,
            hq_basic_items: null,
            hq_basic2_items: null,
            hq_economic_items: null,
            hq_franchise_items: null,
            hq_law_items: null,
            // br_fields_1: ['가맹 시작일', '가맹 개월 수(개월)', '가맹점 수(개)', '임직원 수(명)','가맹 종료(개)','가맹 해지(개)'],
            // br_fields_2: ['평균매출액(년/천원)', '평당 평균매출액(년/천원)','가맹비(천원)','교육비(천원)','보증금(천원)','기타비용(천원)','창업비용(천원)','면적당 비용(천원)','기준면적(천원)','전체비용(천원)'],
            br_items_1: [],
            br_items_2: [],
            br_items_3: [],
            br_items_4: [],
            br_items_5: [],
            brands: null,         
        }
    },
    created() {
        console.log(this.$route.query.name)
        axios.get('http://34.64.236.155:8000/myapp/brand/detail/?name=' + this.$route.query.name).then((res) =>{
            this.br_detail=res.data;
            console.log(this.br_detail)
            axios.get('http://34.64.236.155:8000/myapp/headquarter/?mutual=' + res.data[0].mutual).then((res) =>{
                this.hq=res.data[0];
                console.log('본사' + this.hq)
                this.brandGet();
                this.setHQ();
            })
        })
        
    },
    methods: {
        changeSelect(select){    
            this.isSelected = select
            console.log(this.isSelected)
        },
        brandGet(){
            this.br_items_1.push({
                '가맹 시작일': String(this.br_detail[0].franchise_start_date),
                '가맹 개월 수(개월)': String(this.br_detail[0].franchise_months).replace(/\B(?=(\d{3})+(?!\d))/g, ","),
                '가맹점 수(개)': String(this.br_detail[0].num_of_franchise).replace(/\B(?=(\d{3})+(?!\d))/g, ","),
                '임직원 수(명)' : String(this.br_detail[0].num_of_employees).replace(/\B(?=(\d{3})+(?!\d))/g, ","),
            })
            this.br_items_2.push({
                '가맹 시작(개)': String(this.br_detail[0].num_of_open).replace(/\B(?=(\d{3})+(?!\d))/g, ","),
                '가맹 종료(개)': String(this.br_detail[0].num_of_quit).replace(/\B(?=(\d{3})+(?!\d))/g, ","),
                '가맹 해지(개)': String(this.br_detail[0].num_of_cancel).replace(/\B(?=(\d{3})+(?!\d))/g, ",")
            })
            this.br_items_3.push({
                '평균매출액(년/천원)': String(this.br_detail[0].average_sales).replace(/\B(?=(\d{3})+(?!\d))/g, ",") ,
                '평당 평균매출액(년/천원)': String(this.br_detail[0].average_sales_per_area).replace(/\B(?=(\d{3})+(?!\d))/g, ","),                
            })
            this.br_items_4.push({
                '가맹비': String(this.br_detail[0].franchise_fee).replace(/\B(?=(\d{3})+(?!\d))/g, ",") ,
                '교육비': String(this.br_detail[0].education_fee).replace(/\B(?=(\d{3})+(?!\d))/g, ",") ,
                '보증금': String(this.br_detail[0].deposit).replace(/\B(?=(\d{3})+(?!\d))/g, ",") ,
                '기타비용': String(this.br_detail[0].other_cost).replace(/\B(?=(\d{3})+(?!\d))/g, ",") ,
                '합계': String(this.br_detail[0].startup_cost).replace(/\B(?=(\d{3})+(?!\d))/g, ",") ,
            })
            this.br_items_5.push({
                '단위면적(3.3㎡)당 비용': String(this.br_detail[0].cost_per_area).replace(/\B(?=(\d{3})+(?!\d))/g, ",") ,
                '기준면적(㎡)': String(this.br_detail[0].standard_area).replace(/\B(?=(\d{3})+(?!\d))/g, ",") ,
                '전체비용': String(this.br_detail[0].total_cost).replace(/\B(?=(\d{3})+(?!\d))/g, ",")
            })
        },
        toPrettyString(int_param){
            return String(int_param).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
        },
        setHQ(){
            this.hq_basic_items = [
                {
                    '상호': this.hq.mutual, '대표자': this.hq.representative, '법인 설립 등기일': this.hq.register_law_date, '사업자 등록일': this.hq.register_biz_date, '대표 번호': this.hq.representative_number, 
                }
            ]
            this.hq_basic2_items = [
                {
                    '대표 팩스 번호': this.hq.fax_number, '주소': this.hq.address, '사업자 유형': this.hq.biz_type, '법인 등록 번호': this.hq.law_number, '사업자 등록 번호': this.hq.biz_nubmer,
                }
            ]
            this.hq_economic_items = [
                {
                    '연도': '2020년', '자산': this.toPrettyString(this.hq.assets_2020), '부채': this.toPrettyString(this.hq.liabilities_2020), '자본': this.toPrettyString(this.hq.equity_2020), '매출액': this.toPrettyString(this.hq.sales_2020), '영업이익': this.toPrettyString(this.hq.income_2020), '당기순이익': this.toPrettyString(this.hq.net_income_2020)
                }, 
                {
                    '연도': '2019년', '자산': this.toPrettyString(this.hq.assets_2019), '부채': this.toPrettyString(this.hq.liabilities_2019), '자본': this.toPrettyString(this.hq.equity_2019), '매출액': this.toPrettyString(this.hq.sales_2019), '영업이익': this.toPrettyString(this.hq.income_2019), '당기순이익': this.toPrettyString(this.hq.net_income_2019)
                },
                {
                    '연도': '2018년', '자산': this.toPrettyString(this.hq.assets_2018), '부채': this.toPrettyString(this.hq.liabilities_2018), '자본': this.toPrettyString(this.hq.equity_2018), '매출액': this.toPrettyString(this.hq.sales_2018), '영업이익': this.toPrettyString(this.hq.income_2018), '당기순이익': this.toPrettyString(this.hq.net_income_2018)
                },
                {
                    '연도': '2017년', '자산': this.toPrettyString(this.hq.assets_2017), '부채': this.toPrettyString(this.hq.liabilities_2017), '자본': this.toPrettyString(this.hq.equity_2017), '매출액': this.toPrettyString(this.hq.sales_2017), '영업이익': this.toPrettyString(this.hq.income_2017), '당기순이익': this.toPrettyString(this.hq.net_income_2017)
                }
            ]
            this.hq_franchise_items = [
                {
                    '연도': '2020년', '개점': this.toPrettyString(this.hq.opening_2020), '폐점': this.toPrettyString(this.hq.closing_2020), '명의변경': this.toPrettyString(this.hq.name_change_2020),
                },
                {
                    '연도': '2019년', '개점': this.toPrettyString(this.hq.opening_2019), '폐점': this.toPrettyString(this.hq.closing_2019), '명의변경': this.toPrettyString(this.hq.name_change_2019),
                },
                {
                    '연도': '2018년', '개점': this.toPrettyString(this.hq.opening_2018), '폐점': this.toPrettyString(this.hq.closing_2019), '명의변경': this.toPrettyString(this.hq.name_change_2018),
                },
                {
                    '연도': '2017년', '개점': this.toPrettyString(this.hq.opening_2017), '폐점': this.toPrettyString(this.hq.closing_2017), '명의변경': this.toPrettyString(this.hq.name_change_2017),
                }                
            ]
            this.hq_law_items = [
                {
                    '공정거래위원회 시정 조치': this.hq.num_of_correction, '민사소송 패소 및 민사상 화해': this.hq.num_loss_of_law, '형의 선고': this.hq.num_of_sentences
                }
            ]
            this.overlayShow = false
        },
    }
}
</script>

<style>
.detailTitle{
    font-size: 5vh;
    font-weight: bold;
}
.detailSelect{
    font-size: 2vh;
    margin-top: 10vh;
    cursor: pointer;
}
.detailBody{
    font-size: 1.8vh;
    margin-top: 4vh;
}
.tableTitle{
    text-align: left;
    font-size: 2.2vh;
}

</style>