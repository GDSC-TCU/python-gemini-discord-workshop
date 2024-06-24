import os
import re

from dotenv import load_dotenv

import discord

load_dotenv() # Load environment variable from .env file

class BotClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')

    async def on_message(self, message):
        print(message.content)

    def remove_mention(self, text, user_id):
        result = str.strip(f'{re.sub(f"<.*{user_id}>","",text)}')
        return result

intents = discord.Intents.default()
intents.message_content = True

client = BotClient(intents=intents)

token = os.getenv('DISCORD_BOT_WITH_GEMINI_TOKEN')
client.run(token)