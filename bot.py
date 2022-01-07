import sei
import discord
from loguru import logger

intents = discord.Intents(messages=True, guilds=True)
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    logger.info('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user: # message from bot
        return
    if not message.content.startswith(sei.config.prefix):
        return
    await sei.router.route(client, message)

client.run(sei.config.token)
