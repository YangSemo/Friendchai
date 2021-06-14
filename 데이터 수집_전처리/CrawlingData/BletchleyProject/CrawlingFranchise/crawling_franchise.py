from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import csv

# 저장할 csv 파일 이름
csv_file_name = '2020_brand_03_분식.csv'

# 등록년도 2015-2020
# ?

# 대분류 값
main_category_idx = '21'

# 대분류 한글명 21=외식, 22=도소매 23=서비스
main_category_kor = '외식'

# 중분류 리스트 값 한/중/일/양/치킨
# middle_category_list = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', 'J1', 'K1', 'L1', 'M1', 'N1', 'O1']
middle_category_list = ['B1']

# 중분류 리스트 한글명
middle_category_kor =\
    ['한식', '분식', '중식', '일식', '서양식', '기타 외국식', '패스트푸드', '치킨', '피자', '제과제빵', '아이스크림/빙수', '커피', '음료(커피 외)', '주점', '기타 외식']
# middle_category_kor = ['분식']

# 비교항목
# 업종별/가맹본부별/브랜드별에 항목 달라짐
# 업종별(listIndus01-04) - 업종개황 / 가맹본부변동현황 / 브랜드변동현황 / 가맹점변동현황
# 가맹본부별(listHq01-03) - 성장성 / 안정성 / 수익성
# 브랜드별(listBrand01-04) - 브랜드 개요 / 가맹점 현황 정보 / 가맹점 창업 비용
main_compare = ['1', '2', '3']
listIndus = ['listIndus01', 'listIndus02', 'listIndus03', 'listIndus04']
listHq = ['listHq01', 'listHq02', 'listHq03']
listBrand = ['listBrand01', 'listBrand02', 'listBrand03']

# csv 저장될 속성 리스트
column_list = ['업종']

i = 0
delay = 1

# csv에 하나하나 저장될 컬럼
table_list = []

with open(csv_file_name, 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f)
    browser = webdriver.Chrome('chromedriver.exe')
    browser.get('https://franchise.ftc.go.kr/mnu/00014/program/firHope/view.do')

    flag = False
    time.sleep(delay)

    for value in middle_category_list:
        # 대비교 항목
        sub_compare_category = Select(browser.find_element_by_id('searchCondition'))
        sub_compare_category.select_by_value(main_compare[2])
        time.sleep(delay)

        # 비교 항목
        main_compare_category = Select(browser.find_element_by_id('selListType'))
        main_compare_category.select_by_value(listBrand[1])

        # 업종 대분류 선택
        main_category = Select(browser.find_element_by_id('selUpjong'))
        main_category.select_by_value(main_category_idx)
        time.sleep(delay)

        # 업종 중분류 선택
        middle_category = Select(browser.find_element_by_id('selIndus'))
        middle_category.select_by_value(value)
        time.sleep(delay)

        # 검색
        browser.find_element_by_xpath('//input[@alt="검색"]').click()
        time.sleep(delay)

        # 컬럼 속성 값 입력
        if not flag:
            for head in browser.find_element_by_tag_name('thead').find_element_by_tag_name('tr') \
                    .find_elements_by_tag_name('th'):
                column_list.append(head.text)

            print(column_list)
            w.writerow(column_list)
            flag = True

        tbody = browser.find_element_by_tag_name('table').find_element_by_tag_name('tbody')

        try:
            trs = tbody.find_elements_by_tag_name('tr')

            for tr in trs:
                if flag:
                    flag = False
                    continue
                else:
                    tds = tr.find_elements_by_tag_name('td')
                    table_list.append(middle_category_kor[middle_category_list.index(value)])
                    for td in tds:
                        table_list.append(td.text)

                    print(table_list)
                    w.writerow(table_list)
                    table_list = []


        except:
            print('error')

        browser.refresh()
        flag = True

print('finish')
