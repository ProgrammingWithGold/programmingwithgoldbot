import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '+')

@client.event
async def on_ready():
    print(f'Ping is at {round(client.latency * 1000)}')

@client.command()
async def ping(ctx): 
    await ctx.send(f'Your ping is at ---> {round(client.latency * 1000)}')

client.run('TOKEN')
