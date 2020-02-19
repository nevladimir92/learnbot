import logging

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

import settings

PROXY = {'proxy_url': 'socks5h://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO,
    filename = 'bot.log',
)

logger = logging.getLogger()

def greet_user(bot, update):
     text ='Вызван/start'
     logger.info(text)
     update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = "Привет! {}: Ты написал: {}".format(update.message.chat.first_name, update.message.text)
    logger.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username,
                 update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(settings.API_KEY, request_kwargs = settings.PROXY)
    
    logger.info("Бот запускается")
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start',greet_user))
    dp.add_handler(MessageHandler(Filters.text,talk_to_me))
  
  
    mybot.start_polling()
    mybot.idle()

main()
