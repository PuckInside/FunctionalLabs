class AnyConfig:
    def __init__(self, configFile) -> None:
        self.configFile = configFile

    def getConfig(self):
        return self.configFile

class LazyZonfig:
    
    def __init__(self, path: AnyConfig) -> None:
        self.configPath = path
        self.config = None

    def load_config(self):
        if not self.config:
            self.config = self.configPath.getConfig()
            print("ХА ХА проводим вычисления!\n")

    def getConfig(self):
        self.load_config()
        return self.config

path = AnyConfig("Содержание конфига!")
con = LazyZonfig(path)

print(con.getConfig())

print(con.getConfig())
print(con.getConfig())
print(con.getConfig())