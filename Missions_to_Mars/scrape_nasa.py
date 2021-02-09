from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()

    # Visit NASA news
    url = "https://mars.nasa.gov/news"
    browser.visit(url)

    time.sleep(1)

    # Scrape the page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the news title (inspected the webpage)
    news_title = soup.find('div', class_='content_title').text

    # Get news para
    news_para = soup.find('div', class_='article_teaser_body').text

    # Get the max avg temp
    max_temp = avg_temps.find_all('strong')[1].text

    # BONUS: Find the src for the sloth image
    relative_image_path = soup.find_all('img')[2]["src"]
    sloth_img = url + relative_image_path

    # Store data in a dictionary
    costa_data = {
        "sloth_img": sloth_img,
        "min_temp": min_temp,
        "max_temp": max_temp
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return costa_data
