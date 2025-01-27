from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int(environ.get("API_ID", "26205052"))
API_HASH = environ.get("API_HASH", "5425d539963c1b371728c9003a94118f")

# Your Main Bot Token 
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "7404299810")) # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://mongodb:jIMmiBoFVrg5KDdt@cluster0.czlci.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))
