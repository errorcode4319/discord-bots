import discord
import requests
from discord.ext import commands

# 봇 초기화
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


def get_public_ip():
    try:
        # API 호출로 공인 IP 가져오기
        response = requests.get("https://api.ipify.org")
        response.raise_for_status()  # HTTP 에러가 발생하면 예외 처리
        return response.text
    except requests.RequestException as e:
        print(f"공인 IP를 가져오는 중 오류가 발생했습니다: {e}")
        return None


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello! I'm Public IP Checker Bot")


@bot.command()
async def ip_check(ctx):
    await ctx.send(f"Public IP: {get_public_ip()}")



bot.run(os.getenv('DISCORD_TOKEN'))
