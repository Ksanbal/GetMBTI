from CatHand import CatHandBot

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from itertools import product
import time
import re
import csv
import os
import traceback

opts = webdriver.FirefoxOptions()
opts.add_argument('Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:83.0) Gecko/20100101 Firefox/83.0')
opts.add_argument("--headless")
bot = webdriver.Firefox(executable_path='./geckodriver', options=opts)

# 중복순열 4096개
test = list(product([1,2], repeat=12))

# 이미 넣어본 값은 건너뛰기
with open('result.csv', 'r') as f:
    l = len(f.readlines())
test = test[l:]

# 다운받은 적 있는
result_img = [i[:4] for i in os.listdir('./img')]


try:
    for i in test:
        test_list = list(i)
        bot.get('https://m.fitpetmall.com/main/html.php?htmid=service/mbti_test.html')

        bot.find_element_by_name('dogNm').send_keys('Hello :)')
        bot.find_element_by_class_name('js_start_btn').click()

        for t in test_list:
            time.sleep(1.5)
            if t == 1:
                WebDriverWait(bot, 10).until(EC.element_to_be_clickable\
                ((By.CLASS_NAME, 'answer_box.answer_a'))).click()
            else:
                WebDriverWait(bot, 10).until(EC.element_to_be_clickable\
                ((By.CLASS_NAME, 'answer_box.answer_b'))).click()

        result = WebDriverWait(bot, 10).until(EC.presence_of_element_located\
            ((By.CLASS_NAME, 'img_illustration'))).get_attribute('src')

        result = re.compile('\w{4}.png').findall(result)[0][:4]

        if result not in result_img:
            bot.save_screenshot(f'img/{result}.png')
            result_img.append(result)

        with open('result.csv', 'a') as f:
            csv.writer(f).writerow(test_list+[result])

    CatHandBot.sendTalk('끝났엄')
    bot.quit()
    
except Exception as ex:
    CatHandBot.sendTalk(f'에러 났따아...\n*****\nError\n{traceback.format_exc()}\n*****')
