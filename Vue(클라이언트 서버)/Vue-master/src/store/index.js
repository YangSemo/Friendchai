import axios from 'axios';
import Vue from 'vue'
import Vuex from 'vuex'
import router from '../../router'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex);

export const store = new Vuex.Store({
    plugins: [createPersistedState()],
    state: {
        name: "",
        isLogin: false,
    },
    mutations:{
        loginSuccess(state, payload){  //로그인 성공
            console.log(payload)
            state.name = payload.username
            state.isLogin = true
        },
        loginFail(state){               //로그인 실패
            console.log('로그인 실패')
            alert('이메일과 비밀번호를 확인하세요')
            state.name = ''
            state.isLogin = false
        },
        logout(state){                  //로그아웃
            if(state.isLogin){
                state.name = ''
                state.isLogin = false
                alert('정상적으로 로그아웃 되었습니다')
                router.push('/').catch(()=>{})
            }
        },
    },
    actions:{
        login({state, commit}, loginObject){    //로그인 시도
            if(state.isLogin){
                alert('이미 로그인된 상태입니다')
            }
            else{
                axios({
                    method: 'POST',
                    url: 'http://34.64.236.155:8000/myapp/login/',
                    data: {
                        email: loginObject.email,
                        password: loginObject.password
                    }
    
                }).then((res) =>{
                    console.log(res.data)
                    if(res.data.length == 0){
                        commit('loginFail')
                    }else{
                        commit('loginSuccess', res.data[0])
                        alert(state.name+'님 반갑습니다');
                        router.push('/').catch(()=>{})
                    }
                });
            }
        }
    }
})