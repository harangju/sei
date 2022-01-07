import discord
from .. import config
from loguru import logger

async def help(client, message, args):
    logger.info('Help is coming.')
    embed = discord.Embed(title='What would you like to do?')
    embed.set_author(
        name=client.user.name, icon_url=client.user.avatar_url
    )
    pre = config.prefix
    if len(args)==0: # no args
        embed.add_field(
            name='Manage scholarship',
            value=f"`{pre}help scholarship`",
            inline=True
        )
        embed.add_field(
            name='Manage wallets',
            value=f"`{pre}help wallets`",
            inline=True
        )
        embed.add_field(
            name='Player stats',
            value=f"`{pre}stats` `{pre}statsManager` `{pre}statsGuild`",
            inline=False
        )
        embed.add_field(
            name='Tip',
            value=f"`{pre}tip @receiver 100` (SLP)",
            inline=False
        )
        embed.set_footer(
            text=f"DM {client.user.name} with any private info (eg keys)."
        )
        await message.channel.send(embed=embed)
    elif args[0]=='scholars':
        pass
    else:
        logger.error('Help argument not recognized.')
