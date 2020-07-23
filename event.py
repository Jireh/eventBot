import sys, os
import discord

class newEvent:
    def __init__(self, title, date, time):
        self.title = title
        self.date = date
        self.time = time
        self.users = []