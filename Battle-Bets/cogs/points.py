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
            users = json.load(f)
        with open('users.json', 'w', encoding='utf8') as f: #creates duplicates for every message - NEEDS FIXING!!!
            users['user'].append({
                'userID': str(message.author.id),
                'user': str(message.author.name),
                'points': '0',
            })

            json.dump(users, f, sort_keys=True, indent=4, ensure_ascii=False)

# view leader board command
    @commands.command(name='leaders', help='View Leaderboard')
    async def leaders(self, ctx):
        
        embed = discord.Embed(title="Leaderboard 👑", description="", color=0x00b8b5)

        # read from json
        with open('users.json') as f:
                users = json.load(f)

        # get points
        for user in users['user']:
            username = user.get('user', user)
            points = user.get('points', user)
            embed.add_field(name="User: " + username, value="Points: " + points, inline=False)
        f.close()

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
