from src.actions.action import Action


class Register(Action):
    def run(self, bridge, target, brightness):
        bridge.connect()
        return f"OK: registered username={bridge.username}"
