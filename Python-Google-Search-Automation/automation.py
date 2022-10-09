import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome('/home/fawaz/Documents/chromeDriver/chromedriver')

browser.get('https://www.google.co.in/')

search_input = browser.find_element(By.NAME, "q")
search_input.send_keys('hellow world')
time.sleep(2)
click_search = browser.find_element(By.CSS_SELECTOR,'input[type="submit"]')
# click_search = browser.find_element(By.NAME,'btnK')
print('jh;aflsdjf',click_search,'ljkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk;fdsa')
click_search.click()

# <input class="gLFyf gsfi" jsaction="paste:puy29d;" maxlength="2048" name="q" type="text" aria-autocomplete="both" aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" autofocus="" role="combobox" spellcheck="false" title="Search" value="" aria-label="Search" data-ved="0ahUKEwia0aHz59D6AhXTEIgKHVdgDewQ39UDCAQ">
# <input class="gNO89b" value="Google Search" aria-label="Google Search" name="btnK" role="button" tabindex="0" type="submit" data-ved="0ahUKEwjc2P6N6tD6AhXYe94KHbEqAsYQ4dUDCAs">