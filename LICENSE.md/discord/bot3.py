import asyncio
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import datetime
import sys, traceback
########################################
def get_prefix(bot, message):
    prefixes = ['>?', 'lol ', '!']
    if not message.guild:
        return '?'
    return commands.when_mentioned_or(*prefixes)(bot, message)
initial_extensions = ['music', 'translate']
                      
bot = commands.Bot(command_prefix=get_prefix, description='A Rewrite Cog Example')


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

@bot.command() #Simple Ping Pong command
async def ping(ctx):
    await ctx.send(':ping_pong: Pong!')

@bot.command()#Embeds the word 'Hi'
async def embed(ctx):
    embed = discord.Embed(description = 'Hi')
    await ctx.send(embed = embed)

@bot.command()#Gives User Information
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title = 'User Info',image = user.avatar,colour = user.colour)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name = "Username: ", value = user.name, inline=True)
    embed.add_field(name = "Join Date: ", value = user.joined_at,inline=True)
    embed.add_field(name = "Display name: ", value = user.display_name,inline=True)
    embed.add_field(name = "Account Created at: ",value = user.created_at,inline=True)
    await ctx.send(embed = embed)

@bot.command()#A simple password to channel program
async def password(ctx, *, password):
    if password=='123':
        role = discord.utils.get(ctx.guild.roles, name='x')
        await ctx.send('Granted')
        ctx.message.delete()
        await ctx.message.author.add_roles(role)
    else:
        await ctx.send('Try Again')
        
@bot.command()#testing within console
async def user(ctx):
    print('hi : {}'.format(ctx.message.author))
    
@bot.command()#Kick command
async def kick(ctx,user:discord.Member):
    if ctx.message.author.guild_permissions.administrator==True and user.guild_permissions.administrator==False:
        print('Kicked: {}'.format(user.name))
        await ctx.send("Bye!")
        await ctx.guild.kick(user)
        print('Users currently : {}'.format(bot.get_all_members()))
    else:
        await ctx.send('Bye! {}'.format(ctx.message.author.mention))
@bot.command()
async def ban(ctx, *, user : discord.Member):
    if ctx.message.author.guild_permissions.administrator==True and user.guild_permissions.administrator==False:
        embed = discord.Embed(title = 'Banned!', description = "{} got banned".format(user.name), colour = ctx.message.author.color)
        try:
            await ctx.guild.ban(user)
        except Exception as e:
            if 'Permissions too low' in str(e):
                await client.say("The bot does not have sufficient permissions!")
        await ctx.say(embed=embed)
    else:
        await ctx.send('Stop!{}'.format(ctx.message.author.mention))

@bot.command()#Poll command
async def poll(ctx, *, message):
    author = ctx.message.author
    embed = discord.Embed(color=author.color, timestamp=datetime.datetime.utcnow())
    embed.set_author(name="Poll", icon_url=author.avatar_url)
    embed.description = message
    embed.set_footer(text=author.name)
    x = await ctx.send(embed=embed)
    await x.add_reaction("👍")
    await x.add_reaction("\U0001f937")
    await x.add_reaction("👎")

bot.run('MjgxODg5NzMzNDAyMDM0MTc4.DRMapA.MBSqSM2YG2TMgpeu4qH_D29Fosg', bot=True, reconnect=True)