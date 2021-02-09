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

    
    # Visit the JPL url to get the image
    image_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    browser.visit(image_url)

    # Scrape the image into Soup
    img_html = browser.html
    img_soup = BeautifulSoup(img_html, 'html.parser')
    
    # Click FULL IMAGE link
    browser.click_link_by_partial_text('FULL IMAGE')
    
    featured_image_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars2.jpg"
    soup.find_all('img')[2]["src"]
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
