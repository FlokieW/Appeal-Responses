import asyncio
import os

import discord
from discord.ext import commands
from datetime import datetime as d
from discord.ext.commands import has_permissions
from pymongo import MongoClient

from dotenv import load_dotenv
from pathlib import Path

basepath = Path()
basedir = str(basepath.cwd())
envars = basepath.cwd() / '.env'
load_dotenv(envars)
admin = os.getenv('admin')
offtopic = os.getenv('offtopic')

mongo_url = os.getenv('mongo_url')
main_guild_id = os.getenv('main_guild_id')
appeal_guild_id = os.getenv('appeal_guild_id')
punishment_logs_id = os.getenv('punishment_logs_id')
cmd_id = os.getenv('cmd_id')
appeals_id = os.getenv('appeals_id')

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

def setup(bot):
    bot.add_cog(Utility(bot))
