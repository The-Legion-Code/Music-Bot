import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='?', intents = discord.Intents.all())
  
for i in range(len(cogs)):
  cogs[i].setup(client)

client.run("OTg0MzAxNjcxNzY3MjQ0ODEw.GnAPK8.sNKv2JdnFrLHsO6c7dtGQaDFMw3pb-EBYcSOJo")
