from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
from itertools import product
import csv
from tqdm import tqdm
from CatHand import CatHandBot

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

# bot = webdriver.Chrome('./chromedriver', chrome_options=options)
bot = webdriver.Chrome('./chromedriver')

# 중복순열 4096개
# test = list(product([1,2], repeat=12))
test = [
    (2,2,2,2,2,2,2,2,2,2,2,2),
    (2,1,2,1,2,1,2,1,2,1,2,1)
]
percent = 0

try:
    for i in tqdm(test):
        test_list = list(i)
        bot.get('https://m.fitpetmall.com/main/html.php?htmid=service/mbti_test.html')

        name_box = bot.find_element_by_name('dogNm').send_keys('Hello :)')
        next_btn = bot.find_element_by_class_name('js_start_btn').click()
        # time.sleep(1)

        for t in test_list:
            time.sleep(1.5)
            if t == 1:
                # WebDriverWait(bot, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'answer_box.answer_a')))
                bot.find_element_by_class_name('answer_box.answer_a').click()
            else:
                # WebDriverWait(bot, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'answer_box.answer_b')))
                bot.find_element_by_class_name('answer_box.answer_b').click()
        
        # WebDriverWait(bot, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'img_illustration')))
        time.sleep(1)
        result = bot.find_element_by_class_name('img_illustration').get_attribute('src')
        result = re.compile('\w{4}.png').findall(result)[0][:4]

        bot.save_screenshot(f'img/{result}.png')

        test_list.append(result)

        with open('result.csv', 'a') as f:
            wr = csv.writer(f)
            wr.writerow(test_list)

        percent += 1

        if percent % 500 == 0:
            CatHandBot.sendTalk(f'열심히 하는중 : {percent}%')    
    CatHandBot.sendTalk('끝났엄')
    bot.quit()
    
except Exception as ex:
    CatHandBot.sendTalk(f'에러 났따아...\n*****\nError{ex}\n*****')
    print('*****\nError', ex, '\n*****')