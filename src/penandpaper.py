import random

import discord
from discord.ext import commands
from discord.utils import get

import config as cfg


def write_history(text):
    with open("history.txt", "a") as the_file:
        the_file.write(text + "\n")


class Pen_And_Paper(commands.Cog, name="Pen and Paper"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="strange", brief="!strange <difficulty>")
    async def strange(self, ctx, number, option=0):
        """special command for the pen and paper game Strange. Roll a D20 and check against a specific difficulty.

        Parameters
        ----------
        ctx : context

        number : integer
        difficult of the roll
        """
        user = ctx.author
        dice = random.randint(1, 20)
        raw = dice
        if option != 0:
            dice = dice + option

        print("option: {}, raw: {}, dice: {}".format(option, raw, dice))
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if dice >= int(number) * 3:
            if dice == 20:
                write_history("good job " + user.name + ". dice = " + str(dice) + ", strange = " + str(number))
                if voice and voice.is_connected():
                    voice.play(discord.FFmpegPCMAudio(cfg.PATH + "sound/20.mp3"))
                    voice.source = discord.PCMVolumeTransformer(voice.source)
                    voice.source.volume = 0.4
                    await ctx.send("good job " + user.name + " (" + str(dice) + ")")
            else:
                write_history("good job " + user.name + ". dice = " + str(dice) + ", strange = " + str(number))
                await ctx.send("good job " + user.name + " (" + str(dice) + ")")
        else:
            if dice == 1:
                write_history("Ohoh :hot_face: " + user.name + ". dice = " + str(dice) + ", strange = " + str(number))
                if voice and voice.is_connected():
                    voice.play(discord.FFmpegPCMAudio(cfg.PATH + "sound/1.mp3"))
                    voice.source = discord.PCMVolumeTransformer(voice.source)
                    voice.source.volume = 0.4
                    await ctx.send("Ohoh :hot_face: " + user.name + " (" + str(dice) + "). Setzt lieber ein XP du Noob")
            else:
                write_history("Ohoh " + user.name + ". dice = " + str(dice) + ", strange = " + str(number))
                await ctx.send("Ohoh " + user.name + " (" + str(dice) + ")")

    @commands.command(name="cypher", brief="get a cypher.", pass_context=True)
    async def cypher(self, ctx):
        """get a cypher

        Parameters
        ----------
        ctx : context

        """
        user = ctx.author
        cypher_file = cfg.PATH + "files/cypher.txt"
        with open(cypher_file) as f:
            possible_responses = [line.rstrip() for line in f]
        result = random.choice(possible_responses)
        write_history(user.name + ": Cypher -> " + str(result))

        await ctx.send(result)

    @commands.command(name="d6", brief="rolls a 6-sided dice")
    async def d6(self, ctx):
        """role a 6-sided dice

        Parameters
        ----------
        ctx : context
        """
        await ctx.send(random.randint(1, 6))

    @commands.command(name="d8", brief="rolls a 8-sided dice")
    async def d8(self, ctx):
        """role a 8-sided dice

        Parameters
        ----------
        ctx : context
        """
        await ctx.send(random.randint(1, 8))

    @commands.command(name="d10", brief="rolls a 10-sided dice")
    async def d10(self, ctx):
        """role a 10-sided dice

        Parameters
        ----------
        ctx : context
        """
        await ctx.send(random.randint(1, 10))

    @commands.command(name="d20", brief="rolls a 20-sided dice")
    async def d20(self, ctx):
        """role a 20-sided dice

        Parameters
        ----------
            ctx : context

        """
        await ctx.send(random.randint(1, 20))

    @commands.command(name="d100", brief="rolls a 100-sided dice")
    async def d100(self, ctx):
        """role a 100-sided dice

        Parameters
        ----------
        ctx : context

        """
        await ctx.send(random.randint(1, 100))

    @commands.command(name="character", brief="Information aboud Characters")
    async def character(self, ctx):
        datei = open(cfg.PATH + "files/character.txt", "r")
        await ctx.send(datei.read())
