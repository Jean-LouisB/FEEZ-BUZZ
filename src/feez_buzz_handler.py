from config import Config


class FeezBuzzHandler:
    @staticmethod
    def get_value_to_show(n: int, is_simple_output:bool=Config.DEFAULT_IS_SIMPLE_OUTPUT):
        """
        Returns:
            The str value or the corresponding output from Config.divisors (n or output)
        Raises:
            ValueError: If a Config.divisors key is 0.
            ValueError: If the number provided is not an integer.
        """
        if 0 in Config.DIVISORS:
            raise ValueError("See your config file. divisors key can't be 0")
        try:
            n = FeezBuzzHandler.valid_n(n)
        except Exception as e:
            raise e
        value_to_return = []
        for k, v in Config.DIVISORS.items():
            if n % k == 0:
                if is_simple_output:
                    value_to_return.append(str(v["output"]))
                else:
                    value_to_return.append(str(v["func"](n)))
        return Config.SUB_SEPARATOR.join(value_to_return) if value_to_return else str(n)

    @staticmethod
    def valid_n(n: int):
        if n == 0:
            raise ValueError("number can be 0.")
        if not isinstance(n, int):
            try:
                n = int(n)
            except Exception as e:
                raise ValueError(
                    f"number have to be an integer, not {type(n)} -> ({n})")
        return n
