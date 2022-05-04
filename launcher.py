import base_bot
import info_bot
import echo_bot
import WIKIPEDIA_bot

if __name__ == "__main__":
    base_bot.main(info_bot.get_text, echo_bot.handle_text, WIKIPEDIA_bot.handle_text)
