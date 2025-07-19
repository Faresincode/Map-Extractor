from selenium import *
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.common.keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
#...webdriver import
from webdriver_manager.chrome import ChromeDriverManager
import time
#..import regex
import re
import random
import regex
import xpath_locators as xp
import os
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException 
import pandas as pd
import streamlit as st
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

global driver
def get_countries_list_from_text_file():
    global countries_list 
    # get countries list from profiles_data.txt
    with open ("all_countries.txt" ,"r" ,encoding='utf-8') as country:
        count_list1=country.readlines ()#line:92
    country.close()
    country_list=[]
    for countr in count_list1:
        clean_countr=countr.strip()
        country_list.append(clean_countr)
    country_list=list(filter(None, country_list))
    countries_list=country_list
get_countries_list_from_text_file()

global country
global targeted_address
global keyword
st.title("Map data extractor")
country=st.selectbox("select your targeted country",countries_list )
targeted_address=st.text_input("Write your targeted address")
keyword=st.text_input("What would you like to search about?")

email_regex = """(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
target = 'https://www.google.com/maps/@28.0948734,1.666194,5z?hl=en&entry=ttu'
min_wait = 1
max_wait = 4
visit_time = random.randint(min_wait, max_wait)
# Program Variables
cwd = os.getcwd()
user_data_dir_p1 = fr"{cwd}\core_1\Data\profile"
profile = "Default"


def run_chrome_portable():
    global options
    global driver
    # Setting basic options
    options = webdriver.ChromeOptions()
    options.binary_location = fr"{cwd}\core_1\App\Chrome-bin\chrome.exe"
    ## remove notification
    prefs = {"profile.default_content_setting_value.notifications" : 2}
    options.add_experimental_option("prefs",prefs)
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # To let chrome open eve after code execution
    options.add_experimental_option("detach", True)
    # Set Chrome Profile
    options.add_argument(fr"--user-data-dir={user_data_dir_p1}")
    options.add_argument(fr"--profile-directory={profile}")
    # Launch Driver
    driver = webdriver.Chrome(options=options)  
    driver.implicitly_wait(30)                     
    driver.delete_all_cookies()
    # maximize window
    driver.maximize_window()
    driver.implicitly_wait(100)
    
# search process function 
def search_query():
    driver.get(target)
    gmapsearch_area_input=driver.find_element(By.XPATH,xp.gmapsearch_area_input_xpath)
    gmapsearch_area_input.send_keys(country)
    gmapsearch_area_input.send_keys(Keys.ENTER)
    time.sleep(visit_time)
    gmapsearch_area_input.clear()
    gmapsearch_area_input.send_keys(targeted_address)
    gmapsearch_area_input.send_keys(Keys.ENTER)
    time.sleep(visit_time)
    gmapsearch_area_input.clear()
    gmapsearch_area_input.send_keys(keyword)
    gmapsearch_area_input.send_keys(Keys.ENTER)

def scroll_down():
    # scroll to the end of the result search list in the google map but you have to change the  browser luanguage to the enlish 
    #
    
        #while (True):
        #results = driver.find_elements(By.CLASS_NAME, 'hfpxzc')
        #driver.execute_script("return arguments[0].scrollIntoView();", results[-1])
        # Scrape page text
        #page_text = driver.find_element(by=By.TAG_NAME, value='body').text
        #endliststring="You've reached the end of the list."
        #if endliststring not in page_text:
        #    driver.execute_script("return arguments[0].scrollIntoView();", results[-1])
        #else:
        #    break
    #driver.execute_script("return arguments[0].scrollIntoView();", results[-1])
    


    # Scroll loop
    last_count = 0
    same_count_times = 0
    MAX_ATTEMPTS = 5  # How many times to try scrolling when no new results appear

    while True:
        try:
            # Wait for new results to load
            time.sleep(1)
            results = driver.find_elements(By.CLASS_NAME, 'hfpxzc')
            # Check if list is no longer growing
            if len(results) == last_count:
                same_count_times += 1
            else:
                same_count_times = 0
                last_count = len(results)

            # Break if we've reached the end
            page_text = driver.find_element(By.TAG_NAME, 'body').text
            if "You've reached the end of the list." in page_text:
                print("✅ End of list detected.")
                break

            # Also break if no more new results are loading after several attempts
            if same_count_times >= MAX_ATTEMPTS:
                print("⚠️ No new results after several attempts. Assuming end of list.")
                break

            # Scroll to last visible result
            driver.execute_script("arguments[0].scrollIntoView();", results[-1])

        except (StaleElementReferenceException, NoSuchElementException, IndexError):
            print("⚠️ Exception during scrolling, retrying...")
            time.sleep(1)
            continue



def get_company_data():
    # scrape links lists from google map results area
    # Scrape Element Attribute Values List - searchs_results_xpath
    elements_list = driver.find_elements(By.XPATH,xp.searchs_results_xpath)
    searchs_results_element_attribute_values_list = []
    for element in elements_list:
        element_attribute_value = element.get_attribute("href")
        searchs_results_element_attribute_values_list.append(element_attribute_value)
    # make a dataframe with pandas 
    dataframe=pd.DataFrame(columns= ["company_name","domain_name","stars","reviews","full_address","details_adress","position","hours","marcket_site","web_site","email","phone_number"])
    global i
    global allpage
    i=0
    for resultslink in searchs_results_element_attribute_values_list:
        try:
            driver.get(resultslink)
            ##get all page html 
            # Wait until document.readyState == "complete"
            WebDriverWait(driver, 30).until(lambda d: d.execute_script('return document.readyState') == 'complete')
            # Then wait for key element (optional)    
            #WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="sb_form_q"]')))
            page_html = driver.find_element(by=By.TAG_NAME, value='body')
            allpagehtml=page_html.get_attribute('innerHTML')
            allpage=str(allpagehtml)
            # get html code to the companyinfo result fram
            companyinfo_fram = driver.find_element(By.XPATH,xp.companyinfo_fram_xpath)
            companyinfo_fram=companyinfo_fram.get_attribute('innerHTML')
            if xp.frame_servicenamecode in companyinfo_fram:
                servicename=driver.find_element(By.XPATH,xp.servicename_xpath).text
                servicename=servicename.replace("\n","")
                servicename=servicename.replace("","")
            else:
                servicename=""
            if xp.frame_review_stars_code in companyinfo_fram:
                numberof_stars=driver.find_element(By.XPATH,xp.numberof_stars_xpath).get_attribute("aria-label")
                company_review=driver.find_element(By.XPATH,xp.company_review_xpath).get_attribute("aria-label")
            else:
                company_review=""
                numberof_stars=""
            if xp.frame_domainnamecode in companyinfo_fram:
                company_domain_name=driver.find_element(By.XPATH,xp.company_domain_name_xpath).text
                company_domain_name=company_domain_name.strip()
            else:
                company_domain_name=""
            if xp.frame_full_adress_code in companyinfo_fram:
                full_company_adress=driver.find_element(By.XPATH,xp.full_company_adress_xpath).get_attribute("aria-label")
                full_company_adress=full_company_adress.replace("Address:","")
                full_company_adress=full_company_adress.replace("","")
                full_company_adress=full_company_adress.strip()
            else:
                full_company_adress=""
            if xp.frame_address_details_code in companyinfo_fram:
                company_adress_details=driver.find_element(By.XPATH,xp.company_adress_details_xpath).get_attribute("aria-label")
            else:
                company_adress_details=""
            if xp.frame_hours_code in companyinfo_fram:
                open_close=driver.find_element(By.XPATH,xp.hours_xpath).text
                open_closecompany=open_close.replace("","")
                hours=open_closecompany.replace("","")
                hours=hours.strip()
            else:
                hours=""
            if xp.frame_phonenumber_code in companyinfo_fram:
                companyphone=driver.find_element(By.XPATH,xp.company_phone_number_xpath).get_dom_attribute("aria-label")
                company_phone_number=companyphone.replace("Phone:","")
                company_phone_number=company_phone_number.replace("-","")
                company_phone_number=company_phone_number.replace("","")
                company_phone_number=company_phone_number.strip()
            else:
                company_phone_number=""
            if xp.frame_location_code in companyinfo_fram:
                company_location=driver.find_element(By.XPATH,xp.company_location_xpath).get_attribute("aria-label")
                company_location=company_location.replace("Plus code: ","")
                company_location=company_location.replace("","")
                company_location=company_location.strip()
            else:
                company_location=""
            if xp.frame_website_code in companyinfo_fram:
                company_website=driver.find_element(By.XPATH,xp.company_website_xpath).get_attribute("href")
                company_website=company_website.strip()
            else:
                company_website=""
            if xp.frame_marcket_code in companyinfo_fram:
                company_marcket=driver.find_element(By.XPATH,xp.company_marcket_xpath).get_attribute("href")
                company_marcket=company_marcket.strip()
            else:
                company_marcket=""
        #email 
        # get html code to the companyinfo result fram
            companyinfo_text = driver.find_element(By.XPATH,xp.companyinfo_fram_xpath).text
        # scrape element list with regex
            extracted_email_list = re.findall(email_regex, companyinfo_text)
            extracted_email_list=list(filter(None,extracted_email_list))
            if len(extracted_email_list)==0:
                extracted_email_list=""
        except:
            TimeoutException
            NoSuchElementException
            continue
        # add company info to the one list company_info_data_list
        company_info_data_list=[]
        company_info_data_list.append(servicename)
        company_info_data_list.append(company_domain_name)
        company_info_data_list.append(numberof_stars)
        company_info_data_list.append(company_review)
        company_info_data_list.append(full_company_adress)
        company_info_data_list.append(company_adress_details)
        company_info_data_list.append(company_location)
        company_info_data_list.append(hours)
        company_info_data_list.append(company_marcket)
        company_info_data_list.append(company_website)
        company_info_data_list.append(extracted_email_list)
        company_info_data_list.append(company_phone_number)
        #add list to line
        dataframe.loc[i]=company_info_data_list
        i+=1
        dataframe.to_csv("full_company_data.csv",encoding='utf-8',index=False)


run_btn=st.button("Run")
show_data_frame_btn=st.button("Show Company data")
st.write("if you want to re run the software you have to click in cleaning button a lot eof time")
closeallbutton=st.button("Cleaning")
if closeallbutton:
    exit()
    
if run_btn:
    run_chrome_portable()
    search_query()
    scroll_down()
    get_company_data()
    exit()
if show_data_frame_btn:
    df=pd.read_csv('full_company_data.csv')
    st.write(df)


