import telebot

# Initialize the Telegram Bot with your token
bot = telebot.TeleBot("7130300098:AAGoUnClzsjI3qWopx2FGIapFtrSB432tfQ")

# File to store the usernames
USERNAMES_FILE = "bot_usernames.txt"

# Password for adding new bot and deleting bot
PASSWORD = "Br055055055New"

# Load usernames from the file
try:
    with open(USERNAMES_FILE, "r") as file:
        bot_usernames = file.read().splitlines()
except FileNotFoundError:
    bot_usernames = []

# Handler for the /start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome! Use /showbots to view the list of the best tools bots usernames.")

# Handler for the /newbot command
@bot.message_handler(commands=['newbot'])
def newbot(message):
    chat_id = message.chat.id
    if len(message.text.split()) > 1 and message.text.split()[1] == PASSWORD:
        bot.reply_to(message, "Enter the username of the new bot:")
        bot.register_next_step_handler(message, add_bot)
    else:
        bot.reply_to(message, "Wrong password. Access denied.")

# Function to add a new bot
def add_bot(message):
    new_bot_username = message.text
    bot_usernames.append(new_bot_username)
    save_usernames()
    bot.reply_to(message, f"Bot {new_bot_username} has been added successfully!")

# Handler for the /deletebot command
@bot.message_handler(commands=['deletebot'])
def deletebot(message):
    chat_id = message.chat.id
    if len(message.text.split()) > 1 and message.text.split()[1] == PASSWORD:
        bot.reply_to(message, "Enter the username of the bot to delete:")
        bot.register_next_step_handler(message, remove_bot)
    else:
        bot.reply_to(message, "Wrong password. Access denied.")

# Function to remove a bot
def remove_bot(message):
    bot_to_remove = message.text
    if bot_to_remove in bot_usernames:
        bot_usernames.remove(bot_to_remove)
        save_usernames()
        bot.reply_to(message, f"Bot {bot_to_remove} has been deleted successfully!")
    else:
        bot.reply_to(message, f"Bot {bot_to_remove} not found in the list.")

# Handler for the /showbots command
@bot.message_handler(commands=['showbots'])
def showbots(message):
    bot.reply_to(message, "Here are the usernames of all the bots:")
    for username in bot_usernames:
        bot.send_message(message.chat.id, f"{username}")

# Function to save usernames to the file
def save_usernames():
    with open(USERNAMES_FILE, "w") as file:
        file.write("\n".join(bot_usernames))

# Start the bot
bot.polling()
