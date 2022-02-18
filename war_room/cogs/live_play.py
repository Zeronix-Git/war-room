import discord
from discord.ext import commands

class Matchmaker(commands.Cog):
    """ Functionality for handling live play matchmaking """

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """ Says hello """
        member = member or ctx.author
        await ctx.send('Hello {0.name}~'.format(member))