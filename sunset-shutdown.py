from bs4 import BeautifulSoup
import os
import time
import requests
import pandas as pd

country = input('Which country are you in?').lower()
city = input('Which city are you in?').lower()

page = requests.get('https://www.timeanddate.com/sun/' + country + '/' + city)

soup = BeautifulSoup(page.text, 'html.parser')

sunset = soup.find_all('p', class_ = 'dn-mob')[0].text.split()[2][:5]

sunset_datetime = pd.to_datetime(sunset)

starttime=time.time()
while True:
    now = pd.to_datetime('today')
    print(f"now is :[{now}], sunset is: [{sunset_datetime}]")
    if now > sunset_datetime:
        os.system('systemctl poweroff') 
        os.system("shutdown /s /t 1")
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))

