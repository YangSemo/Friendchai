<template>
    <div>
      <!-- Header에 가리는거 내리기용 -->
      <b-container fluid>
          <b-row style="height: 15vh;"></b-row>
      </b-container>

      <b-container fluid>
        <b-row style="padding-bottom: 5vh;">
          <b-col>
            <a style="font-size: 50px; font-weight: bold;">Theme</a><br>
            <a style="font-size: 20px;">원하시는 테마를 골라보세요</a>
          </b-col>
        </b-row>
        <b-row align-h="center" align-v="center" style="padding-bottom: 3vh; height: 27vh;">
          
          <b-col cols="3" class="themeCard">
            <b-row align-v="center" align-h="center" style="height: 100%">
              <b-col @click="detail1">
                <a style="font-size: 3.5vh; font-weight:bold;">안정적인 시작</a><br>
                <a style="font-size: 2vh;">중소기업 프랜차이즈</a>
              </b-col>            
            </b-row>
          </b-col>

          <b-col cols="3" class="themeCard">
            <b-row align-v="center" align-h="center" style="height: 100%">
              <b-col @click="detail2">
                <a style="font-size: 3.5vh; font-weight:bold;">장수 프랜차이즈</a><br>
                <a style="font-size: 2vh;">대기업 프랜차이즈</a>
              </b-col>            
            </b-row>
          </b-col>

          <b-col cols="3" class="themeCard">
            <b-row align-v="center" align-h="center" style="height: 100%">
              <b-col @click="detail3">
                <a style="font-size: 3.5vh; font-weight:bold;">새로운 시작을 함께</a><br>
                <a style="font-size: 2vh;">신생 프랜차이즈</a>
              </b-col>            
            </b-row>
          </b-col>

        </b-row>

        <b-row align-h="center" align-v="center" style="height: 27vh; padding-bottom: 5vh;">
          
          <b-col cols="3" class="themeCard">
            <b-row align-v="center" align-h="center" style="height: 100%">
              <b-col @click="detail4">
                <a style="font-size: 3.5vh; font-weight:bold;">대중적인</a><br>
                <a style="font-size: 2vh;">중견기업 프랜차이즈</a>
              </b-col>            
            </b-row>
          </b-col>

          <b-col cols="3" class="themeCard">
            <b-row align-v="center" align-h="center" style="height: 100%">
              <b-col @click="detail5">
                <a style="font-size: 3.5vh; font-weight:bold;">고투자 고수입</a><br>
                <a style="font-size: 2vh;">넓은 매장의 프랜차이즈</a>
              </b-col>            
            </b-row>
          </b-col>

        </b-row>
      </b-container>
    </div>    
</template>


<script>
export default {
    name: "Theme",
    data(){
      return{

      }
    },
    methods: {
        detail1(){
            this.$router.push({
                path: '/service/recommend/theme/result/all',
                query: {label: '1'}
            })
        },
        detail2(){
            this.$router.push({
                path: '/service/recommend/theme/result/all',
                query: {label: '2'}
            })
        },
        detail3(){
            this.$router.push({
                path: '/service/recommend/theme/result/all',
                query: {label: '3'}
            })
        },
        detail4(){
            this.$router.push({
                path: '/service/recommend/theme/result/all',
                query: {label: '4'}
            })
        },
        detail5(){
            this.$router.push({
                path: '/service/recommend/theme/result/all' ,
                query: {label: '5'}
            })
        },
    }
}
</script>

<style>
.themeCard{
  display: inline-block;
  vertical-align: center;
  margin-right: 3vh;
  background: #B8CCE1;
  height: 100%;
  cursor: pointer;
  border-radius: 15px;
}
</style>