import asyncio

import discord
import os

from pymongo import MongoClient
from discord.ext import commands
from dotenv import load_dotenv
from pathlib import Path

basepath = Path()
basedir = str(basepath.cwd())
envars = basepath.cwd() / '.env'
load_dotenv(envars)
token = os.getenv('discord_token')
prefix = os.getenv('bot_prefix')
mongo_url = os.getenv('mongo_url')
main_guild_id = os.getenv('main_guild_id')
appeal_guild_id = os.getenv('appeal_guild_id')
punishment_logs_id = os.getenv('punishment_logs_id')
cmd_id = os.getenv('cmd_id')
appeals_id = os.getenv('appeals_id')

bot_cmd = os.getenv('bot_cmd')
lfg_casual_na = os.getenv('lfg_casual_na')
lfg_competitive_na = os.getenv('lfg_competitive_na')
lfg_custom_na = os.getenv('lfg_custom_na')
lfg_casual_eu = os.getenv('lfg_casual_eu')
lfg_competitive_eu = os.getenv('lfg_competitive_eu')
lfg_custom_eu = os.getenv('lfg_custom_eu')
lfg_casual_other = os.getenv('lfg_casual_other')
lfg_competitive_other = os.getenv('lfg_competitive_other')
lfg_custom_other = os.getenv('lfg_custom_other')

bot = commands.Bot(command_prefix=prefix, case_insensitive=True)

cluster = MongoClient(mongo_url)
db = cluster["Users"]
collection = db["Users"]

cogs = ['cogs.util', 'cogs.appeal_responses', 'cogs.error_handler']


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="zeppelin.gg"))
    print('{0.user} is now ready!'.format(bot))
    bot.remove_command('help')
    for cog in cogs:
        bot.load_extension(cog)
    return

@bot.event
async def on_message(msg):

    cmd = bot.get_channel(int(cmd_id))

    await bot.process_commands(msg)

    if msg.author.bot == False and msg.channel == cmd:
        await msg.delete()

    return

bot.run(token)
