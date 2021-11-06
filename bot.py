# bot.py
import os
from sqlite3.dbapi2 import SQLITE_ALTER_TABLE

import discord
from discord.ext import commands
from dotenv import load_dotenv
from war_room.core.database.sqlite import SQLiteUserDatabase
from war_room.utils.utils import mkdir_and_touch

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
USER_DB_PATH = os.getenv('USER_DB_PATH')

bot = commands.Bot(command_prefix="!", case_insensitive=True)

mkdir_and_touch(USER_DB_PATH)
user_db = SQLiteUserDatabase(USER_DB_PATH)

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@bot.command(name='user', description="Greet the user!")
async def hello(ctx):
    user_id = ctx.author.id
    if not user_db.contains_user(user_id):
        message = "You are not registered for war!"
    else:
        user = user_db.get_user(user_id)
        message = str(user)
    await ctx.send(message)

@bot.command(name='queue', description="Queue for a specified number of games")
async def register(ctx, desired_game_count: int):
    user_id = ctx.author.id
    
    if not user_db.contains_user(user_id):
        user_db.register_user(user_id)
    user = user_db.get_user(user_id)
    user.game_count = desired_game_count
    user_db.update_user_information(user)

    message = f"You have been registered for {user.game_count} ongoing games"
    await ctx.send(message)

if __name__ == "__main__":
    bot.run(TOKEN)
