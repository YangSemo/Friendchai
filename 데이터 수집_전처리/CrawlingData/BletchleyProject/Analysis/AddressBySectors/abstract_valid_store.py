"""
FinalBrand.csv에 속하지 않는 모든 가게(store)를 제거하고 유효한(valid) 것을 추출(abstract)한다.

"""

import csv
import time

start_time = time.time()

"""
전처리 작업 #1
FinalBrand 내 있는 실존 점포를 가져왔다.

결과: FinalStoreAddress.csv
점포가 브랜드의 업종을 따라가지 않았다. *이는 데이터가 이상함을 말함 💀
"""
# brand_list = []
# with open('../../FinalBrand.csv', 'r', encoding='utf-8-sig', newline='') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         brand_list.append(row[2])

# ['기타음식점', '분식', '양식', '일식', '제과제빵떡케익', '중식', '커피점', '패스트푸드', '한식']
# sector = '한식'
# store_list = []
# with open(sector + '.csv', 'r', encoding='utf-8-sig', newline='') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         store_list.append(row)
#
# total_list = []
# i = 0
# for store in store_list:
#     for brand in brand_list:
#         if brand.__contains__(store[1]) or store.__contains__(brand):
#             i += 1
#             if i >= 1000:
#                 i = 0
#                 print([sector] + store[1:])
#             total_list.append([sector] + store[1:])
#
# with open('KoreanStoreAddress.csv', 'w', encoding='utf-8-sig', newline='') as f:
#     writer = csv.writer(f)
#     for row in total_list:
#         writer.writerow(row)

"""
전처리 작업 #2
점포의 업종을 모두 제거한 상태로 만듬 FinalStoreAddress_2.csv
"""
# total_list = []
# comp_list = []
# sectors = ['Korean', 'Chinese', 'Japanese', 'Occidental', 'Coffee', 'Etc', 'Fastfood', 'Snack', 'Chicken', 'Bread']
# for sector in sectors:
#     with open(sector + 'StoreAddress.csv', 'r', encoding='utf-8-sig', newline='') as f:
#         reader = csv.reader(f)
#         for row in reader:
#             total_list.append(row[1:])
#             # if row[1:] not in comp_list:
#                 # comp_list.append(row[1:])
#     print(sector, len(total_list))
#
# print('read done')
# total_list.sort(key=lambda x: [x[0], x[1]])
#
# with open('FinalStoreAddress_2.csv', 'w', encoding='utf-8-sig', newline='') as f:
#     writer = csv.writer(f)
#     for row in total_list:
#         writer.writerow(row)

"""
전처리 작업 #3
기존에는 이상했던 점포의 업종을
브랜드에 등록된 업종의 이름으로
모든 점포의 업종을 새로 부여했다
FinalStoreAddress_3.csv 
"""
brand_list = []
with open('../../FinalBrand.csv', 'r', encoding='utf-8-sig', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        brand_list.append(row[1:3])

store_list = []
with open('FinalStoreAddress_2.csv', 'r', encoding='utf-8-sig', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        store_list.append(row)

# 6000 x 90000 = 540,000,000 times
total_list = []
comp_list = []
i = 0
for brand in brand_list:
    for store in store_list:
        if brand.__contains__(store[0]) or store[0].__contains__(brand[1]):
            if store not in comp_list:
                i += 1
                comp_list.append(store)
                total_list.append([brand[0]] + store)
                if i >= 1000:
                    i = 0
                    print([brand[0]] + store)

with open('FinalStoreAddress_3.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    i = 0
    for row in total_list:
        i += 1
        writer.writerow([i] + row)

print('Elapsed: ', time.time() - start_time)
