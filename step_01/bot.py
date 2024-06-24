import os
import re

from dotenv import load_dotenv

import discord

load_dotenv() # Load environment variable from .env file

class BotClient(discord.Client):

    def remove_mention(self, text, user_id):
        result = str.strip(f'{re.sub(f"<.*{user_id}>","",text)}')
        return result

