import discord
import os

from discord.ext import commands
from dotenv import load_dotenv
from discord.ext.commands import has_any_role
from pathlib import Path

basepath = Path()
basedir = str(basepath.cwd())
envars = basepath.cwd() / '.env'
load_dotenv(envars)
main_guild_id = os.getenv('main_guild_id')
appeal_guild_id = os.getenv('appeal_guild_id')

class Appeal_Responses(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='approve',
        description='Approve an appeal.',
        aliases=['app', 'a', 'accept'],
    )
    @has_any_role(758104829242507294, 886986131164520518, 897179370752475207)
    async def approve(self, ctx, member: discord.User):

        main_guild = self.bot.get_guild(int(main_guild_id))
        appeal_guild = self.bot.get_guild(int(appeal_guild_id))

        await ctx.message.delete()

        embed = discord.Embed(
            title=f"<:check:711178140281602129> {member.name}#{member.discriminator} (`{member.id}`) their ban appeal has been approved!",
            color=0x6bd467)
        embed2 = discord.Embed(
            title=f"<:check:711178140281602129> {member.name}#{member.discriminator} (`{member.id}`) their ban appeal has been approved but they were not messaged!",
            color=0x6bd467)
        try:
            await member.send("**<:check:711178140281602129> Your ban appeal for the VALORANT Discord has been approved! You can join back by using this link (if the invite link is not working then press `ctrl+r`):** https://discord.gg/VALORANT")
            await ctx.send(content=None, embed=embed)
        except:
            await ctx.send(content=None, embed=embed2)
        await appeal_guild.kick(member)
        await main_guild.unban(member)

        return


    @commands.command(
        pass_context=True,
        name='deny',
        description='Deny an appeal.',
        aliases=['d'],
        usage='cog'
    )
    @has_any_role(758104829242507294, 886986131164520518, 897179370752475207)
    async def deny(self, ctx, member: discord.User):

        appeal_guild = self.bot.get_guild(int(appeal_guild_id))

        await ctx.message.delete()

        embed = discord.Embed(
            title=f"??? {member.name}#{member.discriminator} (`{member.id}`) their ban appeal has been denied.",
            color=0xdd2e44)
        embed2 = discord.Embed(
            title=f"??? {member.name}#{member.discriminator} (`{member.id}`) their ban appeal has been denied but they were not messaged.",
            color=0xdd2e44)
        try:
            await member.send("**??? Your ban appeal for the VALORANT Discord has been denied.**")
            await ctx.send(content=None, embed=embed)
        except:
            await ctx.send(content=None, embed=embed2)
        await appeal_guild.ban(member)        
        
        return

    @commands.command(
        pass_context=True,
        name='reduce',
        description='Informs the user that their ban has been reduced because of their appeal.',
        aliases=['r', 're'],
    )
    @has_any_role(758104829242507294, 886986131164520518, 897179370752475207)
    async def reduce(self, ctx, member: discord.User, arg):

        appeal_guild = self.bot.get_guild(int(appeal_guild_id))

        await ctx.message.delete()

        embed = discord.Embed(
            title=f"???? {member.name}#{member.discriminator} (`{member.id}`) their ban has been reduced to {arg} days.",
            color=0xe1e8ed)
        embed2 = discord.Embed(
            title=f"???? {member.name}#{member.discriminator} (`{member.id}`) their ban has been reduced to {arg} days but they were not messaged.",
            color=0xe1e8ed)

        try:
            await member.send(f"**???? Your appeal has been reviewed and your ban has been reduced to {arg} days.**")    
            await ctx.send(content=None, embed=embed)
        except:
            await ctx.send(content=None, embed=embed2)
        await appeal_guild.kick(member)

        return

    @commands.command(
        pass_context=True,
        name='dmtest',
        description='DM test.',
    )
    @has_any_role(758104829242507294, 886986131164520518, 897179370752475207)
    async def dmtest(self, ctx, member: discord.User):

        embed = discord.Embed(
            title=f"User was DM'd.",
            color=0xe1e8ed)
        embed2 = discord.Embed(
            title=f"User was not DM'd.",
            color=0xe1e8ed)

        try:
            await member.send(f"**DM test**")
            await ctx.send(content=None, embed=embed)
        except:
            await ctx.send(content=None, embed=embed2)

        return


def setup(bot):
    bot.add_cog(Appeal_Responses(bot))
