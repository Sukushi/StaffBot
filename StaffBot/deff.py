#discord imports
import discord
from discord.ext import commands
#global imports
import random, os, re, pathlib, datetime

client = discord.Client()

intents = discord.Intents.default()
intents.members = True

StaffBot = commands.Bot(command_prefix='+',intents=intents)
StaffBot.remove_command('help')
