import telebot
import requests
import random
from bs4 import BeautifulSoup

zhaba_bot = telebot.TeleBot("TOKEN")


@zhaba_bot.message_handler(content_types=["text"])
def get_command(message):
    if message.text == "/start":
        text = "приветули, мои чюваки. это жабабот. он присылает фото жаб"
        zhaba_bot.send_message(message.chat.id, text)

    elif message.text == "/photo":
        photo_id = random.randrange(0, 54)
        if photo_id in range(0,10):
            url = f"http://www.allaboutfrogs.org/funstuff/random/000{photo_id}.jpg"
            url_status = requests.get(f"http://www.allaboutfrogs.org/funstuff/random/00{photo_id}.jpg")
            while url_status.status_code == 404:
                url = f"http://www.allaboutfrogs.org/funstuff/random/000{photo_id}.jpg"
                url_status = requests.get(f"http://www.allaboutfrogs.org/funstuff/random/000{photo_id}.jpg")                
            url = f"http://www.allaboutfrogs.org/funstuff/random/000{photo_id}.jpg"
        if photo_id in range(10,55):
            url = f"http://www.allaboutfrogs.org/funstuff/random/00{photo_id}.jpg"
            url_status = requests.get(f"http://www.allaboutfrogs.org/funstuff/random/00{photo_id}.jpg")
            while url_status.status_code == 404:
                url = f"http://www.allaboutfrogs.org/funstuff/random/00{photo_id}.jpg"
                url_status = requests.get(f"http://www.allaboutfrogs.org/funstuff/random/00{photo_id}.jpg")
        zhaba_bot.send_photo(message.chat.id, photo=url)

    elif message.text == "/joke":
        url = "http://allaboutfrogs.org/funstuff/jokes/jotd/index.shtml"
        page = requests.get(url)
        html_doc = page.text
        soup = BeautifulSoup(html_doc, "html.parser")
        text = soup.getText()
        text = text.replace("Stupid Frog Joke of the Day", "", 1)
        text = text.replace("View all the STUPID FROG JOKES.", "")
        text = text.replace("Back to FROGLAND.", "")
        text = text.strip()
        zhaba_bot.send_message(message.chat.id, text)

    elif message.text == "/help":
        instruction1 = "вам нужна помощь, мои чюваки? \n" 
        instruction2 = "если вы хотите посмотреть на фото жаб, то напишите /photo \n"
        instruction3 = "если вы хотите прочитать очень смешную шутку про жаб, то напишите /joke \n"
        instruction = instruction1 + instruction2 + instruction3
        zhaba_bot.send_message(message.chat.id, instruction)

zhaba_bot.polling(none_stop=True, interval=0)