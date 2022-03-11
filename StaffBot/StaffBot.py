from private import *
from deff import *

from help import *
from dm import *
from koa import *
from bye import *
from love import *

@StaffBot.event
async def on_ready():
	await StaffBot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing,name="+help"))

StaffBot.run(key)