import disnake
from disnake.ext import commands
from config import Config
from npc_generator import NPCGenerator
from ai_integration import generate_backstory

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

@bot.command()
async def npc(ctx):
    """Генерирует полный профиль NPC"""
    npc = bot.npc_generator.generate_npc()
    
    npc_data = {
        "first_name": npc.first_name,
        "last_name": npc.last_name,
        "age": npc.age,
        "marital_status": npc.marital_status,
        "occupation": npc.occupation,
        "traits": npc.traits,
        "appearance": npc.appearance
    }
    
    backstory = await generate_backstory(npc_data)
    
    embed = disnake.Embed(
        title=f"{npc.first_name} {npc.last_name}",
        description=f"**Возраст:** {npc.age}\n**Семейное положение:** {npc.marital_status}",
        color=disnake.Color.blurple()
    )
    embed.add_field(name="Профессия", value=npc.occupation, inline=False)
    embed.add_field(name="Черты характера", value=", ".join(npc.traits), inline=False)
    embed.add_field(name="Внешность", value=npc.appearance, inline=False)
    embed.add_field(name="Предыстория", value=backstory, inline=False)
    
    await ctx.send(embed=embed)

if __name__ == "__main__":
    bot.load_extension("npc_commands") 
    bot.run(Config.DISCORD_TOKEN)