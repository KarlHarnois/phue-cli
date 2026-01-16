import sys
from src.app_error import AppError


class App:
    def __init__(self, loader, controller):
        self.loader = loader
        self.controller = controller

    def run(self):
        try:
            settings = self.loader.load()
            result = self.controller.execute(settings)
            print(result)
            return 0
        except AppError as error:
            print(str(error), file=sys.stderr)
            return 2
