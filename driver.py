import sys, os
from event import newEvent
import discord
from discord.ext import commands, tasks
from datetime import datetime
import time

client = commands.Bot(command_prefix = '!') # prefix used in chat i.e. !bot

# When the bot is ready
@client.event
async def on_ready():
    print("Bot is ready.")

@client.command()
async def speak(ctx):
    await ctx.send('If you see this I will give you 5 dollars <3')

eventList = [] # List of all events currently on the calendar

# User will input (Command) (Name) - (Date) - (Time)
# Will split into individual parts

@client.command(aliases=['makeevent', 'test'])
async def makeEvent(ctx, *, name):
    global eventList
    
    # Barebones syntax check
    if name.count("/") != 1 or name.count("-") != 2 or name.count(":") != 1:
        await ctx.send("Please input valid event. Format: EventName - Month/Day - Time (00:00)")
    else:
        # Create new Event
        splitLine = name.split("-")

        title = splitLine[0]
        # Clean away spaces and convert to datetime
        dateStrip = splitLine[1].replace(' ', '')
        date = datetime.strptime(dateStrip, '%m/%d/%y').date()
        timeStrip = splitLine[2].replace(' ', '')
        datetime.strptime(timeStrip, '%H:%M').time()

        createEvent = newEvent(title, date, time)
        eventList.append(createEvent)
        await ctx.send(f'making event: {title}')

@client.command()
async def listEvents(ctx):
    for i in range(len(eventList)):
        await ctx.send(eventList[i] + '\n')

@tasks.loop(seconds = 1.0)
async def update():
    global eventList
    for event in eventList:
        print(event.title + " " + event.date + " " + event.time)



update.start()
botToken = 'NzI1ODM5NjU2OTM0OTY1MjQ5.XwYvRg.CKmF6xXICgdrwkDkQwxCfqLknSk'
client.run(botToken)

