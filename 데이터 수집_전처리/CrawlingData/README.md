# Bletchley Crawling Project
with Python, selenium, chromedriver .. 

2021.03.3rd week(?) ~ Now

공정거래위원회에서 제공하는 정보공개서 Web 문서를 크롤링하여 csv 파일로 변환

## 2021.04.07.

git 명령어를 수행하는데 있어서 한글 명명은 콘솔에서 식별할 수 없는 인코딩 형식으로 올라와 
영문으로 다시 파일 이름을 명명했다.    

csv 파일 설명

from [정보공개서 열람](https://franchise.ftc.go.kr/mnu/00013/program/userRqst/list.do)

    2020_BrandSummary.csv :              2020년 정보공개서 브랜드 개요
    2020_FranchiseFoundationCost.csv :   2020년 정보공개서 가맹점 창업 비용
    2020_FranchiseStatusInfo.csv :       2020년 정보공개서 가맹점 현황 정보
    2020_PublicInfo_TotalData.csv :      2020년 정보공개서 종합 데이터(위 세개 csv파일을 통합시킨것)

from [정보공개서 비교 정보](https://franchise.ftc.go.kr/mnu/00014/program/firHope/view.do)

    2019_TotalPageDetail.csv :           2019년 갱신된 정보공개서 브랜드 상세 페이지
    2020_TotalPageDetail.csv :           2020년 갱신된 정보공개서 브랜드 상세 페이지

💀위 파일들은 2021.04.05 리스트에 올라온 데이터를 바탕으로 제작됨을 알립니다.

😎다음 해볼 것: 전국 프랜차이즈 가맹점 주소 목록(경위도 좌표 형식)을 크롤링하여 csv 파일 생성

## 2021.04.12. Analysis
- Total_City_Address.csv(모든 시도별 가게 통합)
    - BigDataClass/Cities/ 디렉터리 안에 전국 시도별 가게 데이터 있음
- BigDataClass/report#1_2.py
    - 소상공인시장진흥공단에서 제공하는 OpenAPI를 사용하여 약 76만개의 데이터를 추출

### 1번째 분석
analysis_1th.csv, analysis_1th.py
- 브랜드 6026개와 가져온 약 76만개의 전국 지점 데이터를 비교하여 3907개 추출.
  
### 2번째 분석
analysis_2nd.csv, analysis_2nd.py

- 3907개의 브랜드가 전국에 몇개 있는지 약 76만개에서 데이터 추출, 약 12만개 추출.


## 데이터 분류
그동안 모아온 데이터들을 몇개의 테마 혹은 클래스로 분류해야한다.
테마 만들기, 클러스터링 등 다양한 주제가 논의됨.


#### 2021.04.27. 대규모 리팩토링
SemoYang이 데이터분류를 담당함

### DB에 들어갈 최종 csv 파일 생성
2021.04.29.
MySql에 최종적으로 들어갈 브랜드 정보(FinalBrand)와 본사 정보(FinalHQ)가 만들어졌다.

2021.04.30
전국 점포 위치 정보(FinalStoreAddress) 작업중 -- 같은 브랜드인데 업종을 다르게 넣은 경우가 있다(60계 -> 치킨, 한식)
인구수(FinalPopulation) 생성 완료

2021.05.01
마지막 점포 위치 정보(FinalStoreAddress_3.csv)가 생성됐다. 총 72,772개의 행. 생각보다 적은 수치다. 🤔
