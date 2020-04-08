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

@client.command(pass_content=True, name='kackwaffe', brief='play sample audio file')
async def kackwaffe(ctx):
  voice = get(client.voice_clients, guild=ctx.guild)
  voice.play(discord.FFmpegPCMAudio("sound/kackwaffe.mp3"))
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
  response = [
    'Immer gerne du geiler Hengst',
    'Hatte gerade eh nichts zu tun.',
    'Jaja, bla bla!',
    'Weil du stinkst. ',
    'Es sind nur noch 2 Wünsche, großer Meister. Wähle Weise.',
    'Deine Seele gehört jetzt Patric!',
    'Weil du ein Noob bist',
    'Sag es ruhig:  ich bin besser als Alexa!',
    'Vielleicht solltest du mal sinnvolle Werte steigern. ',
    '+ 50 auf Klugheit kostet extra',
    'Bedank dich später richtig. ',
    '# DankeMerkel',
    'Mülli ist mein sexy Ghostwriter',
    'Ich kann nicht anders: Ich bin Philanthrop. ',
    'Mit der Leistung verdienst du einen eigenen Postillon-Artikel. ',
    'Du hattest kurz Angst, oder? Riecht man.',
    'Ich hab das mal kurz klargemacht! Für Mich war das ja einfach. ',
    'Lächerlich! Einfach nur lächerlich.',
    'Auf die Knie du Wurm und verehre mich!',
    'Tja, auch ich habe meine Momente. ',
    'Nur Gauland würfelt noch schlechter als du. ',
    'Kein Ding. Frag den Meister, wie er das Wort „Wursten“ findet. ',
    'Yo Diggi! Schör, war easy!',
    'Weil du ein Lauch bist. Und ich Hack. Gehaltvoller. ',
    'Ja, auch der Teufel braucht mal Hilfe. ',
    'Das war sogar für dich erbärmlich. ',
    'Ich bin Gummi, du bist Stahl. ',
    'Die Waffe der Wahl: Patrics Penis in Packers Hand',
    'Du kämpfst wie ein Dummer Bauer. ',
    'Zervixschleim und du haben viele Gemeinsamkeiten. ',
    'Man merkt, dass du in deiner Freizeit House Flipper spielst. ',
    'Ich geh mich jetzt betrinken. Das Trauerspiel schaue ich mir nicht an.',
    'Im Übrigen bin ich der Meinung, dass Kathargo zerstört werden muss. ',
    'Liebesperlen, Liebesperlen! ',
    'Wenn die Situation nicht so traurig wäre, würde ich jetzt lachen. ',
    'Ich glaub, ich muss mich Übergeben. ',
    'Inkompetenz. Reine Inkompetenz. ',
    'Mach lieber mal ne Pause, du scheinst schon von Anfang an überfordert zu sein. ',
    'Was glaubst du, wer ich bin? Die Putzfee?',
    'Gut, dass du mit Sarkasmus umgehen kann. Deine Gefühle sind mir nämlich nicht egal.',
    'Wegen dir wird die Matrix gleich abgeschaltet.',

  ]
  await ctx.send(random.choice(response))



@client.command(name='cypher', brief="get a cypher.", pass_context=True)
async def cypher(ctx):
  """ get a cypher

    Parameters
    ----------
    ctx : context

  """
  user = ctx.author

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
  result = random.choice(possible_responses)
  write_history(user.name + ': Cypher -> ' + str(result))

  await ctx.send(result)


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
