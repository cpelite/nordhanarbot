from discord.ext import commands
import discord

class länder(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def seyffenstein(self, ctx):
        embed = discord.Embed(title="Fakten über das Erzherzogtum Seyffenstein")
        embed.add_field(name="Landesoberhaupt", value="Jennifer von Seyffenstein, Erzherzogin von Seyffenstein")
        embed.add_field(name="Regierungschef", value="Bernhard von Dassen")
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
        embed.add_field(name="Landesoberhaupt", value="Alfred Drewes, Bürgermeister von Treckelhude")
        embed.add_field(name="Regierungschef", value="Alfred Drewes")
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
        embed = discord.Embed(title="Fakten über das Großherzogtum Mikulov")
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
        embed.add_field(name="Gesamtzahl der Sitze", value="269 Sitze")
        embed.add_field(name="Monarchistisch-Christliche-Union (MCU)", value="53 Sitze")
        embed.add_field(name="Sozialisten (S)", value="46 Sitze")
        embed.add_field(name="Christliche Reichsbewegung (CRB)", value="37 Sitze")
        embed.add_field(name="Marxistisch Ökologische Partei (MÖP)", value="27 Sitze")
        embed.add_field(name="Freiheitlich Nationale Versammlung (FNV)", value="20 Sitze")
        embed.add_field(name="Landbund (LB)", value="18 Sitze")
        embed.add_field(name="Partei des Neuen (PN)", value="14 Sitze")
        embed.add_field(name="Nationale Versammlung (NV)", value="13 Sitze")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def rdgrafik(self, message):
        await message.channel.send("https://seyffenstein-bajar.de/lychee/uploads/big/4b60d1599c6794f8b97894b4db7d9dcd.png")
        return

def setup(bot):
    bot.add_cog(länder(bot))
    bot.add_cog(parlamente(bot))