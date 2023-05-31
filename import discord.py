import discord
from discord.ext import commands

# Erstelle eine Instanz des Bot-Clients
bot = commands.Bot(command_prefix='!')

# Event, das ausgeführt wird, wenn der Bot gestartet ist
@bot.event
async def on_ready():
    print(f'Bot ist bereit! Angemeldet als {bot.user.name}')

# Befehl, um den Bot auf eine Nachricht antworten zu lassen
@bot.command()
async def hallo(ctx):
    await ctx.send(f'Hallo {ctx.author.name}!')

# Befehl, um einen Benutzer zu kicken
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member):
    await member.kick()
    await ctx.send(f'{member.mention} wurde gekickt!')

# Befehl, um den Bot zu beenden (nur für den Bot-Eigentümer)
@bot.command()
@commands.is_owner()
async def stop(ctx):
    await bot.logout()

# Token des Bots (du musst dies durch deinen eigenen Token ersetzen)
token = 'DEIN_BOT_TOKEN'

# Den Bot mit dem Token starten
bot.run(token)