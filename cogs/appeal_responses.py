import discord
import os

from discord.ext import commands
from dotenv import load_dotenv
from discord.ext.commands import has_permissions
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
    @has_permissions(kick_members=True)
    async def approve(self, ctx, member: discord.User):

        main_guild = self.bot.get_guild(int(main_guild_id))
        appeal_guild = self.bot.get_guild(int(appeal_guild_id))

        await ctx.message.delete()

        await main_guild.unban(member)
        await appeal_guild.kick(member)

        await member.send(
            "**<:check:711178140281602129> Your ban appeal for the VALORANT Discord has been approved! You can join back by using this link (if the invite link is not working then press `ctrl+r`):** https://discord.gg/VALORANT")

        embed = discord.Embed(
            title=f"<:check:711178140281602129> {member.name}#{member.discriminator} (`{member.id}`) their ban appeal has been approved!",
            color=0x6bd467)
        try:
            await ctx.send(content=None, embed=embed)
        except:
            await ctx.send("Failed to send DM")

        return


    @commands.command(
        pass_context=True,
        name='deny',
        description='Deny an appeal.',
        aliases=['d'],
        usage='cog'
    )
    @has_permissions(kick_members=True)
    async def deny(self, ctx, member: discord.User):

        appeal_guild = self.bot.get_guild(int(appeal_guild_id))

        await ctx.message.delete()

        await appeal_guild.ban(member)

        await member.send("**❌ Your ban appeal for the VALORANT Discord has been denied.**")
        embed = discord.Embed(
            title=f"❌ {member.name}#{member.discriminator} (`{member.id}`) their ban appeal has been denied.",
            color=0xdd2e44)
        await ctx.send(content=None, embed=embed)

        return

    @commands.command(
        pass_context=True,
        name='reduce',
        description='Informs the user that their ban has been reduced because of their appeal.',
        aliases=['r', 're'],
    )
    @has_permissions(kick_members=True)
    async def reduce(self, ctx, member: discord.User, arg):

        appeal_guild = self.bot.get_guild(int(appeal_guild_id))

        await ctx.message.delete()

        await appeal_guild.kick(member)

        await member.send(f"**🕐 Your appeal has been reviewed and your ban has been reduced to {arg} days.**")
        embed = discord.Embed(
            title=f"🕐 {member.name}#{member.discriminator} (`{member.id}`) their ban has been reduced to {arg} days.",
            color=0xe1e8ed)
        await ctx.send(content=None, embed=embed)


        return


def setup(bot):
    bot.add_cog(Appeal_Responses(bot))
