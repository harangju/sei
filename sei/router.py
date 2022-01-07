from loguru import logger
from . import commands

async def route(client, message):
    """route message to command

    client: discord.Client
    message: discord.Message
        has correct prefix

    &help

    &addAdmin (owner)
        discordID
    &removeAdmin (owner)
        discordID
    &showAdmins (admin)

    &addManager (admin)
        discordID
    &removeManager (admin)
        discordID
    &showManagers (admin)

    &setScholarshipRate (admin / manager)
        rate(0.-1.) guildwide(bool)

    &addWallet (scholar) / addWallets (admin / manager)
        address privateKey(opt) / list
    &removeWallet (scholar) / removeWallets (admin / manager)
        address / list
    &showMyWallet (default) / showMyWallets (anyone)
    &setDefaultWallet (anyone)
        address
    &showScholarWallets (manager)
    &showAllWallets (admin)

    DM
    &addScholar / addScholars (manager)
        discordID scholarshipAddress privateKey(opt) scholarAddress(opt)
    &removeScholar / removeScholars (manager)
        discordID
    &showScholars (manager's scholars)
    &showAllScholars (admin)

    &claimSLP (manager / scholar?)
    &claimAllSLP (manager)

    &tip (anyone)
         wallet(opt)

    &stats (scholar / manager / admin)
    &statsManager (manager)
    &statsGuild (admin)
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
