from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link2)

    input1 = browser.find_element_by_xpath('//*[@placeholder="Input your first name"]')
    input1.send_keys('Alex')
    input2 = browser.find_element_by_xpath('//*[@placeholder="Input your last name"]')
    input2.send_keys('Milne')
    input3 = browser.find_element_by_xpath('//*[@placeholder="Input your email"]')
    input3.send_keys('Milne@gmail.com')
    input4 = browser.find_element_by_xpath('//*[@placeholder="Input your phone:"]')
    input4.send_keys('88002553535')
    input5 = browser.find_element_by_xpath('//*[@placeholder="Input your address:"]')
    input5.send_keys('Moscow')

    button = browser.find_element_by_class_name('btn')
    button.click()

finally:
    time.sleep(4)
    browser.quit()

