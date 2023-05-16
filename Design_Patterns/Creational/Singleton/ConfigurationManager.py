class ConfigurationManager:
    _instance = None
    file = None
    @staticmethod
    def get_instance():
        if ConfigurationManager._instance is None:
            ConfigurationManager._instance = ConfigurationManager()
        return ConfigurationManager._instance

    def set_value(self,file):
        self.file = file
        return self.file

    def get_value(self):
        return self.file



cm1 = ConfigurationManager()
print(cm1.get_value())
cm1.set_value("nivedita/c1.txt")
print(cm1.file)
print(cm1.get_value())

cm2 = ConfigurationManager()
print(cm2.file)