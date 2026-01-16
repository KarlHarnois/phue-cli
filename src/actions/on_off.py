from src.actions.action import Action


class OnOff(Action):
    def __init__(self, on):
        self.on = on

    def run(self, bridge, target, brightness):
        target.set_on(bridge, self.on)
        if brightness is not None:
            target.set_brightness(bridge, brightness)
        state = "on" if self.on else "off"
        return f"OK: {target.describe()} action={state} bri={brightness}"
