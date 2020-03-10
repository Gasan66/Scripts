import xlrd
from statistics import mean

wb = xlrd.open_workbook('salaries.xlsx')
sheet_names = wb.sheet_names()
sheet = wb.sheet_by_name(sheet_names[0])
regions = [''.join(list(x.split())) for x in sheet.col_values(0)[1:]]
profs = [' '.join(list(x.split())) for x in sheet.row_values(0)[1:]]
price_region = []
price_prof = []
# row = sheet.row_values(1)
for row in range(1, sheet.nrows):
    region = sheet.row_values(row)[0]
    list_of_price_region = sorted(sheet.row_values(row)[1:])
    med_price = list_of_price_region[len(list_of_price_region) // 2]
    price_region.append((region, med_price))

for col in range(1, sheet.ncols):
    prof = sheet.col_values(col)[0]
    list_of_price_prof = [int(i) for i in sheet.col_values(col)[1:]]
    avg_price = mean(list_of_price_prof)
    price_prof.append((prof, avg_price))



    # region = sheet.row_values(row)[0]
    # list_of_price = sorted(sheet.row_values(row)[1:])
    # price = list_of_price[len(list_of_price) // 2]
    # # print(price)
    # regions.append((region, price))

print(price_prof)
print(price_region)
print(sorted(price_prof, key=lambda x: x[1], reverse=True), sorted(price_region, key=lambda x: x[1], reverse=True), sep='\n')
