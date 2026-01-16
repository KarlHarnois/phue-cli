class LightTarget:
    def __init__(self, name):
        self.name = name

    def is_on(self, bridge):
        return bridge.get_light(self.name, "on")

    def set_on(self, bridge, on):
        bridge.set_light(self.name, "on", on)

    def set_brightness(self, bridge, bri):
        bridge.set_light(self.name, "bri", bri)

    def describe(self):
        return f"light={self.name}"
