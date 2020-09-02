#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""A bot to list all members of a server."""
import csv
import sys
import discord
from discord.ext import commands
from discord.ext.commands import Bot

bot = Bot(command_prefix = ">")


@bot.event
async def on_ready():
    print('bot login>', )
    print('bot.user.name: ', bot.user.name)
    print('bot.user.id: ', bot.user.id)
    print('------')



@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.CommandNotFound):
        return
    else:
        print(error)


@bot.command(pass_context=True)
async def list(ctx):
    """Returns a CSV file of all users on the server."""
    await bot.request_offline_members(ctx.message.server)
    nicknames = [m.display_name for m in ctx.message.server.members]
    with open('temp.csv', mode='w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, dialect='excel')
        for v in nicknames:
            writer.writerow([v])
    await bot.send_file(ctx.message.author, 'temp.csv', filename='stats.csv',
                        content="Here you go! Check your PM's.")


@bot.command()
async def info(ctx):
    embed = discord.Embed(title="users2csv bot", description="export user list", color=0xeee657)
    
    embed.add_field(name="Author", value="walker#9296")
    
    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")
 
    # give users a link to invite thsi bot to their server
	
	
	
	
    embed.add_field(name="Invite", value="[Invite link](https://discord.com/api/oauth2/authorize?client_id=750373870745288756&permissions=0&scope=bot)")
 
    await ctx.send(embed=embed)
	
	
bot.remove_command('help')
 
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="users2csv bot", description="export user list. 命令:", color=0xeee657)
 
    embed.add_field(name="$list", value="export user list", inline=False)
    embed.add_field(name="$info", value="about this bot", inline=False)
    embed.add_field(name="$help", value="bot help", inline=False)
 
    await ctx.send(embed=embed)


if __name__ == '__main__':
    print(sys.argv[0], sys.argv[1], sys.argv[2])
    bot.run(sys.argv[1])