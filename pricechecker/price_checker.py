from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from time import sleep
from selenium.webdriver.chrome.options import Options

options=Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('--headless')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("disable-infobars")

from bs4 import BeautifulSoup
import random
from flask import flash, render_template, make_response


def open_browser(topic_url):
    """
        This starts the chrome browser and opens the url
    """
    ## windows
    # PATH = 'C://Users/hp/Desktop/Chrome Driver/chromedriver.exe'

    ## linux
    PATH = "/usr/lib/chromium-browser/chromedriver"

    

    try:
        print("start")
        driver = webdriver.Remote(f"http://selenium:4444", DesiredCapabilities.CHROME, options=options)
       

        driver.get(topic_url)
        print("starting")
        sleep(5)
        
    except Exception as e:
        print(e)

    return driver



def scroll_down_the_page(driver):
    """
        This implements an infinite scroll on twitter and stops at the end of the page
    """
    # Get scroll height

    try:
        last_height = driver.execute_script("return document.body.scrollHeight")
        

        new_height = 10

        list_of_items = []
        
        while True:

            driver.execute_script(f"window.scrollTo(0, {new_height});")
            sleep(5)
            
            search_items = driver.find_elements_by_class_name("_3t7zg")
            search_items = [item.text for item in search_items]
            sleep(2)

            # driver.find_elements_by_class_name("_1RtJV product-img")
    
            list_of_items.append(search_items)
        
            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script(f"return {new_height+350}")
            print(new_height)
            if new_height > last_height:
                break
    except Exception as e:
        print(e)
        
    return list_of_items


def create_name_price(item):
    item = item.split("\n")
    item_dict = {
        "name": item[0],
        "price": item[1]}
    
    return item_dict

# def create_link_image(soup):
    
#     link_image_section = soup.find_all(class_="_3t7zg _2f4Ho")
    
#     image_links = []
#     for item in link_image_section:
#         link = item['href']
#         image = item.find("img")['src']
#         image_link = {"link": link, "image": image}
#         image_links.append(image_link)
    
#     return image_links


def parse_naira(dict_):
    try:
        price = dict_.get('price')
        if "NGN" in price:
            price = price.split("NGN")[1]
            price = float(price.replace(",",""))
            dict_['price'] = price
        elif "US $" in price:
            price = price.split("US $")[1]
            price = float(price.replace(",",""))
            dict_['price'] = round(price * 350,2)
    except:
        dict_ = {}
    return dict_


def create_link_image(soup):
    
    try:
        link_image_section = soup.find_all(class_="_3t7zg _2f4Ho")
        
        image_links = []
        for item in link_image_section:
            try:
                link = item['href']
                image = item.find("img")['src']
            except:
                image = "NA"
                link = "NA"
            image_link = {"link": link, "image": image}
            image_links.append(image_link)
    except Exception as e:
        print(e)
    return image_links



def check_ali_express_price(search_item):
    search_item = "+".join(search_item.split(" "))

    url = "https://www.aliexpress.com/"
    driver = open_browser(url)

    driver.find_element_by_id("search-key").send_keys(search_item)
    driver.find_element_by_id("search-key").send_keys(Keys.RETURN)

    #sorting
    class_path_text = "[class='svg-icon m price-order']"
    driver.find_element_by_css_selector(class_path_text).click()
    sleep(3)

    search_items = driver.find_elements_by_class_name("_3t7zg")
    search_items = [[item.text for item in search_items][0]]
    sleep(2)

    search_items = [create_name_price(item) for item in search_items]

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    image_links = create_link_image(soup)
    image_links = image_links[:len(search_items)][0]


    
    search_items = [parse_naira(item) for item in search_items][0]
    
    full_item = {**search_items, **image_links }

    
    driver.quit()

    return full_item


def check_jumia_price(search_item):
    search_item = "+".join(search_item.split(" "))
    url = f"https://www.jumia.com.ng/catalog/?q={search_item}&sort=lowest-price#catalog-listing"

    driver = open_browser(url)

    try:
        names = driver.find_elements_by_class_name("name")
        names = [a.text for a in names][0]
    except:
        names = "NA"

    try:
        images = driver.find_elements_by_class_name("img")
        images = [c.get_attribute("src") for c in images][0]
    except:
        images = "NA"
    
    try:
        links = driver.find_elements_by_class_name("core") 
        links = [a.get_attribute("href") for a in links][0]
    except:
        links = "NA"

    try:
        price = driver.find_elements_by_class_name("prc")
        price = [a.text for a in price][0]
        price = int(price.split(" ")[1])
    except:
        price = "NA"

    data = {
        "name": names,
        "image": images,
        "link": links,
        "price": price
    }
    driver.quit()
    
    return data


def start_price_checker(search_item):
    
    try:
        jumia_data = check_jumia_price(search_item)
        
        ali_express_data = check_ali_express_price(search_item)
        
        if jumia_data['price'] > ali_express_data['price']:
            return ali_express_data
        elif jumia_data['price'] < ali_express_data['price']:
            return jumia_data
        elif jumia_data['price'] == ali_express_data['price']:
            return random.choice([jumia_data, ali_express_data])
        else:
            return {"name": "NA", "price":"NA", "image":"NA", "link":"NA"}

    except Exception as e:
        print(e)

