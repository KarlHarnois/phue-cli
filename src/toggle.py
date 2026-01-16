from src.action import Action


class Toggle(Action):
    def run(self, bridge, target, brightness):
        target.set_on(bridge, not target.is_on(bridge))
        if brightness is not None:
            target.set_brightness(bridge, brightness)
        return f"OK: {target.describe()} action=toggle bri={brightness}"
