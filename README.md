# mastopublish

This code publish a tuut from a data file.  

### Dependencies

-   **Python 3**
-   Mastodon account

### Usage:

Within Python Virtual Environment:

1. Optionally, create a new user for running the bot: `adduser --disabled-login user_name`

2. Clone the repository `git clone https://github.com/lgbaixauli/mastopublish.git` 

3. Crate a virtual environment `python3 -m venv .venv` and activate it `source .venv/bin/activate`

4. Run `pip install -r requirements.txt` to install needed libraries.  

5. Modify options in the `config.yaml` file. For exemple, the access type or file names.

6. It's possible to fill in the config yaml the cliend id, cliend secret and access token of an application created in the Mastodon web (with de "development" opction). Also, it's possilbe to indicate credentials access and run `python3 quote.py` manually once to setup and get its access token to Mastodon instance.

7. Use your favourite scheduling method to set `publish.sh` to run every minute. For example,  add  `* * * * * /home/user_name/mastopublish/publish.sh 2>&1 | /usr/bin/logger -t MASTOPUBLISH` in `crontab -e`. The system and error log will be in `/var/log/syslog`. 

   Don't forgot the execution privilegies `chmod +x publish.sh`. 
   Don't forgot update the user_name in `publish.sh`
