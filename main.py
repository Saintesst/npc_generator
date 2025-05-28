import disnake
from disnake.ext import commands
from config import Config
from npc_generator import NPCGenerator

class NPCToolBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=Config.PREFIX,
            intents=disnake.Intents.all(),
            activity=disnake.Game(name="Генерация NPC")
        )
        self.npc_generator = NPCGenerator()

    async def on_ready(self):
        print(f'Бот {self.user} готов к работе!')

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        await ctx.send(f"Произошла ошибка: {error}")

bot = NPCToolBot()


if __name__ == "__main__":
    bot.load_extension("npc_commands") 
    if not Config.DISCORD_TOKEN:
        raise ValueError("Discord token is not set in configuration")
    bot.run(Config.DISCORD_TOKEN)
    