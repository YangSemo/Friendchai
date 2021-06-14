<template>
    <div>
      <b-card class="card" title="안정적인 시작!" sub-title="중소기업 프렌차이즈">
        <b-card-text>
          안정적인 브랜드의 프렌차이즈
        </b-card-text>
        <b-button variant="primary" @click="detail1">브랜드 정보 자세히보기</b-button>
      </b-card>
      <b-card class="card" title="대규모 프렌차이즈" sub-title="대기업 프렌차이즈">
        <b-card-text>
          이유 있는 장수 브랜드
        </b-card-text>
        <b-button variant="primary" @click="detail2">브랜드 정보 자세히보기</b-button>
      </b-card>
      <b-card class="card" title="새로운 시작을 함께!" sub-title="신생 프렌차이즈" >
        <b-card-text>
          트렌디한 높은 개점률의 프렌차이즈
        </b-card-text>
        <b-button variant="primary" @click="detail3">브랜드 정보 자세히보기</b-button>
      </b-card>
      <b-card class="card" title="중소 기업 프렌차이즈" sub-title="중견기업 프렌차이즈">
        <b-card-text>
          초보 창업자에게 가장 무난하게 시작할 수 있는 프렌차이즈
        </b-card-text>
        <b-button variant="primary" @click="detail4">브랜드 정보 자세히보기</b-button>
      </b-card>
      <b-card class="card" title="고투자 고수입 브랜드" sub-title="넓은 매장의 프렌차이즈">
        <b-card-text>
          여유 있는 창업자에게 추천하는 브랜드
        </b-card-text>
        <b-button variant="primary" @click="detail5">브랜드 정보 자세히보기</b-button>
      </b-card>                        
    </div>    
</template>

<script>
export default {
    name: "Theme",
    data(){

    },
    methods: {
        detail1(){
            this.$router.push({
                name: 'ThemeResult',
                params: {label: 1}
            })
        },
        detail2(){
            this.$router.push({
                name: 'ThemeResult',
                params: {label: 2}
            })
        },
        detail3(){
            this.$router.push({
                name: 'ThemeResult',
                params: {label: 3}
            })
        },
        detail4(){
            this.$router.push({
                name: 'ThemeResult',
                params: {label: 4}
            })
        },
        detail5(){
            this.$router.push({
                name: 'ThemeResult',
                params: {label: 5}
            })
        },
    }
}
</script>

<style>

</style>