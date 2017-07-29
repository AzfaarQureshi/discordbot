import discord
import asyncio
from discord.ext import commands
import logging
import simplejson as json
import requests


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

description = '''Music and Memes, though it has a bunch of other random functions too'''

bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Instance running')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

@bot.group()
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')


@bot.command()
async def memes(ctx):
    r = requests.get("https://api.imgflip.com/get_memes")
    jobj = r.json()
    memes = jobj['data']['memes']
    length = len(memes)
    memename = ""
    memename2 = ""
    counter = 0
    switch = False
    for x in range (0, 50):
        if switch == False:
            memename = memename + str(x) + ". " + memes[x]['name'] + " || "
            switch = True
        elif switch == True:
            memename = memename + str(x) + ". " + memes[x]['name'] + " \n"
            switch = False
    for x in range (50, 100):
        if switch == False:
            memename2 = memename2 + str(x) + ". " + memes[x]['name'] + " || "
            switch = True
        elif switch == True:
            memename2 = memename2 + str(x) + ". " + memes[x]['name'] + " \n"
            switch = False
    await ctx.send('_**LIST OF AVAILABLE MEMES**_')
    await ctx.send (memename)
    await ctx.send (memename2 + '\n BROUGHT TO YOU BY POPULAR DEMAND \n 100. Mocking spongebob')
    await ctx.send('to create a meme use "?meme" followed by meme number and "toptext" "bottomtext"')
    
@bot.command()
async def meme(ctx, reqid : int, toptext : str, botext : str):
    r = requests.get("https://api.imgflip.com/get_memes")
    jobj = r.json()
    memes = jobj['data']['memes']
    if reqid == 100:
        id = 102156234
    else:
        id = memes[reqid]['id']
    v = requests.post('https://api.imgflip.com/caption_image', data = {'template_id':id, 'username' : 'devaccount', 'password':'azfaar123', 'text0' : toptext, 'text1': botext})
    response = v.json()
    print (response)
    await ctx.send(response['data']['url'])

    
bot.run('MzM5Mjc1NDMxNTUzMjY5NzYw.DFjtMw.07IyneSoNDq2knFJ0jpGNv3pAvg')
