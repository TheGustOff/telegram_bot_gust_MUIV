import base_bot
import info_bot
import echo_bot
import WIKIPEDIA_bot
import test_bot
import Text_game_bot
import Dialog_bot

if __name__ == "__main__":
    base_bot.main(info_bot.get_text, echo_bot.handle_text, WIKIPEDIA_bot.handle_text, test_bot.handle_text, Text_game_bot.send_echo, Dialog_bot.get_name)
