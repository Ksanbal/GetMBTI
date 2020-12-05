from selenium import webdriver
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
bot = webdriver.Chrome('./chromedriver', chrome_options=options)
bot = webdriver.Chrome('./chromedriver')

# 중복순열 4096개
# test = list(product([1,2], repeat=12))
test = [
    (2,2,2,2,2,2,2,2,2,2,2,2),
    (2,1,2,1,2,1,2,1,2,1,2,1)
]

try:
    for i in tqdm(test):
        test_list = list(i)
        bot.get('https://m.fitpetmall.com/main/html.php?htmid=service/mbti_test.html')

        name_box = bot.find_element_by_name('dogNm').send_keys('Hello :)')
        next_btn = bot.find_element_by_class_name('js_start_btn').click()
        time.sleep(1)

        for t in test_list:
            if t == 1:
                bot.find_element_by_class_name('answer_box.answer_a').click()
            else:
                bot.find_element_by_class_name('answer_box.answer_b').click()
            time.sleep(1)
        
        result = bot.find_element_by_class_name('img_illustration').get_attribute('src')
        result = re.compile('\w{4}.png').findall(result)[0][:4]
        time.sleep(1)

        img = bot.find_element_by_class_name('save_image')
        bot.save_screenshot(f'img/{result}.png')

        test_list.append(result)

        with open('result.csv', 'a') as f:
            wr = csv.writer(f)
            wr.writerow(test_list)
    CatHandBot.sendTalk('끝났엄')
    bot.quit()
except Exception as ex:
    print('*****\nError', ex, '\n*****')