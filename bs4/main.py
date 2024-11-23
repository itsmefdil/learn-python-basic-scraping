from bs4 import BeautifulSoup
import requests

website = 'https://subslikescript.com/movie/Titanic-46435'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())

box = soup.find('article', class_='main-article')

title = box.find('h1').get_text()
plot = box.find('p', class_='plot').get_text()
transcript = box.find('div', class_='full-script').get_text(strip=True , separator='\n')

# print(title)
# print(plot)
# print(transcript)

# with open ('titanic.txt', 'w') as file:
#     file.write(title + '\n\n')
#     file.write(plot + '\n\n')
#     file.write(transcript)

with open(f'{title}.txt', 'w') as file:
    file.write(transcript)
