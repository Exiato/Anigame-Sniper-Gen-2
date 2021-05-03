import discord
from discord.ext import commands 
import json
from colorama import init, Fore, Back, Style
from datetime import datetime
init(convert=True)
import asyncio
with open("config.json") as f:
    config = json.load(f)
SUPPORT_TOKEN = config.get("SUPPORT_TOKEN")
TOKEN = config.get("TOKEN")
AS = config.get("Anigame Sniper")
IS = config.get("Izzi Sniper")
pre = config.get("PREFIX")
wf = config.get("LATENCY")
print(Style.BRIGHT)

print(Fore.GREEN + """
▄▀█ █▄░█ █ █▀▀ ▄▀█ █▀▄▀█ █▀▀
█▀█ █░▀█ █ █▄█ █▀█ █░▀░█ ██▄

█▀ █▄░█ █ █▀█ █▀▀ █▀█
▄█ █░▀█ █ █▀▀ ██▄ █▀▄

█▀ █░█ █▀█ █▀█ █▀█ █▀█ ▀█▀
▄█ █▄█ █▀▀ █▀▀ █▄█ █▀▄ ░█░ for anigame sniper version 3""")
client = discord.Client()
print()
print(Fore.GREEN + f"Made by Sebastian")
async def get_channel_for_ani():
    with open("ani.json", "r") as f:
        guil = json.load(f) 
    return guil 
async def get_channel_for_izzi():
    with open("izzi.json", "r") as f:
        guil = json.load(f) 
    return guil

@client.event
async def on_ready():
    print(Fore.GREEN + f"logged in as {client.user}")
    if config.get('Anigame Sniper') == "y":
        print(Fore.GREEN + f"Anigame Sniper - ON") 
    else:
        print(Fore.GREEN + f"Anigame Sniper - OFF") 

    if config.get('Izzi Sniper') == "y":
        print(Fore.GREEN + f"Izzi Sniper - ON") 
    else:
        print(Fore.GREEN + f"Izzi Sniper - OFF") 
    
    print(Fore.GREEN + f"{round(client.latency * 1000)} ms")
    print(Fore.GREEN + "Format - guild_id|channel_id|guild_name|channel_name")
    guil = await get_channels() 
    l = len(guil)
    if l == 1:
        print(Fore.GREEN + f"sniper is on in {l} channel!")
    else:
        print(Fore.GREEN + f"sniper is on in {l} channels!")
    print(Fore.GREEN + f"Prefix - {pre}")
    print(Fore.GREEN + f"latency - {wf} seconds")
    un = open("username.txt","r")
    x = un.read()
    print(f"-------------->Sniping for {x}<--------------")
    un.close() 

async def get_channels():
    with open("channels.json", "r") as f:
        guil = json.load(f) 
    return guil 
 
@client.event
async def on_message(msg):
    with open("config.json", "r") as j:
        y = json.load(j)
        pre = y.get("PREFIX")
    a = y.get("Anigame Sniper")
    b = y.get("Izzi Sniper")
    if a == "y":
        if msg.author.id == 571027211407196161:
            un = open("username.txt","r")
            x = un.read().split("#")[0]
            a = msg.content
            ar = msg.author.id 
            now = datetime.now() 
            current_time = now.strftime("%H:%M:%S")
            if a.endswith(f"has been added to **{x}'s** collection!") and ar == 571027211407196161:
                card = []
                sec = list(a.split("has"))[0]
                for i in sec:
                    if i == "_" or i == "*":
                        pass
                    else:
                        card.append(i)
                card = "".join(str(elem) for elem in card)
                print(Fore.GREEN + f"Anigame --> {card}| {current_time}")

            g = msg.guild.name
            gi = msg.guild.id
            chan = msg.channel.name
            id_ = msg.channel.id
            guil = await get_channels() 
            _ani_ = await get_channel_for_ani()
            x = f"{gi}|{id_}" 
            if x in guil:
                try:
                    for embed in msg.embeds:
                            d = (embed.to_dict()['description'])
                            if d == "*A wild anime card appears!*": 
                                a = (embed.to_dict()['footer'])
                                text = (a['text'])
                            
                            else:
                                try:
                                    _ani_.pop(f"{id_}" , None)
                                    with open("ani.json" , "w") as f:
                                        json.dump(_ani_ , f)
                                except:
                                    pass
                                return

                    r = text.split()
                    li = [r[1] , r[2]]
                    kek = ' '.join([str(elem) for elem in li])
                    _ani_[f"{id_}"] = f"{kek}"
                    with open("ani.json", "w") as f:
                        json.dump(_ani_, f)

                except:
                    try:
                        _ani_.pop(f"{id_}" , None)
                        with open("ani.json" , "w") as f:
                            json.dump(_ani_ , f)
                    except:
                        pass 
                    return
    
    if b == "y":
        if msg.author.id == 784851074472345633:
            un = open("username.txt","r")
            x = un.read().split("#")[0]
            un.close() 
            a = msg.content
            ar = msg.author.id 
            now = datetime.now() 
            current_time = now.strftime("%H:%M:%S")
            if a.endswith(f"has been added to **{x}'s** collection.") and ar == 784851074472345633:
                card = []
                sec = list(a.split("has"))[0]
                for i in sec:
                    if i == "_" or i == "*":
                        pass
                    else:
                        card.append(i)
                card = "".join(str(elem) for elem in card)
                print(Fore.GREEN + f"Izzi --> {card}| {current_time}")
                
            g = msg.guild.name
            gi = msg.guild.id
            chan = msg.channel.name
            id_ = msg.channel.id
            guil = await get_channels() 
            _izzi_ = await get_channel_for_izzi()
            x = f"{gi}|{id_}" 
            if x in guil:
                try:
                    for embed in msg.embeds:
                        d = (embed.to_dict()['description'])
                        if d.endswith("appeared._"):
                            a = (embed.to_dict()['footer'])
                            text = (a['text'])
                        
                        else:
                            try:
                                _izzi_.pop(f"{id_}" , None)
                                with open("izzi.json" , "w") as f:
                                    json.dump(_izzi_ , f)
                            except:
                                pass 
                            return
                        r = text.split()
                        li = [r[1] , r[2] , r[5]]
                        kek = ' '.join([str(elem) for elem in li])
                        _izzi_[f"{id_}"] = f"{kek}"
                        with open("izzi.json", "w") as f:
                            json.dump(_izzi_, f)

                except:
                    try:
                        _izzi_.pop(f"{id_}" , None)
                        with open("izzi.json" , "w") as f:
                            json.dump(_izzi_ , f)
                    except:
                        pass 
                    return

print(Fore.RESET)       
client.run(SUPPORT_TOKEN) 
