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
        driver = webdriver.Remote(f"http://selenium:4444/wd/hub/", DesiredCapabilities.CHROME, options=options)
        # driver = webdriver.Remote(f"http://127.0.0.1:4444/wd/hub/", DesiredCapabilities.CHROME, options=options)
        # driver = webdriver.Remote(DesiredCapabilities.FIREFOX, options=options)
        # driver = webdriver.Remote(desired_capabilities={'browserName':'firefox'}, options=options)
        # driver = webdriver.Remote(desired_capabilities={'browserName':'firefox'})
        
        # driver = webdriver.Chrome(PATH, options=options)
        print("st")
        driver.get(topic_url)
        print("starting")
        
        sleep(5)
        
    except Exception as e:
        print(e)

    return driver

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








url = "https://www.aliexpress.com/"
driver = open_browser(url)

search_item = "pencil"
driver.find_element_by_id("search-key").send_keys(search_item)
sleep(1)
driver.find_element_by_id("search-key").send_keys(Keys.RETURN)
sleep(3)

print(driver.save_screenshot("ukeme.png"))
soup = BeautifulSoup(driver.page_source, 'html.parser')
image_links = create_link_image(soup)

print(image_links)
driver.quit()











# <div class="container">
#         <!-- Example row of columns -->
#         <div class="row">
#           <div class="col-md-4">
#             <h2>Heading</h2>
#             <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. </p>
#             <p><a class="btn btn-secondary" href="#" role="button">View details &raquo;</a></p>
#           </div>
#           <div class="col-md-4">
#             <h2>Heading</h2>
#             <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. </p>
#             <p><a class="btn btn-secondary" href="#" role="button">View details &raquo;</a></p>
#           </div>
#           <div class="col-md-4">
#             <h2>Heading</h2>
#             <p>Donec sed odio dui. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Vestibulum id ligula porta felis euismod semper. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>
#             <p><a class="btn btn-secondary" href="#" role="button">View details &raquo;</a></p>
#           </div>
#         </div>


curl --location --request POST 'http://localhost:8010/get_price' --header 'Content-Type: application/json' --data-raw '{"search_item": "pencil"}'