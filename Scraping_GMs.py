#important libraries for web scraping
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

#choosing window size options
options = Options()
options.add_argument("window-size=1920,1080")

#creating fake user agents
ua = UserAgent()
user_agent = ua.random
options.add_argument(f'user-agent={user_agent}')

#setting the browser for scraping
driver = webdriver.Chrome(options=options)

#we perform the actions on chess.com
try:
    driver.get(url='https://www.chess.com/players')
    for i in range(1, 26): #this is the algorithm for this specific website
        player_name = driver.find_element(By.CSS_SELECTOR, f"#view-master-players > div > div.post-preview-list-component > div:nth-child({i}) > div > h2 > a.master-players-player-name > span.post-author-name").text
        player_stats = driver.find_element(By.CSS_SELECTOR, f"#view-master-players > div > div.post-preview-list-component > div:nth-child({i}) > div > h2 > a.master-players-world-stats").text
        player_title = driver.find_element(By.CSS_SELECTOR, f"#view-master-players > div > div.post-preview-list-component > div:nth-child({i}) > div > h2 > a.master-players-player-name > span.master-players-chess-title").text
        print(player_stats,player_title,player_name)
        time.sleep(0.3)
#in case the website's servers are off
except Exception as ex:
    print(ex.__class__.__name__)
#clossing the window when the program is finished
finally:
    driver.close()
    driver.quit()