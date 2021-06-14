<template>
    <div>
        <!-- Header 크기 - Footer크기 -->
        <b-container fluid>
            <b-row style="height: 15vh;"></b-row>
        </b-container>

        <b-container fluid>
            <b-row style="padding-bottom: 5vh;" align-h="center">
                <b-col cols="3">
                    <a style="font-size: 50px; font-weight: bold;">UserSet</a><br>
                    <a style="font-size: 20px;">우선순위를 정해보세요</a>
                </b-col>
            </b-row>
            <b-row align-h="center" align-v="center" style="padding-bottom: 3vh;">
                <b-col cols="3">
                    <b-card class="condition" >
                        <b-card-text>가맹사업 개월수</b-card-text>
                        <b-select v-model="p[0]" :options="options" @change="onSelectChanged(0)"></b-select>
                    </b-card>
                </b-col>
                <b-col cols="3">
                    <b-card class="condition">
                        <b-card-text>가맹점 수</b-card-text>                       
                        <b-select v-model="p[1]" :options="options" @change="onSelectChanged(1)"></b-select>
                    </b-card>
                </b-col>
                <b-col cols="3">
                    <b-card class="condition">
                        <b-card-text>평균 매출액</b-card-text>
                        <b-select v-model="p[2]" :options="options" @change="onSelectChanged(2)"></b-select>
                    </b-card>
                </b-col>
            </b-row>
            <b-row align-v="center" align-h="center" style="padding-bottom: 3vh;">
                <b-col cols="3">
                    <b-card class="condition">
                        <b-card-text>창업비용</b-card-text>
                        <b-select v-model="p[3]" :options="options" @change="onSelectChanged(3)"></b-select>
                    </b-card>
                </b-col>
                <b-col cols="3">
                    <b-card class="condition">
                        <b-card-text>개점률</b-card-text>
                        <b-select v-model="p[4]" :options="options" @change="onSelectChanged(4)"></b-select>
                    </b-card>
                </b-col>
                <b-col cols="3">
                    <b-card class="condition">
                        <b-card-text>폐점률</b-card-text>
                        <b-select v-model="p[5]" :options="options" @change="onSelectChanged(5)"></b-select>
                    </b-card>
                </b-col>
            </b-row>
            <b-row align-h="end">
                <b-col cols="4">
                    <b-button @click="result">
                        결과확인
                    </b-button>
                </b-col>
                <b-col cols="4">
                    <a style="color: rgb(226, 65, 65);">* 중복설정 불가</a>
                </b-col>
            </b-row>
        </b-container>

        <!--화면 맞춤용-->
        <b-container fluid>
            <b-row style="height: 10.8vh;"></b-row>
        </b-container>
    </div>
</template>

<script>
export default {
    name: "UserSet",
    data(){
        return{
            p:[],
            options: [
                {
                    value: 0, text: '1순위'
                },
                {
                    value: 1, text: '2순위'
                },
                {
                    value: 2, text: '3순위'
                },
                {
                    value: 3, text: '4순위'
                },
                {
                    value: 4, text: '5순위'
                },
                {
                    value: 5, text: '6순위'
                },
            ],
            changed:[],
        }  
    },
    methods: {
        onSelectChanged(){
            console.log(this.p);
            for(var i = 0; i < this.p.length; i++){
                for(var j = 0; j < this.p.length; j++){
                    if(i == j){
                        continue;
                    }
                    if(this.p[i] == this.p[j]){
                        alert("해당 요소는 이미 선택했습니다.");
                        return;
                    }
                }
            }
        },
        result(){
            // var condition = [0, 1, 2, 3, 4, 5]
            // var cond = []
            // for(var i = 0; i < 6; i++){
            //     cond[i] = this.p[i]
            // }
            // cond.sort()
            // for(i = 0; i < 6; i++){
            //     if(cond[i] != condition[i]){
            //         alert('중복된 값이 있습니다')
            //         return;
            //     }
            // }

            this.$router.push({
                path: '/service/recommend/userset/result/all',
                query: {
                    p1: this.p[0],
                    p2: this.p[1],
                    p3: this.p[2],
                    p4: this.p[3],
                    p5: this.p[4],
                    p6: this.p[5],
                }
            })
            
        },
    },
}
</script>

<style>
.condition{
    height: 100%;
    width: 100%;
    border-radius: 15px;
    font-size: 2.5vh;
    font-weight: bold;
    padding: 1.5vh;
}
</style>