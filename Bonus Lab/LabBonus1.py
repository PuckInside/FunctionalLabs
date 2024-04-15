import enum

class PaternType(enum.Enum):

    none = -1
    EverythingAfter = 0
    OneAfter = 1
    

def IsPatern(string: str, patern: str):
    
    splitList = patern.split('.')
    return splitList

print(IsPatern("aaafff", "a.....fff"))