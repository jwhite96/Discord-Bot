import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='?', help='Bot Information')
    async def info(self, ctx):
        embed=discord.Embed(title="Battle Bets", description="--- Short Description ---", color=0x00b8b5)
        embed.add_field(name="Help", value="Type $help to get the full list of commands", inline=False)
        embed.add_field(name="Bets", value="Type $bet to start a new bet", inline=False)
        embed.add_field(name="Bank", value="Type $bank to view your own balance", inline=False)
        embed.add_field(name="Leaderboard", value="Type $leaders to view the leaderboard", inline=True)
        embed.set_footer(text="© Copyright 2020")
        await ctx.send(embed=embed)

    # clear chat - REMOVE LATER OR ADD PERMISSIONS
    @commands.command(name='clear', help='Clear Chat')
    async def clear(self, ctx):
        await ctx.channel.purge()


# setup cog
def setup(bot):
    bot.add_cog(Help(bot))
