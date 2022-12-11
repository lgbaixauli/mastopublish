###
# Mastopublish, bot para publicar datos en Mastodon
###  

from bundle.mastobot import Mastobot
from bundle.config import Config
from bundle.logger import Logger

import yaml
import random

class Runner:
    '''
    Main runner of the app
    '''
    def init(self):

        self._config     = Config()
        self._logger     = Logger(self._config).getLogger()
        self._bot        = Mastobot(self._config)

        self.init_app_options()
        self.init_test_options()

        self._logger.info("init app")

        return self


    def init_app_options(self):

        data_file_name = self._config.get("app.data_file_name") 
        with open(data_file_name, 'r') as stream:
            self._data  = yaml.safe_load(stream)
        

    def init_test_options (self):

        self._push_disable    = self._config.get("testing.disable_push")


    def run(self):

        self._logger.debug ("runing app")

        post_text, data_id = self.publish_text()

        if self._config.get("testing.disable_push"):
            self._logger.info("push answer disabled with " + str(data_id))                    
        else:
            self._logger.info("answering notification with " + str(data_id))
            self.mastodon.status_post(post_text, language="en")

        self._logger.info("end app")


    def publish_text(self):        
    
        aleatorio = random.choice(self._data) 

        data_id  = aleatorio["id"]                    
        quote    = aleatorio["quote"]                    
        comments = aleatorio["comments"]                    
        origin   = aleatorio["origin"]   

        self._logger.debug("id      : " + str(data_id))                    
        self._logger.debug("quote   : " + quote)                    
        self._logger.debug("comments: " + comments)                     
        self._logger.debug("origin  : " + origin)   
         
        post_text  = quote + "\n\n"
        if comments:
            post_text += comments + "\n"
        post_text += origin

        post_text = (post_text[:400] + '... ') if len(post_text) > 400 else post_text

        self._logger.debug ("answer text\n" + post_text)

        return post_text, aleatorio["id"]


# main

if __name__ == '__main__':
    Runner().init().run()
