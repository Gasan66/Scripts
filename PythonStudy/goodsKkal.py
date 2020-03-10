import xlrd

wb = xlrd.open_workbook('trekking1.xlsx')
sheet_names = wb.sheet_names()
sheet = wb.sheet_by_name(sheet_names[0])
goods = []

for row in range(1, sheet.nrows):
    goods.append((sheet.row_values(row)[0], int(sheet.row_values(row)[1])))

goods.sort(key=lambda x: (-x[1], x[0]))
for good in goods:
    print(good[0])
# print(goods)
# print(*sorted(goods, key=lambda x: (-x[1], x[0])), sep='\n')
