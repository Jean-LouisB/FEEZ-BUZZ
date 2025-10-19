from config import Config

class ConfigError(Exception):pass

def valid_config():
    attr_required = ["MAX","SEPARATOR","SUB_SEPARATOR","END_OUTPUT",  "DIVISORS", "DEFAULT_ITERABLE", "DEFAULT_IS_SIMPLE_OUTPUT"]
    for att in attr_required:
        if not hasattr(Config, att):
            raise ConfigError(f"Missing required attribute: {att}")
    if 0 in Config.DIVISORS:
        raise ConfigError("'DIVISORS' key can't be 0")
    if Config.MAX <=1:
        raise ConfigError("'MAX' must be greater than 1.")
    for k,v in Config.DIVISORS.items():
        if not all([sub_k in v.keys() for sub_k in Config.DIVISORS_KEYS]):
            raise ConfigError(f"Items of 'DIVISORS' must have the keys {Config.DIVISORS_KEYS}.")

def print_list_to_str(result:list[str], sep :int=Config.SEPARATOR, end:str=Config.END_OUTPUT) :
    return f"{sep.join(result)}{end}"

def which_output():
    chooses = {
        "o":True,
        "f":False
    }
    choose = input("Output or function (o/f) (enter = 'o'): ") or 'o'
    if not choose in chooses:
        print("Error : Choose between 'o' and 'f'.")
        return which_output()
    return chooses[choose.lower()]
