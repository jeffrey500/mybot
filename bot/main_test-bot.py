import random

import sys
import discord
from discord import Colour

client = discord.Client()


# debug
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    game = discord.Game("*help")
    await client.change_presence(status=discord.Status.online, activity=game)


# make sure author is an actual user
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # hello command
    elif message.content.startswith('*hello'):
        await message.channel.send("Hello <@" + str(message.author.id) + "> ! " + ":slight_smile:")
    # help command*
    elif message.content.startswith('*help'):
        embed = discord.Embed(title='Help', description='help for you :slight_smile:', colour=Colour.blue())
        embed.add_field(name="For server admins (more info *info_server_admins)", value="nothing(yet)", inline=False)
        embed.add_field(name="not nice stuff (more info *info_not_nice)", value="`roast` `kill` `insane_detection`",
                        inline=False)
        embed.add_field(name="Miscellaneous (more info *info_miscellaneous)",
                        value="`coinflip` `hello` `credits` `hi bot`(creators only)", inline=False)
        embed.add_field(name="epic gifs (more info *info_gifs)", value="`table_flip` `fish_artillery` `nani`",
                        inline=False)
        embed.add_field(name="made by SunnyJimBob#7082 ever since 07/27/2020", value="_ ", inline=False)

        await message.channel.send(message.channel, embed=embed)

    # more info about not nice stuff
    elif message.content.startswith("*info_not_nice"):
        embed = discord.Embed(title="More info about not nice stuff", description='info for you :slight_smile:',
                              colour=Colour.red())
        embed.add_field(name="roast", value="*roast @user will roast anyone you put after *roast", inline=False)
        embed.add_field(name="kill", value="*kill @user will make anyone you put after *kill die in a funny way",
                        inline=False)
        embed.add_field(name="insane_detection", value="*insane_detection tells you how sane you are")

        await message.channel.send(message.channel, embed=embed)

    # more info about Miscellaneous

    elif message.content.startswith('*info_miscellaneous'):
        embed = discord.Embed(title='More info about miscellaneous', description='help for you :slight_smile:', colour=Colour.gold())
        embed.add_field(name="hello", value="*hello makes the bot say hello back to you", inline=False)
        embed.add_field(name="coinflip", value="*coinflip randomly chooses between heads and tails ",inline=False)
        embed.add_field(name="credits",value="*credits gives you the list of people who worked on this bot", inline=False)
        embed.add_field(name="hi bot",value="only for creators",inline=False)
        await message.channel.send(embed=embed)

    # more info about gifs

    elif message.content.startswith('*info_gifs'):
        embed = discord.Embed(title="more info about gifs", description='info for you :slight_smile:',
                              colour=Colour.green())
        embed.add_field(
            name="*table_flip",
            value="will give you a table flip gif (credit to https://tenor.com/view/table-flip-machine-kaomoji-gif-17427776)",
            inline=False)
        embed.add_field(
            name="*fish_artillery",
            value="will give you a gif of a fish cannon (credit to https://tenor.com/view/fishy-explosion-human-fish-cannon-gif-17822939)",
            inline=False)
        embed.add_field(
            name="*nani",
            value=" will give you a nani gif (credit to https://media.giphy.com/media/1NVugSXiJGJZvWMOud/giphy.gif)",
            inline=False)

        await message.channel.send(message.channel, embed=embed)

        # coinflip
    elif message.content.startswith('*coinflip'):
        ok = random.randint(1, 100)
        if ok > 50:
            text = "heads"
        else:
            text = "tails"
        await message.channel.send(text)
    # credits
    elif message.content.startswith('*credits'):
        embed = discord.Embed(title='Credits', colour=Colour.blue())
        embed.add_field(name="creator", value="SunnyJimBob#7082", inline=False)
        embed.add_field(name="contributor", value="Meow.#6462", inline=False)
        embed.add_field(name="sponsors", value="None(yet)", inline=False)

        await message.channel.send(message.channel, embed=embed)
    # hi bot
    elif message.content.startswith('*hi bot'):
        if str(message.author) == "SunnyJimBob#7082":
            await message.channel.send("hello creator")
        else:
            await message.channel.send("***ew your a normie, not a creator*** :rage: ")


    # gifs

    elif message.content.startswith('*table_flip'):
        await message.channel.send("https://tenor.com/view/table-flip-machine-kaomoji-gif-17427776")
    elif message.content.startswith('*fish_artillery'):
        await message.channel.send("https://tenor.com/view/fishy-explosion-human-fish-cannon-gif-17822939")
    elif message.content.startswith('*nani'):
        await message.channel.send("https://media.giphy.com/media/1NVugSXiJGJZvWMOud/giphy.gif")

    # insane_detection

    elif message.content.startswith('*insane_detection'):
        sane = random.randint(1, 100)
        if sane > 50:
            await message.channel.send("<@"+str(message.author.id) + ">")
            embed = discord.Embed(title='Your insane!', colour=Colour.dark_red())
            embed.add_field(name="you are " + str(sane) + "% insane", value=":zany_face:")
            embed.add_field(name="Should you see a doctor?", value="Um duh your insane!!!", inline=False)
        elif sane < 50:
            message.channel.send("<@"+str(message.author.id)+">")
            embed = discord.Embed(title='Your sane!', colour=Colour.dark_blue())
            embed.add_field(name="you are " + str(sane) + "% insane", value=":slight_smile:")
            embed.add_field(name="Should you see a doctor?", value="No, but you should still get it checked",
                            inline=False)
        await message.channel.send(message.channel, embed=embed)

    # roast
    elif message.content.startswith('*roast'):
        hi = random.randint(1, 7)
        if hi == 1:
            await message.channel.send('Mirrors cant talk, luckly for you, they cant laugh either :rofl:')
        elif hi == 2:
            await message.channel.send('Some day youll go far... and i hope you stay there :rofl:')
        elif hi == 3:
            await message.channel.send('If laughter is the best medicine, your face must be curing the world. :rofl:')
        elif hi == 4:
            await message.channel.send(
                'When i see your face theres not a thing i would change... except the direction i was walking in :rofl:')
        elif hi == 5:
            await message.channel.send('Hey, you have something on your chin... no, the 3rd one down :rofl:')
        elif hi == 6:
            await message.channel.send('you :rofl:')
        elif hi == 7:
            await message.channel.send('Everyone when you fall: OMG is the floor ok?')



client.run(sys.argv[1])
