import urllib.request
import zipfile
import xlrd


url = 'https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip'
zip_file, headers = urllib.request.urlretrieve(url, 'rogaikopyta.zip')
ext_dir = 'archives'
# print(zipfile.is_zipfile(zip_file))
archive = zipfile.ZipFile(zip_file, 'r')
files = archive.namelist()
employee_list = []
# archive.extractall(ext_dir)
# print(archive.printdir())
# print(files)

for file in files:
    wb = xlrd.open_workbook(ext_dir + '/' + file)
    sheet = wb.sheet_by_index(0)
    employee_list.append((sheet.cell_value(1, 1), int(sheet.cell_value(1, 3))))
    # print(sheet.cell_value(1, 1), sheet.cell_value(1, 3))
# print(sorted(employee_list))
for employee in sorted(employee_list):
    print(*employee)
