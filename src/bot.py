import nextcord as discord

from nextcord.ext import commands
from constants import GUILD_ID

intents = discord.Intents().all()
bot = commands.Bot(
    command_prefix=".",
    intents=intents,
    allowed_mentions=discord.AllowedMentions(everyone=False),
)
guild = bot.get_guild(GUILD_ID)
keywords = {}
