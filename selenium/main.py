from selenium import webdriver
import pandas as pd
import re

website = "https://www.adamchoi.co.uk/overs/detailed"
path = "./chromedriver"
driver = webdriver.Chrome(path)
driver.get(website)

am_btn = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')

am_btn.click()

matchs = driver.find_elements_by_tag_name('tr')

date = []
home_team = []
score = []
away_team = []

for match in matchs:
    try:
        date_text = match.find_element_by_xpath('./td[1]').text
        home_text = match.find_element_by_xpath('./td[2]').text
        score_text = match.find_element_by_xpath('./td[3]').text
        away_text = match.find_element_by_xpath('./td[4]').text

        # Clean the text
        date_text = re.sub(r'Next match.*', '', date_text).strip()
        home_text = re.sub(r'Next match.*', '', home_text).strip()
        score_text = re.sub(r'Next match.*', '', score_text).strip()
        away_text = re.sub(r'Next match.*', '', away_text).strip()

        date.append(date_text)
        home_team.append(home_text)
        score.append(score_text)
        away_team.append(away_text)

    except Exception as e:
        print(f"Skipping a row due to an error: {e}")
        continue

driver.quit()

# Print lengths of lists to debug
print(f"Lengths - date: {len(date)}, home_team: {len(home_team)}, score: {len(score)}, away_team: {len(away_team)}")

# Ensure all lists have the same length before creating the DataFrame
min_length = min(len(date), len(home_team), len(score), len(away_team))
date = date[:min_length]
home_team = home_team[:min_length]
score = score[:min_length]
away_team = away_team[:min_length]

df = pd.DataFrame({'date': date , 'home_team': home_team, 'score': score,'away_team': away_team})

df.to_csv('footbal_data.csv', index=False)
print(df)
