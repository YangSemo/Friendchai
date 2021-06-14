<template>
    <div class="modal">
        <b-modal ref='register-modal' show="lg" :modal-class="my-modal" id="register" title="회원가입" @hidden="reset" centered hide-footer>
            <b-form @submit.stop.prevent>
               <label for="id">E-mail</label>
                <b-form-input type="text" id="id" v-model="form.userId" required></b-form-input>
                <br>
                <label for="id">User Name</label>
                <b-form-input type="text" v-model="form.userName" required></b-form-input>
                <br>
                <label for="password">Password</label>
                <b-form-input v-model="form.password" type="password" id="password" aria-describedby="password-help-block" required></b-form-input>
                <b-form-text id="password-help-block">
                    <!-- 비밀번호는 ~~~~ -->
                </b-form-text>
                <br>
                <label for="password_check">Password Check</label>
                <b-form-input v-model="form.password_check" type="password" id="password_check" required></b-form-input>
                <br>
            </b-form>
            <b-button variant="primary" @click="regist">제출</b-button>       
        </b-modal>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data(){
        return {
            form: {
                userId: '',
                userName: '',
                password: '',
                password_check: '',
                isModalVisible: false,
            },
        }
    },
    methods: {
        regist(){
            axios({
                method: 'post',
                url: 'http://34.64.236.155:8000/myapp/register/',
                data:{
                    email: this.form.userId,
                    password: this.form.password,
                    username: this.form.userName,
                }
            }).then((res) =>{
                if(res.status == 200){
                    alert('회원가입에 성공하였습니다');
                    this.closeModal();
                    this.$router.push('/').catch(()=>{})
                }
            })
        },
        reset(){
            this.form.userId='',
            this.form.userName='',
            this.form.password='',
            this.form.password_check=''
        },
        closeModal(){
            this.$refs['register-modal'].hide()
        }
    },
    computed: {
        
    }
}
</script>

<style>
/* .input{
    margin: 10px;
    text-align: left;
}
.card{
    height: 100%;
} */
.modal{
    display: flex;
    align-items: center;
}
</style>