import asyncio
import logging
import random

from discord import Game
from discord.ext.commands import Bot

# own
import config as cfg

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

BOT_PREFIX = ("?", "!")

client = Bot(command_prefix=BOT_PREFIX)


@client.command(name='d6', brief="rolls a 6-sided dice")
async def d6(ctx):
  """ role a 6-sided dice

  Parameters
  ----------
  ctx
  """
  await ctx.send(random.randrange(1, 6))


@client.command(name='d10', brief="rolls a 10-sided dice")
async def d10(ctx):
  """ role a 10-sided dice

  Parameters
  ----------
  ctx
  """
  await ctx.send(random.randrange(1, 10))


@client.command(name='d20', brief="rolls a 20-sided dice")
async def d20(ctx):
  """ role a 20-sided dice

  Parameters
  ----------
  ctx
  """
  await ctx.send(random.randrange(1, 20))


@client.command(name='d100', brief="rolls a 100-sided dice")
async def d100(ctx):
  """ role a 100-sided dice

  Parameters
  ----------
  ctx
  """
  await ctx.send(random.randrange(1, 100))


@client.command(name='strange', brief="!strange <number>")
async def strange(ctx, number):
  """ special command for the pen and paper game Strange. Roll a D20 and check against a specific difficulty.

    Parameters
    ----------
    ctx

    number : integer
      difficult of the roll
  """

  user = ctx.author
  dice = random.randrange(1, 20)
  print(dice)
  print("strange: " + str(int(number) * 3))
  if dice >= int(number) * 3:
    await ctx.send('good job ' + user.name + ' (' + str(dice) + ')')
  else:
    if dice == 1:
      logger.info('strange' + user.name + ' (' + str(dice))
      await ctx.send('Ohoh :hot_face: ' + user.name + ' (' + str(dice) + '). Setzt lieber ein XP du Noob')
    else:
      logger.info('strange' + user.name + ' (' + str(dice))
      await ctx.send('Ohoh ' + user.name + ' (' + str(dice) + ')')


@client.command(name='chuck', brief="chuck norris jokes.", pass_context=True)
async def chuck(ctx):
  """ Print a chuck norris joke

    Parameters
    ----------
    ctx
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


client.loop.create_task(list_servers())
client.run(cfg.TOKEN)
