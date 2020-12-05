import telegram

api_key = '1495480005:AAFjSTbDnJE5_5oiq811nEvTyM7ZM6HNg30'

bot = telegram.Bot(token=api_key)

# chat_id = bot.get_updates()[-1].message.chat_id
sanbal_id = 843819664

def sendTalk(text):
    bot.sendMessage(chat_id=sanbal_id, text=text)
