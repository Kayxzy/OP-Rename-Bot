# (c) @AbirHasan2005

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    API_ID = int(os.environ.get("API_ID", "18971259"))
    API_HASH = os.environ.get("API_HASH", "3f1373ede58a6d52d89ec0f8700fd688")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5979614687:AAHbj6UprKT9hq7jSOSBMS4Ln683EwSEdJg")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID", 1668766845))
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "1668766845").split()))
    PRO_USERS.append(OWNER_ID)
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://Kayex:Kayex@cluster0.tup4a.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001848660912"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
