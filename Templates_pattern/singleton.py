class ConfigManage:
    _instance = None
    _initialisation = False


    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Create new instance")
            cls._instance = super(ConfigManage, cls).__new__(cls)
        return cls._instance

    def __init__(self, settings: dict):

        if not self._initialisation:
            self.settings = settings
            self._initialisation = True
            print(f"ConfigManager Init")

    def get_settings(self, key: str):
        return self.settings.get(key)

    def update_settings(self, key: str, value):
        self.settings[key] = value
        print(f"Updated. {key} have {value}")
        
config1 = ConfigManage({"font": "Arial", "font-size": 14})
print(config1.get_settings("font"))

config2 = ConfigManage({"db_host": "localhost"})
print(config2.get_settings("font"))
print(config2.get_settings("db_host"))

config2.update_settings("color", "red")

print(config1.get_settings("color"))