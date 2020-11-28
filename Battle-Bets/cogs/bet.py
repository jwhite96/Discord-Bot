import json
import discord
from datetime import datetime
from discord.ext import commands


class Bet(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # new bet command
    @commands.command(name='bet', help='Place a New Bet', pass_context=True)
    async def bet(self, ctx, *, text):
        await ctx.message.delete()

        # bet variables
        user = ctx.message.author.name
        time = datetime.now().strftime("%Y-%m-%d %H:%M")
        # create new bet and add to json file

        # print bet in embed
        embed = Bet.printNewBet(self, user, text, time)
        message = await ctx.send(embed=embed)
        await message.add_reaction("✅")
        await message.add_reaction("❌")
        

    # create bet embed
    def printNewBet(self, user, text, time):
        embed=discord.Embed(title=user + " placed a new bet", 
        description= "```" + text + "```", color=0x43b581)
        #embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name='Points: ', value="```0```", inline=False)
        embed.add_field(name='Bet Ends: ', value="```" + time + "```", inline=False)
        embed.add_field(name="Actions:", value="```Accept the Bet: ✅``` ```Decline the Bet: ❌```", inline=False)       

        return embed


    # view bets command
    @commands.command(name='viewbets', help='View Current Bets')
    async def viewbets(self, ctx):
        ...


# setup cog
def setup(bot):
    bot.add_cog(Bet(bot))
