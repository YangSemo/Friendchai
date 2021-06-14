<template>
    <div>
        <!-- Header 크기 - Footer크기 -->
        <b-container fluid>
            <b-row style="height: 70px;"></b-row>
        </b-container>

        <b-container fluid style="height: 87.5vh;">
            <b-row align-v="stretch">
                <b-col style="background-color: #9CC0BA;" cols="3">
                    <b-row style="margin:4vh auto; font-size: 4vh; font-weight: bold;" align-h="center">
                        <b-col cols="auto">
                            브랜드 찾기
                        </b-col>
                    </b-row>
                    <b-row align-h="start" align-v="center" no-gutters class="dropbox">
                        <b-col cols="4" style="text-align: center;">
                            도 / 특별시
                        </b-col>
                        <b-col cols="6">
                            <b-select v-model="m_do">
                                <option disabled value="">도 / 특별시 / 광역시 / 특별자치시</option>
                                <option v-for="(m_do, index) in do_s" :key="index">{{m_do}}</option>
                            </b-select>
                        </b-col>
                    </b-row>
                    <b-row align-h="start" align-v="center" no-gutters class="dropbox">
                        <b-col cols="4" style="text-align: center;">
                            시 / 구
                        </b-col>
                        <b-col cols="6">
                            <b-select v-model="m_sigu">
                                <option disabled value="">시 / 구</option>
                                <option v-for="(m_sigu, index) in dynamicChangeByDo(m_do)" :key="index">{{m_sigu}}</option>
                            </b-select>
                        </b-col>
                    </b-row>
                    <b-row align-h="start" align-v="center" no-gutters class="dropbox">
                        <b-col cols="4" style="text-align: center;">
                            읍 / 면 / 동
                        </b-col>
                        <b-col cols="6">
                            <b-select v-model="m_dong">
                                <option disabled value="">읍 / 면 / 동</option>
                                <option v-for="(m_dong, index) in dynamicChangeBySigu(m_sigu)" :key="index">{{m_dong}}</option>
                            </b-select>
                        </b-col>
                    </b-row>
                    <b-row align-h="start" align-v="center" no-gutters class="dropbox">
                        <b-col cols="4" style="text-align: center;">
                            업종
                        </b-col>
                        <b-col cols="6">
                            <b-select v-model="sector">
                                <option disabled value="">업종</option>
                                <option value='한식'>한식</option>
                                <option value='중/일식'>중/일식</option>
                                <option value='치킨'>치킨</option>
                                <option value='카페'>카페</option>
                                <option value='분식'>분식</option>

                                <option value='제과제빵'>제과제빵</option>
                                <option value='주점'>주점</option>
                                <option value='패스트푸드'>패스트푸드</option>
                                <option value='기타 외식'>기타 외식</option>
                                <option value='기타 외국식'>기타 외국식</option>
                            </b-select>
                        </b-col>
                    </b-row>
                    <b-row align-h="center">
                        <b-col cols="6">
                            <b-button @click="result">한눈에 보기</b-button>
                        </b-col>
                    </b-row>
                    <hr>
                    <b-row>
                        <b-col>
                            <p id='population_content'></p>
                        </b-col>
                    </b-row>
                    <b-container style="overflow: scroll; height: 34vh;">
                    <b-row v-for="item in fran" :key="item" align-h="center">
                        <b-col cols="8" class="mapCard" @click="detail(item.brand_name)">
                            <strong style="font-size: 20px;">{{item.brand_name}}</strong><br>
                            {{item.sector}}<br>
                            <!-- 주소: <p>{{latlngToAddress(item.latitude, item.longitude)}}</p> -->
                        </b-col>
                    </b-row>
                    </b-container>
                    <b-row>
                        <b-col>
                            <div id='alert'></div>
                        </b-col>
                    </b-row>
                </b-col>
                <b-col id="map" class="map" cols="9">
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>
import axios from 'axios'
    import location_data from '@/data/location.js'
    export default{
        data(){
            return {
                m_do: '',
                m_sigu: '',
                m_dong: '',
                sector: null,
                population: '',
                location_data: location_data.locate,
                do_s: null,
                fran: null,
                address: null,
            }
        },
        created() {
            this.addKakaoMapScript();
            var a = new Array;
            for(var i=0; i<location_data.locate.length; i++){
                if(!a.includes(location_data.locate[i].do))
                {
                    a.push(location_data.locate[i].do);
                }
            }
            this.do_s = a;
        },
        methods: {
            detail(name){
                this.$router.push({
                    name: 'BrandDetail',
                    query: {name: name},
                })
            },
            result()
            {
                axios.get('http://34.64.236.155:8000/myapp/address/?do=' 
                        + this.m_do + '&sigu=' + this.m_sigu + "&dong=" + this.m_dong + '&sector=' + this.sector).then((res) =>{
                    this.fran = res.data;
                    axios.get('http://34.64.236.155:8000/myapp/population/?do=' 
                            + this.m_do + '&sigu=' + this.m_sigu + "&dong=" + this.m_dong).then((res) =>{
                                // {{m_do}} {{m_sigu}} {{m_dong}}의 인구수 : {{population}}명
                                document.getElementById('population_content').textContent = this.m_do + ' ' + this.m_sigu + ' ' + this.m_dong + '의 인구수는 ' + toPrettyString(res.data[0].population) + '명입니다.';
                        // this.population = res.data[0].population
                    })
                    this.initMap();
                    function toPrettyString(int_param) {
                        return String(int_param).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
                    }
                })
            },
            addKakaoMapScript(){
                const script = document.createElement("script");
                /* global kakao */
                script.onload = () => kakao.maps.load(this.initMap);
                script.src = "http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=480de901dd8b4754fa3f8e437d642a05&libraries=services";
                document.head.appendChild(script);
            },
            initMap(){
                document.getElementById('alert').innerHTML = '';
                document.getElementById('map').innerHTML = '';

                if (this.fran.length == 0)
                {
                    // 텍스트로 없다고 알림
                    document.getElementById('alert').innerHTML = '<strong>해당 지역의 '+ this.sector + ' 업종 데이터가 없습니다.</strong>';

                    // 카카오맵도 없애버리기
                    var tag2 = document.createElement('div');
                    tag2.innerHTML = '<br><br><strong>데이터가 없습니다.</strong>';
                    document.getElementById('map').appendChild(tag2);
                    return;
                }

                var container = document.getElementById("map");
                var middle_lat = 0;
                var middle_lng = 0;
                var brand_list1 = new Array
                for(var i =0; i < this.fran.length; i++){
                    brand_list1.push({
                        content: this.fran[i].brand_name,
                                // "\r\n주소: " + this.latlngToAddress(this.fran[i].latitude, this.fran[i].longitude),
                        latlng: new kakao.maps.LatLng(this.fran[i].latitude, this.fran[i].longitude)
                    })
                    middle_lat += parseFloat(this.fran[i].latitude);
                    middle_lng += parseFloat(this.fran[i].longitude);
                }
                middle_lat /= this.fran.length;
                middle_lng /= this.fran.length;

                var options = {
                    center: new kakao.maps.LatLng(middle_lat, middle_lng),
                    level: 5
                };
                var map = new kakao.maps.Map(container, options);
                for (i = 0; i < brand_list1.length; i++) {
                    // 마커를 생성합니다
                    var marker = new kakao.maps.Marker({
                        map: map, // 마커를 표시할 지도
                        position: brand_list1[i].latlng // 마커의 위치
                    });
                //     // 마커에 표시할 인포윈도우를 생성합니다 
                    var infowindow = new kakao.maps.InfoWindow({
                        content: brand_list1[i].content // 인포윈도우에 표시할 내용
                    });
                //     // 마커에 mouseover 이벤트와 mouseout 이벤트를 등록합니다
                        // 이벤트 리스너로는 클로저를 만들어 등록합니다 
                        // for문에서 클로저를 만들어 주지 않으면 마지막 마커에만 이벤트가 등록됩니다
                    kakao.maps.event.addListener(marker, 'mouseover', makeOverListener(map, marker, infowindow));
                    kakao.maps.event.addListener(marker, 'mouseout', makeOutListener(infowindow));
                }
                // 인포윈도우를 표시하는 클로저를 만드는 함수입니다 
                function makeOverListener(map, marker, infowindow) {
                    return function() {
                        infowindow.open(map, marker);
                    };
                }
                // // 인포윈도우를 닫는 클로저를 만드는 함수입니다 
                function makeOutListener(infowindow) {
                    return function() {
                        infowindow.close();
                    };
                }
                
            },
            dynamicChangeByDo(m_do)
            {
                var b = new Array;
                for(var i = 0; i < location_data.locate.length; i++)
                {
                    if(location_data.locate[i].do == m_do && !b.includes(location_data.locate[i].si))
                    {
                        b.push(location_data.locate[i].si);
                    }
                }
                return b.sort();
            },
            dynamicChangeBySigu(m_sigu)
            {
                var b = new Array;
                for(var i = 0; i < location_data.locate.length; i++)
                {
                    if(location_data.locate[i].si == m_sigu && !b.includes(location_data.locate[i].dong))
                    {
                        b.push(location_data.locate[i].dong);
                    }
                }
                return b.sort();
            },
            latlngToAddress(latitude, longitude)    
            {
                var coord = new kakao.maps.LatLng(latitude, longitude);
                var geocoder = new kakao.maps.services.Geocoder();

                geocoder.coord2Address(coord.getLng(), coord.getLat(), (result, status) => {
                    if (status === kakao.maps.services.Status.OK) {
                        console.log(result[0].address.address_name, typeof(result[0].address.address_name));
                        this.address = result[0].address.address_name;
                        
                    }
                });
                console.log(this.address)
                return this.address;
            },
            
        },
    }
</script>


<style>
.map{
    height:87.6vh;
    z-index: 0;
}
.tab{
    float:left;
    width: 30%;
}
.dropbox{
    margin: 1.5vh auto;
}
.mapCard{
    margin: 0.5vh auto;
    border-style: solid;
    border-width: 1px;
    border-radius: 10px;
    background: #C6DFD6;
    cursor: pointer;
}
</style>