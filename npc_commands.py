import disnake
from disnake.ext import commands
from npc_generator import NPCGenerator
from ai_integration import generate_backstory
from ai_integration_v2 import generate_backstory_local

class NPCCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.generator = NPCGenerator()

    @commands.slash_command(
        name="npc",
        description="Сгенерировать случайного NPC"
    )
    async def npc_slash(self, inter: disnake.ApplicationCommandInteraction):
        """Слэш-команда для генерации NPC"""
        await inter.response.defer()
        
        npc = self.generator.generate_npc()
        npc_data = {
            "gender": npc.gender,
            "first_name": npc.first_name,
            "last_name": npc.last_name,
            "race": npc.race,
            "alignmemt": npc.alignment,
            "age": npc.age,
            "marital_status": npc.marital_status,
            "occupation": npc.occupation,
            "traits": npc.traits,
        }
        
        backstory = await generate_backstory_local(npc_data)
        
        embed = disnake.Embed(
            title=f"{npc.first_name} {npc.last_name}",
            color=disnake.Color.dark_teal()
        )
        embed.add_field(name="Пол", value=npc.gender, inline=False)
        embed.add_field(name="Раса", value=npc.race, inline=False)
        embed.add_field(name="Возраст", value=npc.age, inline=True)
        embed.add_field(name="Мировозрение", value=npc.alignment, inline=False)
        embed.add_field(name="Семейное положение", value=npc.marital_status, inline=True)
        embed.add_field(name="Профессия", value=npc.occupation, inline=False)
        embed.add_field(name="Черты характера", value=", ".join(npc.traits), inline=False)
        embed.add_field(name="Предыстория", value=backstory, inline=False)
        
        await inter.edit_original_message(embed=embed)

def setup(bot):
    bot.add_cog(NPCCommands(bot))