import requests


from .config import load_config
from .bot_config import BotConfig


def send_message_to_admin(text):
    bot_config_instance = load_config("bot_directory/config.cfg", BotConfig, "=")
    token = bot_config_instance.bot_token
    url = "https://api.telegram.org/bot"
    url += token
    method = url + "/sendMessage"

    # print(bot_config_instance.admins)
    for channel_id in bot_config_instance.admins:
        r = requests.post(method, data={
            "chat_id": channel_id,
            "text": text
        })

        if r.status_code != 200:
            print("post_text error")
