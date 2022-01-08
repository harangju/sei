import discord
from .. import config
from loguru import logger

async def help(client, message, args):
    logger.info('Help is coming.')
    embed = discord.Embed()
    embed.set_author(
        name=client.user.name, icon_url=client.user.avatar_url
    )
    pre = config.prefix
    if len(args)==0: # no args
        embed.title = 'What would you like to do?'
        embed.add_field(
            name=':mortar_board: Manage scholarship',
            value=f"`{pre}help scholarship`",
            inline=True
        )
        embed.add_field(
            name=':credit_card: Manage wallets',
            value=f"`{pre}help wallets`",
            inline=True
        )
        embed.add_field(
            name=':video_game: Player stats',
            value=f"`{pre}stats` `{pre}statsManager` `{pre}statsGuild`",
            inline=False
        )
        embed.add_field(
            name=':money_with_wings: Tip $SLP',
            value=f"`{pre}tip @receiver 100 (optional) walletID`",
            inline=False
        )
    elif args[0]=='scholarship':
        embed.title = ':mortar_board: Manage scholarship'
        embed.add_field(
            name='Add scholar',
            value=f"`{pre}addScholar @scholarDiscord roninAddress privateKey(optional) scholarAddress(optional)`",
            inline=False
        )
        embed.add_field(
            name='Remove scholar',
            value=f"`{pre}removeScholar @scholarDiscord`",
            inline=True
        )
        embed.add_field(
            name='Show scholars',
            value=f"`{pre}showScholars`",
            inline=True
        )
        embed.add_field(
            name='Show all scholars',
            value=f"`{pre}showAllScholars`",
            inline=True
        )
        embed.add_field(
            name='Claim SLP',
            value=f"`{pre}claimSLP @scholarDiscord`",
            inline=True
        )
        embed.add_field(
            name='Claim All SLP',
            value=f"`{pre}claimAllSLP`",
            inline=True
        )
    elif args[0]=='wallets':
        embed.title = ':credit_card: Manage wallets'
        embed.add_field(
            name='Add wallet',
            value=f"`{pre}addWallet roninAddress` optional (DM) `privateKey`",
            inline=False
        )
        embed.add_field(
            name='Remove wallet',
            value=f"`{pre}removeWallet roninAddress`",
            inline=False
        )
        embed.add_field(
            name='Set default wallet',
            value=f"`{pre}setDefaultWallet roninAddress`",
            inline=False
        )
        embed.add_field(
            name='Show my wallets',
            value=f"`{pre}showWallets`",
            inline=True
        )
        embed.add_field(
            name='Show scholar wallets (managers only)',
            value=f"`{pre}showScholarWallets`",
            inline=True
        )
    elif args[0]=='admin':
        embed.title = ':technologist: Admin only'
        embed.add_field(
            name='Show all wallets',
            value=f"`{pre}showAllWallets`",
            inline=True
        )
        embed.add_field(
            name='Show admins',
            value=f"`{pre}showAdmins`",
            inline=True
        )
        embed.add_field(
            name='Add manager',
            value=f"`{pre}addManager @discord`",
            inline=True
        )
        embed.add_field(
            name='Remove manager',
            value=f"`{pre}removeManager @discord`",
            inline=True
        )
        embed.add_field(
            name='Show managers',
            value=f"`{pre}showManagers`",
            inline=True
        )
    else:
        logger.error(f"Help argument {args[0]} not recognized.")
    embed.set_footer(
        text=f"DM {client.user.name} with any private info (eg keys)."
    )
    await message.channel.send(embed=embed)
