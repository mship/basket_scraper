# web scraper using BeautifulSoup
# by Michael Shippee
# first import necessary libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
# this holds the target URL
scrape_this = "https://giftbasketsdenver.com/collections/gift-baskets"
# open the page, read it as html, then close page
request_page = urlopen(url=scrape_this)
page_html = request_page.read()
request_page.close()
# per BeautifulSoup documentation, calling our html parser 'soup'
soup = BeautifulSoup(page_html, 'html.parser')
# find all divs with class based on investigating page's URL
baskets = soup.find_all('div', class_='thumbnail__caption textAlign--center')
# iterate through. could also save results to a CSV or spreadsheet
for basket in baskets:
    # save the text based on some other types. Price class ended up with new lines that messed with formatting, so strip is necessary
    title = basket.find('a', class_='hidden-product-link').text
    price = basket.find('span', class_='money').text.strip()

    print(title + ", " + price)
