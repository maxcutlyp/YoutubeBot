import discord
from discord.ext import commands
import yt_dlp

bot = commands.Bot(command_prefix='.')

def main():
    with open('./token.txt') as t:
        lines = t.readlines()
        token = lines[0][:-1]
    bot.run(token)

@bot.command(name='play')
async def play(ctx, *args):
    query = ' '.join(args)
    # source address as 0.0.0.0 to force ipv4 because ipv6 breaks it for some reason
    # this is equivalent to --force-ipv4 (line 312 of https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/options.py)
    await ctx.send(f'Downloading `{query}`...')
    with yt_dlp.YoutubeDL({'format': 'worstaudio',
                           'source_address': '0.0.0.0',
                           'default_search': 'ytsearch',
                           'outtmpl': '%(id)s.%(ext)s'}) as ydl:
        ydl.download([query])

@bot.event
async def on_ready():
    print(f'logged in successfully as {bot.user.name}')

if __name__ == '__main__':
    main()
