from dotenv import load_dotenv
import os


load_dotenv()


class Config:
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
    OPENAI_KEY = os.getenv("OPENAI_API_KEY")
    PREFIX = "!"
    DEBUG = False