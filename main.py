from CatHand import CatHandBot
from GetMBTIAlgorithm import getMBTI as GMT
import time

for i in range(10):
    temp_result = GMT()
    if temp_result[0]:
        CatHandBot.sendTalk(temp_result[1])
        break
    else:
        CatHandBot.sendTalk(temp_result[1])
        time.sleep(10)
        CatHandBot.sendTalk('Try to restart')
        continue
