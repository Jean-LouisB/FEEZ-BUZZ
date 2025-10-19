from feez_buzz_handler import FeezBuzzHandler
from config import Config
import handlers
"""
Config contains the divisors list and them output values to show.
FeezBuzzHandler.get_value_to_show returns the value or the output.
"""


def run(iterable: list[int] = Config.default_iterable):
    print(
        handlers.print_list_to_str(
            [
                FeezBuzzHandler.get_value_to_show(i) for i in iterable
            ]
        )
    )


if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        print(f"{str(e)}")
