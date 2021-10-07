import os
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
from youtubesearchpython import VideosSearch
from youtubesearchpython.legacy import overrides

load_dotenv()

client1 = commands.Bot(command_prefix='!')  # prefix our commands with '.'
players = {}

# command for bot to join the channel of the user, if the bot has already joined and is in a different channel, it will move to the channel the user is in
@client1.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client1.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

# command to play sound from a youtube URL
@client1.command()
async def play(ctx, SongName):
    url = VideosSearch(SongName, limit = 1).result()['result'][0]['link']
    print(url)
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(client1.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['url']
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice.is_playing()
        await ctx.send(f"> **Now Playing**\n> {url}")
    # check if the bot is already playing
    else:
        await ctx.send("Music is already playing")
        return

# command to resume voice if it is paused
@client1.command()
async def resume(ctx):
    voice = get(client1.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        voice.resume()
        await ctx.send('Music is resuming')

# command to pause voice if it is playing
@client1.command()
async def pause(ctx):
    voice = get(client1.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.pause()
        await ctx.send('Music has been paused')

# command to stop voice
@client1.command()
async def stop(ctx):
    voice = get(client1.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.stop()
        await ctx.send('Music has been Stoped...')

# command to clear channel messages
@client1.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send("Messages have been cleared")

# command to clear channel messages
@client1.command()
async def Help(ctx):
    await ctx.send("""> **Just Listen Bot Commands**\n> **__!join__**\n> Joins the user voice channel\n> **__!play  \"<SONG-NAME>__\"**\n> Plays the song\n> **__!pause__**\n> Pause the current playing song\n> **__!resume__**\n> Resume playing the current song\n> **__!stop__**\n> Stops the current playing song\n> **__!Help__**\n> Displays all the commands of the Bot""")


client1.run(os.getenv('TOKEN'))