<template>
    <div>
        사용자 우선순위 설정<br>
        <div class="select">           
            <b-form-select v-model="data_list[0].data1" :options="options"></b-form-select>
            <br><span>선택함: {{data_list[0].data1}}</span>
            <br><br>
            <b-form-select v-model="data2" :options="options"></b-form-select>
            <br><span>선택함: {{data2}}</span>
            <br><br>
            <b-form-select v-model="data3" :options="options"></b-form-select>
            <br><span>선택함: {{data3}}</span>
            <br><br>
            <b-form-select v-model="data4" :options="options"></b-form-select>
            <br><span>선택함: {{data4}}</span>
            <br><br>
            <b-form-select v-model="data5" :options="options"></b-form-select>
            <br><span>선택함: {{data5}}</span>
            <br><br>
            <b-form-select v-model="data6" :options="options"></b-form-select>
            <br><span>선택함: {{data6}}</span>
            <br><br>
            {{data_list[0].data1}}의 값{{data_list[0].weight}}

            <b-button @click="result" variant="primary">결과</b-button>
        </div>
    </div>
</template>

<script>
export default {
    name: "UserSet",
    data(){
        return{
            data_list: [
                {data1: '', weight: '0.9'},
                {data2: '', weight: '0.7'},
                {data3: '', weight: '0.5'},
                {data4: '', weight: '0.3'},
                {data5: '', weight: '0.2'},
                {data6: '', weight: '0.1'},
            ],
            options: [
                {
                    value: 'p1', text: '가맹사업 개월수'
                },
                {
                    value: 'p2', text: '가맹점 수'
                },
                {
                    value: 'p3', text: '가맹점 평균 매출액'
                },
                {
                    value: 'p4', text: '창업비용'
                },
                {
                    value: 'p5', text: '개점률'
                },
                {
                    value: 'p6', text: '폐점률'
                },
            ]
        }  
    },
    methods: {
        result(){
            this.$router.push({
                name: 'UserSetResult',
                params: {data: this.data_list}
            })
        },
    },
    computed: {
        
    }
}
</script>

<style>
.select{
    width: 10%;
    margin-left: auto;
    margin-right: auto;
}
</style>