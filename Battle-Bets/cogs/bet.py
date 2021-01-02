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

        # bet variables - ADD POINTS IN!
        user = ctx.message.author.name
        time = datetime.now().strftime("%Y-%m-%d %H:%M")
        status = 0 # 0 for active; 1 for inactive

        # save bet to json file
        with open('bets.json', 'r', encoding='utf8') as f:
            bets = json.load(f)
        with open('bets.json', 'w', encoding='utf8') as f:
            bets['bet'].append({
                'user': str(user),
                'bet': str(text),
                'time': str(time),
                'status': status,
            })

            json.dump(bets, f, sort_keys=True, indent=4, ensure_ascii=False)

        # print bet in embed
        embed = Bet.printNewBet(self, user, text, time)
        message = await ctx.send(embed=embed)
        await message.add_reaction("✅")
        await message.add_reaction("❌")
        

    # create bet embed
    def printNewBet(self, user, text, time):
        embed=discord.Embed(title=user + " placed a new bet", 
        description= "```" + text + "```", color=0x00b8b5)
        #embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name='Points: ', value="```0```", inline=False)
        embed.add_field(name='Time Created: ', value="```" + time + "```", inline=False)
        embed.add_field(name="Actions:", value="```Accept the Bet: ✅``` ```Decline the Bet: ❌```", inline=False)       

        return embed


    # view bets command
    @commands.command(name='viewbets', help='View Current Bets')
    async def viewbets(self, ctx):
        embed = discord.Embed(title="Current Bets 💰", description="", color=0x00b8b5)

        # read from json
        with open('bets.json') as f:
                bets = json.load(f)

        # get bets - ADD POINTS IN!
        for bet in bets['bet']: 
            # ADD - if status = 0; display bet
            username = bet.get('user', bet)
            bet = bet.get('bet', bet)
            embed.add_field(name="Bet: " + bet, value="Created by: " + username, inline=False)
        f.close()

        await ctx.send(embed=embed)

# setup cog
def setup(bot):
    bot.add_cog(Bet(bot))
