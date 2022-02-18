import os
from war_room.cogs import hello
from dotenv import load_dotenv
from discord.ext import commands

if __name__ == "__main__":
    bot = commands.Bot(command_prefix='$')
    bot.add_cog(hello.Hello(bot))

    load_dotenv()
    TOKEN = os.getenv('TOKEN')
    bot.run(TOKEN)
