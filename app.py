import streamlit as st
import selenium
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

username = st.text_input("Enter your email address")
user_password = st.text_input("Enter a password", type="password")
if st.button("Accept All"):
    driver = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Projects\Auto-Accept\chromedriver.exe")
    driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
    driver.maximize_window()

    

    try:
        user = driver.find_element(By.XPATH,"//input[@id = 'username']")
        password = driver.find_element(By.XPATH,"//input[@id = 'password']")
        submit = driver.find_element(By.XPATH,"//button[@type = 'submit']")
        user.send_keys(username)
        password.send_keys(user_password)
        submit.click()
        time.sleep(3)
        driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
        driver.get('https://www.linkedin.com/mynetwork/invitation-manager/')

    except:
        print("ELement not found")

    time.sleep(10)
    try:
        buttons = driver.find_elements(By.XPATH,"//button[@class='invitation-card__action-btn artdeco-button artdeco-button--2 artdeco-button--secondary ember-view']")
        print(len(buttons))
        if(len(buttons) == 0):
            st.text("No Pending Connections")
        for item in buttons:                                      
            item.click()
            time.sleep(3)


    except:
        print("No pending invitations")

    time.sleep(10)
    driver.quit()