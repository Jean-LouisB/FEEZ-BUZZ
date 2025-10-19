from config import Config

class ConfigError(Exception):pass

def valid_config():
    attr_required = ["MAX","SEPARATOR","SUB_SEPARATOR","END_OUTPUT",  "DIVISORS", "DEFAULT_ITERABLE", "DEFAULT_IS_SIMPLE_OUTPUT"]
    for att in attr_required:
        if not hasattr(Config, att):
            raise ConfigError(f"See your config file. Missing required attribute: {att}")
    if 0 in Config.DIVISORS:
        raise ConfigError("See your config file. 'DIVISORS' key can't be 0")
    if Config.MAX <=1:
        raise ConfigError("See your config file. 'MAX' must be greater than 1.")
    keys_required = ["output","func"]
    for k,v in Config.DIVISORS.items():
        if not all([sub_k in v.keys() for sub_k in keys_required]):
            raise ConfigError(f"See your config file. Items of 'DIVISORS' must have the keys {keys_required}.")

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
