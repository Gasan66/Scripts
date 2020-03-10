from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from collections import Counter

html = urlopen('https://stepik.org/media/attachments/lesson/209719/2.html').read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
res = soup.find_all('code')
print(res)
page = str(html)

list_page = []
state = 0

for sym in page:
    if sym == '<':
        state = 1

result = Counter(sorted(re.findall(r'<code>(.*?)</code>', page)))

print(result)
