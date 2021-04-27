import asyncio
import logging
import random

import discord
from discord import Game
from discord.ext.commands import Bot
from discord.utils import get
#from discord.ext import commands
#from prettytable import PrettyTable

# own
import config as cfg

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


BOT_PREFIX = ("?", "!")

client = Bot(command_prefix=BOT_PREFIX)

@client.command(pass_context=True, name='join', brief='join bot to the voice channel')
async def join(ctx):
  """ join voice channel

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

@client.command(pass_context=True,name='leave', brief='disconnect bot from the voice channel')
async def leave(ctx):
  """ leave voice channel

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


@client.command(pass_content=True, name='play', brief='play sample audio file')
async def play(ctx):
  voice = get(client.voice_clients, guild=ctx.guild)
  voice.play(discord.FFmpegPCMAudio(cfg.PATH + "sound/test.mp3"))
  voice.source = discord.PCMVolumeTransformer(voice.source)
  voice.source.volume = 0.07

@client.command(pass_content=True, name='kackwaffe', brief='play sample audio file')
async def kackwaffe(ctx):
  voice = get(client.voice_clients, guild=ctx.guild)
  voice.play(discord.FFmpegPCMAudio(cfg.PATH + "sound/kackwaffe.mp3"))
  voice.source = discord.PCMVolumeTransformer(voice.source)
  voice.source.volume = 0.7

@client.command(name='d6', brief="rolls a 6-sided dice")
async def d6(ctx):
  """ role a 6-sided dice

  Parameters
  ----------
  ctx : context
  """
  await ctx.send(random.randint(1, 6))

@client.command(name='d8', brief="rolls a 8-sided dice")
async def d8(ctx):
  """ role a 8-sided dice

  Parameters
  ----------
  ctx : context
  """
  await ctx.send(random.randint(1, 8))



@client.command(name='d10', brief="rolls a 10-sided dice")
async def d10(ctx):
  """ role a 10-sided dice

  Parameters
  ----------
  ctx : context
  """
  await ctx.send(random.randint(1, 10))


@client.command(name='d20', brief="rolls a 20-sided dice")
async def d20(ctx):
  """ role a 20-sided dice

  Parameters
  ----------
    ctx : context

  """
  await ctx.send(random.randint(1, 20))


@client.command(name='d100', brief="rolls a 100-sided dice")
async def d100(ctx):
  """ role a 100-sided dice

  Parameters
  ----------
  ctx : context

  """
  await ctx.send(random.randint(1, 100))


@client.command(name='strange', brief="!strange <difficulty>")
async def strange(ctx, number):
  """ special command for the pen and paper game Strange. Roll a D20 and check against a specific difficulty.

    Parameters
    ----------
    ctx : context

    number : integer
      difficult of the roll
  """
  user = ctx.author
  dice = random.randint(1, 20)

  voice = get(client.voice_clients, guild=ctx.guild)


  print(dice)
  print("strange: " + str(int(number) * 3))
  if dice >= int(number) * 3:
    if dice == 20:
      write_history('good job ' + user.name + '. dice = ' + str(dice) + ', strange = ' + str(number))
      if voice and voice.is_connected():
        voice.play(discord.FFmpegPCMAudio("sound/20.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.4
      await ctx.send('good job ' + user.name + ' (' + str(dice) + ')')
    else:
      write_history('good job ' + user.name + '. dice = ' + str(dice) + ', strange = ' + str(number))
      await ctx.send('good job ' + user.name + ' (' + str(dice) + ')')
  else:
    if dice == 1:
      write_history('Ohoh :hot_face: ' + user.name + '. dice = ' + str(dice) + ', strange = ' + str(number))
      if voice and voice.is_connected():
        voice.play(discord.FFmpegPCMAudio("sound/1.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.4
      await ctx.send('Ohoh :hot_face: ' + user.name + ' (' + str(dice) + '). Setzt lieber ein XP du Noob')
    else:
      write_history('Ohoh ' + user.name + '. dice = ' + str(dice) + ', strange = ' + str(number))
      await ctx.send('Ohoh ' + user.name + ' (' + str(dice) + ')')


@client.command(name='character',brief='Information aboud Characters')
async def character(ctx):
  datei = open('character.txt', 'r')
  await ctx.send(datei.read())

@client.command(name='notice', brief='use !notice "text" to create a notice in the log.')
async def notice(ctx, text):
  user = ctx.author
  write_history(user.name + ': ' + str(text))

@client.command(name='thanks',brief='test it =)')
async def thanks(ctx):
  thx_file = cfg.PATH + "files/thanks.txt"
  with open(thx_file) as f:
      response = [line.rstrip() for line in f]
  await ctx.send(random.choice(response))

@client.command(name='whisky_aroma',brief='Whiksy Aroma =)')
async def whisky_aroma(ctx):
  thx_file = cfg.PATH + "files/aroma.txt"
  with open(thx_file) as f:
      response = [line.rstrip() for line in f]
  t1 = random.choice(response)
  t2 = random.choice(response)
  t3 = random.choice(response)

  await ctx.send(t1 + ', ' + t2 + ' und ' + t3)


@client.command(name='thanks_voice',brief='test it =)')
async def thanks_voice(ctx):
  thx_file = cfg.PATH + "files/thanks.txt"
  with open(thx_file) as f:
      response = [line.rstrip() for line in f]
  await ctx.send(random.choice(response),tts=True)

@client.command(name='cypher', brief="get a cypher.", pass_context=True)
async def cypher(ctx):
  """ get a cypher

    Parameters
    ----------
    ctx : context

  """
  user = ctx.author
  cypher_file = cfg.PATH + "files/cypher.txt"
  with open(cypher_file) as f:
      possible_responses = [line.rstrip() for line in f]
  result = random.choice(possible_responses)
  write_history(user.name + ': Cypher -> ' + str(result))

  await ctx.send(result)

@client.command(name='map_skeld', brief="", pass_context=True)
async def map_skeld(ctx):
  await ctx.send(file=discord.File('images/map_skeld.jpg'))


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
  with open('history.txt', 'a') as the_file:
    the_file.write(text +'\n')

if __name__ == "__main__":
  client.loop.create_task(list_servers())
  client.run(cfg.TOKEN)
