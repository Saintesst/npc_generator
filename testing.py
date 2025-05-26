import disnake
from disnake import ui, SelectOption
from disnake.ext import commands
import random

# Шаблоны для NPC
DEFAULT_NAMES = ["Альрик", "Бренда", "Карстен", "Лираэль", "Торгрим"]
DEFAULT_RACES = ["Человек", "Эльф", "Гном", "Орк", "Дварф"]
DEFAULT_DESCRIPTION = "Таинственный незнакомец с неизвестными намерениями."

# Настройка бота
bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all())

# Модальное окно для создания NPC
class NPCCreationModal(ui.Modal):
    def __init__(self):
        components = [
            ui.TextInput(
                label="Имя NPC (необязательно)",
                placeholder="Оставьте пустым для случайного имени",
                custom_id="npc_name",
                style=disnake.TextInputStyle.short,
                required=False
            ),
            ui.TextInput(
                label="Раса NPC (необязательно)",
                placeholder="Оставьте пустым для случайной расы",
                custom_id="npc_race",
                style=disnake.TextInputStyle.short,
                required=False
            ),
            ui.TextInput(
                label="Описание NPC (необязательно)",
                placeholder="Оставьте пустым для стандартного описания",
                custom_id="npc_description",
                style=disnake.TextInputStyle.paragraph,
                required=False
            )
        ]
        super().__init__(title="Создание NPC", components=components)

    async def callback(self, inter: disnake.ModalInteraction):
        # Получаем введенные данные (или используем значения по умолчанию)
        name = inter.text_values["npc_name"] or random.choice(DEFAULT_NAMES)
        race = inter.text_values["npc_race"] or random.choice(DEFAULT_RACES)
        description = inter.text_values["npc_description"] or DEFAULT_DESCRIPTION

        # Создаем NPC с дополнительными параметрами по умолчанию
        npc = {
            "Имя": name,
            "Раса": race,
            "Описание": description,
            "Здоровье": 100,
            "Уровень": random.randint(1, 10)
        }

        # Формируем красивый вывод
        embed = disnake.Embed(
            title=f"Создан NPC: {name}",
            description=f"**Раса:** {race}\n**Описание:** {description}",
            color=disnake.Color.green()
        )
        embed.add_field(name="Характеристики", value=f"❤️ Здоровье: {npc['Здоровье']}\n⭐ Уровень: {npc['Уровень']}")

        await inter.response.send_message(embed=embed)

# Команда для создания NPC
@bot.slash_command(name="create_npc", description="Создать NPC с настраиваемыми параметрами")
async def create_npc(inter: disnake.ApplicationCommandInteraction):
    await inter.response.send_modal(modal=NPCCreationModal())

# Запуск бота
@bot.event
async def on_ready():
    print(f"Бот {bot.user} готов к работе!")

bot.run("YOUR_BOT_TOKEN")