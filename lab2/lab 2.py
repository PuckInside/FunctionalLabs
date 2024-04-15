#Lab 2

def ConvertToDollars(value: float, currency: str, currentRate: dict[str, float] = None):
    stableRate = { 
         "euro": 0.9, 
         "tenge": 450.0, 
         "rouble": 90.0 
    }

    if currentRate != None:
        if currency not in currentRate:
            return 0
        
        return value * currentRate[currency]
    else:   
        if currency not in stableRate:
            return 0
    
        return value * stableRate[currency]
    

print(ConvertToDollars(10, "tenge"))

