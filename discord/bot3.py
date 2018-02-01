import asyncio
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import datetime
import sys, traceback
import time
########################################
def get_prefix(bot, message):
    prefixes = ['>?', 'lol ', '##']
    if not message.guild:
        return '?'
    return commands.when_mentioned_or(*prefixes)(bot, message)
initial_extensions = ['cogs.music', 'cogs.translate','cogs.mod','cogs.fun']
                      
bot = commands.Bot(command_prefix=get_prefix, description='A Fuj-Bot!')


@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    if __name__ == '__main__':
        for extension in initial_extensions:
            try:
                bot.load_extension(extension)
            except Exception as e:
                print(f'Failed to load extension {extension}.', file=sys.stderr)
                traceback.print_exc()
    print(f'Successfully logged in and booted...!')

@bot.event
async def on_guild_join(server):
    print("New Server Joined: {}!".format(server))
    owner=bot.get_user(162939111680901122)
    servername= server.name
    serverreg= server.region
    serverid= server.id
    channel=discord.utils.get(server.text_channels)
    serverowner= server.owner
    ownerid= server.owner_id
    joinedguild = discord.Embed(colour = discord.Colour(0xA522B3))
    joinedguild.set_author(name = '[SERVER JOINED]')
    joinedguild.add_field(name="Server Name:", value= servername)
    joinedguild.add_field(name="Server ID:", value= serverid)
    joinedguild.add_field(name="Server Region:", value= serverreg)
    joinedguild.add_field(name="Server Owner:", value= serverowner)
    joinedguild.set_footer(text = time.strftime("%d/%m/%Y - %I:%M:%S %p CET"))
    await owner.send(embed = joinedguild)



bot.run('MzkyMTA1ODg2ODk5NzY1MjU4.DRrSsA.aawWm282Ht923J1sc_eC3GD6x6A', bot=True, reconnect=True)