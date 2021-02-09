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
    image_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars1.jpg"
    browser.visit(featured_image_url)

    # Scrape the image into Soup
    img_html = browser.html
    img_soup = BeautifulSoup(img_html, 'html.parser')
        
    mars_img = img_soup.find_all('img')
    mars_img_path = mars_img.get('src')
    featured_image_url = image_url +  mars_img_path
    print(featured_image_url)

    
    # Visit the Mars Facts site
    marsfacts = 'https://space-facts.com/mars/'

    # Read html and convert to dataframe
    facts_table = pd.read_html(marsfacts)
    df = facts_table[0]
    df.columns = ['facts', 'value']
    df.set_index('facts', inplace=True)
    df

    # Convert the data to an HTML table string
    facts_html = df.to_html()
    facts_html = facts_html.replace('\n', '')
    facts_html

    # Visit the Mars Hemispheres site
        usgs_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(usgs_url)

        # Scrape page into Soup
        html_usgs_mars = browser.html
        soup_usgs_mars = BeautifulSoup(html_usgs_mars, 'html.parser')

        # Get all Mars Hemisphere image attributes
        mars_all_items = soup_usgs_mars.find_all('div', class_='item')
        url_usgs = 'https://astrogeology.usgs.gov'

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
