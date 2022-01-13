import pandas as pd
import bs4
#import requests
#import re
#from fake_useragent import UserAgent
from selenium import webdriver

"""
ua = UserAgent()
print(ua.chrome)

header = {'User-Agent':str(ua.chrome)}
url = "https://stats.paj.gr.jp/en/pub/htmls/20220108_en_n2.html"

res = requests.get(url, headers=header)
print(res.url)

res = requests.get(url, headers=header, allow_redirects= False)
print("------")
print(res.text)
"""
## KEEPS REDIRECTING to index.php

#Using Selenium
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://stats.paj.gr.jp/en/pub/htmls/20220108_en_n2.html")

#Get pass the redirect
element = driver.find_element_by_link_text('Agree')
element.click()

#Get to last week all Japan
elements = driver.find_elements_by_xpath('//*[@href]')
elements[3].click()

#Get the page code
html = driver.page_source
driver.quit()


#Convert to BS
soup = bs4.BeautifulSoup(html,"lxml")

#Get tables
table = soup.find_all('table')[1]

#Table Scrape function
def table_scrape(table_num):

    data = []
    list_header = [" ", "Current week"]

    # for getting the data
    HTML_data = soup.find_all("table")[1].find_all("table")[table_num].find_all("tr")[1:]

    for element in HTML_data:
        sub_data = []
        for sub_element in element:
            try:
                if sub_element.get_text() != "" and sub_element.get_text() != "\n" and "Sul" not in sub_element.get_text():
                    sub_data.append(sub_element.get_text())
            except:
                continue
        data.append(sub_data)
    #print(data)

    for row in data:
        del row[2:]

    #Storing the data into Pandas
    file_name = str(table.find_all("u")[table_num].getText())
    file_name = file_name.replace("\n", "")
    file_name = file_name + ".csv"

    #create DataFrame
    dataFrame = pd.DataFrame(data=data, columns=list_header)

    #Converting Pandas DataFrame into CSV file
    dataFrame.to_csv(file_name, mode='w+')

#Run through all tables
for table_no in range(0,6):
    table_scrape(table_no)
