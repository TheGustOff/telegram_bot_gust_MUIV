import base_bot
import info_bot
import echo_bot
import WIKIPEDIA_bot

base_bot.text_handlers(info_bot.get_text, echo_bot.handle_text, WIKIPEDIA_bot.handle_text)

if __name__ == "__main__":
    base_bot.main()
