from src.feez_buzz_handler import FeezBuzzHandler
from config import Config
from src import handlers
"""
Config contains the divisors list and them output values to show.
FeezBuzzHandler.get_value_to_show returns the value or the output.
"""


def run(iterable: list[int] = Config.DEFAULT_ITERABLE,is_simple_output:bool=True):
    print(
        handlers.print_list_to_str(
            [
                FeezBuzzHandler.get_value_to_show(i, is_simple_output=is_simple_output) for i in iterable
            ]
        )
    )


if __name__ == "__main__":
    try:
        handlers.valid_config()
        run(is_simple_output=handlers.which_output())
    except handlers.ConfigError as e:
        print(f"\nError in your config file, please check it:\n\n       {str(e)}\n")
    except Exception as e:
        print(f"Unknown error :\n\n    {str(e)}\n")
