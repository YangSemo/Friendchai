import Vue from 'vue'
import Router from 'vue-router'

//메인 화면
import Main from '@/components/Layout/Main'

//브랜드 기능
import BrandDetail from '@/components/Service/Brand/BrandDetail'
import BrandList from '@/components/Service/Brand/BrandList'
import BrandSearch from '@/components/Service/Brand/BrandSearch'

//지도
import Map from '@/components/Service/Map/Map'

//추천 기능
import Choice from '@/components/Service/Recommend/Choice'
import ThemeResult from '@/components/Service/Recommend/Theme/ThemeResult'
import UserSetResult from '@/components/Service/Recommend/UserSet/UserSetResult'
import Theme from '@/components/Service/Recommend/Theme/Theme'

//사용자 관리
import UserSet from '@/components/Service/Recommend/UserSet/UserSet'
import Register from '@/components/User/Register'
import FindPW from '@/components/User/FindPW'

//테마 추천 결과 업종별 중첩라우트 부분
import KoreanResult from '@/components/Service/Recommend/Theme/korean'
import CafeResult from '@/components/Service/Recommend/Theme/cafe'
import ChickenResult from '@/components/Service/Recommend/Theme/chicken'
import FastfoodResult from '@/components/Service/Recommend/Theme/fastfood'
import ChijapResult from '@/components/Service/Recommend/Theme/chijap'
import KimbobResult from '@/components/Service/Recommend/Theme/kimbob'
import HofResult from '@/components/Service/Recommend/Theme/hof'
import EtcResult from '@/components/Service/Recommend/Theme/etc'
import EtcfResult from '@/components/Service/Recommend/Theme/etcf'
import AllResult from '@/components/Service/Recommend/Theme/all'
import BreadResult from '@/components/Service/Recommend/Theme/bread'

//사용자 설정 추천 결과 업종별 중첩라우트 부분
import koreanResult from '@/components/Service/Recommend/UserSet/korean'
import cafeResult from '@/components/Service/Recommend/UserSet/cafe'
import chickenResult from '@/components/Service/Recommend/UserSet/chicken'
import fastfoodResult from '@/components/Service/Recommend/UserSet/fastfood'
import chijapResult from '@/components/Service/Recommend/UserSet/chijap'
import kimbobResult from '@/components/Service/Recommend/UserSet/kimbob'
import hofResult from '@/components/Service/Recommend/UserSet/hof'
import etcResult from '@/components/Service/Recommend/UserSet/etc'
import etcfResult from '@/components/Service/Recommend/UserSet/etcf'
import allResult from '@/components/Service/Recommend/UserSet/all'
import breadResult from '@/components/Service/Recommend/UserSet/bread'

Vue.use(Router)

export default new Router({
    mode: "history",
    routes:[
        {
            path: '/',
            name: 'Main',
            component: Main
        },
        {
            path: '/service/brand/branddetail/:brandname?',
            name: 'BrandDetail',
            component: BrandDetail,
        },
        {
            path: '/service/brand/brandlist',
            name: 'BrandList',
            component: BrandList,
        },
        {
            path: '/service/brand/brandsearch/:searchparam?',
            name: 'BrandSearch',
            component: BrandSearch,
        },
        {
            path: '/service/map',
            name: 'Map',
            component: Map,
        },
        {
            path: '/service/recommend/choice',
            name: 'Choice',
            component: Choice,
        },
        {
            path: '/service/recommend/theme',
            name: 'Theme',
            component: Theme,
        },
        {
            path: '/service/recommend/userset',
            name: 'UserSet',
            component: UserSet,
        },
        {
            path: '/service/recommend/userset/result/:param?',
            name: 'UserSetResult',
            component: UserSetResult,
            meta:{authRequired: true},
            children:[
                {     
                    path:'korean/:param?',
                    name:'koreanResult',
                    component: koreanResult,
                    children: [
                        {
                            path:'detail',
                            name:'1',
                            component: BrandDetail
                        }
                    ]
                },
                {
                    path:'cafe',
                    name:'cafeResult',
                    component: cafeResult,
                    children: [
                        {
                            path:'detail',
                            name:'2',
                            component: BrandDetail
                        }
                    ]
                },
                {
                    path:'chicken',
                    name:'chickenResult',
                    component: chickenResult,
                    children: [
                        {
                            path:'detail',
                            name:'3',
                            component: BrandDetail
                        }
                    ]
                },
                {
                    path:'fastfood',
                    name:'fastfoodResult',
                    component: fastfoodResult,
                    children: [
                        {
                            path:'detail',
                            name:'4',
                            component: BrandDetail
                        }
                    ]
                },
                {
                    path:'chijap',
                    name:'chijapResult',
                    component: chijapResult,
                    children: [
                        {
                            path:'detail',
                            name:'5',
                            component: BrandDetail
                        }
                    ]
                },
                {
                    path:'kimbob',
                    name:'kimbobResult',
                    component: kimbobResult,
                    children: [
                        {
                            path:'detail',
                            name:'6',
                            component: BrandDetail
                        }
                    ]
                },
                {
                    path:'hof',
                    name:'hofResult',
                    component: hofResult,
                    children: [
                        {
                            path:'detail',
                            name:'7',
                            component: BrandDetail
                        }
                    ]
                },
                {
                    path:'etc',
                    name:'etcResult',
                    component: etcResult,
                    children: [
                        {
                            path:'detail',
                            name:'8',
                            component: BrandDetail
                        }
                    ]
                },
                {
                    path:'etcf',
                    name:'etcfResult',
                    component: etcfResult,
                    children: [
                        {
                            path:'detail',
                            name:'9',
                            component: BrandDetail
                        }
                    ]
                },
                {
                    path:'all/:param?',
                    name:'allResult',
                    component: allResult,
                    children: [
                        {
                            path:'detail',
                            name:'10',
                            component: BrandDetail
                        }
                    ]

                },
                {
                    path:'bread',
                    name:'breadResult',
                    component: breadResult,
                    children: [
                        {
                            path:'detail',
                            name:'21',
                            component: BrandDetail
                        }
                    ]

                },

            ]
        },
        {
            path: '/service/recommend/theme/result',
            name: 'ThemeResult',
            component: ThemeResult,
            children:[
                {     
                    path:'korean',
                    name:'KoreanResult',
                    component: KoreanResult,
                    children: [
                        {
                            path:'detail',
                            name:'11',
                            component: BrandDetail
                        }
                    ]
                },
                {
                    path:'cafe',
                    name:'CafeResult',
                    component: CafeResult,
                    children: [
                        {
                            path:'detail',
                            name:'12',
                            component: BrandDetail
                        }
                    ]
                },
                {
                    path:'chicken',
                    name:'ChickenResult',
                    component: ChickenResult,
                    children: [
                        {
                            path:'detail',
                            name:'13',
                            component: BrandDetail
                        }
                    ]
                },
                {
                    path:'fastfood',
                    name:'FastfoodResult',
                    component: FastfoodResult,
                    children: [
                        {
                            path:'detail',
                            name:'14',
                            component: BrandDetail
                        }
                    ]
                },
                {
                    path:'chijap',
                    name:'ChijapResult',
                    component: ChijapResult,
                    children: [
                        {
                            path:'detail',
                            name:'15',
                            component: BrandDetail
                        }
                    ]
                },
                {
                    path:'kimbob',
                    name:'KimbobResult',
                    component: KimbobResult,
                    children: [
                        {
                            path:'detail',
                            name:'16',
                            component: BrandDetail
                        }
                    ]
                },
                {
                    path:'hof',
                    name:'HofResult',
                    component: HofResult,
                    children: [
                        {
                            path:'detail',
                            name:'17',
                            component: BrandDetail
                        }
                    ]
                },
                {
                    path:'etc',
                    name:'EtcResult',
                    component: EtcResult,
                    children: [
                        {
                            path:'detail',
                            name:'18',
                            component: BrandDetail
                        }
                    ]
                },
                {
                    path:'etcf',
                    name:'EtcfResult',
                    component: EtcfResult,
                    children: [
                        {
                            path:'detail',
                            name:'19',
                            component: BrandDetail
                        }
                    ]
                },
                {
                    path:'all',
                    name:'AllResult',
                    component: AllResult,
                    children: [
                        {
                            path:'detail',
                            name:'20',
                            component: BrandDetail
                        }
                    ]
                },
                {
                    path:'bread',
                    name:'BreadResult',
                    component: BreadResult,
                    children: [
                        {
                            path:'detail',
                            name:'22',
                            component: BrandDetail
                        }
                    ]

                },

            ]
        },
        {
            path: '/user/register',
            name: 'Register',
            component: Register
        },
        {
            path: '/user/findpw',
            name: 'FindPW',
            component: FindPW
        },
    ],
})