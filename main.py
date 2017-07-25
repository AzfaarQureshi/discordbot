import discord
import asyncio
import logging
from discord.ext import commands

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#client = discord.Client()

description = '''Music and Memes, though it has a bunch of other random functions too'''

bot = commands.Bot(command_prefix='//', description=description)

@bot.event
async def on_ready():
    print('Instance running')
    print('instance username:' + bot.user.name)
    print('instance userid: ' + bot.user.id)
    print('------')

@bot.command()
async def wake(message):
    if message.content.startswith('wake'):
        counter = 0
        tmp = await bot.send_message(message.channel, 'Calculating messages...')
        async for log in bot.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await bot.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith(bot_prefix+'sleep'):
        await asyncio.sleep(5)
        await bot.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith(bot_prefix+'greet'):
        await bot.send_message(message.channel, 'hello!')
        await bot.change_presence(game=discord.Game(name='with your mom'))
       
@bot.event
async def on_message_edit(before, after):
    if before.author.bot == False:
        await bot.send_message(before.channel, 'oi! change that back')
        await bot.send_message(before.channel, 'this is what is was before: ' + before.content)

bot.run('MzM5Mjc1NDMxNTUzMjY5NzYw.DFjtMw.07IyneSoNDq2knFJ0jpGNv3pAvg')