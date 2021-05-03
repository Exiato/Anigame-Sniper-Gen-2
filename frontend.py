import discord
import json
from colorama import init, Fore, Back, Style
init(convert=True)
import asyncio
from os import system
with open("config.json") as f:
    config = json.load(f)
TOKEN = config.get("TOKEN")
AS = config.get("Anigame Sniper")
IS = config.get("Izzi Sniper")
pre = config.get("PREFIX")
wf = config.get("LATENCY")
print(Style.BRIGHT)
print(Fore.CYAN + """
▄▀█ █▄░█ █ █▀▀ ▄▀█ █▀▄▀█ █▀▀   █▀ █▄░█ █ █▀█ █▀▀ █▀█
█▀█ █░▀█ █ █▄█ █▀█ █░▀░█ ██▄   ▄█ █░▀█ █ █▀▀ ██▄ █▀▄ ver.3.0""")
client = discord.Client()
print()
print(Fore.MAGENTA + f"Made by Sebastian")
@client.event
async def on_ready():
    print(Fore.CYAN + f"logged in as {client.user}")
    if config.get('Anigame Sniper') == "y":
        print(Fore.CYAN + f"Anigame Sniper - ON") 
    else:
        print(Fore.RED + f"Anigame Sniper - OFF") 

    if config.get('Izzi Sniper') == "y":
        print(Fore.CYAN + f"Izzi Sniper - ON") 
    else:
        print(Fore.RED + f"Izzi Sniper - OFF") 
    
    print(Fore.YELLOW + f"{round(client.latency * 1000)} ms")
    print(Fore.YELLOW + "Format - guild_id|channel_id|guild_name|channel_name")
    guil = await get_channels() 
    l = len(guil)
    if l == 1:
        print(Fore.YELLOW + f"sniper is on in {l} channel!")
    else:
        print(Fore.YELLOW + f"sniper is on in {l} channels!")
    print(Fore.YELLOW + f"Prefix - {pre}")
    print(Fore.YELLOW + f"latency - {wf} seconds")
    un = open("username.txt" , "w")
    un.write(str(client.user))
    un.close()
    system("title "+"Anigame Sniper")

async def get_channels():
    with open("channels.json", "r") as f:
        guil = json.load(f) 
    return guil 
async def get_channel_for_ani():
    with open("ani.json", "r") as f:
        guil = json.load(f) 
    return guil 
async def get_channel_for_izzi():
    with open("izzi.json", "r") as f:
        guil = json.load(f) 
    return guil 

@client.event
async def on_message(msg):
    if msg.content == f"{pre}add":
        if client.user != msg.author:
            return
        await msg.delete()
        g = msg.guild.name
        gi = msg.guild.id
        chan = msg.channel.name
        id_ = msg.channel.id
        guil = await get_channels()
        if f"{gi}|{id_}" in guil:
            print(Fore.RED + f"{gi}|{id_}|{g}|{chan} is already being snipped!")
            return
        
        else:
            guil[f"{gi}|{id_}"] = f"{g}|{chan}"
            with open("channels.json", "w") as f:
                json.dump(guil, f)
        print(Fore.CYAN + f"Turned ON sniper in {gi}|{id_}|{g}|{chan}")

    if msg.content == f"{pre}remove":
        if client.user != msg.author:
            return
        await msg.delete()
        g = msg.guild.name
        gi = msg.guild.id
        chan = msg.channel.name
        id_ = msg.channel.id

        guil = await get_channels()
        if f"{gi}|{id_}" not in guil:
            print(Fore.RED + f"{gi}|{id_}|{g}|{chan} is not being snipped!")
            return

        guil.pop(f"{gi}|{id_}" , None)
        with open("channels.json" , "w") as f:
            json.dump(guil , f)

        print(Fore.RED + f"Turned OFF sniper in {gi}|{id_}|{g}|{chan}")

    if msg.content == f"{pre}channels":
        if client.user != msg.author:
            return
        await msg.delete()
        guil = await get_channels() 
        l = len(guil) 
        if l == 1:
            print(Fore.YELLOW + f"sniper is ON in {l} channel!")
        else:
            print(Fore.YELLOW + f"sniper is ON in {l} channels!")
        for i in guil:
            x = guil.get(i)
            print(Fore.YELLOW + f"-->{i}|{x}<--")

    if msg.content == f"{pre}ping":
        if client.user != msg.author:
            return
        await msg.delete()
        print(Fore.YELLOW + f"ping - {round(client.latency * 1000)} ms")

    if msg.content == f"{pre}clear":
        if client.user != msg.author:
            return
        await msg.delete()
        guil = await get_channels() 
        guil.clear()

        with open("channels.json" , "w") as f:
            json.dump(guil , f)
        print(Fore.RED + "removed sniping from all the channels")

    if msg.content.startswith(f"{pre}anigametoggle"):
        if client.user != msg.author:
            return
        await msg.delete()
        
        text = msg.content 
        le = len(text)
        split = text.split()
        rm = (split[1:le])
        kek = ' '.join([str(elem) for elem in rm])
        if kek == "y" or kek == "n":
            with open("config.json", "r") as d:
                y = json.load(d) 

            y["Anigame Sniper"] = f"{kek}"
            with open("config.json", "w") as f:
                json.dump(y, f)

            if kek == "n":
                print(Fore.RED + f"Anigame sniper is now OFF")
            else:
                print(Fore.CYAN + f"Anigame sniper is now ON")

        else:
            print(Fore.RED + f"{kek} isnt a valid option | y = ON | n = OFF")

    if msg.content.startswith(f"{pre}latency"):
        if client.user != msg.author:
            return
        await msg.delete()
        with open("config.json", "r") as lol:
            y = json.load(lol) 
        slep = int(y.get("LATENCY"))
        print(Fore.CYAN + f"Latency is {slep} seconds")
        
    if msg.content.startswith(f"{pre}setlatency"):
        if client.user != msg.author:
            return
        await msg.delete()
        text = msg.content 
        le = len(text)
        split = text.split()
        rm = (split[1:le])
        kek = ' '.join([str(elem) for elem in rm])
        try:
            kek = int(kek) 
            with open("config.json", "r") as d:
                y = json.load(d) 

            y["LATENCY"] = f"{kek}"
            with open("config.json", "w") as f:
                json.dump(y, f)

            print(Fore.CYAN + f"Latency is now {kek} seconds")

        except:
            print(Fore.RED + f"{kek} isnt a number!")

    if msg.content.startswith(f"{pre}izzitoggle"):
        if client.user != msg.author:
            return
        await msg.delete()
        text = msg.content 
        le = len(text)
        split = text.split()
        rm = (split[1:le])
        kek = ' '.join([str(elem) for elem in rm])
        if kek == "y" or kek == "n":
            with open("config.json", "r") as d:
                y = json.load(d) 

            y["Izzi Sniper"] = f"{kek}"
            with open("config.json", "w") as f:
                json.dump(y, f)

            if kek == "n":
                print(Fore.RED + f"Izzi sniper is now OFF")
            else:
                print(Fore.CYAN + f"Izzi sniper is now ON")

        else:
            print(Fore.RED + f"{kek} isnt a valid option | y = ON | n = OFF")

    if msg.content.startswith(f"{pre}snipers"):
        if client.user != msg.author:
            return
        await msg.delete()
        with open("config.json", "r") as l:
            y = json.load(l)

        a = y.get("Anigame Sniper")
        b = y.get("Izzi Sniper")

        if a == "y":
            print(Fore.CYAN + "Anigame Sniper - ON")
        else:
            print(Fore.RED + "Anigame Sniper - OFF")

        if b == "y":
            print(Fore.CYAN + "Izzi Sniper - ON")
        else:
            print(Fore.RED + "Izzi Sniper - OFF")

    if msg.author.id == 571027211407196161:
        x = client.user.name 
        a = msg.content
        ar = msg.author.id
        ch_ = msg.channel.id 
        gh_ = msg.guild.id
        _ani_ = await get_channel_for_ani() 
        with open("config.json", "r") as lol:
            y = json.load(lol) 
            slep = int(y.get("LATENCY"))
        await asyncio.sleep(slep+float(0.5))
        with open("ani.json", "r") as lol:
            y = json.load(lol) 
            claim = y.get(f'{ch_}')

        with open("channels.json", "r") as chans:
            chan = json.load(chans)
        if f"{gh_}|{ch_}" in chan:
            try:
                await msg.channel.send(claim) 
                _ani_.pop(f"{ch_}" , None)
                with open("ani.json" , "w") as f:
                    json.dump(_ani_ , f)
            except:
                return 

    if msg.author.id == 784851074472345633:
        x = client.user.name 
        a = msg.content
        ar = msg.author.id 
        ch_ = msg.channel.id 
        gh_ = msg.guild.id
        _izzi_ = await get_channel_for_izzi()
        with open("config.json", "r") as lol:
            y = json.load(lol) 
            slep = int(y.get("LATENCY"))
        await asyncio.sleep(slep+float(0.5))
        with open("izzi.json", "r") as lol:
            y = json.load(lol) 
            claim = y.get(f'{ch_}')

        with open("channels.json", "r") as chans:
            chan = json.load(chans)
        if f"{gh_}|{ch_}" in chan:
            try:
                await msg.channel.send(claim)
                _izzi_.pop(f"{ch_}" , None)
                with open("izzi.json" , "w") as f:
                    json.dump(_izzi_ , f)
            except:
                return 
print(Fore.RESET)       
client.run(TOKEN, bot=False)