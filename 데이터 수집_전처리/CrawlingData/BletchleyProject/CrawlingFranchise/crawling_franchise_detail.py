from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import csv

origin_link = 'https://franchise.ftc.go.kr'

link_str =\
    "https://franchise.ftc.go.kr/mnu/00013/program/userRqst/list.do?" \
    "searchCondition=&searchKeyword=&column=tNm&selUpjong=21&selIndus=&pageUnit=300&pageIndex="

delay = 0.5

table_list = []
column_list = []

prev = time.process_time()
with open('../DeprecatedCSVs/2020_PublicInfoDetails.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    browser = webdriver.Chrome('chromedriver.exe')

    flag = False

    # 1 ~ 21
    for value in range(1, 22):
        # 이동
        browser.get(link_str + str(value))
        time.sleep(delay)

        # 컬럼 속성 값 입력; 한번만 실행하면 됨
        if not flag:
            for head in browser.find_element_by_tag_name('thead').find_element_by_tag_name('tr') \
                    .find_elements_by_tag_name('th'):
                column_list.append(head.text)
            column_list.append('링크')

            print(column_list)
            writer.writerow(column_list)
            flag = True

        tbody = browser.find_element_by_tag_name('table').find_element_by_tag_name('tbody')

        try:
            trs = tbody.find_elements_by_tag_name('tr')

            i = 0
            for tr in trs:
                tds = tr.find_elements_by_tag_name('td')
                link = tds[1].find_elements_by_xpath('//a[@class="authCtrl"]')[i].get_attribute('onclick')
                i += 2

                for td in tds:
                    table_list.append(td.text)
                table_list.append(origin_link + link[9:len(link) - 3])

                print(table_list)
                writer.writerow(table_list)
                table_list = []

        except:
            print('error')

print('complete')