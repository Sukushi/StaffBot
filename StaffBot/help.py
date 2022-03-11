from deff import *

@StaffBot.command()
async def help(ctx,args=""):
	love = """
**Love commands**
	`+sendlove` : send love to someone random
	`+loveyou` : send your love to someone random

	`+sendlove [name or nickname or mention]` : send love to person
	`+loveyou [name or nickname or mention]` : send your love to person
	"""

	test = """
**Test commands**
	this is just a test
	"""

	if (args == "love"):
		helpMess = love
	elif (args == "test"):
		helpMess = test
	else:
		helpMess = love # + test
		
	await ctx.send(helpMess)
