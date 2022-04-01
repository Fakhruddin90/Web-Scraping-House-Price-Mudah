# %%time
# measure the execution time

# run this code if selenium packages not install in your machine
# !pip install selenium

# import packages
from selenium import webdriver
import pandas as pd
import time

# create variables array for storing informations
house_titles = []
house_types = []
house_prices = []
house_bedrooms = []
house_bathrooms = []
house_areas = []
house_locations = []
house_releases_date = []
house_urls = []

def scrape(main_url, pages):
    
    # load chrome browser
    # for macos
    # webdriver_path = '/Users/fakhruddinmohamadsaupe/Documents/Development/JupyterNotebook/Web-Scraping-House-Price-Mudah_my'
    driver = webdriver.Safari()

    # for windows 
    # driver = webdriver.Chrome()
    
    # dynamic url for pages
    def get_url(main_url, page):
        """Generate url by page"""
        #     url ='https://www.mudah.my/putrajaya/houses-for-sale-2040?o=' + str(page)
        url = main_url + str(page)
        return url

    # ask user to input maximum page that need to be scrap
    # max_page = driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div[1]').text[-3:]
    # max_page = int(max_page)
    #max_page = int(input("Please insert maximum page to scrap: "))

    # iterate code by page
    for page in range(1,pages+1):
        url = get_url(main_url, page)
        driver.get(url)

        # fetch information using xpath
        titles = driver.find_elements_by_xpath('//*[@id="__next"]/div[3]/div[4]/div[1]/div/div[2]/a')
        types = driver.find_elements_by_xpath('//*[@id="__next"]/div[3]/div[4]/div[1]/div/div[2]/div[2]/div[1]/div')
        prices = driver.find_elements_by_xpath('//*[@id="__next"]/div[3]/div[4]/div[1]/div/div[2]/div[1]/div')
        bedrooms = driver.find_elements_by_xpath('//*[@id="__next"]/div[3]/div[4]/div[1]/div/div[2]/div[2]/div[3]/div')
        bathrooms = driver.find_elements_by_xpath('//*[@id="__next"]/div[3]/div[4]/div[1]/div/div[2]/div[2]/div[4]/div')
        areas = driver.find_elements_by_xpath('//*[@id="__next"]/div[3]/div[4]/div[1]/div/div[2]/div[2]/div[2]/div')
        locations = driver.find_elements_by_xpath('//*[@id="__next"]/div[3]/div[4]/div[1]/div/div[3]/div[1]/span[2]/span')
        releases_date = driver.find_elements_by_xpath('//*[@id="__next"]/div[3]/div[4]/div[1]/div/div[3]/div[1]/span[1]/span')
        urls = driver.find_elements_by_xpath('//*[@id="__next"]/div[3]/div[4]/div[1]/div/div[2]/a')

        # loop through the iterations and append in the arrays
        for title in titles:
            house_titles.append(title.text)
        
        for type_ in types:
            house_types.append(type_.text)

        for price in prices:
            house_prices.append(price.text)

        for bedroom in bedrooms:
            house_bedrooms.append(bedroom.text)

        for bathroom in bathrooms:
            house_bathrooms.append(bathroom.text)

        for area in areas:
            house_areas.append(area.text)

        for location in locations:
            house_locations.append(location.text)

        for release_date in releases_date:
            house_releases_date.append(release_date.text)

        for url in urls:
            house_urls.append(url.get_attribute('href'))

    #     time.sleep(0.5)
    
    # quit the browser
    driver.quit()


# export dataframe into csv file
def save_to_csv(filetitle, df):
    import datetime as dt
    #extract dataframe to csv files
    x = dt.datetime.now()
    today = x.strftime("%d%m%Y-%H%M") #date should be in string format in order to insert in filename
    fileName = f'./data/{filetitle}-{today}.csv'
    df.to_csv(fileName, index=False)


def main():
    
    main_url = str(input("Please insert url to scrape: "))
    pages = int(input("Please insert maximum page to scrape: "))
    filetitle = str(input("Please input csv filename: "))
    
    # run scrape() function
    scrape(main_url, pages)
    
    # extract to pandas dataframe
    # store the value in dataframe
    df = pd.DataFrame({
        "Title":house_titles,
        "Types":house_types,
        "Price":house_prices,
        "Bedrooms":house_bedrooms, 
        "Bathrooms":house_bathrooms, 
        "Areas":house_areas, 
        "Location":house_locations,
        "Release Date":house_releases_date,
        "Url":house_urls
    })
    
    # run save_to_csv() function
    save_to_csv(filetitle, df)
    
    return df

data = main()