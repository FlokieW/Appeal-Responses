import asyncio

import discord
import os

from pymongo import MongoClient
from discord.ext import commands
from dotenv import load_dotenv
from discord.ext.commands import has_permissions
from datetime import datetime as d
from pathlib import Path

basepath = Path()
basedir = str(basepath.cwd())
envars = basepath.cwd() / '.env'
load_dotenv(envars)
token = os.getenv('discord_token')
prefix = os.getenv('bot_prefix')
bot = commands.Bot(command_prefix=prefix, case_insensitive=True)
cogs = ['cogs.appeal_responses']


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="zeppelin.gg"))
    print('{0.user} is now ready!'.format(bot))
    bot.remove_command('help')
    for cog in cogs:
        bot.load_extension(cog)
    return

class Utility(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='?ping',
        description='The ping command',
        aliases=['p']
    )
    @has_permissions(kick_members=True)
    async def ping(self, ctx):

        start = d.timestamp(d.now())

        msg = await ctx.send(content='Pinging')
        await msg.edit(content=f'**Pong!** _One message round-trip took `{(d.timestamp(d.now()) - start) * 1000}ms`._')

        return

bot.run(token)
