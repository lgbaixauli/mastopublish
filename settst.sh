#!/bin/bash

cd /home/mastopublish/mastopublish/

sed -i 's/force_mention: False/force_mention: True/g' config.yaml
sed -i 's/user_mention: \"none\"/user_mention: \"kergozh\"/g' config.yaml
sed -i 's/disable_post: True/disable_post: False/g' config.yaml
sed -i 's/loglevel: 20/loglevel: 10/g' config.yaml
          

