from private import *
from deff import *

suppr = ("?"," ","!",",",".",";","/",":","$","%","*","|","(",")","\"","^")

@StaffBot.event
async def on_message(ctx):
	if ctx.author.id != idStaffBot:
		# update sentence
		msg = ctx.content.lower()
		msg = re.sub("<:.*:.*>","",msg)
		msg = re.sub("x[)]+","",msg)
		msg = re.sub("xd+","",msg)
		
		while (msg.endswith(suppr)) :
			msg = msg[:-1]
		
		# don't casse mes couilles
		if ctx.author.id != idMe:
			await react(ctx,msg)			

	await StaffBot.process_commands(ctx)

async def react(ctx,msg):
	koa = ("quoi","kwa","quwa","koua","kua","koa","quoa","coi")
	uno = ("hein")
	ouai = ("ouais")
	ui = ("oui")
	meh = ("mais")
	nope = ("non","nom")

	rep = ("deux","feur","stern","stiti","zon","bril")
	msgRet = ""
	nik = False
	if (msg.endswith(rep)) :
		for sup in rep:
			new = ""
			msg = new.join(msg.rsplit(sup,1))
		while (msg.endswith(suppr)):
			msg = msg[:-1]
		cheh = True

	if (msg.endswith(koa)) :
		msgRet = "feur"
	if (msg.endswith(uno)):
		msgRet = "deux"
	if (msg.endswith(ouai)):
		msgRet = "stern"
	if (msg.endswith(ui)) :
		msgRet = "stiti"
	if (msg.endswith(meh)) :
		msgRet = "zon"
	if (msg.endswith(nope)) :
		msgRet = "bril"

	if cheh == True and msgRet != "":
		msgRet += " (cheh)"
	if (msgRet != "") :
		await ctx.channel.send(msgRet)
