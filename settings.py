from pathlib import Path
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent

env_path = os.path.join(BASE_DIR, ".env")
load_dotenv(env_path)

LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')

CONFIGS_DIR = os.path.join(BASE_DIR, "rich_menu_configs")
IMAGES_DIR = os.path.join(BASE_DIR, "images")