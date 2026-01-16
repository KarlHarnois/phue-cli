class GroupTarget:
    def __init__(self, name):
        self.name = name

    def is_on(self, bridge):
        return bridge.get_group(self.name, "on")

    def set_on(self, bridge, on):
        bridge.set_group(self.name, "on", on)

    def set_brightness(self, bridge, bri):
        bridge.set_group(self.name, "bri", bri)

    def describe(self):
        return f"group={self.name}"
