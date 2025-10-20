from src.feez_buzz_handler import FeezBuzzHandler
from config import Config
from src import handlers
"""
Config contains the divisors list and them output values to show.
FeezBuzzHandler.get_value_to_show returns the value or the output.
"""


def run(iterable: list[int] = Config.DEFAULT_ITERABLE, is_simple_output: bool = True, item_to_item:bool=False):
    processed_list = [
                    FeezBuzzHandler.get_value_to_show(i, is_simple_output=is_simple_output) for i in iterable
                ]
    if item_to_item:
        handlers.print_item_to_item(processed_list)
    else:
        print(
            handlers.print_list_to_str(
                processed_list
            )
    )


if __name__ == "__main__":
    try:
        handlers.valid_config()
        run(is_simple_output=handlers.which_output(), item_to_item=handlers.which_print_mode())
    except handlers.ConfigError as e:
        print(
            f"\nError in your config file, please check it:\n\n       {str(e)}\n")
    except Exception as e:
        print(f"Unknown error :\n\n    {str(e)}\n")
