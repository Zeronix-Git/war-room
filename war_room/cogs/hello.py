import discord
from discord.ext import commands

class Hello(commands.Cog):
    """ A simple example to familiarize myself with the Cog syntax. """

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}.'.format(member))

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """ Says hello """
        member = member or ctx.author
        await ctx.send('Hello {0.name}~'.format(member))