#Created by  Md Jisan.  tg @jisan7509

import asyncio
from telethon import events
from userbot.utils import admin_cmd
from platform import uname
from userbot import ALIVE_NAME


F = ("⢀⣠⣾⠀⠀⠀⠀⣠⣤\n"
"⠀⠀⠀⢰\n"
"⣧⣀⣀⣾\n"
"⡏⠉⠛⢿\n"
"⠀⠀⠀⠈⠛⢿⠿⠛⠉⠁⠀\n"
"⣧⡀⠀⠀⠀⠀⠙⠿⠿⠻⠿⠟⠿⠛⠉⠀⠀⠀⠀⠀⣸\n"
"⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴\n"
"⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴\n"
"⡟⠀⠀⢰⣹⡆⠀⠀⠀⠀⠀⠀⣭⠀⠀⠸\n"
"⠃⠀⠀⠈⠉⠀⠀⠀⠤⠀⠀⠉⠁⠀⠀⠀⢿\n"
"⠀⢾⠀⠀⠀⠀⡠⠤⢄⠀⠀⠠⠀\n"
"⡀⠀⠉⠀⠀⠀⠀⠀⢄⠀⢀⠀⠀⠀⠉⠉⠁⠀\n"
"⣧⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⢹\n"
"⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
"⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴\n"
"⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸\n"
"🅼🅰️ 🅺🅸 🅲🅷🆄⢸\n"
"🅿️🅸🅺🅰️ 🅿️🅸🅺🅰️ 🅿️🅸🅺🅰️🅲🅷🆄\n")


G = ("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
"⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⡀⠀⠀⠀⠀⠀⠀\n"
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
"⠀⠀⠀⠀⠀⠀⠀⢿⠟⠀⠀⠀⠀⠀⠀\n"
"⠀⠀⠀⠀⠀⠀⠀⠘⠻⣄⠀⠀⠀⠀⠀\n"
"⠀⠀⠀⠀⣴⡆⠀⠀⠉⠉⠀⠈⡆⠀\n"
"⠀⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⢻⠀\n"
"⠀⠀⠀⠟⠀⠀⠀⠀⠀⠀⠀⣸⡄\n"
"⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠙\n"
"⠀⠀⠘⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⢰⣾⠏\n"
"⠀⢠⣧⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠟⠁⠀\n"
"⠀⢸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ Ah\n shit, here we go again.\n")


H = ("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
"⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀\n"
"⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣦⡀⠀⠀⠀\n"
"⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣆⠀⠀\n"
"⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⠿⢿⣆⠀\n"
"⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⠭⢤⣴⣦⣤⣹⠀\n"
"⠀⠀⢀⣾⣮⣽⣾⣥⣴⢂⠔⢚⢿⣦\n"
"⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣌⢤⣾⡟\n"
"⠀⣾⠇⠀⠀⣤⣄⣀⡀⠈⠻⡇\n"
"⠀⠉⠈⠉⠀⠀⢦⡈⢻⣤⣽⡹⡇\n"
"⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣜⡇\n"
"⠀⠀⠀⠀⠀⠀⠀⠀⢸⣮⣭⣽⠀\n"
"⠀⠀⠀⠀⠀⠀⣀⣀⣈⠇⠀\n"
"⠀⠀⠀⠀⠀⠀⢿⠃⠀⠀\n"
"⠀⠀⠀⠀⠀⠀⠀⠹⠀⠀⠀⠀⠀\n"
"⣠⢼⡄\n"
"⣀⣤⣴⣾⣭⣭⣭⣾⡀\n"
"⣾⣸⣧\n"
"⢿⣯⢻⡄\n"
"⢸⣮⡟⢹⡟⢛⢻⢻⣧\n"
"⡏⡟⡛⢻⠸⣬⢸\n"
"⣧⢿⣧⣥⣾⡟⣴⣝⠿⠿⣫⣾⡆\n"
"⢸⣮⡻⠿⠿⣟⣫⣾⣾⡏⡇\n"
"⢸⡇⢻⣇⡇\n"
"⢸⡇⢿⢸\n"
"⢃⣾⣾⡏⡇\n"
"⠸⢣⢶⣟⣖⣻⣮⣽⣻⣖⣤⣭⡉\n"
"⢹⠣⣛⣣⣭⣁⡛⠻⢽⢻⣽⡧⡄\n"
"⣌⡛⢿⣽⢘⡻⠏⣛⣀\n"
"⣦⠙⡅⠚⣡⣴⡆\n"
"⣰⣱⣾\n"
"⢀⢸\n"
"⣸⠣\n"
"⠿⠛⠑⣮⣝⣛⠿⠿\n"
"⢠⡟\n"
"⢸⠇⢹⡟\n"
"⣸⠏⠸⢟⣣\n"
"ɮǟȶǟʊ ȶɦǟʀӄɨօ ӄʏǟ ɦǟǟʟ ,ӄɛֆǟ ʟǟɢǟ\n")


I = ("\n"
"⠿⠿⠿⠿⠿⠿⢿\n"
"⣧⣤⣤⠀⢠⣤⡄⢸\n"
"   ⠸⠿⠇⢸\n"
"⠿⠷⣤⣀⣤⣾\n"
"⡏⢀⣤⣤⡀⠹\n"
"⡇⠘⠿⠿⠃⢠\n"
"⠦⠤⠤⠴⢿\n"
"⣧⣤⣤⣄⡀   \n"
"⣧⣤\n"
"⣇⣀⣀⣀⡀   \n"
"⠿⠿⠿⠟⠀\n"
"⣧⣤⣤⣤⣴⣾\n"
"⠉⠉⢉⣉⣉⣉⣉⣉⣉⡉⠉\n"
"⠀⠀⠻⠿⠿⠿⠿⠇⠀\n"
"⠀⠀⣤⣤⣤⣤⣾⡇⠀⠀⠀\n"
"⠀⠀⢉⣩⣭⣭⣭⡄⠀⠀⠀\n"
"⠀⠀⡟⠋⠉⠋⠁⠀⠀⠀\n"
"⠀⠀⣾⡆⠀⠀⠀\n"
"⠀⠀⡆⠀\n"
"⠀⠀⣾⣏⠀⠀⣹⡇⠀⠀⠀\n"
"⠀⠀⠘⠿⠿⠿⠟⠃⠀⠀⠀⢹\n"
"\n"
"\n")

n = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
@borg.on(admin_cmd(pattern="sthink (.*)"))
async def kakashi(think):
    name = think.pattern_match.group(1)
    A = (f"**  ➥ {name} .\n\n**"
        "⠀⠀⠀⠀⢀⣀⣀⣀\n"
        "⠀⠀⠀⠰⠿⠛⠛⠻⠿\n"
        "⠀⠀⠀⠀⠀⠀⣀⣄⡀⠀⠀⠀⠀⢀⣀⣀⣤⣄⣀⡀\n"
        "⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠛⠛⡛⠿⠷\n"
        "⠀⠀⠀⠀⠀⠘⠿⠿⠋⠀⠀⠀⠀⠀⠀⠇\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁\n"
        "⠀\n"
        "⠀⠀⠀⠀⣄⠀⢶⣤⣀\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⠗\n"
        "⠀⠀⠀⣰⠀⠀⠀⠀⢀⣀⣠⣤⣴⡄\n"
        "⠀⣠⣾⣥⠿⠿⠛⠃\n"
        "⢰⡄\n"
        "⢸⡁\n"
        "⠈⢿⠁\n"
        "⠀⠀⠛⢿⠟\n")
    await think.edit(n + A)
    
    
n = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"        
@borg.on(admin_cmd(pattern="sdick (.*)"))
async def kakashi(dicksay):
    name = dicksay.pattern_match.group(1)
    B = (f"**  ➥ {name} .\n**"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠖⠲⢄\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠞⠁⠀⠀⠀⠀⢱\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠎⠀⠀⠀⠀⠀⠀⠀⣸\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣄⠀⠀⠀⠀⢀⡠⠖⠁\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠁⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣯⠇⠀⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⣻⣯⠏⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⣠⠾⣽⠏⠀⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⠀⢀⣴⠋⠀⠀⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⣴⣻⠁⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⠀⣠⢾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⣟⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⢸⢿⣯⣻⡟⡆⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠸⣹⡇⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⠹⣟⠁⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⠀⠈⠛⠯⡯⠟⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n")
    await dicksay.edit(n + B)


n = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"        
@borg.on(admin_cmd(pattern="sfrog (.*)"))
async def kakashi(frogsay):
    name = frogsay.pattern_match.group(1)
    C = (f"**  ➥ {name} .\n\n**"
        "⣀⣀⣤⣤⣄⣠⣴⣦⣄\n"
        "⣠⣴⣾⠿⣦\n"
        "⢠⠾⣋⣭⣄⡀⠙⠻⠛⠋⠉⠉⠉⠙⠛⠿\n"
        "⡎⡟⢻⡼⣡⣾⣦⠈⠛⢿\n"
        "⡇⣾⠟⢰⠁⣇⣸⣠\n"
        "⣦⣭⣭⣄⣤⣤⣴⣧⡘⠻⠛⠛⠁⣀⣴\n"
        "⢉⣹⣦\n"
        "⠛⠛⠛⠛⠻⠿⢿\n"
        "⡇⢀⣀⣀⠉⠉⠛⠛⠻⠿\n"
        "⠈⣆⢿⣤⣤⣀⣀⡀⠉⢻\n"
        "⡀⠸⠂⢠\n"
        "⡇⠃⢀\n"
        "⡇⠠⠋⣠⣾\n"
        "⠁⠐⠛⠛⠛⠉⠉⠉⠉⣠⣾\n"
        "⠻⣦⣀⣀⣀⣀⣀⣤⣤⣤⣤⣾⠋\n")
    await frogsay.edit(n + C)
    
    
@borg.on(admin_cmd(pattern="sputin (.*)"))
async def kakashi(putinsay):
    name = putinsay.pattern_match.group(1)
    D = (f"**Vladimir Putin ➥ {name} .\n\n**"
        "⣻\n"
        "⣵⠿⡟⣛⣧⣯⣝⡻⢿\n"
        "⠋⠁⣴⣦⣍⢿\n"
        "⢷⣾⣏⢼\n"
        "⢹⢻⠎⠔⣛⡏\n"
        "⢸⠇⡶⠿⠟⡛⠛⠻⠿⠿⣗⢣\n"
        "⠐⣾⣾⣁⣔⣤⣀⢲\n"
        "⣾⣟⢟⣾\n"
        "⣟⡷⣮⣽⠛⢻⣽⡇⣾\n"
        "⢻⡷⠻⢻⡻⣯⣝⢿⣟⣛⣛⣛⠝⢻\n"
        "⠸⡟⣹⣦⠋⠻⢿⡾⠃⡂⢾\n"
        "⠟⠋⢻⣧⣲⡀⡀⠉⠱⣠⣾⡇⠉⠛⢿\n"
        "⠈⢾⣾⣇⠉⠉\n"
        "⠸⠟⠃⢈⣻\n"
        "⢿⣾⡄⢾⡄\n"
        "⠸⠃⠈⢿\n")
    await putinsay.edit(D)



@borg.on(admin_cmd(pattern="sdead (.*)"))
async def kakashi(deadfrog):
    name = deadfrog.pattern_match.group(1)
    E = (f"**Froggy ➥ {name} .\n\n**"
        "⡇\n"
        "⡇\n"
        "⡇\n"
        "⡇⠋⣉⣉⣉⡙⠻\n"
        "⠃⠹⠟⣡⢟⣛⣛⡻⢿⣦⣩⣤⣬⡉⢻\n"
        "⢀⢤⣾⠿⠿⠿⢮⡃⣛⡻⢿⠈\n"
        "⡟⢡⣴⣯⠤⣤⣭⣮⣔⡈⠛⢓⠦⠈⢻\n"
        "⠏⣠⣯⡪⢛⠿⢿⣮⣄⠙\n"
        "⣾⡭⠴⣽⣽⣛⠿⠿⠇\n"
        "⠿⣝⣛⢛⢋⣥⣴\n"
        "⢿⠱⣛⠾⣭⣛⢿⡀\n"
        "⠑⠽⡻⢿⣮⣽⣯⣽⣳⠮⣽⣟⣲⠯⢭⣛⡇\n"
        "⠈⠑⠊⠉⠟⣻⠿⣾⣭⠷⠂⣴\n"
        "⠁⠙⠒⠙⠯⠍⠙⢉⣡\n"
        "⠙\n")
    await deadfrog.edit(E)
    
  
@borg.on(admin_cmd(pattern="strump (.*)"))
async def kakashi(trumpsay):
    name = trumpsay.pattern_match.group(1)
    J = (f"**Donald Trump ➥ {name} .\n\n**"
        "⠿⠛⠋⠉⡉⣉⡛⣛⠿\n"
        "⠋⠁⢀⣸⠿⡯⢙⠿\n"
        "⡀⡀⢀⣀⣉⣉⣉⠁⠐\n"
        "⡇⠁⣀⠈⠿⢟⡛⠛⠛⠛\n"
        "⡆⠈⠁⠰⣄⣴⡬⢵⣴⣤⣽\n"
        "⡇⢀⢄⡀⡉⠻⠁⠘⠛\n"
        "⠃⠈⠻⢘⣧⣀⠾⠿⠦⢳\n"
        "⣤⡀⢀⡀⠻⢣⡒⢤⢾\n"
        "⠋⢘⣦⡀⠉⠛⠻⠻⠺⠟⠛⠿\n"
        "⠋⠁⢻⣄⡀⢀⣤⣾⡀⢹\n"
        "⢻⡤⠰⡆⠈⠛⢦⣀⡀⡀\n"
        "⠈⢿⠟⢣⠈⠹⣀\n"
        "⠘⢺⣇⠸\n"
        "⠹⡇⠸⡄⠈⠁\n"
        "⢻⡇⢹⣧⠘\n")
    await trumpsay.edit(J)


@borg.on(admin_cmd(pattern="schina (.*)"))
async def kakashi(ckmkb):
    name = ckmkb.pattern_match.group(1)
    K = (f"**🅲🅺🅼🅺🅱 ➥ {name} .\n\n**"
        "⠟⠋⢁⢁⢁⢁⢁⢁⢁⢁⠈⢻⢿\n"
        "⠃⠈⡀⠭⢿\n"
        "⡟⢀⣾⡆\n"
        "⡇⢀⣧⢸\n"
        "⣇⠿⠙⡟⠡⣴⣽⣧⢸\n"
        "⣾⣟⣭⣾⣴⢄\n"
        "⡟⣩⡏⢻\n"
        "⣹⠘⠷⣦⣀⣠⡶⠁⠈⠁\n"
        "⣍⠃⣴⡔⠒⣠⢀⡨\n"
        "⣦⡘⠿⠿⠟⠃⣠⡇⠈⠻\n"
        "⠟⠋⢁⣠⣀⣠⣾⡟⠉⠙⠻\n"
        "⠟⠁⢸⡯⢓⣴⣾⡟\n"
        "⡟⠹⠁\n"
        "⣸⡷⡇⣴⣾⠃\n"
        "⠃⣦⣄⠇\n"
        "⢸⠗⢈⡶⡏\n")
    await ckmkb.edit(K)
 
 
@borg.on(admin_cmd(pattern=r"spika"))
async def kakashi(pikachu):
    await pikachu.edit(F)
    
@borg.on(admin_cmd(pattern=r"sshit"))
async def kakashi(shit):
    await shit.edit(G)
    
@borg.on(admin_cmd(pattern=r"sxx"))
async def kakashi(saxy):
    await saxy.edit(H)
    
@borg.on(admin_cmd(pattern=r"sporn"))
async def kakashi(pornhub):
    await pornhub.edit(I)