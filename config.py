import os


class Config:
    DOMAIN_NAME = 'http://mtips5s_web:8000'
    # Discord Bot
    DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
    MTIPSCODER_CHANNEL_ID = int(os.getenv('MTIPSCODER_CHANNEL_ID'))
