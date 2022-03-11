from private import *
from deff import *

@StaffBot.event
async def on_voice_state_update(member, before, after):
	if (after.channel == None):
		if((datetime.datetime.now().hour>=21) | (datetime.datetime.now().hour<=6)):
			nomicro = member.guild.get_channel(idServer)
			if (member.nick == None):
				await nomicro.send("Bonne nuit "+member.name+" !")
			else:
				await nomicro.send("Bonne nuit "+member.nick+" !")
