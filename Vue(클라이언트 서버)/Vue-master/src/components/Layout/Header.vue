<template>
    <div>
        <Login></Login>
        <Register></Register>

        <b-container class="header" fluid>
            <b-row align-h="end">
                <b-col id="brandTitle" cols="4" @click="goHome" class="pointer"><strong>프랜드차이</strong></b-col>
                <b-col id="header-right" cols="4" v-if="!this.isLogin" style="text-align: right">&nbsp;<span @click="$bvModal.show('register')" class="pointer">회원가입</span>&nbsp;<span @click="$bvModal.show('login')" class="pointer">로그인</span></b-col>
                <b-col id="header-right" cols="4" v-if="this.isLogin" style="text-align: right;">{{ name }} 님 <span @click="logout()" class="pointer" style="font-weight: bold;">로그아웃</span></b-col>
                <div class="w-100"></div>
            </b-row>
            <b-row v-if="this.isLogin" align-h="center">
                <b-col :class="['select', isSelected === 'brand' ? 'select2' : '']" cols="2"><a @click="goBrand">브랜드</a></b-col>
                <b-col :class="['select', isSelected == 'recommend' ? 'select2' : '']" cols="2"><a @click="goRecommend">추천</a></b-col>
                <b-col :class="['select', isSelected == 'map' ? 'select2' : '']" cols="2"><a @click="goMap">지도</a></b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>
import Login from '@/components/User/Login'
import Register from '@/components/User/Register'
import { mapState, mapMutations } from 'vuex'

export default {
    name: 'Header',
    data(){
        return {
            show: false,
            isSelected: '',
        }
    },
    computed:{
        ...mapState(['name', 'isLogin'])
    },
    methods: {
        ...mapMutations(['logout']),
        goHome(){
            this.isSelected = ''
            this.$router.push('/').catch(()=>{})
        },
        // goRegister(){
        //     this.isSelected = '',
        //     this.$router.push('/user/register').catch(()=>{})
        // },
        goBrand(){
            this.isSelected = 'brand'
            this.$router.push({name: 'BrandList'}).catch(()=>{})
        },
        goRecommend(){
            this.isSelected = 'recommend'
            this.$router.push({name: 'Choice'}).catch(()=>{})
        },
        goMap(){
            this.isSelected = 'map'
            this.$router.push({name: 'Map'}).catch(()=>{})
        }
    },
    components: {
        Login,
        Register,

    }
}
</script>

<style>
.pointer{
    cursor: pointer;
}
#header-right{
    text-align: right;
}
#brandTitle{
    font-size: 35px;
    padding-bottom: 10px;
}
.header{
    padding-top: 10px;
    position: fixed;
    background: #EDECEA;
    z-index: 2;
}
.select{
    margin-top: 8px;
    margin-bottom: 8px;
    padding-top: 2px;
    padding-bottom: 2px;
    font-size: 22px;
    font-weight: bold;
    cursor: pointer;
    border-radius: 40px;
    /* background-color: white;     */
}
.select2{
    background-color: #C6DFD6; 
}
</style>