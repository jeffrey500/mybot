import random

import discord
from discord import Colour

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    game = discord.Game("*help")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('*hello'):
        await message.channel.send("Hello " + str(message.author) + " ! " + ":slight_smile:")
    elif message.content.startswith('*help'):
        embed = discord.Embed(title='Help', description='help for you :slight_smile:', colour=Colour.blue())
        embed.add_field(name="For sever admins", value="nothing(yet)", inline=False)
        embed.add_field(name="Miscellaneous", value="coinflip, hello, credits, hi bot(creators only)", inline=False)

        await message.channel.send(message.channel, embed=embed)
    elif message.content.startswith('*coinflip'):
        ok = random.randint(1, 2)
        if ok == 1:
            text = "head"
        else:
            text = "tail"
        await message.channel.send(text)
    elif message.content.startswith('*credits'):
        embed = discord.Embed(title='Credits', colour=Colour.blue())
        embed.add_field(name="creator", value="SunnyJimBob#7082", inline=False)
        embed.add_field(name="contributor", value="None(yet)", inline=False)
        embed.add_field(name="sponsors", value="None(yet)", inline=False)
        await message.channel.send(message.channel, embed=embed)

    if message.content.startswith('*hi bot'):
        if str(message.author) == "SunnyJimBob#7082":
            await message.channel.send("hello creator")






client.run('Njc1MTg5NDkyNzc2MzA0NjYx.XjzhNw.c_KAZkWF0t8E1OyBzbq2SfynI7Y')