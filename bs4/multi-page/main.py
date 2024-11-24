from bs4 import BeautifulSoup
import requests
import os
import time

root = 'https://subslikescript.com'
website = f'{root}/movies_letter-A'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())

# pagination
pagination = soup.find('ul', class_='pagination')
pages = pagination.find_all('li', class_='page-item')
last_page = pages[-2].text
print("Last page is: ", last_page)


for page in range(1, int(last_page)+1):
    print(f"Scraping page {page}")
    print(f'{website}?page={page}')
    result = requests.get(f'{website}?page={page}')
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    box = soup.find('article', class_='main-article')

    links = []
    for link in box.find_all('a', href=True):
        links.append(link['href'])

    # print(links)

    for link in links:
        time.sleep(1)
        try:
            result = requests.get(f'{root}/{link}')
            content = result.text
            soup = BeautifulSoup(content, 'lxml')

            box = soup.find('article', class_='main-article')

            title = box.find('h1').get_text()
            transcript = box.find('div', class_='full-script').get_text(strip=True , separator='\n')

            print("============== SCRAPED ==============")
            print("title :", title)
            print("time :" , time.strftime("%H:%M:%S", time.localtime()))
            print("file_name :", title+".txt")
            print("=====================================")
            os.makedirs('movies', exist_ok=True)
            with open(os.path.join('movies', f'{title}.txt'), 'w', encoding='utf-8') as file:
                    file.write(transcript)
        except:
            print("____Link not working____")
            print(link)

print("Scraping done!")
