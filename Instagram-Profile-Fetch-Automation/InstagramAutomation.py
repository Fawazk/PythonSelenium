import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from config import PASSWORD,USERNAME

users = ['']

browser = webdriver.Chrome(
    executable_path='/home/fawaz/Documents/chromeDriver/chromedriver')
browser.maximize_window()
browser.get('https://www.instagram.com/')
time.sleep(3)
input_username = browser.find_element(
    By.CSS_SELECTOR, 'input[name="username"]')
input_username.send_keys(USERNAME)
input_password = browser.find_element(
    By.CSS_SELECTOR, 'input[name="password"]')
input_password.send_keys(PASSWORD)
browser.find_element(
    By.CSS_SELECTOR, 'button[type ="submit"]').click()
time.sleep(5)
for user in users:
    browser.get(f'https://www.instagram.com/{user}/')
    time.sleep(4)
    posts,followers,following = browser.find_elements(By.CLASS_NAME,'_ac2a')
    print(posts.text,followers.text,following.text)
    bio = browser.find_element(By.CLASS_NAME,'_aa_c')
    print(bio.text)

    with open(f"{user}.txt",'w') as file:
        file.write(f"Number of Posts: {posts.text}\n Number of followers : {followers.text} \n Number of Following : {following.text}\n\n Bio : {bio.text}")

    time.sleep(3)

    
    # <div class="_aacl _aacp _aacu _aacx _aad6 _aade">
    # 📍 Developer / Freelancer / YouTuber<br>🌎 Kerala 🇮🇳 / ex-ʀɪყɑɗɦɪɑn 🇸🇦
    # <br>📬 Stay humble. Be kind. Work hard.<br>📸 Tag Me #codeband</div>
