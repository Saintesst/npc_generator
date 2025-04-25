import disnake
from disnake.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()


bot = commands.Bot()

@bot.event
async def on_ready():
    print(f"Bot {bot.user.name} is ready!")
    

bot.run(os.getenv('DS_TOKEN'))