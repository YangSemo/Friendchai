<template>
    <div>
        <!-- Header 크기 - Footer크기 -->
        <b-container fluid>
            <b-row style="height: 5vh;"></b-row>
        </b-container>
        
        <b-container fluid>
            <b-row align-h="center" align-v="center" id="contain">
                <b-col cols="4" class="content" @click="theme">
                    <img class="img" src="@/assets/theme.png" fluid><br>
                    <p class="choice">테마</p>
                    <h5>당신을 위해 준비해뒀어요</h5>
                </b-col>

                <b-col cols="4" class="content" @click="userset">
                    <img class="img" src="@/assets/userset.png" fluid><br>
                    <p class="choice">사용자설정</p>
                    <h5>당신에게 맞춰줄게요</h5>
                </b-col>
            </b-row>

        </b-container>
    </div>
</template>

<script>
export default {
    name: "Choice",
    data(){
        return{
            
        }
    },
    methods: {
        theme(){
            this.$router.push({
                name: 'Theme'
            })
        },
        userset(){
            this.$router.push({
                name: 'UserSet'
            })
        }
    }
}
</script>

<style>
.title{
    font-size: 50px;
}
.choice{
    font-size: 4vh;
    font-weight: bold;
}
.img{  
    height: 25vh;
    cursor: pointer;
    margin-bottom: 15px;
}
#contain{
    height: 80vh;
}
</style>