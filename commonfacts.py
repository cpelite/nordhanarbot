from discord.ext import commands
import discord

class länder(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def seyffenstein(self, ctx):
        embed = discord.Embed(title="Fakten über das Erzherzogtum Seyffenstein")
        embed.add_field(name="Landesoberhaupt", value="Jennifer von Seyffenstein, Erzherzogin von Seyffenstein")
        embed.add_field(name="Regierungschef", value="Stephan von Demelstein")
        embed.add_field(name="Landeshauptstadt", value="Syffia")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def bajar(self, ctx):
        embed = discord.Embed(title="Fakten über das Königreich Bajar")
        embed.add_field(name="Landesoberhaupt", value="Friedrich Viktor August von Bajar, König von Bajar")
        embed.add_field(name="Regierungschef", value="Gerhard Störer")
        embed.add_field(name="Landeshauptstadt", value="Bajarsia")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def hamartia(self, ctx):
        embed = discord.Embed(title="Fakten über das Herzogtum Hamartia")
        embed.add_field(name="Landesoberhaupt", value="Johannes von Hamartia, Herzog von Hamartia")
        embed.add_field(name="Regierungschef", value="vakant")
        embed.add_field(name="Landeshauptstadt", value="Hamartia-Stadt")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def treckelhude(self, ctx):
        embed = discord.Embed(title="Fakten über die Hansestadt Treckelhude")
        embed.add_field(name="Landesoberhaupt", value="Tobias Brinkzik-Morgenlich, Bürgermeister von Treckelhude")
        embed.add_field(name="Regierungschef", value="Tobias Brinkzik-Morgenlich")
        embed.add_field(name="Landeshauptstadt", value="Treckelhude")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def treckelhude(self, ctx):
        embed = discord.Embed(title="Fakten über die reichsunmittelbare Stadt San Vezzano")
        embed.add_field(name="Landesoberhaupt", value="Filippo di Castellani, Gouverneur von San Vezzano")
        embed.add_field(name="Regierungschef", value="Eugenio Marcano, Doge von San Vezzano")
        embed.add_field(name="Landeshauptstadt", value="San Vezzano")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def mikulov(self, ctx):
        embed = discord.Embed(title="Fakten über die reichsunmittelbare Stadt San Vezzano")
        embed.add_field(name="Landesoberhaupt", value="Pavel Sebirov, Großherzog von Mikulov")
        embed.add_field(name="Regierungschef", value="-")
        embed.add_field(name="Landeshauptstadt", value="Mikulov")
        await ctx.send(embed=embed)
        return

class parlamente(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def reichsdiät(self, ctx):
        embed = discord.Embed(title="Die aktuelle Sitzverteilung in der Reichsdiät")
        embed.add_field(name="Gesamtzahl der Sitze", value="261 Sitze")
        embed.add_field(name="Sozialisten (S)", value="95 Sitze")
        embed.add_field(name="Grüne (G)", value="8 Sitze")
        embed.add_field(name="Liberale (L)", value="49 Sitze")
        embed.add_field(name="Konservative (K)", value="63 Sitze")
        embed.add_field(name="Landbund (LB)", value="24 Sitze")
        embed.add_field(name="Freiheitlich Nationale Versammlung (FNV)", value="21 Sitze")
        embed.add_field(name="Christliche Reichsbewegung (CRB)", value="1 Sitz")
        await ctx.send(embed=embed)
        return

def setup(bot):
    bot.add_cog(länder(bot))
    bot.add_cog(parlamente(bot))