# TestBot

A Discord bot that can send embeds to channels.

## Features

- Send embeds to specified channels using the `/embed` command
- Customize embed colors
- Set embed title and content

## Command Usage

``/embed <color> <channel> <title> <message>``

- `<color>`: The color of the embed (e.g., red, blue, green, or hex code like #FF0000)
- `<channel>`: The channel to send the embed to (either channel ID or mention)
- `<title>`: The title of the embed
- `<message>`: The content of the embed

## Setup

1. Clone this repository
2. Install the required packages:
   `pip install -r requirements.txt`
3. Create a `.env` file with your bot token:
   `DISCORD_TOKEN=your_token_here`
4. Run the bot:
   `python main.py`

## Requirements

- Python 3.8 or higher
- discord.py 2.0 or higher
- python-dotenv

## License

MIT