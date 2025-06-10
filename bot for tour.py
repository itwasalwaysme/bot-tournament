import discord
from discord.ext import commands,tasks
import pytz
from datetime import datetime, timedelta
from colorama import Fore
import random

bot = commands.Bot("#", intents=discord.Intents.all())

horarios = {
    "8:00": "Mitosis Tournament Australia",
    "9:00": "Mitosis Tournament Australia",
    "10:00": "Mitosis Tournament China",
    "11:00": "Mitosis Tournament China",
    "12:00": "Mitosis Tournament Australi",
    "14:00": "Mitosis Tournament China",
    "14:00": "Mitosis Tournament Europe",
    "15:30": "Mitosis Tournament Europe",
    "17:00": "Mitosis Tournament Europe",
    "18:30": "Mitosis Tournament Europe",
    "19:00": "Mitosis Tournament Suda",
    "20:00": "Mitosis Tournament Europe",
    "20:30": "Mitosis Tournament Suda",
    "21:00": "Mitosis Tournament Mexico",
    "22:00": "Mitosis Tournament Suda",
    "22:30": "Mitosis Tournament Mexico",
    "23:30": "Mitosis Tournament Suda",
    "00:00": "Mitosis Tournament Mexico",
    "01:00": "Mitosis Tournament Suda",
    "01:30": "Mitosis Tournament Mexico",
    "03:00": "Mitosis Tournament Mexico",
}

@bot.event
async def on_ready():   
    await bot.tree.sync()
    tour.start()
    print("Bot inicicializado")

colors = [discord.Color.purple(), discord.Color.blue(), discord.Color.dark_blue(), discord.Color.dark_magenta(), discord.Color.gold(), discord.Color.orange()]

color = random.choice(colors)

async def box(server:str, minutes:int):
    embed = discord.Embed(title=f"{server}")
    embed.description = f"{minutes} min"
    embed.set_author(name="💫Bot Tournament💫", icon_url="https://images-ext-1.discordapp.net/external/RGOVRYlb6TDPuc_UwITP5rsciqNzaYCDfq7hTXKjdl8/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/812483756249186304/f33aadf3457bae2bb920bbf808f20881.png?format=webp&quality=lossless")
    embed.color = color
    return embed

# 30 MINUTES
@tasks.loop(seconds=30) 
async def tour() -> str | None:
    channel = bot.get_channel(1379909757904883762)
    min:int = 0
    data = datetime.now()
    fuso_horario = pytz.timezone("Europe/Madrid")
    agora = data.astimezone(fuso_horario).time()
    for k, v in horarios.items():
        hora = datetime.strptime(k, "%H:%M")

        before30 = timedelta(minutes=-30)
        h30 = hora + before30

        before20 = timedelta(minutes=-20)
        h20 = hora + before20

        before10 = timedelta(minutes=-10)
        h10 = hora + before10        

        before5 = timedelta(minutes=-5)
        h5 = hora + before5

        if agora.hour == h30.hour and agora.minute == h30.minute:
            min = 30
            await channel.send(content="@everyone", embed=await box(server=v, minutes=min))
            print(Fore.LIGHTGREEN_EX + "Success" + Fore.RESET)

        elif agora.hour == h20.hour and agora.minute == h20.minute:
            min = 20
            await channel.send(content="@everyone", embed=await box(server=v, minutes=min))
            print(Fore.LIGHTGREEN_EX + "Success" + Fore.RESET)

        elif agora.hour == h10.hour and agora.minute == h10.minute:
            min = 10
            await channel.send(content="@everyone", embed=await box(server=v, minutes=min))
            print(Fore.LIGHTGREEN_EX + "Success" + Fore.RESET)

        elif agora.hour == h5.hour and agora.minute == h5.minute:
            min = 5
            await channel.send(content="@everyone", embed=await box(server=v, minutes=min))
            print(Fore.LIGHTGREEN_EX + "Success" + Fore.RESET)

bot.run(<YOUR_TOKEN>)
