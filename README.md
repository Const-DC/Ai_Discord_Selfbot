# Discord Self-Bot with Local LLM Integration (Ollama)

A Discord self-bot that uses a locally hosted large language model (LLM) via Ollama to generate automated replies. Designed for personal use, the bot listens to messages received by your Discord user account and responds based on message content.

## ⚠️ Important Disclaimer

**This is a self-bot and operates under a user account. Self-bots are against Discord's Terms of Service and can lead to account termination if used improperly. Use at your own risk, and only in controlled or authorized environments.**

## 🚀 Features

- **Local LLM Integration**: Uses Ollama to run models locally for privacy and control
- **Automated Responses**: Generates intelligent replies based on message content
- **Access Control**: Whitelist system to control who the bot responds to
- **Human-like Typing**: Artificial typing delays to make responses appear natural
- **Mention Detection**: Responds when mentioned if no whitelist is configured
- **Easy Setup**: Simple configuration and installation process

## 📋 Requirements

- Python 3.9 or higher
- Valid Discord user token
- Ollama LLM system installed and running locally
- Supported model (e.g., `phi3:mini`) pulled via Ollama

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/discord-selfbot-ollama.git
cd discord-selfbot-ollama
```

### 2. Install Dependencies
```bash
pip install discord.py requests asyncio
```

### 3. Install and Setup Ollama
Download and install Ollama from [https://ollama.ai](https://ollama.ai)

Pull a supported model:
```bash
ollama pull phi3:mini
```

Start Ollama service:
```bash
ollama serve
```

### 4. Configure the Bot
1. Create a `config.py` file in the project directory
2. Add your Discord token and configuration:

```python
DISCORD_TOKEN = "your_discord_token_here"
OLLAMA_MODEL = "phi3:mini"
OLLAMA_URL = "http://localhost:11434/api/generate"
WHITELIST_USERS = []  # List of user IDs, leave empty to only respond to mentions
```

### 5. Run the Bot
```bash
python selfbot.py
```

## ⚙️ How It Works

1. **Message Interception**: The bot uses `discord.py` with `commands.Bot` in self-bot mode to intercept messages
2. **Access Control**: Checks if the message sender is in the whitelist or if the bot is mentioned
3. **Prompt Generation**: Formats the received message into a prompt for the LLM
4. **LLM Processing**: Sends the prompt to the local Ollama API endpoint
5. **Response Generation**: Extracts and processes the LLM response
6. **Human-like Delay**: Adds artificial typing delays using `asyncio` and `random` modules
7. **Message Sending**: Sends the generated response back to the Discord channel

## 🔧 Configuration Options

### Whitelist Configuration
- **Empty List**: Bot only responds when mentioned
- **User IDs**: Bot responds to specific users in the whitelist

### Model Configuration
You can change the Ollama model in the configuration:
```python
OLLAMA_MODEL = "llama2"  # or any other pulled model
```

### API Endpoint
The default Ollama API endpoint is:
```
http://localhost:11434/api/generate
```

## 📁 Project Structure

```
discord-selfbot-ollama/
├── selfbot.py          # Main bot script
├── config.py           # Configuration file
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── .gitignore         # Git ignore file
```

## 🔒 Security Considerations

- **Token Safety**: Never commit your Discord token to version control
- **Local Processing**: All LLM processing happens locally for privacy
- **Access Control**: Use the whitelist feature to limit bot interactions
- **Rate Limiting**: Be mindful of Discord's rate limits to avoid detection

## 🐛 Troubleshooting

### Common Issues

**Bot not responding:**
- Check if Ollama is running (`ollama serve`)
- Verify the model is pulled (`ollama list`)
- Ensure the Discord token is valid

**Connection errors:**
- Verify Ollama API endpoint is accessible
- Check if the specified model exists
- Ensure no firewall is blocking local connections

**Rate limiting:**
- Reduce response frequency
- Increase typing delays
- Monitor Discord API rate limits

## 📝 Example Usage

```python
# Basic configuration
WHITELIST_USERS = [123456789012345678]  # Replace with actual user IDs
OLLAMA_MODEL = "phi3:mini"

# The bot will now respond to messages from whitelisted users
# and generate responses using the local phi3:mini model
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚖️ Legal Notice

This software is provided for educational and personal use only. Users are responsible for complying with Discord's Terms of Service and any applicable laws. The authors are not responsible for any misuse of this software or any consequences resulting from its use.

## 🙏 Acknowledgments

- [Discord.py](https://github.com/Rapptz/discord.py) - Discord API wrapper
- [Ollama](https://ollama.ai) - Local LLM hosting platform
- [OpenAI](https://openai.com) - Inspiration for LLM integration patterns
