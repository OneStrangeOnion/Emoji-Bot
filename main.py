import discord
import re

client = discord.Client()
debug = True

# TODO: run emojiPicker as Cog
    # https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html
    #TODO: run $setup command on bot startup

# TODO: turn print debugging into logging

# TODO: Create all server roles


keyFile = open('key.txt', 'r')
key = keyFile.readline()
client.run(key)
keyFile.close()
