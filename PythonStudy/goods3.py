import xlrd

wb = xlrd.open_workbook('trekking3.xlsx')
sheet_names = wb.sheet_names()
menu_sheet = wb.sheet_by_name(sheet_names[1])
content_sheet = wb.sheet_by_name(sheet_names[0])

day_numbers = list(set(menu_sheet.col_values(0)[1:]))
day_numbers.sort()
print(day_numbers)

# kcal = 0
# proteins = 0
# fats = 0
# carbs = 0

for day in day_numbers:
    kcal = 0
    proteins = 0
    fats = 0
    carbs = 0
    for menu_row in range(1, menu_sheet.nrows):
        # print(menu_sheet.row_values(menu_row)[0])
        if day == menu_sheet.row_values(menu_row)[0]:
            for content_row in range(1, content_sheet.nrows):
                if menu_sheet.row_values(menu_row)[1] == content_sheet.row_values(content_row)[0]:
                    list_of_content = [0 if x == '' else x for x in content_sheet.row_values(content_row)]
                    kcal += menu_sheet.row_values(menu_row)[2]/100 * list_of_content[1]
                    proteins += menu_sheet.row_values(menu_row)[2]/100 * list_of_content[2]
                    fats += menu_sheet.row_values(menu_row)[2]/100 * list_of_content[3]
                    carbs += menu_sheet.row_values(menu_row)[2]/100 * list_of_content[4]
                    # print(menu_sheet.row_values(menu_row), [0 if x == '' else x for x in content_sheet.row_values(content_row)])
    print(int(kcal), int(proteins), int(fats), int(carbs))
