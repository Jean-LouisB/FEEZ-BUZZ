from config import Config
import time
import sys

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

def print_item_to_item(result:list[str]):
    for r in result:
        # print(r, end="\r")
        sys.stdout.write("\r" + " "*50)
        sys.stdout.write("\r"+str(r))
        sys.stdout.flush()
        time.sleep(Config.ITEM_TO_ITEM_SLEEP)
    print()

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

def which_print_mode():
    print("\nWhich print mode?\n")
    print("     1 - list.")
    print("     2 - item to item.\n")
    choose = input("Your choose (1 or 2) : ")
    if choose not in ["1","2"]:
        return which_print_mode()
    return True if choose == "2" else False