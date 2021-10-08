import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

client1 = commands.Bot(command_prefix='!')  # prefix our commands with '.'
players = {}

@client1.event
async def on_ready():
    print(f'{client1.user.name} has connected to Discord!')

# command to clear channel messages
@client1.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send("Messages have been cleared")

# command to clear channel messages
@client1.command()
async def Help(ctx):
    await ctx.send("""> **Just Listen Bot Commands**\n> **__!join__**\n> Joins the user voice channel\n> **__!play  \"<SONG-NAME>__\"**\n> Plays the song\n> **__!pause__**\n> Pause the current playing song\n> **__!resume__**\n> Resume playing the current song\n> **__!stop__**\n> Stops the current playing song\n> **__!Help__**\n> Displays all the commands of the Bot""")

@client1.command()
# @commands.has_permissions(manage_messages=True)
async def load(_, extensions):
    client1.load_extension(f'cogs.{extensions}')


@client1.command()
# @commands.has_permissions(manage_messages=True)
async def unload(_, extensions):
    client1.unload_extension(f'cogs.{extensions}')


@client1.command()
# @commands.has_permissions(manage_messages=True)
async def reload(_, extensions):
    client1.unload_extension(f'cogs.{extensions}')
    client1.load_extension(f'cogs.{extensions}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client1.load_extension(f'cogs.{filename[:-3]}')

client1.run(os.getenv('TOKEN'))