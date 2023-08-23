from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
import glob


from selenium import webdriver
website = 'https://trends.google.com/trends/?geo=US'
options = Options()
options.add_experimental_option("prefs", {
 "download.default_directory": r"C:\Users\trends\Desktop\Trends\output_files_mobile_games"
  })
driver = webdriver.Chrome(options=options)
driver.get(website)
driver.maximize_window()

btn = driver.find_element(
    "xpath", '//button[@class="UywwFc-LgbsSe UywwFc-LgbsSe-OWXEXe-dgl2Hf Qt4Qjb"]')
btn.click()

#select months button
WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    (By.XPATH, '//md-select-value[@id="select_value_label_9"]'))).click()

#select 12 months from dropdown
WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    (By.XPATH, '//md-option[@id="select_option_19"]'))).click()

#select input field
element = driver.find_element("xpath", '//input[@id="input-24"]')


# Erase 3 characters from the end of the entered text
time.sleep(5)
element.send_keys(Keys.CONTROL + "A")
element.send_keys(Keys.BACKSPACE)
# element.send_keys(30*Keys.BACKSPACE)
# time.sleep(5)
element.send_keys("mobile game")
# element.clear()
element.send_keys(Keys.ENTER)
time.sleep(5)

# Code for clicking on cookie, Got It button at the aitom of the screen
# WebDriverWait(driver, 1).until(EC.element_to_be_clickable(
#     (By.XPATH, "/html/body/div[1]/div/span[2]/a[2]"))).click()
# time.sleep(1)

# START : code for downloading CSV
#Multi Timeline download
WebDriverWait(driver, 1).until(EC.element_to_be_clickable(
    (By.XPATH, '//button[@class="widget-actions-item export"][1]'))).click()
time.sleep(1)

#Related Queries Download
time.sleep(1)
WebDriverWait(driver, 1).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div[2]/div[2]/div/md-content/div/div/div[4]/trends-widget/ng-include/widget/div/div/div/widget-actions/div/button[1]"))).click()
time.sleep(1)
# END : code for downloading CSV
print("seed timeline and queries downloaded")


# -------------------------------------
# Logic for Getting Rising and Top Queries as array
time.sleep(1)
import numpy as np
df = pd.read_csv('output_files_mobile_games/relatedQueries.csv',names=['Query', 'Value'])
found = df[(df.Query == "TOP")].index.values[0]
found2 = df[(df.Query == "RISING")].index.values[0]

last = df.index[-1]

top = df.iloc[found+1:found2-1]
rising = df.iloc[found2+1:last]

toparr = top['Query'].to_numpy()
risingarr = rising['Query'].to_numpy()

#----------------------
topcount = 1
risingcount = 1
print("starting: all seed children timeline and queries download")
for i in toparr:
    print(f"{topcount}: {i}")
    element.send_keys(Keys.CONTROL + "A")
    element.send_keys(Keys.BACKSPACE)
    element.send_keys(i)
    element.send_keys(Keys.ENTER)
    time.sleep(5)

    # START : code for downloading CSV
    # COMMENTEDTIMELINE NOT REQUIRED
    #multi timeline csv
    # try:
    #     WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
    #         (By.XPATH, '//button[@class="widget-actions-item export"][1]'))).click()
    #     time.sleep(1)
    # except:
    #     print("Seed Children's Timeline: Unable to click donwnload")


    # related Queries csv
    try:
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
            (By.XPATH,
             "/html/body/div[2]/div[2]/div/md-content/div/div/div[4]/trends-widget/ng-include/widget/div/div/div/widget-actions/div/button[1]"))).click()
        time.sleep(1)
    except:
        print(f"{i}'s Related Queries: Unable to click donwnload")
        time.sleep(100)
    topcount = topcount+1

#RISING PART
for j in risingarr:
    print(f"{risingcount}: {j}")
    element.send_keys(Keys.CONTROL + "A")
    element.send_keys(Keys.BACKSPACE)
    element.send_keys(j)
    element.send_keys(Keys.ENTER)
    time.sleep(5)

    # START : code for downloading CSV
    # multi timeline csv
    #COMMENTEDTIMELINE NOT REQUIRED
    # try:
    #     WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
    #         (By.XPATH, '//button[@class="widget-actions-item export"][1]'))).click()
    #     time.sleep(1)
    # except:
    #     print("Seed Children's Timeline: Unable to click donwnload")

    # related Queries csv

    try:
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
            (By.XPATH,
             "/html/body/div[2]/div[2]/div/md-content/div/div/div[4]/trends-widget/ng-include/widget/div/div/div/widget-actions/div/button[1]"))).click()
        time.sleep(1)
    except:
        print(f"{j}'s Related Queries: Unable to click donwnload")
        time.sleep(100)
    risingcount = risingcount + 1

print("completed: all seed children timeline and queries download")


#allrealtedqueries in one big csv

csv_files = glob.glob('output_files_mobile_games/relatedQueries *.{}'.format('csv'))
df_csv_append = pd.DataFrame()
# append the CSV files
l = []
for f in csv_files:
    l.append(pd.read_csv(f,names=['Query', 'Value']))

df_res = pd.concat(l, ignore_index=True)

df2 = df_res.drop_duplicates(subset=['Query'])
df2 = df2.dropna(subset=['Value'])
df2.reset_index(inplace=True)
df2.pop('index')
df2.to_csv('MasterQueries.csv')

print("Master Sheet Created")
print(df2)

# ----------------REPEAT2 for MASTER RELATED QUERIES---------------------
# Logic for Getting Rising and Top Queries as array
import numpy as np
df = pd.read_csv('MasterQueries.csv')

toparr = df['Query'].to_numpy()
print(toparr)

#----------------------

print("starting: all seed grandchildren timeline download")
count2 = 1
for i in toparr:
    print(count2)
    element.send_keys(Keys.CONTROL + "A")
    element.send_keys(Keys.BACKSPACE)
    element.send_keys(i)
    element.send_keys(Keys.ENTER)
    time.sleep(5)

    # START : code for downloading CSV
    #multi timeline csv
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, '//button[@class="widget-actions-item export"][1]'))).click()
        time.sleep(5)
    except:
        print(f"{i}'s Timeline: Unable to Download")
        time.sleep(100)
    count2 = count2 + 1

print("completed: all seed grandchildren timeline download")

#----------ALL MULTITIMELINE DATA IN CSV------

