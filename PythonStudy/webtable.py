from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://stepik.org/media/attachments/lesson/209723/5.html').read().decode('utf-8')
soup = BeautifulSoup(html, 'html5lib')
table = soup.find('table')
# table_body = table.find('tbody')
rows = table.find_all_next('tr')

res = 0

for row in rows:
    for element in row.find_all('td'):
        res += int(element.get_text())
        print(element.get_text())
print(res)

# print(rows)
