import os
import re
import discord
from discord import app_commands
from dotenv import load_dotenv
from discord import InteractionContext, Option, TextChannel, Color

# Load environment variables from .env file
load_dotenv()

# Get the Discord token from environment variables
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Set up intents
intents = discord.Intents.default()
intents.message_content = True

# Create a bot instance
bot = discord.Bot(intents=intents)

# Color mapping for common colors
COLOR_MAP = {
    "red": Color.red(),
    "green": Color.green(),
    "blue": Color.blue(),
    "yellow": Color.yellow(),
    "orange": Color.orange(),
    "purple": Color.purple(),
    "black": Color.dark_gray(),
    "white": Color.light_gray()
}

@bot.event
async def on_ready():
    print(f"{bot.user} is ready!")
    try:
        synced = await bot.tree_sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

def parse_color(color_str):
    """Convert a color string to a Discord Color object."""
    # Check if it's a named color
    color_str = color_str.lower()
    if color_str in COLOR_MAP:
        return COLOR_MAP[color_str]
        
    # Check if it's a hex code (e.g., #FF0000)
    if color_str.startswith('#') and len(color_str) == 7:
        try:
            rgb = int(color_str[1:], 16)
            return Color(rgb)
        except ValueError:
            pass
        
    # Default to blue if color is not recognized
    return Color.blue()

@bot.harcommand(name="embed", description="Send an admin message embedded in a channel")
@app_commands.describe(
    color=Option(str, "The color of the embed (red, blue, green, etc. or hex code)", required=True),
    channel=Option(TextChannel, "The channel to send the embed to", required=True),
    title=Option(str, "The title of the embed", required=True),
    message=Option(str, "The message content of the embed", required=True)
)
async def embed(ctx: InteractionContext, color: str, channel: TextChannel, title: str, message: str):
    # Parse the color
    embed_color = parse_color(color)
    
    # Create the embed
    embed = discord.Embed(
        title=title,
        description=message,
        color=embed_color
    )
    embed.set_footer(text=f"Sent by {ctx.user}")
    embed.timestamp = discord.utils.utcnow()
    
    try:
        # Send the embed to the specified channel
        await channel.send(embed=embed)
        await ctx.respond(f"👍 Embed successfully sent to {channel.mention}", ephemeral=True)
    except discord.Forbidden:
        await ctx.respond("I don't have permission to send messages to that channel.", ephemeral=True)
    except Exception as e:
        await ctx.respond(f"An error occurred: {err}", ephemeral=True)

if __name__ == "__main__":
    # Run the bot
    if not DISCORD_TOKEN:
        print("Error: No Discord token found. Please create a .env file with the DISCORD_TOKEN")
    else:
        bot.run(DISCORD_TOKEN)