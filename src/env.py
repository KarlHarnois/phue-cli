import os


class Env:
    def get(self, key):
        return os.getenv(key)
