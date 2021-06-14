<template>
    <div id="a">
        


        <b-card class="result">
            <b-tabs pills card vertical>
                <b-tab v-for="(title, index) in 3" v-bind:title="titles[index]" :key="index" active>
                    <b-card-text>
                        <div>
                            <h1>{{brand[index].brandname}}</h1>
                            <b-tabs content-class="mt-3">
                                <b-tab title="브랜드 정보" active>
                                    <div>
                                        <b-table :items="items"></b-table>
                                    </div>
                                </b-tab>
                                <b-tab title="본사 정보"><p>본사 정보</p></b-tab>
                            </b-tabs>
                        </div>
                    </b-card-text>
                </b-tab>
            </b-tabs>
        </b-card>
    </div>

</template>
<script>
import data from '@/data/brandinfo.js'

export default {
    data() {
        return {
            brand: data.Brands,
            items: '',
            titles: [
                'Top1', 'Top2', 'Top3', 'Top4', 'Top5', 'Top6', 'Top7', 'Top8', 'Top9', 'Top10'
            ]
        }
    },
    computed:{
        
    }
        
    
    
}
</script>

<style>
#a{
    height: 100%;
    width: 100%;
}
.result{
    margin-top: 0px;
    height: 100%;
}
</style>