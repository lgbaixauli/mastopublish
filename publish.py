###
# Mastopublish, bot para publicar datos en Mastodon
###  

from bundle.mastobot import Mastobot
from bundle.config import Config
from bundle.logger import Logger

import random

BOT_NAME = "Publishbot"

class Bot(Mastobot):

    def __init__(self, botname: str = BOT_NAME) -> None:

        super().__init__(botname = botname)
        

    def run(self, botname: str = BOT_NAME) -> None:

        action = self._actions["Publish_Terry"]
        quote  = random.choice(action["quotes"]) 

        if self._push_disable:
            self._logger.info("pushing answer disabled with quote " + str(quote["id"]))                    

        else:
            self._logger.info("answering with quote " + str(quote["id"]))
            self.mastodon.status_post(self.find_text(quote), language="en")

        super().run(botname = botname)


    def find_text(self, quote):        
    
        text     = quote["text"]                    
        comments = quote["comments"]                    
        source   = quote["source"]   

        self._logger.debug("text    : " + text)                    
        self._logger.debug("comments: " + comments)                     
        self._logger.debug("source  : " + source)   
         
        post_text  = text + "\n\n"
        if comments: post_text += comments + "\n"
        post_text += source + "\n\n"
        post_text += "#GNUTerryPratchett, #SpeakHisName, #Discworld" 

        post_text = (post_text[:400] + '... ') if len(post_text) > 400 else post_text

        self._logger.debug ("answer text\n" + post_text)

        return post_text


# main

if __name__ == '__main__':
    Bot().run()
