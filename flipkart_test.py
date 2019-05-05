from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

import re
import os
import time



class FlipkartBot(object):

    def __init__(self, items):
        self.flipkart_url = "https://www.flipkart.com/"
        self.items = items

        self.profile = webdriver.FirefoxProfile()
        self.options = Options()

        self.driver = webdriver.Firefox(firefox_profile=self.profile,
                                        firefox_options=self.options)

        self.driver.get(self.flipkart_url)

        
        self.html = self.driver.page_source
        self.soup = BeautifulSoup(self.html, 'html.parser')
        self.html = self.soup.prettify('utf-8')

    def search_items(self):
        urls =  []
        costs = []
        names = []
        for item in self.items:
            print(f"Searching for {item}...")

            self.driver.get(self.flipkart_url)
            signup_button_close = self.driver.find_element_by_xpath("/html/body/div[2]/div/div/button")
            signup_button_close.click()

            search_input = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
            search_input.send_keys(item)

            time.sleep(4)

            search_button = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button")
            search_button.click()

            time.sleep(4)
            

            category_button = self.driver.find_element_by_css_selector("._1qKb_B > select:nth-child(1) > option:nth-child(1)")
            category_button.click()
            
            time.sleep(4)
           
            dropdown = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div/div[1]/div[2]/div[1]/div/section[2]/div[4]/div[1]/select")
            select = Select(dropdown)
            select.select_by_value("30000")
            
            time.sleep(4)
            
            assure_select = self.driver.find_element_by_css_selector("._1_fxb2 > label:nth-child(1) > div:nth-child(2)")
            assure_select.click()
            
            time.sleep(4)
            
            apple_select =  self.driver.find_element_by_css_selector("section._1gjf4c:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > div:nth-child(2)")
            apple_select.click()
            
                            
            for i in range(2,7):

                url_link = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div["+str(i)+"]/div/div/div/a")
                url = url_link.get_attribute("href")

                name_link = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div["+str(i)+"]/div/div/div/a/div[2]/div[1]/div[1]")
                name = name_link.text

                cost_link = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div["+str(i)+"]/div/div/div/a/div[2]/div[2]/div[1]/div/div[1]")
                cost = cost_link.text

                urls.append(url)
                names.append(name)
                costs.append(cost)

        
            List = [urls, names, costs]
            
        return print(List)

            

items = ["iPhone 6"]
flipkart_bot = FlipkartBot(items)
flipkart_bot.search_items()


