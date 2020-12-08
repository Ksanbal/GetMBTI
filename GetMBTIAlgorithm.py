from selenium import webdriver
import time
import re
from itertools import product
import csv
from CatHand import CatHandBot
import traceback

opts = webdriver.FirefoxOptions()
opts.add_argument('Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:83.0) Gecko/20100101 Firefox/83.0')
opts.add_argument("--headless")
bot = webdriver.Firefox(executable_path='./geckodriver', options=opts)

# 중복순열 4096개
test = list(product([1,2], repeat=12))
result_img = []

with open('result.csv', 'w') as f:
	pass

try:
    for i in test:
        test_list = list(i)
        bot.get('https://m.fitpetmall.com/main/html.php?htmid=service/mbti_test.html')

        bot.find_element_by_name('dogNm').send_keys('Hello :)')
        bot.find_element_by_class_name('js_start_btn').click()

        for t in test_list:
            time.sleep(1.5)
            if t == 1:
                bot.find_element_by_class_name('answer_box.answer_a').click()
            else:
                bot.find_element_by_class_name('answer_box.answer_b').click()

        time.sleep(1)
        result = bot.find_element_by_class_name('img_illustration').get_attribute('src')
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
