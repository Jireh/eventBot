import sys, os
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!') # prefix used in chat i.e. !bot

# When the bot is ready
@client.event
async def on_ready():
    print("Bot is ready.")

@client.command()
async def speak(ctx):
    await ctx.send('woof!')

eventList = [] #list of all events currently on the calendar

@client.command(aliases=['makeevent', 'test'])
async def makeEvent(ctx, *, name):
    global eventList
    eventList.append(name)
    await ctx.send(f'making event: {name}')
    await ctx.send(f"Most recent event: {eventList[len(eventList)-1]}")

@client.command()
async def listEvents(ctx):
    for i in range(len(eventList)):
        await ctx.send(eventList[i] + '\n')



botToken = 'TEMP'
client.run(botToken)
#test change
