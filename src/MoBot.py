import asyncio
import logging
import random

import discord
from discord import Game
from discord.ext.commands import Bot
from discord.utils import get

# own
import config as cfg
import penandpaper

logger = logging.getLogger("discord")
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)


BOT_PREFIX = ("?", "!")

client = Bot(command_prefix=BOT_PREFIX)


@client.command(pass_context=True, name="join", brief="join bot to the voice channel")
async def join(ctx):
    """join voice channel

    Parameters
    ----------
    ctx : context
    """
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"The bot has connected to {channel}\n")

    await ctx.send(f"joined {channel}")


@client.command(pass_context=True, name="leave", brief="disconnect bot from the voice channel")
async def leave(ctx):
    """leave voice channel

    Parameters
    ----------
    ctx : context
    """
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"the bot has left {channel}")
        await ctx.send(f"the bot has left {channel}")
    else:
        print("Bot was told to leave voice channel, but was not in one")
        await ctx.send("Bot was told to leave voice channel, but was not in one")


@client.command(pass_content=True, name="play", brief="play sample audio file")
async def play(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio(cfg.PATH + "sound/test.mp3"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07


@client.command(pass_content=True, name="kackwaffe", brief="play sample audio file")
async def kackwaffe(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio(cfg.PATH + "sound/kackwaffe.mp3"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.7


@client.command(name="notice", brief='use !notice "text" to create a notice in the log.')
async def notice(ctx, text):
    user = ctx.author
    write_history(user.name + ": " + str(text))


@client.command(name="thanks", brief="test it =)")
async def thanks(ctx):
    thx_file = cfg.PATH + "files/thanks.txt"
    with open(thx_file) as f:
        response = [line.rstrip() for line in f]
    await ctx.send(random.choice(response))


@client.command(name="whisky_aroma", brief="Whiksy Aroma =)")
async def whisky_aroma(ctx):
    thx_file = cfg.PATH + "files/aroma.txt"
    with open(thx_file) as f:
        response = [line.rstrip() for line in f]
    t1 = random.choice(response)
    t2 = random.choice(response)
    t3 = random.choice(response)

    await ctx.send(t1 + ", " + t2 + " und " + t3)


@client.command(name="thanks_voice", brief="test it =)")
async def thanks_voice(ctx):
    thx_file = cfg.PATH + "files/thanks.txt"
    with open(thx_file) as f:
        response = [line.rstrip() for line in f]
    await ctx.send(random.choice(response), tts=True)


@client.event
async def on_ready():
    await client.change_presence(activity=Game(name="with humans"))
    print("Logged in as " + client.user.name)


async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)


def write_history(text):
    with open("history.txt", "a") as the_file:
        the_file.write(text + "\n")


client.add_cog(penandpaper.Pen_And_Paper(client))

if __name__ == "__main__":
    client.loop.create_task(list_servers())
    client.run(cfg.TOKEN)
