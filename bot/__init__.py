import os
from pyrogram import Client
from dotenv import load_dotenv

if os.path.exists('config.env'):
  load_dotenv('config.env')

api_id = int(os.environ.get("API_ID",29452145))
api_hash = os.environ.get("API_HASH","5a2784e571fe5043852d32396a34a13b")
bot_token = os.environ.get("BOT_TOKEN","7445547849:AAHfX4_8TQ57cg71Q_l9ABoa6RfgfPWHgsE")
download_dir = os.environ.get("DOWNLOAD_DIR", "downloads/")
sudo_users = list(set(int(x) for x in os.environ.get("SUDO_USERS","6169288210").split()))

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

data = []
crf = []
watermark =[]

if not download_dir.endswith("/"):
  download_dir = str(download_dir) + "/"
if not os.path.isdir(download_dir):
  os.makedirs(download_dir)
