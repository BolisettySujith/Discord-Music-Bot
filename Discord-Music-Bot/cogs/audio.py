from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
from youtubesearchpython import VideosSearch
from youtubesearchpython.legacy import overrides



class Audio(commands.Cog):
    def __init__(self, client):
        self.client = client

    # command for bot to join the channel of the user, if the bot has already joined and is in a different channel, it will move to the channel the user is in
    @commands.command()
    async def join(self,ctx):
        """Add bot to voice channel"""
        channel = ctx.message.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

    # command to play sound from a youtube URL
    @commands.command()
    async def play(self,ctx, SongName):
        url = VideosSearch(SongName, limit = 1).result()['result'][0]['link']
        print(url)
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
        FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        voice = get(self.client.voice_clients, guild=ctx.guild)

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
    @commands.command()
    async def resume(self,ctx):
        voice = get(self.client.voice_clients, guild=ctx.guild)

        if not voice.is_playing():
            voice.resume()
            await ctx.send('Music is resuming')

    # command to pause voice if it is playing
    @commands.command()
    async def pause(self,ctx):
        voice = get(self.client.voice_clients, guild=ctx.guild)

        if voice.is_playing():
            voice.pause()
            await ctx.send('Music has been paused')

    # command to stop voice
    @commands.command()
    async def stop(self,ctx):
        voice = get(self.client.voice_clients, guild=ctx.guild)

        if voice.is_playing():
            voice.stop()
            await ctx.send('Music has been Stoped...')
    
    @commands.command()
    async def leave(self,ctx):
        voice = ctx.message.guild.voice_client
        await voice.disconnect()


def setup(client):
    client.add_cog(Audio(client))