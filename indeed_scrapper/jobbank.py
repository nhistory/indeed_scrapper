from selenium import webdriver
from bs4 import BeautifulSoup

# make webdrive object
driver = webdriver.Chrome('/Users/leesehwan/Downloads/chromedriver')
URL = "https://www.jobbank.gc.ca/jobsearch/jobsearch?sort=M&searchstring=developer"
# set loading time for 3 seconds
driver.implicitly_wait(3)
driver.get(URL)

# parse page html source by selenium
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# count number of full pages
pages = soup.find("span", {"class": "found"}).string
full_pages = int(pages) // 25


def show_more_page():
    # find element of more result btn
    more_result = driver.find_element_by_id('moreresultbutton')
    more_result.click()
    driver.get(URL)


for i in range(10):
    show_more_page()
