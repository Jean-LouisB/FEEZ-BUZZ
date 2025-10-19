from config import Config

def print_list_to_str(result:list[str], sep :int=Config.sep, end:str=Config.end) :
    return f"{sep.join(result)}{end}"