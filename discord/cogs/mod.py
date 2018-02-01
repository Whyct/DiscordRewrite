import asyncio
import discord
import discord
from discord.ext.commands import Bot
from discord.ext import commands

class Moderation:
    def __init__(self,bot):
        self.bot = bot

    @commands.command()#Kick command
    async def kick(self,ctx,user:discord.Member):
        if ctx.message.author.guild_permissions.administrator==True and user.guild_permissions.administrator==False:
            print('Kicked: {}'.format(user.name))
            await ctx.send("Bye!")
            await ctx.guild.kick(user)
        else:
            await ctx.send('Bye! {}'.format(ctx.message.author.mention))
    @commands.command()
    async def ban(self,ctx, *, user : discord.Member):
        if ctx.message.author.guild_permissions.administrator==True and user.guild_permissions.administrator==False:
            embed = discord.Embed(title = 'Banned!', description = "{} got banned".format(user.name), colour = ctx.message.author.color)
            try:
                await ctx.guild.ban(user)
            except Exception as e:
                if 'Permissions too low' in str(e):
                    await ctx.send("The bot does not have sufficient permissions!")
            await ctx.say(embed=embed)
        else:
            await ctx.send('Stop!{}'.format(ctx.message.author.mention))

    @commands.command()
    async def mute(self,ctx, *, user : discord.Member):
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        if role==None:
            await ctx.send('The {} role has not been created'.format(role))
        elif ctx.message.author.guild_permissions.administrator==True:
                embed = discord.Embed(title = 'Muted!', description = "{} has been muted".format(user.name), colour = ctx.message.author.color)
                await user.add_roles(role)
                await ctx.send(embed=embed)
        else:
            await ctx.send('This command can only be used by administrators')
def setup(bot):
    bot.add_cog(Moderation(bot))