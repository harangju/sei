from loguru import logger
from . import commands

async def route(client, message):
    """route message to command

    client: discord.Client
    message: discord.Message
        correct prefix assumed
    """
    logger.info(f"Message received: {message}")

    words = message.content.split(" ")
    command, args = words[0][1:], words[1:]

    logger.info(f"Command: {command}")
    logger.info(f"Args: {args}")

    if command=='help':
        await commands.help(client, message, args)
    elif command=='':
        pass
    elif command=='':
        pass

    if message.content.startswith('&hello'):
        await message.channel.send(content=f"Hello, {message.author.mention}!")
