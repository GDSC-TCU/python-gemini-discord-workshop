import os
import re

import discord
import gemini
from dotenv import load_dotenv

load_dotenv()

class BotClient(discord.Client):
    gemini = gemini.Gemini(token=os.getenv('GOOGLE_API_KEY'))
    async def on_ready(self):
        print(f'Logged on as {self.user}')

    async def on_message(self, message):
        if message.content.startswith('!word'):
            message_for_ai = 'Please tell me the meaning of this word: ' + message.content[6:]
            async with message.channel.typing():
                response = self.gemini.get_word_response(message_for_ai)
                await message.channel.send(response)
        elif message.guild.get_member(self.user.id) in message.mentions:
            message_for_ai = self.remove_mention(message.content, self.user.id)
            print(message_for_ai)
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