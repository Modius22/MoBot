import asyncio
import logging
import random

import discord
from discord import Game
from discord.ext.commands import Bot
from discord.utils import get
from discord.ext import commands
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
  voice.play(discord.FFmpegPCMAudio("sound/test.mp3"))
  voice.source = discord.PCMVolumeTransformer(voice.source)
  voice.source.volume = 0.07

@client.command(name='d6', brief="rolls a 6-sided dice")
async def d6(ctx):
  """ role a 6-sided dice

  Parameters
  ----------
  ctx : context
  """
  await ctx.send(random.randrange(1, 6))


@client.command(name='d10', brief="rolls a 10-sided dice")
async def d10(ctx):
  """ role a 10-sided dice

  Parameters
  ----------
  ctx : context
  """
  await ctx.send(random.randrange(1, 10))


@client.command(name='d20', brief="rolls a 20-sided dice")
async def d20(ctx):
  """ role a 20-sided dice

  Parameters
  ----------
    ctx : context

  """
  await ctx.send(random.randrange(1, 20))


@client.command(name='d100', brief="rolls a 100-sided dice")
async def d100(ctx):
  """ role a 100-sided dice

  Parameters
  ----------
  ctx : context

  """
  await ctx.send(random.randrange(1, 100))


@client.command(name='strange', brief="!strange <number>")
async def strange(ctx, number):
  """ special command for the pen and paper game Strange. Roll a D20 and check against a specific difficulty.

    Parameters
    ----------
    ctx : context

    number : integer
      difficult of the roll
  """

  user = ctx.author
  dice = random.randrange(1, 20)
  print(dice)
  print("strange: " + str(int(number) * 3))
  if dice >= int(number) * 3:
    write_history('good job ' + user.name + '. dice = ' + str(dice) + ', strange = ' + str(number))
    await ctx.send('good job ' + user.name + ' (' + str(dice) + ')')
  else:
    if dice == 1:
      write_history('Ohoh :hot_face: ' + user.name + '. dice = ' + str(dice) + ', strange = ' + str(number))
      await ctx.send('Ohoh :hot_face: ' + user.name + ' (' + str(dice) + '). Setzt lieber ein XP du Noob')
    else:
      write_history('Ohoh ' + user.name + '. dice = ' + str(dice) + ', strange = ' + str(number))
      await ctx.send('Ohoh ' + user.name + ' (' + str(dice) + ')')



@client.command(name='chuck', brief="chuck norris jokes.", pass_context=True)
async def chuck(ctx):
  """ Print a chuck norris joke

    Parameters
    ----------
    ctx : context

  """
  possible_responses = [
    'Wenn Chuck Norris von einem Zombie gebissen wird, dann verwandelt sich der Zombie in Chuck Norris.',
    'Chuck Norris streichelt keine Tiere, die Tiere streicheln sich selbst, wenn er in der Nähe ist.',
    'Chuck Norris schmeißt eine Party mit tollen Gästen, 100 Meter weit.',
    'Chuck Norris hatte in seinem Leben nur einmal Todesangst. Als er sich das erste Mal im Spiegel gesehen hat.',
    'Chuck Norris kann einen Hut aus einem Hasen zaubern.',
    'Chuck Norris wurde gestern geblitzt, beim Einparken.',
    'Wenn Chuck Norris ein Ei essen möchte, pellt er das Huhn.',
    'Chuck Norris hat bis zur Unendlichkeit gezählt. Drei mal.',
    'Chuck Norris kann rote Filzstifte nach Farbe sortieren.',
    'Wie viele Liegestütze schafft Chuck Norris? Alle.',
    'Einige Leute tragen Superman Schlafanzüge. Superman trägt Chuck Norris Schlafanzüge.',
    'Chuck Norris ist so schnell, dass die Navigationsgerät immer in der Vergangenheit mit ihm sprechen muss.',
    'Chuck Norris kann ein Feuer entfachen, indem er zwei Eiswürfel aneinander reibt.',
    'Chuck Norris klebt Tische unter Kaugummis.',
    'Chuck Norris kann eine Drehtür zuschlagen.',
    'Chuck Norris kennt die letzte Ziffer der Zahl Pi.',
    'Chuck Norris kann sogar ein Happy Meal zum Weinen bringen.',
    'Wenn Chuck Norris einschlafen möchte, zählen die Schafe Chuck Norris.',
    'Seit Chuck Norris schwimmen kann, ist Arielle nur noch eine Meerfrau.',
    'Chuck Norris isst keinen Honig, er kaut Bienen.',
    'Chuck Norris hat sich einen Virus eingefangen, doch er wird nicht krank, er lässt ihn nur bei sich wohnen.',
    'Chuck Norris verhandelt nicht mit Terroristen. Er kassiert Schutzgeld.',
    'Für Chuck Norris sind Chuck Norris Witze nur harmlose Fakten.',
    'Chuck Norris trinkt seinen Kaffee am liebsten schwarz. Ohne Wasser.',
    'Chuck Norris schläft nicht mit einer Waffe unter dem Kissen, Chuck Norris schläft mit einem Kissen unter einer Waffe.',
    'Chuck Norris kann eine Bank ausrauben und zwar per Telefonbanking.',
    'Chuck Norris malt ein 5-Eck mit vier Strichen.',
    'Chuck Norris lacht auch zuerst am Besten.',
    'Chuck Norris fährt in England auf der rechten Seite.',
    'Chuck Norris hat keine Angst vor der Dunkelheit, die Dunkelheit hat Angst vor Chuck Norris',

  ]
  await ctx.send(random.choice(possible_responses))



@client.command(name='cypher', brief="get a cypher.", pass_context=True)
async def cypher(ctx):
  """ get a cypher

    Parameters
    ----------
    ctx : context

  """
  possible_responses = ['Abeyance trap',
    'Age taker',
    'Analeptic',
    'Antidote',
    'Armor reinforcer',
    'Attractor',
    'Blackout',
    'Condition remover',
    'Contextualizer',
    'Contingent activator',
    'Curative',
    'Curse bringer',
    'Darksight',
    'Death module',
    'Disguise module',
    'Draining capacitor',
    'Effect resistance',
    'Effort enhancer',
    'Effort enhancer (combat)',
    'Enduring shield',
    'Equipment cache',
    'Flashburst',
    'Focus hook',
    'Force armor projector',
    'Force screen projector',
    'Gas ammunition',
    'Glue',
    'Grenade',
    'Grenade (creature)',
    'Grenade (gravity inversion)',
    'Grenade (recursion)',
    'Grenade (recursion collapsing)',
    'Information lenses',
    'Insight',
    'Intellect booster',
    'Intelligence enhancement',
    'Knowledge enhancement',
    'Lift',
    'Magnetic master',
    'Manipulation beam',
    'Mapper',
    'Matter translation ray',
    '48 Meditation aid',
    'Melt all',
    'Memory switch',
    'Mental scrambler',
    'Mind meld',
    'Mind-restricting wall',
    'Mind stabilizer',
    'Monoblade',
    'Monohorn',
    'Multiphasic module',
    'Null field',
    'Nullification ray',
    'Nutrition and hydration',
    'Phase changer',
    'Phase wall',
    'Radiation spike',
    'Ray emitter',
    'Ray emitter (command)',
    'Ray emitter (friend slaying)',
    'Ray emitter (fear)',
    'Ray emitter (mind-disrupting)',
    'Recursion anchor',
    'Recursion code',
    'Reflex enhancer',
    'Remembering',
    'Repeating module',
    'Sheltering recursion',
    'Slave maker',
    'Sleep inducer',
    'Sniper module',
    'Speed boost',
    'Spying grenade',
    'Stasis keeper',
    'Stim',
    'Strange ammunition',
    'Strange apotheosis',
    'Strength boost',
    'Strength enhancer',
    'Surveillance set',
    'Telepathic bond',
    'Temporary shield',
    'Tissue regeneration',
    'Tracker',
    'Translation remedy',
    'Transvolution',
    'Trick embedder',
    'Uninterruptible power source',
    'Vanisher',
    'Visual displacement device',
    'Vocal translator',
    'Water adapter',
    'Wings',

  ]
  await ctx.send(random.choice(possible_responses))


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


client.loop.create_task(list_servers())
client.run(cfg.TOKEN)
