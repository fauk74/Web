from selenium import webdriver
import time

chrome_driver="C:/Development/chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie=driver.find_element_by_id("cookie")
items=driver.find_elements_by_css_selector(("#store div"))
item_ids=[item.get_attribute("id") for item in items]
timeout=time.time()+5
five_min=time.time()+60*5


while True:
    cookie.click()
    if time.time() > timeout:
        all_prices=driver.find_elements_by_css_selector(("#store b"))
        item_prices=[]

        #convert b text into integer
        for price in all_prices:
            element=price.text
            if element !="":
                cost=int(element.split("-")[1].strip().replace(",","") )
                item_prices.append(cost)

        #create a dictionary of upgrades
        cookie_upgrades={}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]]=item_ids[n]
        #get current cookie count

        cookie_count=driver.find_element_by_id("money").text
        cookie_count=int(cookie_count.strip().replace(",",""))

        #Find affordable upgrades
        affordable={}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable[cost]=id

        #purchase the most expensive
        highest_affordable=max(affordable)
        print(highest_affordable)
        to_purchase_id=affordable[highest_affordable]

        driver.find_element_by_id(to_purchase_id).click()

        timeout=time.time()+ 5

        #break after 5 minutes

        if time.time() > five_min:
            cookie_pers=driver.find_element_by_id("cps").text
            print(cookie_pers)
            break



