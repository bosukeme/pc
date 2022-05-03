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


from ordered_set import OrderedSet
from bs4 import BeautifulSoup



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



def start_price_checker(search_item):
    url = "https://www.aliexpress.com/"
    driver = open_browser(url)

    driver.find_element_by_id("search-key").send_keys(search_item)
    driver.find_element_by_id("search-key").send_keys(Keys.RETURN)

    #sorting
    class_path_text = "[class='svg-icon m price-order']"
    driver.find_element_by_css_selector(class_path_text).click()

    search_items = driver.find_elements_by_class_name("_3t7zg")
    search_items = [item.text for item in search_items]
    sleep(2)


    # list_of_items = scroll_down_the_page(driver)
    # list_of_items = [a for b in list_of_items for a in b]
    # list_of_items = OrderedSet(list_of_items)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    image_links = create_link_image(soup)
    image_links = image_links[:len(search_items)]


    search_items = [create_name_price(item) for item in search_items]
    print

    all_items = []
    for index in range(len(search_items)):
        items = {**search_items[index], **image_links[index]}
        all_items.append(items)
    
    driver.quit()
    return all_items[:1]