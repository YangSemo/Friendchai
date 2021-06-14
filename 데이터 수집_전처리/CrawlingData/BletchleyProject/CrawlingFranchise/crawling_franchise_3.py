import csv
import numpy as np
import time

start = time.time()
print('start:', start)
years = ['2020', '2019']
file_name = '_listBrand.csv'

list_2020 = []
list_2019 = []

for year in years:
    with open('정보공개서//' + year + file_name, 'r', encoding='utf-8-sig', newline='') as f:
        reader = csv.reader(f)
        i = 0
        for row in reader:
            if i == 0:
                i += 1
                continue

            if year == '2020':
                list_2020.append(np.array(row))
            elif year == '2019':
                list_2019.append(np.array(row))

list_2020.sort(key=lambda x: (x[0], x[1]))
list_2019.sort(key=lambda x: (x[0], x[1]))

temp20 = sorted(np.array(list_2020)[:, :3], key=lambda x: (x[0], x[1]))
temp19 = sorted(np.array(list_2019)[:, :3], key=lambda x: (x[0], x[1]))

commons = []
for row20 in temp20:
    for row19 in temp19:
        if np.array_equal(row20, row19):
            commons.append(row20)
            break
print(len(commons), commons)

equal_20 = []
for row20 in list_2020:
    for row in commons:
        if np.array_equal(row20[:3], row):
            # print('.', end='')
            equal_20.append(row20)
            break

equal_19 = []
for row19 in list_2019:
    for row in commons:
        if np.array_equal(row19[:3], row):
            # print('.', end='')
            equal_19.append(row19)
            break

with open('../Analysis/Clustering/avgs.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    for i in range(0, len(equal_20)):
        if np.array_equal(equal_20[i][:3], equal_19[i][:3]):
            a = int(equal_19[i][3])
            b = int(equal_20[i][3])
            writer.writerow(
                list(equal_20[i][:3]) + [round(((int(equal_20[i][3]) - int(equal_19[i][3])) / int(equal_19[i][3])) * 100, 2)])

#
# with open('merged_avg_2.csv', 'w', encoding='utf-8-sig', newline='') as f:
#     writer = csv.writer(f)
#     for i in range(0, len(equal_20)):
#         if np.array_equal(equal_20[i][:3], equal_19[i][:3]) and np.array_equal(equal_20[i][:3], equal_18[i][:3]) \
#                 and np.array_equal(equal_18[i][:3], equal_19[i][:3]):
#             arr = list(equal_20[i][:3])
#             print(int(equal_20[i][3]), ' + ', int(equal_19[i][3]), ' + ', int(equal_18[i][3]), ' = ',
#                   (int(equal_20[i][3]) + int(equal_19[i][3]) + int(equal_18[i][3])) / 3)
#             writer.writerow(
#                 arr + [round(((int(equal_20[i][3]) + int(equal_19[i][3]) + int(equal_18[i][3])) / 3), 2)])

print('\ncomplete\n', '경과시간: ', time.time() - start)
