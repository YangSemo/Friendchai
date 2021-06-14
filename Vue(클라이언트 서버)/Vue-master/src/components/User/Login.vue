<template>
    <div class="modal">
        <b-modal ref='login-modal' show="lg" :modal-class="my-modal" id="login" title="로그인" @hidden="reset" centered hide-footer>
            <b-form @submit.stop.prevent>
                <label for="id" >ID</label>
                <b-form-input placeholder="이메일을 입력해주세요" type="text" id="id" v-model="form.email" required></b-form-input>
                <br>
                <label for="password">Password</label>
                <b-form-input v-model="form.password" type="password" id="password" required></b-form-input>                
                <br>

                <b-button type="submit" variant="primary" @click="[login({ email: form.email, password: form.password}),closeModal()]">로그인</b-button>&nbsp;

            </b-form>
        </b-modal>
    </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
    data(){
        return {
            form: {
                email: '',
                password: '',
            }               
        }
    },
    methods: {
        ...mapActions(['login']),
        reset(){
            this.form.email = ''
            this.form.password = ''
        },
        closeModal(){
            setTimeout(function(){
                this.$refs['login-modal'].hide();
            }.bind(this), 3500);
            // this.$refs['login-modal'].hide();
        }
    }
}
</script>

<style>
.modal{
    display: flex;
    align-items: center;
}
</style>