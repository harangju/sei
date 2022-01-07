from loguru import logger

async def route(message):
    logger.info(f"Message received: {message}")

    

    if message.content.startswith('&hello'):
        await message.channel.send(content=f"Hello, {message.author.mention}!")
