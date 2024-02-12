from bot import discord


async def is_banned(user: discord.User, guild: discord.Guild):
    try:
        await guild.fetch_ban(user)
        return True
    except Exception:
        return False
