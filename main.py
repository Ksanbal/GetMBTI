from CatHand import CatHandBot
from GetMBTIAlgorithm import getMBTI as GMT

while(True):
    temp_result = GMT()
    if temp_result[0]:
        CatHandBot.sendTalk(temp_result[1])
        break
    else:
        CatHandBot.sendTalk(temp_result[1])
        continue