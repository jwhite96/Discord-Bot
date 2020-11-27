import discord
import json
from discord.ext import commands


class Points(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # add new user to points
    @commands.Cog.listener()
    async def on_message(self, message):
        with open('users.json', 'r', encoding='utf8') as f:
            user = json.load(f)
        with open('users.json', 'w', encoding='utf8') as f:
            user[str(message.author.id)] = {}
            user[str(message.author.id)]['points'] = 0
            json.dump(user, f, sort_keys=True, indent=4, ensure_ascii=False)

# view leader board command
    @commands.command(name='leaders', help='View Leaderboard')
    async def leaders(self, ctx):
        
        # read from json
        ...

        embed = discord.Embed(title="Leaderboard 👑",
                              description=" ",
                              color=0xfff700)
        await ctx.send(embed=embed)

# view users points command
    @commands.command(name='bank', help='View Your Points')
    async def points(self, ctx):
        
        # read from json
        points = 0

        response = "Your Points: "
        await ctx.send(response)

# setup cog
def setup(bot):
    bot.add_cog(Points(bot))
