from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
import time
import csv

# 등록년도 2017-2020
years = ['2020', '2019', '2018', '2017']

# 대분류 값
main_category_idx = '21'

# 대분류 한글명 21=외식, 22=도소매 23=서비스
main_category_kor = '외식'

# 중분류 리스트 값
middle_category_list = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', 'J1', 'K1', 'L1', 'M1', 'N1', 'O1']

# 중분류 리스트 한글명
middle_category_kor = \
    ['한식', '분식', '중식', '일식', '서양식', '기타 외국식', '패스트푸드', '치킨', '피자', '제과제빵', '아이스크림/빙수', '커피', '음료(커피 외)', '주점', '기타 외식']

middle_category = {'A1': '한식', 'B1': '분식', 'C1': '중식', 'D1': '일식', 'E1': '서양식', 'F1': '기타 외국식',
                   'G1': '패스트푸드', 'H1': '치킨', 'I1': '피자', 'J1': '제과제빵', 'K1': '아이스크림/빙수',
                   'L1': '커피', 'M1': '음료(커피 외)', 'N1': '주점', 'O1': '기타 외식'}

# 비교항목
# 업종별/가맹본부별/브랜드별[0, 1, 2]에 항목 달라짐
# 브랜드별(listBrand01-03) - 브랜드 개요 / 가맹점 현황 정보 / 가맹점 창업 비용
main_compare = ['1', '2', '3']

listBrand = ['listBrand01', 'listBrand02', 'listBrand03']

# csv 저장될 속성 리스트
column_list = ['업종']

i = 0
delay = 1

# csv에 하나하나 저장될 컬럼
table_list = []
total_list = []

# 저장할 csv 파일 이름
csv_file_name = '_listBrand.csv'

for year in years:
    header_flag = False
    with open('정보공개서/' + year + csv_file_name, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        browser = webdriver.Chrome('chromedriver.exe')
        browser.get('https://franchise.ftc.go.kr/mnu/00014/program/firHope/view.do')

        time.sleep(delay)
        # 년도
        year_category = Select(browser.find_element_by_id('selYear'))
        year_category.select_by_value(year)

        for value in middle_category_list:
            # 대비교 항목
            sub_compare_category = Select(browser.find_element_by_id('searchCondition'))
            sub_compare_category.select_by_value(main_compare[2])

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

            # 검색
            browser.find_element_by_xpath('//input[@alt="검색"]').click()
            time.sleep(delay)

            # 컬럼 속성 값 입력
            if not header_flag:
                writer.writerow(['업종', '브랜드', '상호', '평균매출액'])
                print(['업종', '브랜드', '상호', '평균매출액'])
                header_flag = True

            tbody = browser.find_element_by_tag_name('table').find_element_by_tag_name('tbody')

            try:
                trs = tbody.find_elements_by_tag_name('tr')

                avg_flag = True
                for tr in trs:
                    if avg_flag:
                        avg_flag = False
                        continue
                    else:
                        tds = tr.find_elements_by_tag_name('td')
                        if tds[7].text == '0':
                            continue

                        if tds[7].text.split(','):
                            temp = ''
                            arr = tds[7].text.split(',')
                            for data in arr:
                                temp += data
                        else:
                            temp = tds[7].text

                        table_list = [middle_category_kor[middle_category_list.index(value)],
                                      tds[0].text, tds[1].text, temp]
                        if table_list not in total_list:
                            total_list.append(table_list)
                            writer.writerow(table_list)
                            print(table_list)

                        table_list = []
            except NoSuchElementException:
                print('exception: There is no such element..')
            except TimeoutError:
                print('exception: timeout..')

print('finish')
