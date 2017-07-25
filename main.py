import discord
import asyncio
import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
client = discord.Client()

bot_prefix="//"

@client.event
async def on_ready():
    print('Instance running')
    print('instance username:' + client.user.name)
    print('instance userid: ' + client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith(bot_prefix+'wake'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith(bot_prefix+'sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith(bot_prefix+'greet'):
        await client.send_message(message.channel, 'hello!')
        await client.change_presence(game=discord.Game(name='with your mom'))
       
@client.event
async def on_message_edit(before, after):
    if before.author.bot == False:
        await client.send_message(before.channel, 'oi! change that back')
        await client.send_message(before.channel, 'this is what is was before: ' + before.content)

client.run('MzM5Mjc1NDMxNTUzMjY5NzYw.DFjtMw.07IyneSoNDq2knFJ0jpGNv3pAvg')