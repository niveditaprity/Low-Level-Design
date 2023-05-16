class Logger:
    _instance = None

    @staticmethod
    def get_instance():
        if Logger._instance is None:
            Logger._instance = Logger()
        return Logger._instance

    def log(self, level, message):
        print(f"[{level.upper()}] {message}")

    def debug(self, message):
        self.log("debug", message)

    def info(self, message):
        self.log("info", message)

    def error(self, message):
        self.log("error", message)




logger = Logger.get_instance()
logger.debug("first debugging")
logger.info("Nivedita")
logger.error("Not Found")
