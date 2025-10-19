from config import Config

def valid_config():
    if 0 in Config.DIVISORS:
        raise ValueError("See your config file. divisors key can't be 0")

def print_list_to_str(result:list[str], sep :int=Config.SEPARATOR, end:str=Config.END_OUTPUT) :
    return f"{sep.join(result)}{end}"

def which_output():
    chooses = {
        "o":True,
        "f":False
    }
    choose = input("Output or function (o/f) : ")
    if not choose in chooses:
        print("Error : Choose between 'o' and 'f'.")
        return which_output()
    return chooses[choose.lower()]
