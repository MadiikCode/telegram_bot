from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
#HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")