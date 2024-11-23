from bs4 import BeautifulSoup
import requests

root = 'https://subslikescript.com'
website = f'{root}/movies'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())

box = soup.find('article', class_='main-article')
links = box.findAll('a', href=True)

links_list = []
for link in links:
    links_list.append(root + link['href'])

print(links_list)
