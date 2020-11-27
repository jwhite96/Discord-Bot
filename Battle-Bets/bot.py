# bot.py
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')


# online
@bot.event
async def on_ready():
    print('Connected to Discord!')
    bot.load_extension('cogs.help')
    bot.load_extension('cogs.points')
    bot.load_extension('cogs.bet')


bot.run(TOKEN)
