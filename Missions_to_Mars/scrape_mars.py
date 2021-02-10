from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd


def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

mars_data = {}

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
    browser.visit(image_url)

    time.sleep(1)

    # Scrape the image into Soup
    img_html = browser.html
    img_soup = bs(img_html, 'html.parser')
        
    for link in img_soup.find_all('img'):
        featured_image_url = link.get('src')

    print(featured_image_url)

    
    # Visit the Mars Facts site
    marsfacts = 'https://space-facts.com/mars/'

    # # use read_html to scrape out tables and select the relevant table 
    # convert to dataframe
    facts_table = pd.read_html(marsfacts)
    df = facts_table[0]
    df.columns = ['facts', 'value']
    df.set_index('facts', inplace=True)
    df

    # Convert the dataframe to an HTML table string
    facts_html = df.to_html()
    facts_html = facts_html.replace('\n', '')
    facts_html

    # Visit the Mars Hemispheres site
    usgs_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(usgs_url)

    # Scrape page into Soup
    usgs_html = browser.html
    usgs_soup = bs(usgs_html, 'html.parser')

    # Inspect and find relevant tags
    usgs_all = usgs_soup.find_all('div', class_='item')
    usgs = 'https://astrogeology.usgs.gov'


    # Define an empty list to hold the urls
    hemisphere_urls = []

    # Run a loop 
    for x in usgs_all:
        # Get the title of the hemisphere image
        title = x.find('h3').text
            
        # Get the path of hemisphere image
        img_path = x.find('a',class_='itemLink product-item')['href']
            
        #Visit the image url
        browser.visit(usgs + img_path)
            
        # Scrape the page
        usgs_html_path = browser.html
        usgs_soup_html = bs(usgs_html_path, 'html.parser')
            
        # Get the full image url
        img_tag = usgs_soup_html.find('div', class_ = 'downloads')
        hem_img_url = img_tag.find('a')['href']
            
        #Append the dictionary with the image url string and the hemisphere title
        hemisphere_urls.append({'title': title, 'img_url': hem_img_url})
        
    # Display the Mars Hemisphere image url list
    print(hemisphere_urls)
        
    # Append all data 
    mars_data['news_title'] = news_title
    mars_data['news_para'] = news_para
    mars_data['featured_image_url'] = featured_image_url
    mars_data['facts'] = facts_html
    mars_data['hemisphere_urls'] = hemisphere_urls

    # Return results
    return mars_data


    # Close the browser after scraping
    browser.quit()
