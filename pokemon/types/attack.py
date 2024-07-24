
class Attack:
    """
    Parameters
    ----------
    name (str):required
        name of the pokemon
    power (int) : required
        power of the pokemon
    log_level (int) : optional
        log level for the logger, accepted values are 10,20,30....
    """
    def __init__(self , name , power , log_level=20) -> None:
        self.__name = name
        self.__power = power
        self.log_level = log_level
    
    def get_name(self) -> str:
        return self.__name;
    def get_power(self) -> int:
        return self.__power
    