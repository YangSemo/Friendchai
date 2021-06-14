<template>
    <div>
        <!-- Header 크기 - Footer크기 -->
        <b-container fluid>
            <b-row style="height: 0vh;"></b-row>
        </b-container>
        <b-container fluid="xl">
            <b-row class="mainSearch" style="height: 40vh;" align-h="center" align-v="end">
                <b-col style="font-size: 40px; font-weight: bold;">
                    브랜드 검색
                </b-col>
            </b-row>
            <b-row class="mainSearch" style="height: 5vh;" align-h="center" align-v="end">
                <b-col cols="6">
                    <b-input-group>
                        <b-input type="text" v-model="search" style="border-radius: 20px 0 0 20px;"></b-input><b-button @click="searchbrand" style=" border-radius: 0 20px 20px 0;"><img src="@/assets/search.png" style="height: 14px;"></b-button>
                    </b-input-group>
                </b-col>
            </b-row>
            <b-row class="icon" style="height: 6vh; margin-top: 4vh;" align-h="center" align-v="start">
                <b-col cols="1.5">
                    <img @click="gobrand('korean')" src="@/assets/korean.png" style="height: 7vh;"><br><strong>한식</strong>
                </b-col>
                <b-col cols="2">
                    <img @click="gobrand('cafe')" src="@/assets/cafe.png" style="height: 7vh;"><br><strong>카페</strong>
                </b-col>
                <b-col cols="0.8">
                    <img @click="gobrand('chicken')" src="@/assets/chicken.png" style="height: 7vh;"><br><strong>치킨</strong>
                </b-col>
                <b-col cols="2">
                    <img @click="gobrand('fastfood')" src="@/assets/fastfood.png" style="height: 7vh;"><br><strong>패스트푸드</strong>
                </b-col>
                <b-col cols="1.5">
                    <img @click="gobrand('bread')" src="@/assets/bread.png" style="height: 7vh;"><br><strong>제과제빵</strong>
                </b-col>
            </b-row>
            <b-row class="icon" style="height: 46vh; margin-top: 4vh;" align-h="center" align-v="start">
                <b-col cols="1.5">
                    <img @click="gobrand('chijap')" src="@/assets/chijap.png" style="height: 7vh;"><br><strong>중/일식</strong>
                </b-col>
                <b-col cols="2">
                    <img @click="gobrand('kimbob')" src="@/assets/kimbob.png" style="height: 7vh;"><br><strong>분식</strong>
                </b-col>
                <b-col cols="0.8">
                    <img @click="gobrand('hof')" src="@/assets/hof.png" style="height: 7vh;"><br><strong>주점</strong>
                </b-col>
                <b-col cols="2">
                    <img @click="gobrand('etc')" src="@/assets/etc.png" style="height: 7vh;"><br><strong>기타외식</strong>
                </b-col>
                <b-col cols="1.5">
                    <img @click="gobrand('etc_f')" src="@/assets/etcf.png" style="height: 7vh;"><br><strong>기타외국식</strong>
                </b-col>
            </b-row>
            
        </b-container>

        <b-container class="img1" fluid>
            <div class="img-cover"> 
                <b-row class="introduce"  align-v="center">
                    <b-col class="top" style="color: white"><strong>안녕하세요 프랜드차이입니다</strong><br>
                        <a style="font-size:5vh;">신규 가맹사업자들을 위한 서비스를 지금 바로 만나보세요</a>
                    </b-col>
                </b-row>
            </div>                
        </b-container>

        <div class="w-100" style="height: 40vh;"></div>

        <b-container class="img2" fluid>
            <div class="img-cover">

                <b-row align-v="center" class="introduce">
                    <b-col cols="5">
                        <b-row  class="top" align-h="center">
                            <strong>브랜드 추천</strong>
                        </b-row>
                        <b-row style="height: 20vh;"></b-row>
                        <b-row align-h="center">
                            <a style="font-size: 3.2vh;">신규 창업자들을 위한 추천 서비스</a>
                        </b-row>
                    
                    </b-col>
                    <b-col cols="7" >
                        <b-row  class="middle">
                            <b-col cols="3">
                                테마
                            </b-col>
                            <b-col>
                                저희가 미리 정해둔 테마를 만나보세요
                            </b-col>
                        </b-row>
                        <b-row style="height: 10vh;">
                        </b-row>
                        <b-row  class="middle">
                            <b-col cols="3">
                                사용자 설정
                            </b-col>
                            <b-col>
                                조건을 설정하셔도 돼요
                            </b-col>
                        </b-row>                    
                    </b-col>
                </b-row>
            </div>
        </b-container>
        <div class="w-100" style="height: 40vh;"></div>

        <b-container class="img3" fluid>
            <div class="img-cover">
                <b-row align-v="center" class="introduce">
                    <b-col cols="5">
                        <b-row  class="top" align-h="center">
                            <strong>브랜드 정보</strong>
                        </b-row>
                        <b-row style="height: 20vh;"></b-row>
                        <b-row align-h="center">
                            <a style="font-size: 3.2vh;">궁금하신 브랜드가 있다면</a>
                        </b-row>
    
                    </b-col>
                    <b-col cols="7" >
                        <b-row  class="middle">
                            <b-col cols="3">
                                검색
                            </b-col>
                            <b-col>
                                원하는 브랜드를 찾아보세요
                            </b-col>
                        </b-row>
                        <b-row style="height: 10vh;">
                        </b-row>
                        <b-row  class="middle">
                            <b-col cols="3">
                                카테고리
                            </b-col>
                            <b-col>
                                업종별로도 모아봤어요
                            </b-col>
                        </b-row>                    
                    </b-col>
                </b-row>
            </div>
        </b-container>

        <div class="w-100" style="height: 40vh;"></div>

        <b-container class="img4" fluid>
            <div class="img-cover">
                <b-row align-v="center" class="introduce">
                    <b-col cols="5">
                        <b-row  class="top" align-h="center">
                            <strong>지도</strong>
                        </b-row>
                        <b-row style="height: 20vh;"></b-row>
                        <b-row align-h="center">
                            <a style="font-size: 3.2vh;">지도에서 브랜드를 찾아보세요</a>
                        </b-row>
    
                    </b-col>
                    <b-col cols="7" >
                        <b-row  class="middle">
                            <b-col cols="3">
                                위치
                            </b-col>
                            <b-col>
                                원하는 위치를 고르세요
                            </b-col>
                        </b-row>
                        <b-row style="height: 10vh;">
                        </b-row>
                        <b-row  class="middle">
                            <b-col cols="3">
                                카테고리
                            </b-col>
                            <b-col>
                                업종별로 위치를 표시해줄게요
                            </b-col>
                        </b-row>                    
                    </b-col>
                </b-row>
            </div>
        </b-container>
        <div class="w-100" style="height: 10vh;"></div>
    </div>
</template>

<script>
export default {
    data(){
        return{
            search: ''
        }
    },
    methods:{
        gobrand(sector){
            this.$router.push({
                name: 'BrandList',
                query: {
                    sector: sector
                }
            })
        },
        searchbrand(){
            this.$router.push({
                name: 'BrandSearch',
                query: {searchparam: this.search},
            })
        },
    }
}
</script>

<style>
.img1{
position: relative;
/* src: "@/assets/contract.jpg"; */
background-image: url(https://i1.wp.com/bestonetax.com/wp-content/uploads/2018/11/business-3167295_640.jpg?resize=640%2C423);
height: 70vh;
background-size: cover;
}
.img2{
position: relative;
/* src: "@/assets/contract.jpg"; */
background-image: url('../../assets/recommend.jpg');
height: 70vh;
background-size: cover;
}
.img3{
position: relative;
/* src: "@/assets/contract.jpg"; */
background-image: url('../../assets/detail.jpg');
height: 70vh;
background-size: cover;
}
.img4{
position: relative;
/* src: "@/assets/contract.jpg"; */
background-image: url('../../assets/map.png');
height: 70vh;
background-size: cover;
}
 .img-cover{
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.7);                                                                 
    z-index:0;
} 
.icon{
    cursor: pointer;
}
.introduce{
    width: 100%;
    text-align: center;
    height: 70vh;
    color: white;
}
.top{
    font-size: 7vh;
}
.middle{
    font-size: 4vh;
    text-align: left;
    border-left: 1px;
    border-left-style: solid;
    margin-top: 5vh;
    padding-left: 20px;
}
.mainContainer{
    background-color: #C6DFD6;
}
.mainContainer2{
    background-color: #E9DDC8;
}
</style>