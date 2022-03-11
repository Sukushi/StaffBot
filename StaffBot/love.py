from deff import *

@StaffBot.command()
async def sendlove(ctx,args=""):
	await ctx.message.delete()
	if args == "":
		member = await findmemberrandom(ctx)
	else:
		member = await findmember(ctx,args)
	if (member != None):
		await ctx.send("Someone send you love "+member.mention)	

@StaffBot.command()
async def loveyou(ctx,args=""):
	await ctx.message.delete()
	if args == "":
		member = await findmemberrandom(ctx)
	else:
		member = await findmember(ctx,args)
	if (member != None):
		author = await findauthor(ctx)
		await ctx.send(author+" send you love "+member.mention)	

async def findmember(ctx,args=""):
	if re.search("<@.*>",args):
		idMember = re.sub("<@|>","",args)
		member = ctx.guild.get_member(int(idMember))
	else:
		member = ctx.guild.get_member_named(args)
	return member

async def findmemberrandom(ctx):
	members = ctx.channel.members
	membersCount = len(members)
	memberNum = random.randint(0,membersCount-1)
	member = members[memberNum]
	return member

async def findauthor(ctx):
	author = ctx.author.nick
	if (author == None):
		author = ctx.author.name
	return author
