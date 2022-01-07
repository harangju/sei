import sei
import discord
import dislash
import configparser
from loguru import logger

config = configparser.ConfigParser()
try:
    config.read(r'./config.cfg')
except:
    logger.error("Please fill out a config.cfg file according to specifications.")
    exit()

intents = discord.Intents(messages=True, guilds=True)
client = discord.Client(intents=intents)
slash = dislash.InteractionClient(client)

bot = discord.Client(intent=intents)
slash = 

# try:
#     prefix = config.get('Bot', 'prefix')
#     if prefix=='': raise Exception('Missing prefix in config.cfg')
# except:
#     logger.error('Please enter `prefix = &` in [Bot] in config.cfg.')
#     exit()
#
# @client.event
# async def on_ready():
#     logger.info('We have logged in as {0.user}'.format(client))
#
# @client.event
# async def on_message(message):
#     if message.author == client.user: # message from bot
#         return
#     if not message.content.startswith(prefix):
#         return
#     await bot.router.route(message)

try:
    token = config.get('Discord', 'token')
    if token=='':
        raise Exception('Missing Discord token in config.cfg.')
except:
    logger.error('Please enter `token = TOKEN` in [Discord] in config.cfg.')
    exit()

client.run(token)
