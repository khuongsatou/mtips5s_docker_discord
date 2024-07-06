import datetime

from config import Config
from discord_bot import bot
print(datetime.datetime.now(), "------ start app.py!")



if __name__ == "__main__":  
    print(datetime.datetime.now(), "------ start doing...!")
    bot.run(Config.DISCORD_TOKEN, reconnect=True)


