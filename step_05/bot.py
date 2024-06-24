import os
import re

from dotenv import load_dotenv

import discord
import gemini

load_dotenv() # Load environment variable from .env file

class BotClient(discord.Client):
    gemini = gemini.Gemini(token=os.getenv('GOOGLE_API_KEY'))
    async def on_ready(self):
        print(f'Logged on as {self.user}')

    async def on_message(self, message):
        if message.guild.get_member(self.user.id) in message.mentions:
            message_for_ai = self.remove_mention(message.content, self.user.id)
            async with message.channel.typing():
                response = self.gemini.get_response(message_for_ai)
                await message.channel.send(response)

    def remove_mention(self, text, user_id):
        result = str.strip(f'{re.sub(f"<.*{user_id}>","",text)}')
        return result

intents = discord.Intents.default()
intents.message_content = True

client = BotClient(intents=intents)

token = os.getenv('DISCORD_BOT_WITH_GEMINI_TOKEN')
client.run(token)