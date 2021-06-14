<template>
    <div>
        <b-container fluid>
            <b-row align-h="start" align-v="center" class="footer">
                <b-col cols="4" class="text-white">
                    양세모팀 AI기반 맞춤형 프랜차이즈 탐색 서비스
                </b-col>
                <b-col cols="1" class="text-white">
                    <b-row align-h="start" style="text-align: left">
                        <b-col>
                            서버, AI
                        </b-col>                        
                    </b-row>
                    <b-row align-h="start" style="text-align: left">
                        <b-col>
                            양세모
                        </b-col>                        
                    </b-row>
                </b-col>
                <b-col cols="1" class="text-white">
                    <b-row align-h="start" style="text-align: left">
                        <b-col>
                            백엔드
                        </b-col>                        
                    </b-row>
                    <b-row align-h="start" style="text-align: left">
                        <b-col>
                            조병민
                        </b-col>                        
                    </b-row>
                </b-col>
                <b-col cols="2" class="text-white">
                    <b-row align-h="start" style="text-align: left">
                        <b-col>
                            프론트엔드
                        </b-col>                        
                    </b-row>
                    <b-row align-h="start" style="text-align: left">
                        <b-col>
                            박상현, 원재민
                        </b-col>                        
                    </b-row>
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>
export default {
    name: 'Footer',
    data(){
        return {
            
        }
    }
}
</script>

<style>
.footer{
    height: 10vh;
    background-color: #464545;
}
.text-white{
    color: #E2DFD8;
}
</style>