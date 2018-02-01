import asyncio
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import datetime
import sys, traceback
import time

class Fun:
    def __init__(self,bot):
        self.bot = bot
    @commands.command() #Simple Ping Pong command
    async def ping(ctx):
        await ctx.send(':ping_pong: Pong!')

    @commands.command()#Embeds the word 'Hi'
    async def embed(self,ctx):
        embed = discord.Embed(description = 'Hi')
        await ctx.send(embed = embed)

    @commands.command()#Gives User Information
    async def info(self,ctx, user: discord.Member):
        embed = discord.Embed(title = 'User Info',image = user.avatar,colour = user.colour)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name = "Username: ", value = user.name, inline=True)
        embed.add_field(name = "Join Date: ", value = user.joined_at,inline=True)
        embed.add_field(name = "Display name: ", value = user.display_name,inline=True)
        embed.add_field(name = "Account Created at: ",value = user.created_at,inline=True)
        await ctx.send(embed = embed)

    @commands.command()#A simple password to channel program
    async def password(self,ctx, *, password):
        if password=='123':
            role = discord.utils.get(ctx.guild.roles, name='x')
            await ctx.send('Granted')
            ctx.message.delete()
            await ctx.message.author.add_roles(role)
        else:
            await ctx.send('Try Again')
        

    @commands.command()#Poll command
    async def poll(self,ctx, *, message):
        author = ctx.message.author
        embed = discord.Embed(color=author.color, timestamp=datetime.datetime.utcnow())
        embed.set_author(name="Poll", icon_url=author.avatar_url)
        embed.description = message
        embed.set_footer(text=author.name)
        x = await ctx.send(embed=embed)
        await x.add_reaction("👍")
        await x.add_reaction("\U0001f937")
        await x.add_reaction("👎")
def setup(bot):
    bot.add_cog(Fun(bot))