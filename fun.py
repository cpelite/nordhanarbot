from discord.ext import commands
import discord

class gifs(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def wat(self, ctx):
        embed = discord.Embed(title="Wat?")
        embed.set_image(url="https://media.tenor.com/images/2c474b0b4404b624d80df839bc688b5f/tenor.gif")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def confusion(self, ctx):
        embed = discord.Embed(title="When Confusion kicks in..")
        embed.set_image(url="https://media.tenor.com/images/afdd108e2e6b46fd825a66e1b92dc87e/tenor.gif")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def triggered(self, ctx):
        embed = discord.Embed(title="TRIGGERED!")
        embed.set_image(url="https://media.tenor.com/images/e0940c7f695430dc680f21c7a48417ba/tenor.gif")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def diggah(self, ctx):
        embed = discord.Embed(title="Diggah...")
        embed.set_image(url="https://media1.tenor.com/images/b557a994267920b1271b49bda6153f01/tenor.gif?itemid=7363931")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def wtf(self, ctx):
        embed = discord.Embed(title="WTF...")
        embed.set_image(url="https://media1.tenor.com/images/86f3b65249fbaca12e142281558c06ac/tenor.gif?itemid=4486363")
        await ctx.send(embed=embed)
        return

def setup(bot):
    bot.add_cog(gifs(bot))
