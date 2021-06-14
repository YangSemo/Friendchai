# DjangoProject
정보공개서로부터 읽어낸 데이터를 웹 통신을 하기 위한 서버 프로토타입 프로젝트
[데이터 수집 프로젝트](https://github.com/PioneerRedwood/CrawlingData)



## 2021.04.29.

Brand, Headquarter 데이터 MySQL에 삽입



### Brand 테이블 정보
    id, 업종(sector), 브랜드 이름(brand_name), 상호(mutual),
    가맹사업 시작일(franchise_start_date), 가맹사업 개월수(franchise_months),
    가맹점수(num_of_franchise), 임직원수(num_of_employees),
    신규개점수(num_of_open), 폐점수(num_of_quit), 해지수(num_of_cancel),
    명의변경수(num_of_name_changing), 평균매출액(average_sales), 면적당 평균 매출액(average_sales_per_area),
    가맹비(franchise_fee), 교육비(education_fee), 보증금(deposit), 기타비용(other_cost),
    창업비용(startup_cost), 면적당 비용(cost_per_area), 기준면적(standard_area), 
    총 비용(total_cost)
✌브랜드 테이블은 정보공개서에서 제공한 데이터를 가공하여 제작했다.



### Headquarter 테이블 정보
    id, 상호(mutual), 대표자(representative), 법인 설립 등기일(register_law_date),
    사업자 등록일(register_biz_date), 대표번호(representative_number), 
    대표 팩스 번호(fax_number), 주소(address), 사업자 유형(biz_type),
    법인 등록 번호(law_number), 사업자 등록 번호(biz_number),
    2020년 자산(assets_2020), 2020년 부채(liabilities_2020), 2020년 자본(equity_2020), 2020년 매출액(sales_2020), 2020년 영업이익(income_2020), 2020년 당기순이익(net_income_2020) ... 
    2020년 개점(opening_2020), 2020년 폐점(closing_2020), 2020년 명의변경(name_change_2020) ... 
    공정거래위원회 시정 조치(num_of_correction), 민사소송 패소 및 민사상 화해(num_loss_of_law), 형의 선고(num_of_sentences)

✌본사 테이블은 정보공개서에서 제공한 데이터를 가공하여 제작했다.



## 2021.05.03 업데이트

StoreAddress와 Population 데이터 MySQL에 삽입



### StoreAddress 테이블 정보

```
id, 업종(sector), 브랜드명(brand_name), 도(do), 시구(sigu), 동(dong), 
경도(longitude), 위도(latitude)
```

✌소상공인진흥공단 OpenAPI에서 제공한 전국 가게 주소 데이터를 가공하여 제작했다.

- 동이 없는 350개의 항은 삭제됐다.



### Population 인구수 테이블 정보

```
id, 도(do), 시구(sigu), 동(dong), 인구수(population)
```

✌2021년 3월에 공개한 행정동별 인구수 공공데이터 csv 파일을 가공하여 제작했다.



##### 브랜드 검색 기능

- 이상한 오류로 id가 1인 '복도네'를 검색하면 에러가 뜬다.

- NoReverseMatch at /myapp/brand_search/ 이 이상한 에러는 id가 1인 브랜드에서만 뜬다.

##### html 파일 리팩토링

- myapp/brand : 첫 화면, 파일 위치: myapp/index.html
- myapp/brand/search/ : 추가된 검색 기능, 파일 위치: myapp/brand/search.html

##### 카카오맵 API 시범 적용

myapp/kakaomap.html [클릭한 위치에 마커 표시하기 - Kakao Maps API](https://apis.map.kakao.com/web/sample/addMapClickEventWithMarker/)

- 경위도로 지도에 나타내면 될 것 같다.
- 실전에서 지도를 사용할 때는 특정 브랜드 + 위치 + 업종 정보가 함께 요청되며 그에 맞는 지도 정보를 띄우기 위한 프로세스를 정할 필요가 있다.

##### Django REST API 시범 적용

[Django REST API 공식 문서](https://www.django-rest-framework.org/)

- 인구수 테이블 관련하여 REST API를 동작했다. 
- Postman이라는 별도의 툴을 통해 통신하는 것을 테스트했다.



##### 🤔추가할 사항

- 로그인, 로그아웃, 아이디 찾기, 비밀번호 찾기, OAuth 등 사용자 관련 REST API
- 카카오맵 API 적극 사용하여 위치와 업종을 지정하여 해당 지역에 속한 모든 업종을 마커로 맵에 표시하기

#### 2021.05.10. 추가 사항
- 로그인, 로그아웃, 회원가입 추가(생각보다 오래 걸렸다😢)

#### 2021.05.16. Class Based View, 분석 모델 추가
- 실제 서버에 배포