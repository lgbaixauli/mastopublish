###
# Mastopublish, bot para publicar datos en Mastodon
###  

from pybot.mastobot import Mastobot
from pybot.config import Config
from pybot.logger import Logger

import random

BOT_NAME = "Terrybot"
MAX_LENGHT = 490

class Bot(Mastobot):

    def __init__(self, botname: str = BOT_NAME) -> None:

        super().__init__(botname = botname)
        self.init_publish_bot()


    def run(self, botname: str = BOT_NAME) -> None:

        quote    = random.choice(self._actions.get("Publish_Terry.quotes"))
        langauge = "en" 
 
        self.post_toot (self.find_text(quote), langauge)

        super().run(botname = botname)


    def find_text(self, quote):        
    
        text     = quote[1]                    
        comments = quote[2]                    
        source   = quote[3]   

        self._logger.debug("id      : " + str(quote[0]))                    
        self._logger.debug("text    : " + text)                    
        self._logger.debug("comments: " + comments)                     
        self._logger.debug("source  : " + source)   
         
        post_text  = text + "\n\n"
        if comments != "":
             post_text += comments + "\n"

        post_text += source + "\n\n"

        hashtag  = "#GNUTerryPratchett, #SpeakHisName, #Discworld" 
        if len(post_text) + len(hashtag) < MAX_LENGHT:
            post_text += hashtag

        post_text = (post_text[:MAX_LENGHT] + '... ') if len(post_text) > MAX_LENGHT else post_text
        self._logger.debug ("answer text\n" + post_text)

        return post_text


# main

if __name__ == '__main__':
    Bot().run()
